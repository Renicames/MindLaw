from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments, DataCollatorForSeq2Seq
import json
import torch
from torch.utils.data import Dataset, DataLoader, Subset
from sklearn.model_selection import KFold
import numpy as np
from rouge_score import rouge_scorer

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Turkish-NLP/t5-efficient-base-turkish")
model = AutoModelForSeq2SeqLM.from_pretrained("Turkish-NLP/t5-efficient-base-turkish")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Load data
with open('unique_qa_dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

class QADataset(Dataset):
    def __init__(self, input_texts, output_texts, tokenizer, max_length):
        self.input_texts = input_texts
        self.output_texts = output_texts
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.input_texts)

    def __getitem__(self, idx):
        input_text = self.input_texts[idx]
        output_text = self.output_texts[idx]
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=self.max_length)
        outputs = self.tokenizer(output_text, return_tensors="pt", padding=True, truncation=True, max_length=self.max_length)
        input_ids = inputs['input_ids'].squeeze()
        attention_mask = inputs['attention_mask'].squeeze()
        labels = outputs['input_ids'].squeeze()
        labels[labels == self.tokenizer.pad_token_id] = -100
        return {"input_ids": input_ids, "attention_mask": attention_mask, "labels": labels}

input_texts = ["Soru: " + item['Soru'] for item in data]
output_texts = ["Cevap: " + item['Cevap'] for item in data]
max_length = 512

dataset = QADataset(input_texts, output_texts, tokenizer, max_length)

# KFold Cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

def ask_chatbot(question):
    inputs = tokenizer.encode(question, return_tensors='pt').to(device)
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

rouge_scores_all = []
f1_scores_all = []

for fold, (train_ids, val_ids) in enumerate(kfold.split(dataset)):
    print(f"Fold {fold + 1}")

    train_dataset = Subset(dataset, train_ids)
    val_dataset = Subset(dataset, val_ids)

    train_dataloader = DataLoader(train_dataset, batch_size=4, shuffle=True)
    val_dataloader = DataLoader(val_dataset, batch_size=4)

    # Data collator oluşturma
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    # Eğitim argümanları
    training_args = TrainingArguments(
        output_dir=f'/results/fold_{fold + 1}',
        num_train_epochs=5,
        per_device_train_batch_size=8,
        save_steps=10_000,
        save_total_limit=2,
        evaluation_strategy="epoch",
        learning_rate=5e-4,
    )

    # Trainer oluşturma
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataloader.dataset,
        eval_dataset=val_dataloader.dataset,
        data_collator=data_collator,
    )

    # Modeli eğitme
    trainer.train()

    # Test setinde değerlendirme yapma
    rouge_scores = []
    f1_scores = []
    for item in val_dataset:
        question = tokenizer.decode(item["input_ids"], skip_special_tokens=True)
        reference_answer = tokenizer.decode(item["labels"], skip_special_tokens=True)
        generated_answer = ask_chatbot(question)

        scores = scorer.score(reference_answer, generated_answer)
        rouge_scores.append(scores)

        # F1 skoru hesaplama
        reference_tokens = reference_answer.split()
        generated_tokens = generated_answer.split()
        common_tokens = set(reference_tokens) & set(generated_tokens)
        if len(reference_tokens) == 0 or len(generated_tokens) == 0:
            f1 = 0.0
        else:
            precision = len(common_tokens) / len(generated_tokens)
            recall = len(common_tokens) / len(reference_tokens)
            if precision + recall == 0:
                f1 = 0.0
            else:
                f1 = 2 * (precision * recall) / (precision + recall)
        f1_scores.append(f1)

    rouge_scores_all.append(rouge_scores)
    f1_scores_all.append(f1_scores)

    # Ortalama ROUGE skorlarını hesaplayın
    avg_rouge1 = sum([score['rouge1'].fmeasure for score in rouge_scores]) / len(rouge_scores)
    avg_rouge2 = sum([score['rouge2'].fmeasure for score in rouge_scores]) / len(rouge_scores)
    avg_rougeL = sum([score['rougeL'].fmeasure for score in rouge_scores]) / len(rouge_scores)
    avg_f1 = np.mean(f1_scores)

    print(f"Fold {fold + 1} Average ROUGE-1 Score: {avg_rouge1}")
    print(f"Fold {fold + 1} Average ROUGE-2 Score: {avg_rouge2}")
    print(f"Fold {fold + 1} Average ROUGE-L Score: {avg_rougeL}")
    print(f"Fold {fold + 1} Average F1 Score: {avg_f1}")

# Ortalama skorları hesaplama
overall_avg_f1_score = np.mean([np.mean(scores) for scores in f1_scores_all])
print(f"Overall Average F1 Score: {overall_avg_f1_score}")

# ROUGE skorlarının ortalamalarını hesaplama
avg_rouge_scores = {
    "rouge1": {
        "precision": np.mean([score['rouge1'].precision for scores in rouge_scores_all for score in scores]),
        "recall": np.mean([score['rouge1'].recall for scores in rouge_scores_all for score in scores]),
        "fmeasure": np.mean([score['rouge1'].fmeasure for scores in rouge_scores_all for score in scores]),
    },
    "rouge2": {
        "precision": np.mean([score['rouge2'].precision for scores in rouge_scores_all for score in scores]),
        "recall": np.mean([score['rouge2'].recall for scores in rouge_scores_all for score in scores]),
        "fmeasure": np.mean([score['rouge2'].fmeasure for scores in rouge_scores_all for score in scores]),
    },
    "rougeL": {
        "precision": np.mean([score['rougeL'].precision for scores in rouge_scores_all for score in scores]),
        "recall": np.mean([score['rougeL'].recall for scores in rouge_scores_all for score in scores]),
        "fmeasure": np.mean([score['rougeL'].fmeasure for scores in rouge_scores_all for score in scores]),
    }
}

print(f"Overall Average ROUGE Scores: {avg_rouge_scores}")
