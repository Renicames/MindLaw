from flask import Flask, request, render_template, jsonify, url_for
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
import os
import json
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Model and tokenizer loading
tokenizer = AutoTokenizer.from_pretrained("renicames/t5-base-turkish-MindLaw")
model = AutoModelForSeq2SeqLM.from_pretrained("renicames/t5-base-turkish-MindLaw")

# Path to the JSON file for user data
current_directory = os.path.dirname(os.path.abspath(__file__))
users_data_file = os.path.join(current_directory, "users_data.json")

# Load or create the JSON file for user data
def load_users_data():
    if os.path.exists(users_data_file):
        with open(users_data_file, 'r') as f:
            return json.load(f)
    else:
        return {"users": {}}

# Save user data to JSON file
def save_users_data(data):
    with open(users_data_file, 'w') as f:
        json.dump(data, f)

# Update user data
def update_user_data(user_id, new_question):
    users_data = load_users_data()
    if user_id not in users_data["users"]:
        users_data["users"][user_id] = {"questions": [], "context": ""}
    
    if not is_related(users_data["users"][user_id]["context"], new_question, users_data["users"][user_id]["questions"]):
        reset_user_data(user_id)
        users_data["users"][user_id]["context"] = new_question
    else:
        users_data["users"][user_id]["context"] = update_context(users_data["users"][user_id]["context"], new_question)
    
    users_data["users"][user_id]["questions"].append(new_question)
    save_users_data(users_data)

# Update user context
def update_context(context, new_question):
    updated_context = context + " " + new_question
    return updated_context

# Compute text similarity using the model
def compute_similarity(text1, text2):
    inputs1 = tokenizer(text1, return_tensors='pt', truncation=True, padding=True, max_length=512)
    inputs2 = tokenizer(text2, return_tensors='pt', truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs1 = model.encoder(**inputs1)
        outputs2 = model.encoder(**inputs2)
    
    embeddings1 = outputs1.last_hidden_state.mean(dim=1)
    embeddings2 = outputs2.last_hidden_state.mean(dim=1)
    
    cosine_similarity = torch.nn.functional.cosine_similarity(embeddings1, embeddings2)
    return cosine_similarity.item()

# Determine if questions are related
def is_related(context, new_question, questions):
    if not context:
        return False
    
    similarities = [compute_similarity(q, new_question) for q in questions]
    average_similarity = sum(similarities) / len(similarities) if similarities else 0
    print(f"Ortalama Benzerlik: {average_similarity}")
    
    return average_similarity > 0.4

# Ask the chatbot and get a response
def ask_chatbot(user_id, question):
    users_data = load_users_data()
    if not is_related(users_data["users"].get(user_id, {}).get("context", ""), question, users_data["users"].get(user_id, {}).get("questions", [])):
        reset_user_data(user_id)
    update_user_data(user_id, question)
    users_data = load_users_data()
    user_context = users_data["users"][user_id]["context"]
    inputs = tokenizer.encode(user_context, return_tensors='pt')
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = answer.replace("Cevap:", "").strip()  # Remove "Cevap:" from the answer
    return answer

# Reset user data
def reset_user_data(user_id):
    users_data = load_users_data()
    if user_id in users_data["users"]:
        users_data["users"][user_id] = {"questions": [], "context": ""}
        save_users_data(users_data)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Project page
@app.route('/project')
def project():
    return render_template('project.html')

# Chat page
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    user_id = request.form.get('user_id', 'default_user')
    question = request.form.get('question', '')

    if request.method == 'POST' and question:
        answer = ask_chatbot(user_id, question)
    else:
        answer = "Lütfen bir soru girin."

    return render_template('chat.html', user_id=user_id, question=question, answer=answer)

# Reset memory
@app.route('/reset', methods=['POST'])
def reset():
    if os.path.exists(users_data_file):
        os.remove(users_data_file)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
