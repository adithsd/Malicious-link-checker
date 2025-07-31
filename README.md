# 🔍 Malicious Link Checker

A Flask web application that uses machine learning to predict whether a given URL is **malicious** or **legitimate** based on historical features.

---

## 🚀 Features

- 🔐 Real-time URL classification using ML
- 🧠 Multiple model support (Random Forest, MLP, Decision Tree)
- 🌗 Dark Mode toggle for better UX
- ⚡ Fast, responsive Bootstrap 5 UI
- 🧰 Easily extensible for new models or features

---

## 📸 Screenshot

![App Screenshot](static/demo.png)




## 🧠 How It Works

1. User enters a URL and selects a model.
2. Flask backend extracts key features from the URL.
3. Selected ML model makes a prediction.
4. The result is classified as **Malicious** or **Legitimate**.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, Bootstrap 5
- **ML Models**: Scikit-learn, joblib
- **Deployment Ready**: Built for GitHub and future deployment

---

## ⚙️ Run Locally

Clone the repo and run it locally:

```bash
git clone https://github.com/adithsd/Malicious-link-checker.git
cd Malicious-link-checker
pip install -r requirements.txt
python Flaskserver.py