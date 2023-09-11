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
st.ballons()
