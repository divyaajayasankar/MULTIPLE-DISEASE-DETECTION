# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:23:11 2023

@author: Divya
"""

import numpy as np

import pickle

import streamlit as st


# loading the saved model

loaded_model = pickle.load(open(r'C:\Users\Divya\OneDrive\Documents\mini project\heart_disease_model.sav','rb'))

# creating a function for Prediction

def Heart_prediction(input_data):
    
    # changing the input_data to numpy array
    
    #input_data = (63,1,3,145,233,1,0,150,0,2.3,0,0,1)
    
    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)
    
    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
        return 'The Person does not have a Heart Disease'
    else: 
        return 'The Person has Heart Disease'
       

def main():
       

    # giving a title

    st.title('Heart Prediction Web App')

       

    # getting the input data from the user

       

    age = st.text_input('age')
    
    sex = st.text_input('sex')
    
    cp = st.text_input('cp')

    trestbps = st.text_input('trestbps')

    chol = st.text_input('chol')

    fbs = st.text_input('fbs')

    restecg = st.text_input('restecg')

    thalach = st.text_input('thalach')

    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')

    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
    

       

    # code for Prediction

    diagnosis = ''

   

    # creating a button for Prediction

   

    if st.button('Heart Test Result'):
        diagnosis = Heart_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
               

    st.success(diagnosis)

if __name__ == '__main__':

    main()  
  