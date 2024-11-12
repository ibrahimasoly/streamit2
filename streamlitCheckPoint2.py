import streamlit as st
import joblib
import pandas as pd
import numpy as np
import sklearn

model =joblib.load("streamlitCheckPoint2.pkl")

st.title("Prediction of individuals are most likely to have or use a bank account")

with st.expander("Please fill in the following information", expanded=True):

     col1, col2 = st.columns(2)
    
    # Ajout d'éléments dans la première colonne
with col1:
    cellphone_access = st.radio("choose cellphone access", ["yes", "no"])
    household_size = st.text_input("household size", placeholder="Household size required")
    location_type = st.selectbox("choose location type", ["Rural", "Urban"])
    relationship_with_head = st.selectbox("choose relationship with head", ["Spouse", "Head of Household", "Other relative", "Child", "Parent"])
    education_level = st.selectbox("choose education level", ["Secondary education", "No formal education", "Vocational/Specialised training", "Primary education", "Tertiary education"])
    
    # Ajout d'éléments dans la deuxième colonne
with col2:
    gender_of_respondent = st.selectbox("choose gender of respondent", ["Female", "male"])
    age_of_respondent = st.text_input("age of respondent",placeholder="Age number required")
    country = st.selectbox("choose country", ["Rwanda", "Tanzania", "Kenya", "Uganda"])
    marital_status = st.selectbox("choose marital status", ["Married", "Single", "Widowed", "Divorced", "Dont know"])
    job_type = st.selectbox("choose job type", ["Self employed", "Government Dependent", "Farming and Fishing", "Formally employed Private", "Informally employed", "Remittance Dependent", "No Income", "Formally employed Government","Other Income", "Dont Know/Refuse to answer"])
    

if st.button("Predict"):
    list=[]
    if household_size :
        location=0
        cellphone=0
        gender=0
        relationship=0
        marital=0
        education=0
        job=0
        countryint=0
        #location_type
        if location_type=="Rural":
            location=0
            list.append(location)
        else:
            location=1
            list.append(location)
        
        #cellphone_access
        if cellphone_access=="yes":
            cellphone=1
            list.append(location)
        else:
            cellphone=0
            list.append(location)
        #household_size
        list.append(int(household_size))
        #age_of_respondent
        list.append(int(age_of_respondent))

        if gender_of_respondent=="Female":
            gender=0
            list.append(gender)
        else:
            gender=1
            list.append(gender)
        
        #relationship_with_head
        if relationship_with_head=="Spouse":
            relationship=0
            list.append(relationship)
        elif relationship_with_head=="Head of Household":
            relationship=0
            list.append(relationship)
        elif relationship_with_head== "Other relative":
            relationship=0
            list.append(relationship)
        elif relationship_with_head== "Child":
            relationship=0
            list.append(relationship)
        else:
            relationship=1
            list.append(relationship)
        #marital_status
        if marital_status== "Married":
            marital=0
            list.append(marital)
        elif marital_status== "Single":
            marital=0
            list.append(marital)
        elif marital_status=="Widowed":
            marital=0
            list.append(marital)
        elif marital_status== "Divorced":
            marital=0
            list.append(marital)
        else:
            marital=1
            list.append(marital)
        #education_level
        if education_level== "Secondary education":
            education=0
            list.append(education)
        elif education_level== "No formal education":
            education=0
            list.append(education)
        elif education_level== "Vocational/Specialised training":
            education=0
            list.append(education)
        elif education_level==  "Primary education":
            education=0
            list.append(education)
        else:
            education=1
            list.append(education)
        #job_type
        if job_type=="Self employed":
            job=0
            list.append(job)
        elif job_type== "Government Dependent":
            job=0
            list.append(job)
        elif job_type== "Farming and Fishing":
            job=0
            list.append(job)
        elif job_type== "Formally employed Private":
            job=0
            list.append(job)
        elif job_type== "Informally employed":
            job=0
            list.append(job)
        elif job_type== "Remittance Dependent":
            job=0
            list.append(job)
        elif job_type==  "No Income":
            job=0
            list.append(job)
        elif job_type=="Formally employed Government":
            job=0
            list.append(job)
        elif job_type=="Other Income":
            job=0
            list.append(job)
        else:
            job=1
            list.append(job)
        #country
        if country=="Rwanda":
            countryint=0
            list.append(countryint)
        elif country== "Tanzania":
            countryint=0
            list.append(countryint)
        elif country=="Kenya":
            countryint=0
            list.append(countryint)
        else:
            countryint=1
            list.append(countryint)

        y=model.predict(np.array(list).reshape(1,-1))
        st.write(y)
        st.success("Form successfully submitted!")
    else:
        st.error("Please fill in all required fields.")
st.write("hello")