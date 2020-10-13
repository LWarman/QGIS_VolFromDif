# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:07:52 2019

@author: cslw1
"""

from PyQt5.QtWidgets import QFileDialog
import pymsgbox
import easygui

title = 'Difference Grid'
path = "C:\Modelling"
vol = 0
filter = "ASC (*.asc)"
qfd = QFileDialog()
count = 0
cellSize = 1
depth = 0

inputGrid = QFileDialog.getOpenFileName(qfd, title, path, filter)
inputGridTxt = inputGrid[0]

cellSize = easygui.enterbox("Cell size of difference grid:")


with open (inputGridTxt, 'r') as f:
    gridList = f.read().split()[12:] #the asc will give a header containing 6 rows of two values separated by a space, skipping these to get to the data

gridList = [float(i) for i in gridList]

for i in gridList:
    if i > 0 < 50:
        count = count + 1
        depth = depth + i
        depth = round(depth,2)

cellSize = float(cellSize)
cellArea = cellSize * cellSize
vol = depth * cellArea
vol = str(vol)     
vol = vol + "m3" 
pymsgbox.alert(text= vol, title="Calculated Volume")
