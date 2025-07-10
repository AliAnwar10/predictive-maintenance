# predictive-maintenance
AI-based Predictive Maintenance using Random Forest  Streamlit
1. 🔍 Problem Statement

2. 📌 Project Description

3. ✅ Solution Overview

4. 🛠️ Technologies Used

5. 📂 Project Structure

6. 💻 Setup Instructions

7. 🧪 Example Usage

8. 📊 Sample Input

9. 📬 Contact

**# 🔧 Predictive Maintenance using Machine Learning**

**## 🔍 Problem Statement**

Unplanned machine failures in industrial environments can lead to serious downtime, high costs, and safety risks. Traditional maintenance schedules are time-based and reactive rather than proactive, which is inefficient.

---
**
## 📌 Project Description**

This project aims to build an intelligent system that can **predict potential failures of machines** in a manufacturing setting by analyzing sensor data. The goal is to shift from reactive maintenance to **predictive maintenance**, thereby reducing costs and improving equipment efficiency.

---

**## ✅ Solution Overview**

- 📊 Performed exploratory data analysis on real-world machine sensor data  
- 🧠 Trained a **Random Forest Classifier** to detect early signs of failure  
- 🗂️ Saved the trained model using `joblib`  
- 🌐 Built a **Streamlit web app** to allow users to upload `.csv` files and receive predictions in real-time  
- 📁 Structured the project for clarity and scalability

---
**
## 🛠️ Technologies Used
**
- Python 3.x
- Jupyter Notebook
- Pandas, NumPy, scikit-learn, joblib
- Streamlit (for the web interface)
- VS Code & Git/GitHub

---

**## 📂 Project Structure
**
predictive-maintenance/
├── app/
│ └── app.py # Streamlit application
├── data/
│ └── predictive_maintenance.csv
├── models/
│ └── maintenance_model.pkl # Trained ML model
├── notebooks/
│ └── predictive_maintenance.ipynb
├── requirements.txt
├── README.md
└── .gitignore


---

## 💻 Setup Instructions

1. **Clone this repository:**

bash
git clone https://github.com/AliAnwar10/predictive-maintenance.git
cd predictive-maintenance

**2. Create a virtual environment:**

python -m venv venv
venv\Scripts\activate  # On Windows

**3. Install required packages:**

pip install -r requirements.txt

**4. Run the Streamlit app:**

streamlit run app/app.py
**🧪 Example Usage**
Visit http://localhost:8501 in your browser

Upload a .csv file with machine sensor readings

Click on Predict Failures

View predictions instantly (0 = No failure, 1 = Failure risk)

**📊 Sample Input Format**


Type,Air temperature [K],Process temperature [K],Rotational speed [rpm],Torque [Nm],Tool wear [min]
M,298.1,308.6,1551,42.8,0
H,298.3,309.1,1600,45.2,12
The app one-hot encodes Type internally and uses the trained model to predict failure.
**
📬 Contact**
Author: Ali Anwar

GitHub: @AliAnwar10

Email: alianwar50k@email.com
