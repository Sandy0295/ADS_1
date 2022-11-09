# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 06:05:32 2022

@author: sande
"""

#importing pandas package to read the files(data set)
import pandas as pd

#importing the pyplot from matplotlib package to plot the visualization graphs
import matplotlib.pyplot as plt

#defining the columns that are required for this scenario from the data set
required_cols = ['elo1_pre','elo2_pre','elo_prob1','elo_prob2','raptor1_pre','raptor2_pre','raptor_prob1','raptor_prob2','score1','score2','total_rating']

#reading the csv file containig our data and reading only first five records with the chosen columns
game_data = pd.read_csv('C:/Users/sande/MS-DS/ADS-1/Assg-1/nba_elo_latest.csv',usecols=required_cols,nrows=5)

#setting the index value to 1 instead of default value 0
game_data.index = game_data.index + 1
