"""
Medical Diagnosis Expert System - Python Backend
Course: CSA2001 - Fundamentals in AI and ML
Uses SWI-Prolog via pyswip to run the Prolog knowledge base.
Run: python app.py
"""

import os
import json
import subprocess
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = BASE_DIR

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_frontend():
    return send_from_directory(FRONTEND_DIR, 'index.html')

# Path to the Prolog knowledge base
PROLOG_KB_PATH = os.path.join(BASE_DIR, '..', 'prolog', 'knowledge_base.pl')

# ─────────────────────────────────────────────
# All known symptoms (mirrors knowledge_base.pl)
# ─────────────────────────────────────────────
SYMPTOMS_LIST = [
    {"id": "fever",               "label": "Fever",                "icon": "🌡️",  "category": "General"},
    {"id": "cough",               "label": "Cough",                "icon": "😮‍💨", "category": "Respiratory"},
    {"id": "sore_throat",         "label": "Sore Throat",          "icon": "🗣️",  "category": "Respiratory"},
    {"id": "runny_nose",          "label": "Runny Nose",           "icon": "🤧",  "category": "Respiratory"},
    {"id": "headache",            "label": "Headache",             "icon": "🤕",  "category": "Neurological"},
    {"id": "fatigue",             "label": "Fatigue",              "icon": "😴",  "category": "General"},
    {"id": "body_ache",           "label": "Body Ache",            "icon": "💪",  "category": "General"},
    {"id": "chills",              "label": "Chills",               "icon": "🥶",  "category": "General"},
    {"id": "nausea",              "label": "Nausea",               "icon": "🤢",  "category": "Digestive"},
    {"id": "vomiting",            "label": "Vomiting",             "icon": "🤮",  "category": "Digestive"},
    {"id": "diarrhea",            "label": "Diarrhea",             "icon": "🚽",  "category": "Digestive"},
    {"id": "shortness_of_breath", "label": "Shortness of Breath",  "icon": "💨",  "category": "Respiratory"},
    {"id": "chest_pain",          "label": "Chest Pain",           "icon": "💔",  "category": "Cardiac"},
    {"id": "rash",                "label": "Skin Rash",            "icon": "🔴",  "category": "Skin"},
    {"id": "itching",             "label": "Itching",              "icon": "😖",  "category": "Skin"},
    {"id": "loss_of_appetite",    "label": "Loss of Appetite",     "icon": "🍽️",  "category": "Digestive"},
    {"id": "sweating",            "label": "Excessive Sweating",   "icon": "💧",  "category": "General"},
    {"id": "dizziness",           "label": "Dizziness",            "icon": "😵",  "category": "Neurological"},
    {"id": "sneezing",            "label": "Sneezing",             "icon": "🤧",  "category": "Respiratory"},
    {"id": "watery_eyes",         "label": "Watery Eyes",          "icon": "👁️",  "category": "General"},
    {"id": "stomach_pain",        "label": "Stomach Pain",         "icon": "🤒",  "category": "Digestive"},
    {"id": "stiff_neck",          "label": "Stiff Neck",           "icon": "🦒",  "category": "Neurological"},
    {"id": "sensitivity_to_light","label": "Sensitivity to Light", "icon": "🔆",  "category": "Neurological"},
    {"id": "yellow_skin",         "label": "Yellow Skin",          "icon": "💛",  "category": "Skin"},
    {"id": "dark_urine",          "label": "Dark Urine",           "icon": "🫗",  "category": "General"},
    {"id": "frequent_urination",  "label": "Frequent Urination",   "icon": "🚾",  "category": "General"},
    {"id": "excessive_thirst",    "label": "Excessive Thirst",     "icon": "🥤",  "category": "General"},
    {"id": "blurred_vision",      "label": "Blurred Vision",       "icon": "👓",  "category": "Neurological"},
    {"id": "slow_healing",        "label": "Slow Healing Wounds",  "icon": "🩹",  "category": "General"},
    {"id": "dry_mouth",           "label": "Dry Mouth",            "icon": "👅",  "category": "General"},
    {"id": "joint_pain",          "label": "Joint Pain",           "icon": "🦴",  "category": "Musculoskeletal"},
    {"id": "swollen_joints",      "label": "Swollen Joints",       "icon": "🦵",  "category": "Musculoskeletal"},
    {"id": "morning_stiffness",   "label": "Morning Stiffness",    "icon": "🌅",  "category": "Musculoskeletal"},
    {"id": "loss_of_smell",       "label": "Loss of Smell",        "icon": "👃",  "category": "Neurological"},
    {"id": "loss_of_taste",       "label": "Loss of Taste",        "icon": "👄",  "category": "Neurological"},
    {"id": "muscle_weakness",     "label": "Muscle Weakness",      "icon": "💪",  "category": "Musculoskeletal"},
]


def run_prolog_diagnosis(symptoms: list[str]) -> list[dict]:
    """
    Calls SWI-Prolog as a subprocess and parses JSON output.
    The Prolog query outputs results in a JSON-friendly format.
    """
    if not symptoms:
        return []

    # Build symptom list in Prolog list syntax
    symptom_list = "[" + ",".join(symptoms) + "]"

    # Prolog query: load KB, run diagnosis, print JSON, halt
    prolog_query = f"""
    :- use_module(library(lists)).
    :- consult('{os.path.abspath(PROLOG_KB_PATH)}').
    :- 
        Symptoms = {symptom_list},
        get_all_diagnoses(Symptoms, Results),
        (   Results = []
        ->  write('[]'), nl
        ;   write('['), nl,
            print_results(Results, first)
        ),
        halt.

    print_results([], _).
    print_results([result(Pct, Disease, Desc, Sev, Prec)|Rest], State) :-
        (State = first -> true ; write(','), nl),
        atom_string(Disease, DiseaseStr),
        atom_string(Sev, SevStr),
        atom_string(Desc, DescStr),
        maplist([P, S]>>(atom_string(P, S)), Prec, PrecStrings),
        atomic_list_concat(PrecStrings, '|SPLIT|', PrecJoined),
        atom_string(PrecJoined, PrecStr),
        PctRounded is round(Pct),
        format('  {{"disease":"~w","percentage":~w,"description":"~w","severity":"~w","precautions":"~w"}}',
               [DiseaseStr, PctRounded, DescStr, SevStr, PrecStr]),
        print_results(Rest, next).
    """

    try:
        result = subprocess.run(
            ['swipl', '-q', '-g', 'true', '-t', 'halt', '--'],
            input=prolog_query,
            capture_output=True,
            text=True,
            timeout=10
        )

        output = result.stdout.strip()
        if not output or output == '[]':
            return []

        # Close the JSON array
        if not output.endswith(']'):
            output += '\n]'

        diagnoses = json.loads(output)
        
        # Process precautions string back to list
        processed = []
        for d in diagnoses:
            precautions = d.get("precautions", "").split("|SPLIT|")
            processed.append({
                "disease": d["disease"].replace("_", " ").title(),
                "disease_id": d["disease"],
                "percentage": d["percentage"],
                "description": d["description"],
                "severity": d["severity"],
                "precautions": [p.strip() for p in precautions if p.strip()]
            })
        return processed

    except subprocess.TimeoutExpired:
        return []
    except (json.JSONDecodeError, Exception):
        # Fallback: use built-in Python diagnosis if SWI-Prolog not available
        return python_fallback_diagnosis(symptoms)


def python_fallback_diagnosis(symptoms: list[str]) -> list[dict]:
    """
    Pure Python implementation of the Prolog knowledge base.
    Used as fallback if SWI-Prolog is not installed.
    """
    DISEASES = [
        {
            "disease_id": "common_cold",
            "disease": "Common Cold",
            "symptoms": ["runny_nose", "sneezing", "sore_throat", "cough", "headache"],
            "description": "A viral infection of the upper respiratory tract.",
            "severity": "mild",
            "precautions": ["Rest and stay hydrated", "Use saline nasal spray", "Take OTC cold medicine", "Avoid close contact with others"]
        },
        {
            "disease_id": "influenza",
            "disease": "Influenza",
            "symptoms": ["fever", "cough", "sore_throat", "body_ache", "headache", "fatigue", "chills"],
            "description": "A contagious respiratory illness caused by influenza viruses.",
            "severity": "moderate",
            "precautions": ["Get annual flu vaccine", "Rest adequately", "Drink plenty of fluids", "Antiviral drugs may help if taken early"]
        },
        {
            "disease_id": "covid_19",
            "disease": "Covid 19",
            "symptoms": ["fever", "cough", "fatigue", "loss_of_smell", "loss_of_taste", "shortness_of_breath", "body_ache"],
            "description": "A respiratory illness caused by the SARS-CoV-2 coronavirus.",
            "severity": "moderate",
            "precautions": ["Isolate immediately", "Get tested", "Monitor oxygen levels", "Seek emergency care if breathing worsens", "Get vaccinated"]
        },
        {
            "disease_id": "dengue_fever",
            "disease": "Dengue Fever",
            "symptoms": ["fever", "headache", "body_ache", "rash", "nausea", "vomiting", "fatigue"],
            "description": "A mosquito-borne viral disease prevalent in tropical regions.",
            "severity": "moderate",
            "precautions": ["Use mosquito repellent", "Stay hydrated", "Monitor platelet count", "Avoid aspirin or ibuprofen", "Hospitalize if severe"]
        },
        {
            "disease_id": "malaria",
            "disease": "Malaria",
            "symptoms": ["fever", "chills", "sweating", "headache", "nausea", "vomiting", "fatigue"],
            "description": "A life-threatening disease caused by Plasmodium parasites transmitted by mosquitoes.",
            "severity": "severe",
            "precautions": ["Take prescribed antimalarial drugs", "Use mosquito nets", "Seek immediate medical care", "Complete full course of medication"]
        },
        {
            "disease_id": "typhoid_fever",
            "disease": "Typhoid Fever",
            "symptoms": ["fever", "headache", "stomach_pain", "nausea", "loss_of_appetite", "fatigue", "diarrhea"],
            "description": "A bacterial infection caused by Salmonella typhi, spread through contaminated food and water.",
            "severity": "moderate",
            "precautions": ["Take prescribed antibiotics", "Drink only boiled or purified water", "Wash hands frequently", "Get vaccinated"]
        },
        {
            "disease_id": "gastroenteritis",
            "disease": "Gastroenteritis",
            "symptoms": ["nausea", "vomiting", "diarrhea", "stomach_pain", "fever", "fatigue"],
            "description": "Inflammation of the stomach and intestines, commonly called stomach flu.",
            "severity": "mild",
            "precautions": ["Stay hydrated with ORS", "Eat light easily digestible food", "Rest", "Wash hands frequently"]
        },
        {
            "disease_id": "pneumonia",
            "disease": "Pneumonia",
            "symptoms": ["fever", "cough", "shortness_of_breath", "chest_pain", "fatigue", "chills"],
            "description": "A serious lung infection that inflames air sacs in one or both lungs.",
            "severity": "severe",
            "precautions": ["Seek immediate medical care", "Take prescribed antibiotics", "Rest completely", "Get pneumococcal vaccine", "Avoid smoking"]
        },
        {
            "disease_id": "allergic_rhinitis",
            "disease": "Allergic Rhinitis",
            "symptoms": ["sneezing", "runny_nose", "itching", "watery_eyes", "headache"],
            "description": "An allergic response causing cold-like symptoms, triggered by pollen, dust or animal dander.",
            "severity": "mild",
            "precautions": ["Identify and avoid allergens", "Use antihistamines", "Keep windows closed during high pollen", "Use air purifier at home"]
        },
        {
            "disease_id": "type2_diabetes",
            "disease": "Type 2 Diabetes",
            "symptoms": ["frequent_urination", "excessive_thirst", "fatigue", "blurred_vision", "slow_healing", "dry_mouth"],
            "description": "A chronic condition affecting blood sugar regulation due to insulin resistance.",
            "severity": "severe",
            "precautions": ["Monitor blood sugar regularly", "Follow a low-sugar diet", "Exercise daily", "Take prescribed medication", "Regular doctor checkups"]
        },
        {
            "disease_id": "arthritis",
            "disease": "Arthritis",
            "symptoms": ["joint_pain", "swollen_joints", "morning_stiffness", "fatigue", "body_ache"],
            "description": "Inflammation of one or more joints causing pain and stiffness.",
            "severity": "moderate",
            "precautions": ["Regular low-impact exercise", "Take anti-inflammatory medication", "Physical therapy", "Maintain healthy weight", "Apply hot/cold packs"]
        },
        {
            "disease_id": "meningitis",
            "disease": "Meningitis",
            "symptoms": ["fever", "headache", "stiff_neck", "nausea", "sensitivity_to_light", "fatigue"],
            "description": "Inflammation of membranes surrounding the brain and spinal cord, often due to infection.",
            "severity": "severe",
            "precautions": ["SEEK EMERGENCY MEDICAL CARE IMMEDIATELY", "Hospitalization required", "Antibiotics or antiviral treatment", "Meningitis vaccine available"]
        },
        {
            "disease_id": "jaundice",
            "disease": "Jaundice",
            "symptoms": ["yellow_skin", "dark_urine", "fatigue", "nausea", "loss_of_appetite", "stomach_pain"],
            "description": "A condition causing yellowing of skin and eyes due to excess bilirubin in the blood.",
            "severity": "moderate",
            "precautions": ["Rest completely", "Avoid alcohol", "Stay hydrated", "Eat a healthy liver-friendly diet", "Seek medical evaluation for root cause"]
        },
        {
            "disease_id": "migraine",
            "disease": "Migraine",
            "symptoms": ["headache", "nausea", "sensitivity_to_light", "dizziness", "fatigue", "vomiting"],
            "description": "A neurological condition causing intense recurring headaches often with other symptoms.",
            "severity": "moderate",
            "precautions": ["Rest in a dark quiet room", "Take prescribed migraine medication", "Stay hydrated", "Identify and avoid personal triggers", "Track episodes in a journal"]
        },
        {
            "disease_id": "asthma",
            "disease": "Asthma",
            "symptoms": ["shortness_of_breath", "cough", "chest_pain", "fatigue"],
            "description": "A chronic respiratory condition where airways narrow and swell, producing extra mucus.",
            "severity": "moderate",
            "precautions": ["Use prescribed inhaler", "Avoid known triggers", "Monitor peak flow", "Create an asthma action plan", "Regular pulmonologist visits"]
        },
    ]

    results = []
    user_set = set(symptoms)
    for d in DISEASES:
        disease_symptoms = set(d["symptoms"])
        matched = len(user_set & disease_symptoms)
        total = len(disease_symptoms)
        pct = round((matched / total) * 100) if total > 0 else 0
        if pct >= 50:
            results.append({
                "disease": d["disease"],
                "disease_id": d["disease_id"],
                "percentage": pct,
                "description": d["description"],
                "severity": d["severity"],
                "precautions": d["precautions"]
            })

    results.sort(key=lambda x: x["percentage"], reverse=True)
    return results


# ─────────────────────────────────────────────
# API ROUTES
# ─────────────────────────────────────────────

@app.route('/api/symptoms', methods=['GET'])
def get_symptoms():
    """Return all known symptoms."""
    return jsonify({"symptoms": SYMPTOMS_LIST})


@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    """
    Accepts a list of symptom IDs and returns diagnosis results.
    Body: { "symptoms": ["fever", "cough", "fatigue"] }
    """
    data = request.get_json()
    if not data or "symptoms" not in data:
        return jsonify({"error": "Please provide a 'symptoms' list."}), 400

    symptoms = data["symptoms"]
    if not isinstance(symptoms, list) or len(symptoms) == 0:
        return jsonify({"error": "symptoms must be a non-empty list."}), 400

    # Try SWI-Prolog first, fallback to Python
    try:
        result = subprocess.run(['swipl', '--version'], capture_output=True, timeout=3)
        use_prolog = result.returncode == 0
    except Exception:
        use_prolog = False

    if use_prolog:
        diagnoses = run_prolog_diagnosis(symptoms)
        engine = "SWI-Prolog"
    else:
        diagnoses = python_fallback_diagnosis(symptoms)
        engine = "Python (Prolog fallback)"

    return jsonify({
        "input_symptoms": symptoms,
        "symptom_count": len(symptoms),
        "diagnoses": diagnoses,
        "total_found": len(diagnoses),
        "engine": engine,
        "disclaimer": "This is an educational AI tool only. Always consult a qualified medical professional for real diagnosis."
    })


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "running", "system": "Medical Diagnosis Expert System"})


if __name__ == '__main__':
    print("=" * 55)
    print("  Medical Diagnosis Expert System")
    print("  CSA2001 - Fundamentals in AI and ML")
    print("=" * 55)
    print(f"  Prolog KB: {os.path.abspath(PROLOG_KB_PATH)}")
    print("  API running at: http://localhost:5000")
    print("=" * 55)
    app.run(debug=True, port=5000)
