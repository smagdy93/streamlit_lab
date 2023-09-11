#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:23:52 2023

@author: safaa
"""
import streamlit as st
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))
n1=st.number_input('First Width', min_value=1,value=1)
n2=st.number_input('Second Width',min_value=1,value=1)
st.balloons()
col1, col2, col3 = st.beta_columns((n1,n2,n3))
with col1:
  st.write('First column')
with col2:
  st.write('Second column')
with col3:
  st.write('Third column')
