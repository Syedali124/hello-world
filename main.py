# Python program to read
# json file
 
 
import json
import pandas as pd

#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="",
#  database="scrapdata"
#)
#mycursor = mydb.cursor()


# Opening JSON file
f = open('data.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
# my_input = ['Engineering', 'Medical']
# my_input.append('Science')
# list1 = []
# list2 = []
# col1 = "X"
# col2 = "Y"
arr = []
for k in data['countries']:
    for i in k['countriesGroup']:
        for a in i['states']:
            for j in a['cities']:

                j["state"] = a['name']
                j["countryName"] = i['name']

                arr.append(j)
                data = pd.DataFrame(arr)
                data.to_csv('file1.csv')

   


    # list1.append(i['title'])
    # list2.append(i['description'])
    # sql = "INSERT INTO product (name, description) VALUES (%s, %s)"
    # val = (i['title'], i['description'])
    # mycursor.execute(sql, val)


# mydb.commit()

#print(mycursor.rowcount, "record inserted.")
# data = pd.DataFrame({'tilte':list1,'description':list2})
# data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)
# Closing file
f.close()
