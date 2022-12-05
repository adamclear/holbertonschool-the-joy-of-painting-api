#!/usr/bin/python3
""" Script to populate MYSql DB using Pandas """
import pandas

readColors = [
    3, 4, 5
]

nameColors = [
    'Title',
    'Season',
    'Episode'
]
dataFrame = pandas.read_csv("data_files/Colors", usecols=readColors, names=nameColors, skiprows=[0])

print(dataFrame)
