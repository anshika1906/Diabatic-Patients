#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Anshika
"""

import numpy as np 
import pickle            # for loading the saved model 
import streamlit as st   # for creating the web page


#loading the saved Model
loaded_model = pickle.load(open('./Diabatic_Patients_model.sav', 'rb')) 


# creating a function for Prediction

def diabetes_prediction(input_data):
    try:
        # Convert input_data values to float and handle possible ValueError
        input_data = [float(value) for value in input_data]
    except ValueError as e:
        return f"Error: {e}. Please enter valid numerical values for all input fields."

    # Change the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Check if the input_data contains non-numeric values
    if not np.issubdtype(input_data_as_numpy_array.dtype, np.number):
        return "Error: Input data must be numeric. Please enter valid numerical values for all input fields."

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Make the prediction
    try:
        prediction = loaded_model.predict(input_data_reshaped)
    except Exception as e:
        return f"Error during prediction: {e}. Please check your model compatibility and input data."

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


  
    
  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()   
      
    
    
    
      
      
      
      