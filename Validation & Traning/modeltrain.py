from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments, DataCollatorForSeq2Seq
import json
import torch
from torch.utils.data import Dataset, DataLoader, random_split

tokenizer = AutoTokenizer.from_pretrained("Turkish-NLP/t5-efficient-base-turkish")
model = AutoModelForSeq2SeqLM.from_pretrained("Turkish-NLP/t5-efficient-base-turkish")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

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
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

training_args = TrainingArguments(
    output_dir='/results',
    num_train_epochs=5,
    per_device_train_batch_size=8,
    save_steps=10_000,
    save_total_limit=2,
    evaluation_strategy="epoch",
    learning_rate=5e-4,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=data_collator,
)

trainer.train()