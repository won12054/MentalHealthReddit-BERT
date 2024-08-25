# 🚀 RedditMentalHealth-BERT

## Overview
This repository contains a project that utilizes **BERT (Bidirectional Encoder Representations from Transformers)** for predicting mental disorders based on user-generated content from Reddit. The goal is to assist in early detection and intervention for mental health issues by analyzing posts from specific mental health-related subreddits.

---

## 📂 Data Collection
The dataset used is the **Reddit SuicideWatch and Mental Health Collection (SWMH)**, comprising **54,412 posts**. These posts focus on various mental health topics, including:

- **Depression**
- **Anxiety**
- **Bipolar Disorder**
- **Suicidal Ideation**

The dataset is referenced from the work of Ji et al. (2021):

> *Ji, S., Li, X., Huang, Z., et al. (2021). Attentive Relation Networks for Early Detection of Mental Health Disorders on Social Media. arXiv preprint arXiv:2102.10021.*

---

## 🛠 Methodology

### 🔄 Preprocessing
- **Tokenization & Padding**: Applied BERT tokenizer, with sequences padded to 256 tokens.
- **BERT Embeddings**: Utilized pre-trained `bert-base-uncased` embeddings.
- **Data Augmentation**: Addressed class imbalance using synonym augmentation.

### 🧠 Model
The model is based on **BERT for sequence classification**, fine-tuned using the **AdamW optimizer**. It was evaluated across multiple metrics, including accuracy, precision, recall, F1-score, and ROC AUC score.

### 📊 Results
- **Accuracy**: 70%
- **ROC AUC Score**: 0.81

The model performed best in classifying anxiety and bipolar disorders.

---

## 🔮 Future Work

Planned enhancements include:

- **Dataset Expansion**: Incorporating a broader range of mental health issues.
- **Advanced Models**: Exploring other large language models like GPT.
- **Personalized Support**: Integrating conversational AI for personalized activity suggestions.
- **Contextual Analysis**: Improving the model to better consider context and sentiment.

---

## 🏆 Acknowledgments

This project was developed as part of the **STEM Fellowship Inter-University Big Data Challenge 2024**. The challenge provided a platform to apply data science techniques to real-world problems, and this project focused on leveraging social media data for mental health insights.

---

## 👥 Contributors

This project was developed by:

- Alejandro Akifarry
- Arshdeep Kaur
- Jungyu Lee
- Pratheepan Gunaratnam
- Sirada Thoungvitayasutee

---
