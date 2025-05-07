# Email-Spam-Classifier



A web application that detects whether a given email message is **Spam** or **Ham** using Machine Learning and Natural Language Processing (NLP).

---

## 🚀 Project Demo

Run the app locally at: `http://127.0.0.1:5000`

---

## 📌 Problem Statement

Unsolicited spam emails flood user inboxes, wasting time and posing security risks. This project aims to build an intelligent system that identifies spam emails using a trained NLP model with over 98% accuracy.

---

## 🛠️ Features

- Real-time email spam detection
- Clean and responsive UI
- 98% accuracy with Naive Bayes classifier
- Trained using labeled SMS/email data

---

## 🧰 Tech Stack

- **Python**
- **scikit-learn**
- **NLTK**
- **Flask**
- **HTML/CSS**
- **Joblib**

---

## 📂 Project Structure

  - **EmailSpamClassifier/**
 -  **├── spam.csv ← Dataset (SMS/email data)**
- **├── model.py ← Trains and saves ML model and vectorizer**
- **├── app.py ← Flask web app backend**
- **├── spam_model.pkl ← Saved trained spam detection model**
- **├── vectorizer.pkl ← Saved CountVectorizer object**
    - **│**
    - **├── templates/**
      -   **│ └── index.html ← Frontend HTML form**
             - **│**
              - **└── static/**
               -  **└── style.css ← (Optional) Custom CSS for UI**

---


---

## 🧪 Model Accuracy

- ✅ **Accuracy:** 98.1% on test data  
- 🧠 **Model Used:** Multinomial Naive Bayes

---

## ▶️ How to Run the Project


# Clone the repository
- **git clone https://github.com/rohitha-k/Email-Spam-Classifier.git**
- **cd Email-Spam-Classifier**

- **# Install dependencies**
- **pip install -r requirements.txt**

- **# Train the model**
  - ** python model.py **

 - **# Run the Flask app**
- **python app.py **

- **# Visit the app**
 - **http://127.0.0.1:5000**
---
 ## 🔍 Sample Inputs
Email Text Example	Predicted Label
- **"Congratulations! You've won a free iPhone. Click to claim!"=	Spam**
- **"Can you send the meeting notes by EOD?"	=Ham**
- **"Hurry up! Sale ends tonight. Limited stock!"=	Spam**
- **"Let's catch up over lunch tomorrow."	=Ham**
  ---

## ✍️ Author
- **Rohitha K**

