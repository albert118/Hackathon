# Author: Albert Ferguson
# IDEA: Read excel data to SQL output for a MySQL database
#
# Reading from several excel files


import sys
import os
import mysql.connector
from mysql.connector import errorcode
import xlrd

#file path to excel files
station_path = "C:\\Users\\Albert\\Desktop\\Hackathon\\Data\\Train info (card type and stationwise) data\\Train Station Entries and Exits Version 1.0.xlsx"
 
#user_path = 
#$pop_path =
DB_NAME = 'nsw_transport_data'
cnx = mysql.connector.connect(user='root', password='ABC123',
							  host='127.0.0.1',
							  database=DB_NAME)

cursor = cnx.cursor()

##d, %d, %d, %d, %d, %d, %d, %d, %d);
# query_station = ("SELECT * FROM station_yearly_aggregates")

add_pop_pred = ("INSERT INTO population_predictions "
			  "(district, year_val, pop_prediction) "
			  "VALUES (%s, %i, %i")

add_yearly_users = ("INSERT INTO yearly_aggregate_users; "
			  "(line_val, cardtype, year_aggregate_vals, year_val) "
			  "VALUES (%s, %s, %i, %i")

add_station_yearly = ("INSERT INTO station_yearly_aggregates "
		"(station, year_val, entries_1, exits_1, entries_2, exits_2, entries_3, exits_3, entries_4, exits_4, entries_daily_avg, exits_daily_avg) "
		"VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")

# TODO, read these from excel data

station_read = xlrd.open_workbook(station_path) 
sheet = station_read.sheet_by_index(0) # TODO GET INDEX
# For row 0 and column 0 
# vsheet.cell_value(0, 0) 
# names of our vals are column headers (ie first row)

year_arr = []
station_arr = []
entries_1 = []
entries_2 = []
entries_3 = []
entries_4 = []
exits_1  = []
exits_2 = []
exits_3 = []
exits_4 = []
daily_exits = []
daily_entries = []



arr_dict = [year_arr,  station_arr, entries_1, exits_1, entries_2, exits_2, entries_3, exits_3, exits_4, entries_4, daily_exits, daily_entries ]
for i in range(1,sheet.nrows):
	for j in range(0, 12):
		if(sheet.cell_value(i,j) == '-'):
			arr_dict[j].append(0.0)
		arr_dict[j].append(sheet.cell_value(i,j))
# data station IO table
for i in range(0, len(year_arr)): # insert into table
	print(station_arr[i], year_arr[i], entries_1[i], entries_2[i], entries_3[i], entries_4[i], exits_1[i], exits_2[i], exits_3[i], exits_4[i], daily_entries[i],  daily_exits[i])
	data = (station_arr[i], year_arr[i], entries_1[i], entries_2[i], entries_3[i], entries_4[i], exits_1[i], exits_2[i], exits_3[i], exits_4[i], daily_entries[i],  daily_exits[i])
	cursor.execute(add_station_yearly, data)

# Insert new station
cnx.commit()
cursor.close()
cnx.close()