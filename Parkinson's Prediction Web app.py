# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:26:52 2023

@author: Divya
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open(r'C:\Users\Divya\OneDrive\Documents\mini project\parkinsons_model.sav','rb'))

# creating a function for Prediction

def parkinson_prediction(input_data):
    input_data = (119.992,157.302,74.997,0.00784,0.00007,0.0037,0.00554,0.01109,0.04374,0.426,0.02182,0.0313,0.02971,0.06545,0.02211,21.033,0.414783,0.815285,-4.81303,0.266482,2.301442,0.284654)
    
    # changing input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    
    if (prediction[0] == 0):
      return "The Person does not have Parkinsons Disease"
    
    else:
      return "The Person has Parkinsons"
  
def main():
      
      
      # giving a title
      st.title('Parkinsons Prediction Web App')
      
      
      # getting the input data from the user
      
    
      b = st.text_input('MDVP:Fo(Hz)')
      c = st.text_input('MDVP:Fhi(Hz)')
      d = st.text_input('MDVP:Flo(Hz)')
      e = st.text_input('MDVP:Jitter(%)')
      f = st.text_input('MDVP:Jitter(Abs)')
      g = st.text_input('MDVP:RAP')
      h = st.text_input('MDVP:PPQ ')
      i = st.text_input('Jitter:DDP')
      j = st.text_input('MDVP:Shimmer')
      k = st.text_input('MDVP:Shimmer(dB)')
      l = st.text_input('Shimmer:APQ3')
      m = st.text_input('Shimmer:APQ5')
      n = st.text_input('MDVP:APQ')
      o = st.text_input('Shimmer:DDA')
      p = st.text_input('NHR')
      q = st.text_input('HNR')
      s = st.text_input('RPDE')
      t = st.text_input('DFA')
      u = st.text_input('spread1')
      v = st.text_input('spread2')
      w = st.text_input('D2')
      x = st.text_input('PPE')
      
      

      
      
      # code for Prediction
      diagnosis = ''
      
      # creating a button for Prediction
      
      if st.button('Parkinson Test Result'):
          diagnosis = parkinson_prediction([b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,v,w,x])
          
          
      st.success(diagnosis)
      
      
      
      
      
if __name__ == '__main__':
      main()
      