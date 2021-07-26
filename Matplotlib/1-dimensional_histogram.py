# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 11:23:43 2021

@author: BornaMarkovic
"""

import matplotlib.pyplot as plt

with open("Goals.txt","r") as f:
    HomeTeamGoals =[ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    AwayTeamGoals = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    
TotalGoal = HomeTeamGoals + AwayTeamGoals    
plt.hist(x = (HomeTeamGoals, AwayTeamGoals, TotalGoal), bins = range(8), 
         label = ["Home Team Goals", "Away Team Goals", "Total Goals Scored"],align = "left")
plt.legend()
plt.xlabel("Goals Scored")
plt.ylabel("Number of goals scored")
plt.show()

plt.hist2d(x = HomeTeamGoals, y = AwayTeamGoals, bins = (range(8),range(7)))
plt.xlabel("Home Team Goals")
plt.ylabel("Away Team Goals")
plt.colorbar()
plt.show()