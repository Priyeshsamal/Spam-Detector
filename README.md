# 📩 Spam Message Detector

A simple Machine Learning project that classifies messages as **Spam** or **Not Spam** using Natural Language Processing (NLP).

---

## 📌 Project Overview

This project takes a text message as input and predicts whether it is spam or not using a trained ML model.

---

## ⚙️ Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## 🧠 How It Works

1. Dataset is created with spam and normal messages  
2. Text is converted into numbers using CountVectorizer  
3. Naive Bayes algorithm is used for classification  
4. The model predicts whether the message is spam or not  

---

## 🚀 How to Run

1. Install required libraries:

pip install pandas scikit-learn streamlit


2. Train the model:

python model.py


3. Run the app:

python -m streamlit run app.py


---

## 📸 Output

- Enter a message  
- Click **Check**  
- Get result:  
  - 🚫 Spam  
  - ✅ Not Spam  

---

## 📂 Project Structure


Spam-Detector/
│
├── app.py
├── model.py
├── model.pkl
├── vectorizer.pkl
├── spam.csv
├── requirements.txt


---

## 🎯 Features

- Simple and easy to use  
- Fast prediction  
- Works completely offline  

---

## 🔮 Future Improvements

- Use larger dataset  
- Improve accuracy  
- Add more NLP techniques  

---

## 👨‍💻 Author

Priyesh Satrughn Samal