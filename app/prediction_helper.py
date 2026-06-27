import pandas as pd
from joblib import load

# Loading the models and scalers
model_young = load('artifacts/model_young.joblib')
model_rest = load('artifacts/model_rest.joblib')

scaler_young = load('artifacts/scaler_young.joblib')
scaler_rest = load('artifacts/scaler_rest.joblib')

def handle_scaling(age, df):
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    scaler = scaler_object['scaler']
    cols_to_scale = scaler_object['cols_to_scale']

    df['income_level'] = -1
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis=1, inplace=True)

    return df

def calculate_risk_score(medical_history):
    risk_scores = {
        'diabetes': 6,
        'heart disease': 8,
        'high blood pressure': 6,
        'thyroid': 5,
        'no disease': 0,
        'none': 0
    }

    diseases = medical_history.lower().split(" & ")

    if len(diseases) == 1:
        diseases.append("none")

    total_risk_score = 0

    for disease in diseases:
        total_risk_score += risk_scores[disease]

    normalized_risk_score = total_risk_score / 14

    return normalized_risk_score

def preprocess_input(input_dict):
    expected_columns = [
        "age",
        "number_of_dependants",
        "income_lakhs",
        "insurance_plan",
        "genetical_risk",
        "normalized_risk_score",
        "gender_Male",
        "region_Northwest",
        "region_Southeast",
        "region_Southwest",
        "marital_status_Unmarried",
        "bmi_category_Obesity",
        "bmi_category_Overweight",
        "bmi_category_Underweight",
        "smoking_status_Occasional",
        "smoking_status_Regular",
        "employment_status_Salaried",
        "employment_status_Self-Employed"
    ]

    # Encoding objects
    insurance_plan_encoding = {'Bronze' : 1, 'Silver' : 2, 'Gold' : 3}

    # Create Data frame
    df = pd.DataFrame(0, columns= expected_columns, index = [0])

    # Let's fill out the dataframe now with the input_dict
    # Let's fill out the dataframe now with the input_dict
    for key, value in input_dict.items():

        if key == 'age':
            df['age'] = value

        elif key == 'number_of_dependants':
            df['number_of_dependants'] = value

        elif key == 'income_lakhs':
            df['income_lakhs'] = value

        elif key == 'genetical_risk':
            df['genetical_risk'] = value

        elif key == 'insurance_plan':
            df['insurance_plan'] = insurance_plan_encoding[value]

        elif key == 'gender':
            if value == 'Male':
                df['gender_Male'] = 1

        elif key == 'region':
            if value == 'Northwest':
                df['region_Northwest'] = 1
            elif value == 'Southeast':
                df['region_Southeast'] = 1
            elif value == 'Southwest':
                df['region_Southwest'] = 1

        elif key == 'marital_status':
            if value == 'Unmarried':
                df['marital_status_Unmarried'] = 1

        elif key == 'bmi_category':
            if value == 'Underweight':
                df['bmi_category_Underweight'] = 1
            elif value == 'Overweight':
                df['bmi_category_Overweight'] = 1
            elif value == 'Obesity':
                df['bmi_category_Obesity'] = 1

        elif key == 'smoking_status':
            if value == 'Occasional':
                df['smoking_status_Occasional'] = 1
            elif value == 'Regular':
                df['smoking_status_Regular'] = 1

        elif key == 'employment_status':
            if value == 'Salaried':
                df['employment_status_Salaried'] = 1
            elif value == 'Self-Employed':
                df['employment_status_Self-Employed'] = 1

    df['normalized_risk_score'] = calculate_risk_score(input_dict['medical_history'])

    df = handle_scaling(input_dict['age'], df)

    return df


def predict(input_dict):
    input_df = preprocess_input(input_dict)

    if input_dict['age'] <= 25:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    return int(prediction)