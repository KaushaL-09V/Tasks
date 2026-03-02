# 🧠 ML Calculator (Clustered Regression)

This project demonstrates how Machine Learning can approximate basic calculator operations (+, −, ×, ÷) using separate regression models for each operator.

Instead of directly applying mathematical formulas, the project:
- Generates synthetic calculator data
- Splits data based on operators
- Trains individual Polynomial Regression models
- Saves trained models for prediction


---

## 🛠 Tech Stack

- Python 3.10+
- Pandas
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📄 File Description

### `data_generator.py`
Generates synthetic dataset containing:
- num1
- num2
- operator (+, -, *, /)
- output

Saves the dataset as `calculator_data.csv`.

---

### `calculator_data.csv`
Dataset used for training regression models.

---

### `train_clustered_models.ipynb`
- Splits dataset based on operator
- Trains separate Polynomial Regression models
- Saves trained models in `saved_model/`

---

### `saved_model/`
Contains trained models:
- `model_add.pkl`
- `model_subtract.pkl`
- `model_multiply.pkl`
- `model_divide.pkl`

---

### `requirements.txt`
Contains required Python dependencies.

---
# ⚙️ Installation Guide

## Step 1️⃣ Clone or Download the Project

```
git clone https://github.com/KaushaL-09V/Tasks.git
cd TASK_2
```

---

## Step 2️⃣ Create Virtual Environment (Optional but Recommended)

```
python -m venv .venv
```

Activate it:

### Windows:
```
.venv\Scripts\activate
```

### Linux / Mac:
```
source .venv/bin/activate
```

---

## Step 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 2️⃣ Generate Dataset if not already generated

```bash
pip python Dataset/data_generator.py
```

### 3️⃣ Train Models
open and run:
```bash
train_clustered_models.ipynb
```