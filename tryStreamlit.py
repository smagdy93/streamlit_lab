#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:23:52 2023

@author: safaa
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.title('Safaa Ballons')
st.text("Your number is " + str(number))
n1=st.number_input('First Width', min_value=1,value=1)
n2=st.number_input('Second Width',min_value=1,value=1)
n3=st.number_input('Third Width',min_value=1,value=1)
st.balloons()
col1, col2, col3 = st.columns((n1,n2,n3))
with col1:
  st.write('First column')
with col2:
  st.write('Second column')
with col3:
  st.write('Third column')
trees_df = pd.read_csv("trees_sample.csv")
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)  
