# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 06:10:40 2024

@author: 8778t
"""

from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from fastapi.middleware.cors import CORSMiddleware

class TextRequest(BaseModel):
    text: str
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = 'C:\\Users\\Public\\6th\\bert_best_model.pth'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=5)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

label_mapping = {
    0: "Anxiety",
    1: "Suicide Watch",
    2: "Bipolar",
    3: "Depression",
    4: "Off My Chest"
}

def encode_texts(texts, tokenizer, max_len=256):
    return tokenizer(
        list(texts),
        add_special_tokens=True,
        max_length=max_len,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )

def predict(text: str):
    inputs = encode_texts([text], tokenizer)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        confidence, predicted_class = torch.max(probabilities, dim=1)
    
    predicted_label = label_mapping[predicted_class.item()]
    confidence_scores = {label_mapping[i]: prob.item() for i, prob in enumerate(probabilities[0])}
    
    return predicted_class.item(), predicted_label, confidence.item(), confidence_scores

@app.post("/predict")
def get_prediction(request: TextRequest):
    predicted_class_number, predicted_class, confidence, confidence_scores = predict(request.text)
    return {
        "predicted_class_number": predicted_class_number, 
        "predicted_class": predicted_class,
        "confidence": confidence,
        "confidence_scores": confidence_scores
    }

# uvicorn backend:app --reload --host 0.0.0.0 --port 8000