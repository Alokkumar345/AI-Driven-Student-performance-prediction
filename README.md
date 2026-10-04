# 🎓 Student Score Prediction System
**project link:** https://ai-driven-student-performance-prediction-xbks2ffbyjcfp4gctz6ha.streamlit.app/

A Machine Learning-based web application that predicts a student's **final score** based on academic performance, attendance, study habits, internal marks, assignments, sleep, and other student-related factors.

The application is built using **Python, Scikit-learn, Pandas, Joblib, and Streamlit** and provides an easy-to-use interface for making real-time predictions.

---

## 🚀 Project Overview

The **Student Score Prediction System** uses a trained **Ridge Regression model** to predict the final score of a student.

Users enter student information through a Streamlit web interface, and the application processes the input and generates:

* 🎯 Predicted Final Score
* 📊 Performance Category

This project demonstrates a complete basic **Machine Learning deployment workflow**:

**Data → Preprocessing → Model Training → Model Saving → Streamlit Deployment → Prediction**

---

## ✨ Features

* 🎓 Student final score prediction
* 📊 Interactive Streamlit interface
* 🤖 Ridge Regression Machine Learning model
* 🔢 Numerical and categorical input handling
* ⚡ Real-time prediction
* 📈 Performance category generation
* 💾 Saved model using Joblib
* 🖥️ Simple and user-friendly UI

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Pandas
* Scikit-learn
* Joblib
* Streamlit

### Machine Learning

* Ridge Regression
* Regression-based score prediction

---

## 📋 Input Features

The model uses the following student attributes:

| Feature                 | Description                     |
| ----------------------- | ------------------------------- |
| `gender`                | Student gender                  |
| `attendance_pct`        | Attendance percentage           |
| `study_hours_per_day`   | Average daily study hours       |
| `previous_score`        | Previous academic score         |
| `assignment_avg`        | Average assignment marks        |
| `internal_marks`        | Internal examination marks      |
| `sleep_hours`           | Average daily sleep hours       |
| `classes_missed`        | Number of classes missed        |
| `extracurricular_level` | Low, Medium, or High            |
| `internet_access`       | Availability of internet access |
| `parent_education`      | Parent's education level        |

---

## 📊 Performance Categories

Based on the predicted score, the application classifies student performance as:

| Predicted Score | Category     |
| --------------: | ------------ |
|            ≤ 40 | ❌ Fail       |
|     40.1 – 54.9 | 📊 Average   |
|       55 – 67.8 | 👍 Good      |
|          > 67.8 | Out of Range |

---

## 📁 Project Structure

```text
Student-Score-Prediction/
│
├── app.py
├── best_ridge_model.pkl
├── requirements.txt
├── README.md
└── dataset/
    └── student_data.csv
```

> `app.py` contains the Streamlit application and `best_ridge_model.pkl` contains the trained Ridge Regression model.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Student-Score-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd Student-Score-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧠 Machine Learning Workflow

The project follows these steps:

```text
Student Dataset
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Feature Selection
       ↓
Categorical Encoding
       ↓
Train-Test Split
       ↓
Feature Scaling
       ↓
Ridge Regression
       ↓
Model Evaluation
       ↓
Save Best Model
       ↓
Joblib
       ↓
Streamlit Application
       ↓
Student Score Prediction
```

---

## 🤖 Why Ridge Regression?

Ridge Regression is a regularized version of Linear Regression.

It adds an **L2 regularization penalty** to the model to reduce the impact of very large coefficients and help prevent overfitting.

The basic objective is:

```text
Loss = MSE + α × Σ(coefficient²)
```

where:

* `MSE` = Mean Squared Error
* `α` = Regularization strength
* Coefficients = Model parameters

---

## 💻 Example Prediction

Suppose a student provides:

```text
Attendance:          85%
Study Hours:         4 hours/day
Previous Score:      75
Assignment Average:  80
Internal Marks:      78
Sleep Hours:         7
Classes Missed:      3
Extracurricular:     Medium
Internet Access:     Yes
Parent Education:    Graduate
```

The model may produce:

```text
🎯 Predicted Final Score: 76.42
📊 Performance Category: Out of Range
```

> The actual prediction depends on the trained model and input values.

---

## 📦 Requirements

Create a `requirements.txt` file:

```text
streamlit
pandas
scikit-learn
joblib
```

Then install them using:

```bash
pip install -r requirements.txt
```

---

## 🌐 Deployment

This Streamlit application can be deployed using platforms such as:

* Streamlit Community Cloud
* Render
* Hugging Face Spaces
* Other Python-compatible cloud platforms

For deployment, make sure the repository contains:

```text
app.py
best_ridge_model.pkl
requirements.txt
```

---

## 🔮 Future Improvements

Possible improvements include:

* 📈 Add data visualization and EDA dashboard
* 🤖 Compare multiple ML models
* 📊 Display model evaluation metrics
* 🎯 Improve prediction accuracy
* 📱 Improve UI/UX
* 🔐 Add user authentication
* 🗄️ Store prediction history in a database
* 📥 Allow CSV file upload for multiple predictions
* ☁️ Deploy the application online
* 📊 Add feature importance / model explainability using SHAP
* 🧠 Add advanced models such as Random Forest, XGBoost, or Gradient Boosting

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Perform data preprocessing
* Handle numerical and categorical features
* Train regression models
* Apply Ridge Regression
* Save and load ML models using Joblib
* Create interactive ML applications using Streamlit
* Connect a trained ML model with a frontend interface
* Deploy a Machine Learning project

---

## 👨‍💻 Author

**Alok Kumar**

B.Tech CSE (AI) Student

Interested in **Machine Learning, Deep Learning, NLP, and AI Engineering**.

---

## ⭐ If You Like This Project

If you find this project useful, consider giving it a ⭐ on GitHub!

