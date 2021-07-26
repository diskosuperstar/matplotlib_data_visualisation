# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:16:41 2021

@author: BornaMarkovic
"""

import matplotlib.pyplot as plt

with open("Goals.txt","r") as f:
    HomeTeamGoals =[ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    AwayTeamGoals = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]


xVariable = []
ticks = ["Game One", "Game Fifty", "Game 100"]
for i in range(len(HomeTeamGoals)):
    xVariable.append(i)
plt.plot(xVariable, AwayTeamGoals, c = "green", ls = "--")
plt.title(r"Our first plot $\frac{1}{2}$")
#plt.show()
#plt.title("Our second plot")
plt.plot(xVariable, HomeTeamGoals, c = "blue",  ls = ":")
plt.xlim(0,145)
plt.ylim(-1,6)
plt.xlabel("Game Number")
plt.ylabel("Goals scored")
plt.xticks([49],["Fourty Nine"])
plt.yticks([3],["Three Goals"])
plt.text(50,4,r"Our$^3$Cusom Text", fontsize = 8)
plt.annotate("Text 2", xy = (30, 5), xytext = (35,5),
             arrowprops = dict(facecolor = "red"))
plt.show()