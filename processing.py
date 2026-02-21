import joblib
import numpy as np
import pandas as pd


features = joblib.load("features.pkl")
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns_to_scale = joblib.load("columns_to_scale.pkl")


def processing(df):


    df["loan_to_income"] = df["loan_amount"] / df["income"].replace(0, 1)
    df["delinquency_ratio"] = df["delinquency_months"] / df["total_months"].replace(0, 1)
    df["avg_dpd_per_delinquency"] = df["total_dpd"] / df["delinquency_months"].replace(0, 1)
    df[columns_to_scale] = scaler.transform(df[columns_to_scale])
    df = pd.get_dummies(df, drop_first=True)
    for col in features:
        if col not in df.columns:
            df[col] = 0
    df = df[features]
    print(df.columns)
    print(df.shape)
    default_probability=model.predict_proba(df)[0][1]
    non_default_probability=1-default_probability
    prediction=model.predict(df)[0]
    print("probability",non_default_probability)
    credit_score=300+(non_default_probability*600)
    return prediction,default_probability,credit_score