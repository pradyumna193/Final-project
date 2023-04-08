# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:02:50 2023

@author: PRADYUMNA PS
"""

import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
model = pickle.load(open('model.sav', 'rb'))

st.title('Marketing Campaign')
st.sidebar.header('Customer Data')

def user_report():
  Marital_Status = st.checkbox('Marital Status', ("Yes", "No") )
  Income = st.number_input('Income','Insert a number')
  Age = st.number_input('Age', 'Insert a number' )
  NumDealsPurchases = st.number_input('NumDealsPurchases', 'Insert a number' )
  NumWebPurchases = st.number_input('NumWebPurchases', 'Insert a number' )
  NumStorePurchases = st.number_input('NumStorePurchases','Insert a number')
  NumWebVisitsMonth = st.number_input('NumWebVisitsMonth', 'Insert a number')
  Days_since_enrolment = st.number_input('Days_since_enrolment','Insert a number')
  Family_Size = st.number_input('Family_Size','Insert a number')
  Spent = st.number_input('Spent','Insert a number')
  
  
  user_report_data = {
      'Marital_Status':Marital_Status,
      'Income':Income,
      'Age':Age,
      'NumDealsPurchases':NumDealsPurchases,
      'NumWebPurchases':NumWebPurchases,
      'NumStorePurchases':NumStorePurchases,
      'NumWebVisitsMonth':NumWebVisitsMonth,
      'Days_since_enrolment':Days_since_enrolment,
      'Family_Size':Family_Size,
      'Spent':Spent
   }
   report_data = pd.DataFrame(user_report_data, index=[0])
   return report_data

user_data = user_report()
st.header('Customer Analysis')
st.write(user_data)

salary = model.predict(user_data)
st.subheader('Customer segments')



      