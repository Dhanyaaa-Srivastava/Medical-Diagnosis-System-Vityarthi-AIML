% ============================================================
% Medical Diagnosis Expert System - Prolog Knowledge Base
% Course: CSA2001 - Fundamentals in AI and ML
% ============================================================

% ------------------------------------------------------------
% SYMPTOM FACTS
% symptom(SymptomID, Description)
% ------------------------------------------------------------
symptom(fever, 'High body temperature').
symptom(cough, 'Persistent coughing').
symptom(sore_throat, 'Pain or irritation in the throat').
symptom(runny_nose, 'Excess nasal discharge').
symptom(headache, 'Pain in the head or upper neck').
symptom(fatigue, 'Extreme tiredness or lack of energy').
symptom(body_ache, 'Pain in muscles and joints').
symptom(chills, 'Feeling of coldness with shivering').
symptom(nausea, 'Feeling of wanting to vomit').
symptom(vomiting, 'Forceful emptying of stomach contents').
symptom(diarrhea, 'Loose or watery stools').
symptom(shortness_of_breath, 'Difficulty in breathing').
symptom(chest_pain, 'Pain or pressure in chest').
symptom(rash, 'Skin irritation or redness').
symptom(itching, 'Uncomfortable skin sensation').
symptom(loss_of_appetite, 'Reduced desire to eat').
symptom(sweating, 'Excessive perspiration').
symptom(dizziness, 'Feeling lightheaded or unsteady').
symptom(sneezing, 'Sudden expulsion of air through nose').
symptom(watery_eyes, 'Excessive tearing from eyes').
symptom(stomach_pain, 'Discomfort in abdominal area').
symptom(stiff_neck, 'Difficulty moving neck').
symptom(sensitivity_to_light, 'Discomfort from bright light').
symptom(yellow_skin, 'Yellowish discoloration of skin').
symptom(dark_urine, 'Unusually dark colored urine').
symptom(frequent_urination, 'Needing to urinate often').
symptom(excessive_thirst, 'Unusual or extreme thirst').
symptom(blurred_vision, 'Loss of sharpness in eyesight').
symptom(slow_healing, 'Wounds that heal slowly').
symptom(dry_mouth, 'Lack of moisture in mouth').
symptom(joint_pain, 'Pain in one or more joints').
symptom(swollen_joints, 'Inflammation around joints').
symptom(morning_stiffness, 'Stiffness after waking up').
symptom(loss_of_smell, 'Inability to detect odors').
symptom(loss_of_taste, 'Inability to taste food').
symptom(muscle_weakness, 'Reduced strength in muscles').

% ------------------------------------------------------------
% DISEASE RULES
% disease(Name, Symptoms, Description, Severity, Precautions)
% A disease is diagnosed when threshold symptoms are present.
% ------------------------------------------------------------

% --- Common Cold ---
disease(common_cold,
    [runny_nose, sneezing, sore_throat, cough, headache],
    'A viral infection of the upper respiratory tract.',
    mild,
    ['Rest and stay hydrated', 'Use saline nasal spray', 'Take OTC cold medicine', 'Avoid close contact with others']).

% --- Influenza (Flu) ---
disease(influenza,
    [fever, cough, sore_throat, body_ache, headache, fatigue, chills],
    'A contagious respiratory illness caused by influenza viruses.',
    moderate,
    ['Get annual flu vaccine', 'Rest adequately', 'Drink plenty of fluids', 'Antiviral drugs may help if taken early']).

% --- COVID-19 ---
disease(covid_19,
    [fever, cough, fatigue, loss_of_smell, loss_of_taste, shortness_of_breath, body_ache],
    'A respiratory illness caused by the SARS-CoV-2 coronavirus.',
    moderate,
    ['Isolate immediately', 'Get tested', 'Monitor oxygen levels', 'Seek emergency care if breathing worsens', 'Get vaccinated']).

% --- Dengue Fever ---
disease(dengue_fever,
    [fever, headache, body_ache, rash, nausea, vomiting, fatigue],
    'A mosquito-borne viral disease prevalent in tropical regions.',
    moderate,
    ['Use mosquito repellent', 'Stay hydrated', 'Monitor platelet count', 'Avoid aspirin or ibuprofen', 'Hospitalize if severe']).

% --- Malaria ---
disease(malaria,
    [fever, chills, sweating, headache, nausea, vomiting, fatigue],
    'A life-threatening disease caused by Plasmodium parasites transmitted by mosquitoes.',
    severe,
    ['Take prescribed antimalarial drugs', 'Use mosquito nets', 'Seek immediate medical care', 'Complete full course of medication']).

% --- Typhoid Fever ---
disease(typhoid_fever,
    [fever, headache, stomach_pain, nausea, loss_of_appetite, fatigue, diarrhea],
    'A bacterial infection caused by Salmonella typhi, spread through contaminated food and water.',
    moderate,
    ['Take prescribed antibiotics', 'Drink only boiled or purified water', 'Wash hands frequently', 'Get vaccinated']).

% --- Gastroenteritis ---
disease(gastroenteritis,
    [nausea, vomiting, diarrhea, stomach_pain, fever, fatigue],
    'Inflammation of the stomach and intestines, commonly called stomach flu.',
    mild,
    ['Stay hydrated with ORS', 'Eat light easily digestible food', 'Rest', 'Wash hands frequently']).

% --- Pneumonia ---
disease(pneumonia,
    [fever, cough, shortness_of_breath, chest_pain, fatigue, chills],
    'A serious lung infection that inflames air sacs in one or both lungs.',
    severe,
    ['Seek immediate medical care', 'Take prescribed antibiotics', 'Rest completely', 'Get pneumococcal vaccine', 'Avoid smoking']).

% --- Allergic Rhinitis ---
disease(allergic_rhinitis,
    [sneezing, runny_nose, itching, watery_eyes, headache],
    'An allergic response causing cold-like symptoms, triggered by pollen, dust or animal dander.',
    mild,
    ['Identify and avoid allergens', 'Use antihistamines', 'Keep windows closed during high pollen', 'Use air purifier at home']).

% --- Diabetes (Type 2) ---
disease(type2_diabetes,
    [frequent_urination, excessive_thirst, fatigue, blurred_vision, slow_healing, dry_mouth],
    'A chronic condition affecting blood sugar regulation due to insulin resistance.',
    severe,
    ['Monitor blood sugar regularly', 'Follow a low-sugar diet', 'Exercise daily', 'Take prescribed medication', 'Regular doctor checkups']).

% --- Arthritis ---
disease(arthritis,
    [joint_pain, swollen_joints, morning_stiffness, fatigue, body_ache],
    'Inflammation of one or more joints causing pain and stiffness.',
    moderate,
    ['Regular low-impact exercise', 'Take anti-inflammatory medication', 'Physical therapy', 'Maintain healthy weight', 'Apply hot/cold packs']).

% --- Meningitis ---
disease(meningitis,
    [fever, headache, stiff_neck, nausea, sensitivity_to_light, fatigue],
    'Inflammation of membranes surrounding the brain and spinal cord, often due to infection.',
    severe,
    ['SEEK EMERGENCY MEDICAL CARE IMMEDIATELY', 'Hospitalization required', 'Antibiotics or antiviral treatment', 'Meningitis vaccine available']).

% --- Jaundice ---
disease(jaundice,
    [yellow_skin, dark_urine, fatigue, nausea, loss_of_appetite, stomach_pain],
    'A condition causing yellowing of skin and eyes due to excess bilirubin in the blood.',
    moderate,
    ['Rest completely', 'Avoid alcohol', 'Stay hydrated', 'Eat a healthy liver-friendly diet', 'Seek medical evaluation for root cause']).

% --- Migraine ---
disease(migraine,
    [headache, nausea, sensitivity_to_light, dizziness, fatigue, vomiting],
    'A neurological condition causing intense recurring headaches often with other symptoms.',
    moderate,
    ['Rest in a dark quiet room', 'Take prescribed migraine medication', 'Stay hydrated', 'Identify and avoid personal triggers', 'Track episodes in a journal']).

% --- Asthma ---
disease(asthma,
    [shortness_of_breath, cough, chest_pain, fatigue],
    'A chronic respiratory condition where airways narrow and swell, producing extra mucus.',
    moderate,
    ['Use prescribed inhaler', 'Avoid known triggers', 'Monitor peak flow', 'Create an asthma action plan', 'Regular pulmonologist visits']).

% ------------------------------------------------------------
% DIAGNOSIS ENGINE
% ------------------------------------------------------------

% Count how many of the disease's symptoms the user has reported
count_matching_symptoms([], _, 0).
count_matching_symptoms([S|Rest], UserSymptoms, Count) :-
    (member(S, UserSymptoms) -> count_matching_symptoms(Rest, UserSymptoms, C1), Count is C1 + 1
    ; count_matching_symptoms(Rest, UserSymptoms, Count)).

% Calculate match percentage
match_percentage(DiseaseSymptoms, UserSymptoms, Percentage) :-
    length(DiseaseSymptoms, Total),
    count_matching_symptoms(DiseaseSymptoms, UserSymptoms, Matched),
    (Total > 0 -> Percentage is (Matched / Total) * 100 ; Percentage is 0).

% Diagnose: return disease if match >= 50%
diagnose(UserSymptoms, Disease, Percentage, Description, Severity, Precautions) :-
    disease(Disease, DiseaseSymptoms, Description, Severity, Precautions),
    match_percentage(DiseaseSymptoms, UserSymptoms, Percentage),
    Percentage >= 50.

% Get all diagnoses sorted by match percentage
get_all_diagnoses(UserSymptoms, SortedResults) :-
    findall(
        result(Pct, Disease, Desc, Sev, Prec),
        diagnose(UserSymptoms, Disease, Pct, Desc, Sev, Prec),
        Results
    ),
    sort(1, @>=, Results, SortedResults).  % sort descending by percentage

% ------------------------------------------------------------
% QUERY INTERFACE
% Run: diagnose_from_symptoms([fever, cough, fatigue], Results)
% ------------------------------------------------------------
diagnose_from_symptoms(Symptoms, Results) :-
    get_all_diagnoses(Symptoms, Results).

% List all known symptoms
list_all_symptoms :-
    forall(symptom(ID, Desc), format("~w: ~w~n", [ID, Desc])).

% List all known diseases
list_all_diseases :-
    forall(disease(Name, _, Desc, Severity, _),
           format("~w (~w): ~w~n", [Name, Severity, Desc])).
