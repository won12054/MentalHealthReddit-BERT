RedditMentalHealth-BERT
Overview
This repository contains a project that leverages BERT (Bidirectional Encoder Representations from Transformers) for predicting mental disorders based on user-generated content from Reddit. By analyzing posts from mental health-related subreddits, this model aims to assist in the early detection and intervention of mental health issues.

Data Collection
We utilized the Reddit SuicideWatch and Mental Health Collection (SWMH) dataset, which includes 54,412 posts discussing various mental health topics such as depression, anxiety, bipolar disorder, and suicidal ideation. The dataset is referenced from the work of Ji et al. (2021), which explores attentive relation networks for detecting mental health disorders:

Ji, S., Li, X., Huang, Z., et al. (2021). Attentive Relation Networks for Early Detection of Mental Health Disorders on Social Media. arXiv preprint arXiv:2102.10021.

Methodology
Preprocessing
Tokenization & Padding: Applied BERT tokenizer, with sequences padded to 256 tokens.
BERT Embeddings: Utilized pre-trained bert-base-uncased embeddings.
Data Augmentation: Used synonym augmentation to address class imbalance.
Model
The model is based on BERT for sequence classification, fine-tuned using the AdamW optimizer and evaluated across metrics like accuracy, precision, recall, F1-score, and ROC AUC score.

Results
Accuracy: 70%
ROC AUC Score: 0.81
The model showed the strongest performance in classifying anxiety and bipolar disorders.
Future Work
Planned improvements include:

Expanding the dataset for better representation.
Exploring advanced models like GPT.
Integrating personalized support through conversational AI.
Enhancing contextual and sentiment analysis for better accuracy.
Contributors
This project was developed by:

Alejandro Akifarry
Arshdeep Kaur
Jungyu Lee
Pratheepan Gunaratnam
Sirada Thoungvitayasutee
License
This project is licensed under the MIT License. See the LICENSE file for details.
