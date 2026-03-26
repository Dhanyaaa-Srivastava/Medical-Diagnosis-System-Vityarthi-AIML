# 🧠 Medical Diagnosis Expert System

A rule-based **AI-powered medical diagnosis system** built using **Prolog, Python (Flask), and Web Technologies**.  
This project demonstrates how classical AI techniques like **knowledge representation** and **backward chaining inference** can be applied to real-world problems.

---

## 📌 Overview

This system allows users to select symptoms through a web interface and receive possible diagnoses based on a Prolog knowledge base.

It uses:
- 🧠 Prolog for reasoning and inference  
- ⚙️ Python (Flask) as backend API  
- 🌐 HTML, CSS, JavaScript for frontend UI  

---

## 🚀 Features

- Interactive symptom selection UI  
- Rule-based diagnosis using Prolog  
- REST API integration (Flask backend)  
- Match percentage calculation for diseases  
- Severity classification (Mild / Moderate / Severe)  
- Precaution suggestions for each disease  
- Offline fallback (pure Python logic if Prolog unavailable)

---

## 🏗️ System Architecture

Frontend (HTML/CSS/JS)  
↓  
Backend (Flask API)  
↓  
AI Engine (SWI-Prolog)

### Components

| Layer | Technology | Description |
|------|------------|-------------|
| Frontend | HTML, CSS, JS | User interface |
| Backend | Python + Flask | API & Prolog integration |
| AI Engine | SWI-Prolog | Knowledge base + inference |

---

## 🧠 How It Works

1. User selects symptoms from UI  
2. Symptoms are sent to Flask backend  
3. Backend runs a Prolog query  
4. Prolog:
   - Matches symptoms with diseases  
   - Calculates match percentage  
   - Returns diseases with ≥ 50% match  
5. Results displayed in UI with diagnosis, severity, and precautions

---

## 📂 Project Structure

project/
│
├── app.py                # Flask backend
├── index.html            # Frontend UI
├── knowledge_base.pl     # Prolog knowledge base
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies (optional)

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.x  
- SWI-Prolog installed  
- pip  

---

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/medical-expert-system.git
cd medical-expert-system
```

### Step 2: Install Dependencies

```bash
pip install flask flask-cors
```

### Step 3: Install SWI-Prolog

Download from: https://www.swi-prolog.org/  
Ensure it is added to your system PATH.

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

http://localhost:5000

---

## 🧪 Example Input

Symptoms:
```
fever, cough, fatigue, loss_of_smell, loss_of_taste
```

Output:
```
Disease: COVID-19
Match: 71%
Severity: Moderate
```

---

## 📊 Knowledge Base

- 36 Symptoms  
- 15 Diseases  
- 50% match threshold  

Each disease includes:
- Name
- Symptoms
- Description
- Severity
- Precautions

---

## ⚠️ Limitations

- All symptoms have equal weight  
- No time-based symptom analysis  
- No lab test integration  
- Limited disease coverage  
- Possible false positives with small symptom sets  

---

## 🔮 Future Enhancements

- Symptom weighting system  
- Bayesian probability model  
- Conversational chatbot interface  
- Integration with medical datasets (ICD-10)  
- Support for lab test inputs  

---

## 📚 Technologies Used

- Python (Flask)
- SWI-Prolog
- HTML
- CSS
- JavaScript
- JSON

---

## 🎓 Academic Context

This project was developed as part of:

CSA2001 – Fundamentals in AI & ML

It demonstrates:
- Knowledge Representation
- Logical Reasoning
- Expert Systems
- AI-based Decision Making

---

## ⚠️ Disclaimer

This system is for **educational purposes only** and is **not a substitute for professional medical advice**.

---

## 👨‍💻 Author

Dhanya Srivastava  
B.Tech AI & ML  

---

## 📖 References

- Artificial Intelligence: A Modern Approach – Russell & Norvig  
- Prolog Programming for Artificial Intelligence – Ivan Bratko  
- SWI-Prolog Documentation  
- Flask Documentation
