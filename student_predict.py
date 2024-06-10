import streamlit as st
import pandas as pd
import numpy as np
import time
import joblib
from sklearn.preprocessing import LabelEncoder
from app_preprocessing import data_preprocessing, encoder_Debtor, encoder_Application_mode, encoder_Displaced, encoder_Gender, encoder_Marital_status, encoder_Scholarship_holder, encoder_Tuition_fees_up_to_date
from prediction import prediction



# Title app
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Jaya Jaya Institute Student Status Prediction App (Prototype)')

st.sidebar.header("About Jaya Jaya Institute")
st.sidebar.write("""
    Jaya Jaya Institute(JJI) merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini JJI telah mencetak banyak lulusan dengan reputasi yang sangat baik, Akan tetapi, terdapat banyak siswa yang tidak menyelesaikan pendidikannya alias _Drop out_
    Dengan jumlah _Drop out_ yang tinggi pada sebuah institusi pendidikan, akan berdampak antara lain menurunnya nilai akreditasi. Hal ini yang mengharuskan JJI mengambil tindakan untuk mendeteksi lebih dini kemungkinan siswa yang akan melakukan _Drop out_ sehingga dapat mengambil langkah yang tepat dan memberikan bimbingan khusus kepada mahasiswa
""")

data = {}
data = pd.DataFrame()
# display result
col1, col2, = st.columns(2)
with col1:
    Marital_status = st.selectbox(label='Select marital status', options=encoder_Marital_status.classes_, index=0)
    data['Marital_status'] = [Marital_status]
with col2:
    Application_mode = st.selectbox(label='Application_mode', options=encoder_Application_mode.classes_, index=1)
    data['Application_mode'] = [Application_mode]


col3, col4 = st.columns(2)
with col3:
    Previous_qualification_grade = st.number_input(label='Previous Qualification Grade', value=100)
    data['Previous_qualification_grade'] = [Previous_qualification_grade]
with col4:
    Admission_grade = st.number_input(label='Admission Grade', value=100)
    data['Admission_grade'] = [Admission_grade]

col5, col6, col7 = st.columns(3)
with col5:
    Displaced = st.selectbox(label='Did student displaced?', options=encoder_Displaced.classes_, index=1)
    data['Displaced'] = [Displaced]
with col6:
    Debtor = st.selectbox(label='Did student debtor?', options=encoder_Debtor.classes_, index=1)
    data['Debtor'] = [Debtor]
with col7:
    Tuition_fees_up_to_date = st.selectbox(label='Did student Tuition fees up to date?', options=encoder_Tuition_fees_up_to_date.classes_, index=1)
    data['Tuition_fees_up_to_date'] = [Tuition_fees_up_to_date]

col8, col9, col10 = st.columns(3)
with col8:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=1)
    data['Gender'] = [Gender]
with col9:
    Scholarship_holder = st.selectbox(label='Scholarship holder', options=encoder_Scholarship_holder.classes_, index=1)
    data['Scholarship_holder'] = [Scholarship_holder]
with col10:
    Age_at_enrollment = st.number_input(label='Age when Enroll Class', min_value=15.0, max_value=100.0, value=18.0)
    data['Age_at_enrollment'] = [Age_at_enrollment]

col11, col12, col13 = st.columns(3)
with col11:
    Curricular_units_1st_sem_enrolled = st.number_input(label='Curricular units 1st sem enrolled', value=0)
    data['Curricular_units_1st_sem_enrolled'] = [Curricular_units_1st_sem_enrolled]
with col12:
    Curricular_units_1st_sem_approved = st.number_input(label='Curricular units 1st sem approved', value=0)
    data['Curricular_units_1st_sem_approved'] = [Curricular_units_1st_sem_approved]
with col13:
    Curricular_units_1st_sem_grade = st.number_input(label='Curricular units 1st sem grade', value=0)
    data['Curricular_units_1st_sem_grade'] = [Curricular_units_1st_sem_grade]

col14, col15, col16, col17, col18 = st.columns(5)
with col14:
    Curricular_units_2nd_sem_enrolled = st.number_input(label='Curricular units 2nd sem enrolled', value=0)
    data['Curricular_units_2nd_sem_enrolled'] = [Curricular_units_2nd_sem_enrolled]
with col15:
    Curricular_units_2nd_sem_evaluations = st.number_input(label='Curricular units 2nd sem evaluations', value=0)
    data['Curricular_units_2nd_sem_evaluations'] = [Curricular_units_2nd_sem_evaluations]
with col16:
    Curricular_units_2nd_sem_approved = st.number_input(label='Curricular units 2nd sem approved', value=0)
    data['Curricular_units_2nd_sem_approved'] = [Curricular_units_2nd_sem_approved]
with col17:
    Curricular_units_2nd_sem_grade = st.number_input(label='Curricular units 2nd sem grade', value=0)
    data['Curricular_units_2nd_sem_grade'] = [Curricular_units_2nd_sem_grade]
with col18:
    Curricular_units_2nd_sem_without_evaluations = st.number_input(label='Curricular units 2nd sem without evaluations', value=0)
    data['Curricular_units_2nd_sem_without_evaluations'] = [Curricular_units_2nd_sem_without_evaluations]

user_input_df = pd.DataFrame(data, index=[0])

with st.expander("Get student with data :"):
    st.dataframe(data=user_input_df)

if st.button('Predict'):
    new_data = data_preprocessing(data=user_input_df)
    time.sleep(2)
    with st.spinner('Predicting...'):
        output = prediction(new_data)
            
        if output == "Graduate":
            st.success(f"Prediction : {output}")
        elif output == "Dropout":
            st.error(f"Prediction : {output}")
        else:
            st.warning(f"Prediction : {output}")
else:
    # Display the user input with no data
    st.subheader("User Input:")
    user_input_df = pd.DataFrame({'nothing' : 'nothing'}, index=[0])
    st.write(user_input_df)