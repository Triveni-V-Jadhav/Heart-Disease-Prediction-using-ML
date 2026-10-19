# ❤️ Heart Disease Prediction System

A machine learning web application that predicts the likelihood of heart disease based on user-provided health parameters. The application uses a trained Random Forest Classifier and provides prediction results through an interactive Streamlit interface.

## 📌 Project Overview

The Heart Disease Prediction System is developed using Python and Machine Learning. Users enter health-related information, and the trained model generates a prediction. The application also displays a probability estimate, a visualization, and a downloadable PDF report.

**Note:** This project is for educational purposes only and is not a substitute for professional medical advice or diagnosis.

## ✨ Features

- User-friendly web interface using Streamlit
- Heart disease prediction using a trained Random Forest model
- Health parameter input form
- Prediction result and probability estimate
- Graphical visualization of the result
- Downloadable PDF report
- Background image and customized interface


## 🛠️ Technologies Used
Python: Main programming language used to develop the application.

Streamlit: Used to create the interactive web interface.

Scikit-learn: Used to train the Random Forest classification model.

Pandas: Used for data handling and preprocessing.

Joblib: Used to save and load the trained machine learning model.

Matplotlib: Used to visualize prediction results.

FPDF: Used to generate downloadable PDF reports.

HTML and CSS: Used where applicable for interface styling.

## 🧠 Machine Learning Algorithm

**Random Forest Classifier**

Random Forest is a supervised machine learning algorithm that combines multiple decision trees to make a classification prediction.

The model is trained using a heart disease dataset and saved as `model.pkl` for use by the application.

## 📂 Project Structure

heart_disease_ui_project/
│
├── app.py
├── train_model.py
├── model.pkl
├── bg.jpg
├── dataset.csv
├── README.md
├── requirements.txt
└── screenshots/
    ├── home.png
    ├── input-form.png
    ├── prediction-result.png
    ├── prediction-chart.png
    └── pdf-report.png

## ⚙️ Installation and Setup

### Step 1: Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL


Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### Step 2: Open the project folder

cd heart_disease_ui_project


### Step 3: Create a virtual environment (optional)

python -m venv venv

Activate it on Windows:

.\venv\Scripts\Activate.ps1


### Step 4: Install the required libraries


pip install -r requirements.txt

### Step 5: Run the application

python -m streamlit run app.py


The application will open in your browser, usually at:

`http://localhost:8501`

## 📊 Expected Output

- Displays a prediction based on the entered health parameters.
- Shows a probability estimate from the trained model.
- Presents a visualization of the prediction.
- Allows the user to download a PDF report.

The model's output is an educational estimate, not a clinically validated assessment of an individual's actual heart disease risk.

## 🎯 Project Objective

To demonstrate how machine learning can be integrated with a web application to analyze health-related input data and present a prediction in an understandable format.


