#!/usr/bin/python3
""" Script to populate MYSql DB using Pandas """
import pandas
import csv
import string
import sqlite3
def populateDB():
    readColors = [
        2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27
    ]
    nameColors = [
        'Thumbnail', 'Title', 'Season', 'Episode', 'Youtube',
        'Black Gesso', 'Bright Red', 'Burnt Umber', 'Cadmium Yellow',
        'Dark Sienna', 'Indian Red', 'Indian Yellow', 'Liquid Black',
        'Liquid Clear', 'Midnight Black', 'Phthalo Blue', 'Phthalo Green',
        'Prussian Blue', 'Sap Green', 'Titanium White', 'Van Dyke Brown',
        'Yellow Ochre', 'Alizarin Crimson'
    ]
    colorFrame = pandas.read_csv("data_files/Colors",
                                usecols=readColors,
                                names=nameColors,
                                skiprows=[0])

    readSubjects = [x for x in range(2, 69)]
    with open('data_files/Subjects') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        nameSubjects = []
        for row in csv_reader:
            nameSubjects.append(row)
            break
    del nameSubjects[0][0:2]
    for x in range(len(nameSubjects[0])):
        new_header = string.capwords(nameSubjects[0][x].replace('_', ' ').lower())
        nameSubjects[0][x] = new_header
    subjectFrame = pandas.read_csv("data_files/Subjects",
                                    usecols=readSubjects,
                                    names=nameSubjects[0],
                                    skiprows=[0])

    finalDateList = []
    with open('data_files/Dates') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ' ')
        dateList = []
        for row in csv_reader:
            dateList.append(row)
    for x in range(len(dateList)):
        dateMonth = dateList[x][1][1:]
        dateDay = dateList[x][2].replace(',', '')
        dateYear = dateList[x][3].replace(')', '')
        finalDateList.append([dateMonth, dateDay, dateYear])
    dateFrame = pandas.DataFrame(finalDateList, columns=['Month', 'Day', 'Year'])

    mergedFrame = pandas.concat([colorFrame, subjectFrame, dateFrame], axis=1)

    connectDB = sqlite3.connect('JoyOfCoding.db')
    mergedFrame.to_sql('episodes', connectDB, index=True, if_exists='replace')
    connectDB.close()
