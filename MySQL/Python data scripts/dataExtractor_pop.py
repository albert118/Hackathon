# Author: Albert Ferguson
# IDEA: Read excel data to SQL output for a MySQL database
#
# Reading from several excel files

import mysql.connector
from mysql.connector import errorcode
import csv

#file path to excel files
_path = "C:\\Users\\Albert\\Desktop\\Hackathon\\Data\\Train info (card type and stationwise) data\\Train Card Type.csv"
 
#user_path = 
#$pop_path =
DB_NAME = 'nsw_transport_data'
cnx = mysql.connector.connect(user='root', password='ABC123',
							  host='127.0.0.1',
							  database=DB_NAME)

cursor = cnx.cursor()

add_user_data = ("INSERT INTO yearly_aggregate_users"
					"(line_val, cardtype, year_aggregate_vals, year_val) "
					"VALUES(%s, %s, %s, %s)")

line_val = []
cardtype = []
year_aggregate_vals = [0, 0, 0] # null allowed!
# 2016 is indexes[2, 7], 2017 is [8, 19] with 2019 [20, 31], 2019 is final two
year_val = [2016, 2017, 2018]

with open(_path) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			# print('Column names: {}\n'.format(row))
			line_count+=1
		else:
			if ('T1' in row[0] or 'T5' in row[0] and 'Adult' in row[1] or 'Child/Youth' in row[1] or 'Concession' in row[1]):
				line_val.append(row[0])
				cardtype.append(row[1])
				for i in range(2, len(row)):
					if (i <= 7 and row[i] != ''):
						year_aggregate_vals[0] += int(row[i].replace(',', ''))
						#print('2016: ', year_aggregate_vals[0])
					elif (i <= 19 and i >= 8 and row[i] != ''):		
						year_aggregate_vals[1] += int(row[i].replace(',', ''))
						#print('2017: ',year_aggregate_vals[1])
					elif (i <= 32 and i >= 20 and row[i] != ''):
						year_aggregate_vals[2] += int(row[i].replace(',', ''))
						#print('2018: ',year_aggregate_vals[2])
					else:
						pass
						#print('[ERROR]')

			print(line_count)
			print(len(line_val))
			print('2016: ', year_aggregate_vals[0])
			print('2017: ',year_aggregate_vals[1])
			print('2018: ',year_aggregate_vals[2], '\n')
			data = (line_val[-1], cardtype[-1], year_aggregate_vals[0], year_val[0])
			cursor.execute(add_user_data, data)
			data = (line_val[-1], cardtype[-1], year_aggregate_vals[1], year_val[1])
			cursor.execute(add_user_data, data)
			data = (line_val[-1], cardtype[-1], year_aggregate_vals[2], year_val[2])
			cursor.execute(add_user_data, data)
			
			line_count+=1
			year_aggregate_vals = [0, 0, 0]

cnx.commit()
cursor.close()
cnx.close()