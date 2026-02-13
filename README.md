# 📧 Spam Email Detection  

<p align="center">
  <b>A Machine Learning Powered Web Application to Detect Spam Emails Using Stacking Classifier</b>
</p>

<p align="center">
  Built using Python, Scikit-learn, Streamlit & MySQL
</p>

---

## 🚀 Project Overview

**Spam Email Detection** is a web-based application that classifies emails as **Spam** or **Not Spam** using multiple machine learning algorithms combined through a powerful **Stacking Classifier** to improve accuracy and prediction stability.

The application transforms raw email text using **TF-IDF Vectorization** and provides a secure login system to ensure controlled access and search history tracking.

---

## ✨ Key Features

### 🧠 Advanced Stacking Classifier
- Combines multiple machine learning models:
  - Support Vector Machine (SVM)
  - Random Forest
  - Naive Bayes
- Enhances overall model accuracy and robustness.
- Reduces bias and variance compared to single models.

### 📊 TF-IDF Text Vectorization
- Converts raw email text into numerical feature vectors.
- Highlights important words using Term Frequency–Inverse Document Frequency.
- Improves spam detection precision.

### 🌐 Interactive Web Interface
- Built using **Streamlit**
- Allows users to:
  - Enter email text
  - Instantly view prediction results
  - Interact with a clean and simple UI

### 🔐 Secure Login System
- User authentication enabled
- Restricts unauthorized access
- Stores and manages user search history securely in database

---

## 🛠️ Tech Stack

| Layer        | Technology Used |
|-------------|----------------|
| 🎨 Frontend | Streamlit |
| ⚙️ Backend  | Python, Scikit-learn |
| 🗄️ Database | MySQL |
| 📚 Libraries | Pandas, NumPy, TfidfVectorizer, Joblib |

---

## 🧠 Machine Learning Workflow

```text
Raw Email Text
        ↓
TF-IDF Vectorization
        ↓
Base Models:
   • Support Vector Machine
   • Random Forest
   • Naive Bayes
        ↓
Stacking Classifier
        ↓
Spam / Not Spam Prediction
```

---

## 📂 Project Structure

```
spam-email-detection/
│
├── model.ipynb          # Model training and preprocessing
├── main.py              # Streamlit frontend application
├── db.py                # Database connection and operations
├── model.joblib         # Saved trained stacking model
├── vectorizer.joblib    # Saved TF-IDF transformer
└── README.md
```

---

## ▶️ How to Run the Application

### Step 1️⃣: Train the Model

1. Open `model.ipynb`
2. Run all cells
3. This will:
   - Preprocess dataset
   - Train stacking classifier
   - Generate:
     - `model.joblib`
     - `vectorizer.joblib`

---

### Step 2️⃣: Run the Streamlit App

Open terminal in project directory and run:

```bash
streamlit run main.py
```

---

### Step 3️⃣: Access the Application

- Streamlit server will start automatically.
- Open the local URL shown in the terminal.
- Login and start detecting spam emails.

---

## 🔐 Security Implementation

- User authentication system
- Protected routes
- Secure database storage using MySQL
- Search history management per user

---

## 📈 Future Improvements

- Deploy on cloud platforms (AWS / Render / Railway)
- Integrate Deep Learning models (LSTM / BERT)
- Add performance analytics dashboard
- Email API integration for real-time spam scanning
- Improve UI/UX with advanced visualization

---

## 👨‍💻 Author

**Ashutosh Dash**

---

<p align="center">
  🚀 Keep Building. Keep Learning.
</p>
