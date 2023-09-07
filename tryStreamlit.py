#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:23:52 2023

@author: safaa
"""
import streamlit as st
import joblib
import pandas as pd
import numpy as np
st.title('Map of Safaa')
# Defining Latitude and Longitude
locate_map = pd.DataFrame(
np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
columns = ['latitude', 'longitude'])
#locate_map = pd.DataFrame([30.033333, 31.233334],columns = ['latitude', 'longitude'])
# Map Function
st.map(locate_map)
