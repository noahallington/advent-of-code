# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:19:48 2018

@author: noaha
"""
import os
import pandas as pd

directory='C:/Users/noaha/Documents/Advent of Code'
os.chdir(directory)

#Get input

frequency = pd.read_table('./day1input.txt',sep='\n',header=None)

#Final Frequency for part 1
print(sum(frequency[0]))

#Part 2
freq_changes = list(frequency[0])

initialFrequency = 0

frequenciesAchieved = [initialFrequency]

foundDuplicate = False

while foundDuplicate == False:
    for change in freq_changes:
        initialFrequency+=change
        if initialFrequency in frequenciesAchieved:
            print(initialFrequency)
            foundDuplicate = True
            break
        else:
            frequenciesAchieved.append(initialFrequency)
            continue
        
    