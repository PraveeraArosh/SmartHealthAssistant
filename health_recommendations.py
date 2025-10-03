def get_age_group(age):
    if 20 <= age < 30:
        return "20-30"
    elif 30 <= age < 40:
        return "30-40"
    elif 40 <= age < 50:
        return "40-50"
    elif 50 <= age < 60:
        return "50-60"
    elif age >= 60:
        return "60+"
    else:
        raise ValueError("Age out of range")

def generate_health_plan(age, gender):
    age_group = get_age_group(age)
    # Placeholder recommendations based on age and gender
    base_plan = {
        "20-30": {
            "screenings": "Annual physical, blood pressure check",
            "exercise": "30 min cardio daily",
            "vitamins": "Multivitamin",
            "meals": "Balanced diet with fruits and veggies"
        },
        "30-40": {
            "screenings": "Cholesterol check, diabetes screening",
            "exercise": "Strength training 3x/week",
            "vitamins": "Vitamin D, Calcium",
            "meals": "High protein, low carb"
        },
        "40-50": {
            "screenings": "Colonoscopy, mammogram (female)",
            "exercise": "Yoga and walking",
            "vitamins": "B12, Omega-3",
            "meals": "Anti-inflammatory foods"
        },
        "50-60": {
            "screenings": "Bone density, prostate (male)",
            "exercise": "Low impact aerobics",
            "vitamins": "Antioxidants",
            "meals": "Heart-healthy diet"
        },
        "60+": {
            "screenings": "Hearing/vision tests, fall risk assessment",
            "exercise": "Gentle stretching",
            "vitamins": "Vitamin K, Folate",
            "meals": "Nutrient-dense small meals"
        }
    }
    plan = base_plan[age_group]
    if gender == "Female":
        plan["screenings"] += ", Pap smear"
    elif gender == "Male":
        plan["screenings"] += ", Testosterone check"
    return plan