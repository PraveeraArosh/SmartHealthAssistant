def get_age_group(age):
    if 20 <= age < 30:
        return "20-30"
    elif 30 <= age < 40:
        return "30-40"
    elif 40 <= age < 50:
        return "40-50"
    elif 50 <= age < 60:
        return "50-60"
    elif 60 <= age < 70:
        return "60-70"
    elif age >= 70:
        return "70+"
    else:
        raise ValueError("Age out of range")

def generate_health_plan(age, gender):
    age_group = get_age_group(age)
    if gender == "Other":
        gender = "Male"  # Default to Male for Other; adjust as needed
    if gender not in ["Male", "Female"]:
        raise ValueError("Invalid gender")
    
    # Detailed recommendations based on plan.docx and supplemented data
    base_plan = {
        "Male": {
            "20-30": {
                "screenings": "Blood pressure every 2 yrs, Lipid profile baseline, Blood glucose (if overweight/family history), BMI, waist circumference, Eye & dental checkups, STI / Hepatitis B & C screening (as needed), Testosterone check",
                "exercise": "150–300 mins moderate aerobic/wk, 2×/wk resistance training (compound lifts), Include flexibility & mobility work, Sports or HIIT optional",
                "vitamins": "Multivitamin (general), Vitamin D (if low sun), Omega-3 if diet lacks fish",
                "meals": "50% vegetables & fruits, 25% lean protein (fish, chicken, eggs, legumes), 25% whole grains, Minimize fast food & sugary drinks, 2–3 L water/day"
            },
            "30-40": {
                "screenings": "BP & lipid check every 2 yrs, Blood glucose every 3 yrs, Liver & kidney function (if risk), Eye, dental, skin check, Testosterone check",
                "exercise": "Maintain aerobic + strength + flexibility, Add stress-relief exercises (yoga, cycling), Focus on core & posture",
                "vitamins": "Vitamin D, Omega-3, CoQ10 (if fatigue), Magnesium (for muscle recovery)",
                "meals": "Moderate-calorie intake, Include fiber-rich foods (salads, fruits), Reduce refined carbs & alcohol, Prioritize protein in all meals"
            },
            "40-50": {
                "screenings": "Annual BP, lipid, glucose, PSA (prostate) discussion if risk, Colon cancer screening (start ~45), Eye & hearing tests, Testosterone check",
                "exercise": "150 min/week moderate cardio, 2×/wk strength (focus: lower back, legs), Stretching daily, Balance drills (single-leg stands)",
                "vitamins": "Vitamin D + calcium, Omega-3, Magnesium & Zinc, B-complex",
                "meals": "45% carbs (mostly whole grain), 30% fats (nuts, olive oil, fish), 25% protein (lean meats, pulses), Limit salt (<5 g/day)"
            },
            "50-60": {
                "screenings": "Annual full check-up: BP, sugar, cholesterol, Colonoscopy every 10 yrs, Prostate & thyroid screening, Bone density if risk, Eye, dental, Testosterone check",
                "exercise": "Moderate cardio (walking, swimming), Resistance bands or weights 2×/wk, Add mobility + balance training",
                "vitamins": "Vitamin D & Calcium, Omega-3, B12 (absorption may drop), Magnesium, Joint support (Glucosamine)",
                "meals": "High-protein (fish, eggs, beans), Plenty of vegetables & fruits, Whole grains, low-fat dairy, Hydrate well; reduce fried/salty foods"
            },
            "60-70": {
                "screenings": "Annual BP, sugar, lipid, renal, Colon, prostate, thyroid, Eye (glaucoma, cataract), Hearing, dental, skin, Fall risk & cognitive screening, Testosterone check",
                "exercise": "150 min/week gentle cardio (walking, swimming), Strength: bodyweight or light weights, Balance (tai chi, yoga), Stretching daily",
                "vitamins": "Vitamin D3, Calcium, B12, Omega-3, Vitamin K2 (for bone health), Multivitamin",
                "meals": "Moderate-calorie, nutrient-dense meals, Protein with every meal, Fiber (fruits, veg, oats), 2–2.5 L water/day"
            },
            "70+": {
                "screenings": "Annual wellness check, Prostate, colon, vision, hearing, Fall risk, cognitive & nutritional assessment, Vaccinations: flu, pneumonia, shingles, Testosterone check",
                "exercise": "Gentle daily movement (walking, stretching), Balance & flexibility focus, Seated resistance bands, Avoid overexertion",
                "vitamins": "Vitamin D, Calcium, B12, Omega-3, Multivitamin, Iron only if deficient",
                "meals": "Soft, easy-to-digest meals, High protein (fish, yogurt, legumes), Small, frequent meals, Hydration critical; include soups & fruit juices"
            }
        },
        "Female": {
            "20-30": {
                "screenings": "BP every 2 yrs, Cholesterol baseline, Pap smear every 3 yrs (age ≥ 21), Blood sugar (if risk), STI / reproductive health, Eye, dental check",
                "exercise": "150 min cardio/wk + 2×/wk resistance, Include flexibility (yoga, pilates), Weight training for bone density",
                "vitamins": "Iron + folate (if menstruating), Vitamin D, Calcium, Omega-3",
                "meals": "Balanced diet: 50% veg & fruits, Iron-rich foods (spinach, red rice, eggs), Lean proteins & whole grains, Hydration: 2 L/day"
            },
            "30-40": {
                "screenings": "BP, sugar, cholesterol every 2–3 yrs, Pap + HPV test (every 5 yrs), Thyroid test (if symptomatic), Breast self-exam monthly",
                "exercise": "Cardio 150 min/wk, Strength 2–3×/wk, Core strengthening, Mind-body (yoga/meditation)",
                "vitamins": "Calcium + Vit D, Iron (if menstruating), Magnesium, Omega-3",
                "meals": "Calorie-conscious balanced meals, Whole grains, fish, leafy greens, Avoid refined sugar, Include probiotics (curd/yogurt)"
            },
            "40-50": {
                "screenings": "Annual BP, lipid, glucose, Mammogram (start 40+), Cervical screening, Thyroid & vitamin D test, Perimenopause hormone profile if needed",
                "exercise": "Cardio + strength + flexibility, Add balance & posture training, Moderate-intensity aerobics",
                "vitamins": "Vitamin D, Calcium, Iron (if menstruating), Omega-3, B-complex, Antioxidants (Vit C, E)",
                "meals": "Emphasize calcium-rich foods (milk, yogurt, tofu), Protein at every meal, Cut sodium, sugar, Plenty of fruits/veggies"
            },
            "50-60": {
                "screenings": "Annual full body check, Bone density (postmenopause), Mammogram, Colonoscopy, Thyroid & glucose",
                "exercise": "Low-impact cardio (walking, swimming), Resistance bands or weights 2×/wk, Add mobility + balance training",
                "vitamins": "Vitamin D & Calcium, Omega-3, B12, Magnesium, Joint support (Glucosamine)",
                "meals": "High-protein (fish, eggs, beans), Plenty of vegetables & fruits, Whole grains, low-fat dairy, Hydrate well; reduce fried/salty foods"
            },
            "60-70": {
                "screenings": "Annual BP, sugar, lipid, renal, Colon, thyroid, Bone density, Mammogram (up to 75), Eye (glaucoma, cataract), Hearing, dental, skin, Fall risk & cognitive screening",
                "exercise": "150 min/week gentle cardio (walking, swimming), Strength: bodyweight or light weights, Balance (tai chi, yoga), Stretching daily",
                "vitamins": "Vitamin D3 (15-20 mcg), Calcium (1200 mg), B12, Omega-3, Vitamin K2 (for bone health), Multivitamin",
                "meals": "Moderate-calorie, nutrient-dense meals, Protein with every meal (fish, yogurt, legumes), Fiber (fruits, veg, oats), 2–2.5 L water/day, Include low-fat dairy"
            },
            "70+": {
                "screenings": "Annual wellness check, Colon (if <85), vision, hearing, Fall risk, cognitive & nutritional assessment, Vaccinations: flu, pneumonia, shingles, Bone density if risk, Mammogram if <75 and risk factors",
                "exercise": "Gentle daily movement (walking, stretching), Balance & flexibility focus, Seated resistance bands, Avoid overexertion",
                "vitamins": "Vitamin D (20 mcg), Calcium (1200 mg), B12, Omega-3, Multivitamin, Iron only if deficient",
                "meals": "Soft, easy-to-digest meals, High protein (fish, yogurt, legumes), Small, frequent meals, Hydration critical; include soups & fruit juices, Nutrient-dense with veggies and fruits"
            }
        }
    }
    plan = base_plan[gender][age_group]
    return plan