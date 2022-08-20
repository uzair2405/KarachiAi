# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 06:48:10 2022

@author: Uzair-Ali
"""


import streamlit as st 
import pandas as pd
    

        
    
def main():
    st.title('Air Passenger Analysis') 
    df = pd.read_csv('AirPassengers.csv')
    #st.table(data)
    month = st.selectbox("Month", list(df['Month'].unique()))
    st.text(df[df['Month']==month])

if __name__ == '__main__':
    main()
    

        
