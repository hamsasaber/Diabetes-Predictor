def evaluate_rules(data):
    """
    Evaluates diabetes risk based on medical rules.
    Input:
        data: a dictionary with keys like 'glucose', 'bmi', 'age', 'blood_pressure', etc.
    Output:
        dict with 'risk_level' and 'explanation'
    """

    glucose = data.get("glucose", 0)
    bmi = data.get("bmi", 0)
    age = data.get("age", 0)
    blood_pressure = data.get("blood_pressure", 0)
    pregnancies = data.get("pregnancies", 0)
    insulin = data.get("insulin", 0)

    risk_factors = []

    # Rule 1: High glucose
    if glucose > 126:
        risk_factors.append("High glucose level (>126 mg/dL)")

    # Rule 2: High BMI
    if bmi > 30:
        risk_factors.append("Obesity (BMI > 30)")

    # Rule 3: Age over 45
    if age >= 45:
        risk_factors.append("Age over 45")

    # Rule 4: High blood pressure
    if blood_pressure >= 85:
        risk_factors.append("Elevated blood pressure (≥85 mmHg)")

    # Rule 5: History of pregnancies (for women)
    if pregnancies >= 3:
        risk_factors.append("Multiple pregnancies (≥3)")

    # Rule 6: High insulin level
    if insulin > 200:
        risk_factors.append("High insulin levels (>200 IU/mL)")

    risk_score = len(risk_factors)

    if risk_score >= 4:
        level = "High Risk"
    elif risk_score >= 2:
        level = "Moderate Risk"
    else:
        level = "Low Risk"

    return {
        "risk_level": level,
        "explanation": risk_factors,
        "risk_score": risk_score
    }
