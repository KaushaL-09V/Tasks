# 🧮 Simple Calculator Project

A Python-based calculator application that supports both:

- 💻 Command Line Interface (CLI)
- 🌐 Web Interface using Streamlit

The calculator performs operations on multiple numbers using a clean OOP structure.

---

## 🚀 Tech Stack

- **Python 3.10+** (uses `match-case`)
- **Streamlit** (for GUI / Web App)
- **OOP (Object-Oriented Programming)**
- **Virtual Environment (.venv)**

---

## 📁 Project Structure

```
TASK_1/
│
├── Calc.py
├── main.py
├── GUI.py
├── requirements.txt
└── .venv
```

---

## 📄 File Explanation

### 1️⃣ Calc.py
- Contains the `Calculator` class.
- Implements the `calculate()` method.
- Uses `match-case` (switch case) to perform:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Handles:
  - Division by zero
  - Invalid operation
  - Less than two numbers & more than two numbers also supported

This file contains the **core business logic**.

---

### 2️⃣ main.py
- CLI (Command Line Interface) version.
- Takes user input from terminal.
- Accepts:
  - Operation (+, -, *, /)
  - Multiple numbers separated by space
- Calls the `Calculator` class.
- Prints the result in terminal.

---

### 3️⃣ GUI.py
- Streamlit-based Web Interface.
- Uses:
  - Dropdown for operation selection
  - Text input for numbers
  - Button to calculate
- Displays:
  - Result (success message)
  - Error messages (if invalid input)

This file acts as the **frontend** of the project.

---

### 4️⃣ requirements.txt
Contains required Python packages:

```
streamlit
```

Used to install dependencies easily.

---

# ⚙️ Installation Guide

## Step 1️⃣ Clone or Download the Project

```
git clone https://github.com/KaushaL-09V/Tasks.git
cd TASK_1
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

# ▶ Running the Project

## 💻 Run CLI Version

From project root folder:

```
python main.py
```

Example:
```
Enter operation: +
Enter numbers separated by space: 10 20 30
Result: 60.0
```

---

## 🌐 Run Streamlit (Web Version)

From project root folder:

```
streamlit run GUI.py
```

It will open automatically in your browser at:

```
http://localhost:8501
```

---

# 🎯 Features

- Supports multiple numbers
- Uses OOP structure
- Clean separation of logic and UI
- Error handling
- Two interfaces (CLI + Web)


---

# 👨‍💻 Author

Kaushal Vadher

---
