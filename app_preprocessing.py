import joblib
import numpy as np
import pandas as pd

encoder_Gender = joblib.load("model/encoder_Gender.joblib")
encoder_Application_mode = joblib.load("model/encoder_Application_mode.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Displaced = joblib.load("model/encoder_Displaced.joblib")
encoder_Marital_status = joblib.load("model/encoder_Marital_status.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")
encoder_Tuition_fees_up_to_date = joblib.load("model/encoder_Tuition_fees_up_to_date.joblib")

scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")

def data_preprocessing(data):
    data = data.copy()
    df = pd.DataFrame()

    # Debug print initial data
    print("Initial Data:", data)
    
    df["Marital_status"] = encoder_Marital_status.transform(np.asarray(data["Marital_status"]).reshape(-1,1))
    df["Application_mode"] = encoder_Application_mode.transform(np.asarray(data["Application_mode"]).reshape(-1,1))
    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))
    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1))
    df["Displaced"] = encoder_Displaced.transform(np.asarray(data["Displaced"]).reshape(-1,1))
    df["Debtor"] = encoder_Debtor.transform(np.asarray(data["Debtor"]).reshape(-1,1))
    df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.transform(np.asarray(data["Tuition_fees_up_to_date"]).reshape(-1,1))
    df["Gender"] = encoder_Gender.transform(np.asarray(data["Gender"]).reshape(-1,1))
    df["Scholarship_holder"] = encoder_Scholarship_holder.transform(np.asarray(data["Scholarship_holder"]).reshape(-1,1))
    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))
    df["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))
    df["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))
    df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))
    df["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))
    df["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))
    df["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))
    df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))
    df["Curricular_units_2nd_sem_without_evaluations"] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_without_evaluations"]).reshape(-1,1))


    return df