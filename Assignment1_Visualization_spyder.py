# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 06:05:32 2022

@author: sande
"""

#importing pandas package to read the files(data set)
import pandas as pd

#importing the pyplot from matplotlib package to plot the visualization graphs
import matplotlib.pyplot as plt

"""
Lines 20-30 represents a function for line plot.
This function can be reused with users choice of columns.
This line plot is plotted between ELO and RAPTOR predicted ratings for two teams before the game.
Graph is plotted between the predicted scores and number of games.
"""
def line_plot(col_a,col_b,col_c,col_d,label_a,label_b,label_c,label_d,title,x_label,y_label):
    plt.figure(figsize=(10,5))
    plt.plot(game_data[col_a],label=label_a)
    plt.plot(game_data[col_b],label=label_b)
    plt.plot(game_data[col_c],label=label_c)
    plt.plot(game_data[col_d],label=label_d)
    plt.title(title,fontsize=13)
    plt.xlabel(x_label,fontsize=13)
    plt.ylabel(y_label,fontsize=13)
    plt.legend(loc='lower left')
    plt.show()

"""
Lines 37-47 represents a function for histogram.
This function can be reused with users choice of columns.
This histogram is plotted between predicted scores and the frequency of occurances(number of games)
"""
def histogram(col_a,col_b,col_c,col_d,label_a,label_b,label_c,label_d,title,x_label,y_label):
    plt.figure(figsize=(25,15)) 
    plt.hist(game_data[col_a],bins = 35,alpha = .25,label=label_a)
    plt.hist(game_data[col_b],bins = 35,alpha = .25,label=label_b)
    plt.hist(game_data[col_c],bins = 35,alpha = .25,label=label_c)
    plt.hist(game_data[col_d],bins = 35,alpha = .25,label=label_d)
    plt.title(title,fontsize=23)
    plt.xlabel(x_label,fontsize=23)
    plt.ylabel(y_label,fontsize=23)
    plt.legend(loc='upper left',prop={'size': 16})
    plt.show()

#defining the columns that are required for this scenario from the data set
required_cols = ['elo1_pre','elo2_pre','elo_prob1','elo_prob2','raptor1_pre','raptor2_pre','raptor_prob1','raptor_prob2','score1','score2','total_rating']

#reading the csv file containig our data and reading only first five records with the chosen columns
game_data = pd.read_csv('C:/Users/sande/MS-DS/ADS-1/Assg-1/nba_elo_latest.csv',usecols=required_cols,nrows=5)

#setting the index value to 1 instead of default value 0
game_data.index = game_data.index + 1

#calling the line_plot function with our own columns
line_plot('elo1_pre','elo2_pre','raptor1_pre','raptor2_pre','ELO1 Prediction','ELO2 Prediction','RAPTOR1 Prediction','RAPTOR2 Prediction','NBA Predictions','Game','Predicted Score')

