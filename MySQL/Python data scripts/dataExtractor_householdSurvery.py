# Author: Albert Ferguson
# IDEA: Read excel data to SQL output for a MySQL database
#
# Reading from several excel files

import mysql.connector
from mysql.connector import errorcode
import csv

#file path to excel files
_path = "C:\\Users\\Albert\\Desktop\\Hackathon\\Data\\pop_data_pred.csv"
 
#user_path = 
#$pop_path =
DB_NAME = 'nsw_transport_data'
cnx = mysql.connector.connect(user='root', password='ABC123',
							  host='127.0.0.1',
							  database=DB_NAME)

cursor = cnx.cursor()

add_user_data = ("INSERT INTO population_predictions "
					"(district, year_val, pop_prediction, district_pred, district_in, district_out) "
					"VALUES(%s, %s, %s, %s, %s, %s)")

district = ["Harris_Park_Pop",	"Parramatta_Pop",	"Westmead_Pop"]
pop_prediction = [456213.5841,
465357.4784,
474501.3727,
483645.2671,
492789.1614,
501933.0557,
511076.95,
520220.8444,
529364.7387,
538508.633,
547652.5273,
556796.4217,
565940.316,
575084.2103,
584228.1046,
593371.999,
602515.8933,
611659.7876,
620803.6819,
629947.5763,
639091.4706,
648235.3649,
657379.2592,
666523.1536
]


district_pred_parra = [364970.8673,
372285.9827,
379601.0982,
386916.2136,
394231.3291,
401546.4446,
408861.56,
416176.6755,
423491.790,
430806.9064,
438122.0219,
445437.1373,
452752.2528,
460067.3682,
467382.4837,
474697.5992,
482012.7146,
489327.8301,
496642.9455,
503958.061,
511273.1765,
518588.2919,
525903.4074,
533218.5228
]

district_pred_westmead = [68432.03761,
69803.62176,
71175.20591,
72546.79006,
73918.37421,
75289.95836,
76661.5425,
78033.12665,
79404.7108,
80776.29495,
82147.8791,
83519.46325,
84891.0474,
86262.63155,
87634.21569,
89005.79984,
90377.38399,
91748.96814,
93120.55229,
94492.13644,
95863.72059,
97235.30474,
98606.88889,
99978.47303
]
# 2016 is indexes[2, 7], 2017 is [8, 19] with 2019 [20, 31], 2019 is final two
year_val = [2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,
2032,
2033,
2034,
2035,
2036,
2037,
2038,
2039,
2040
]

district_in_westmead = [8060,
8200,
7990,
8680,
8840,
9000,
9160,
9320,
9480,
9640,
9790,
9950,
10110,
10270,
10430,
10590,
10740,
10900,
11060,
11220,
11370,
11530,
11690,
11850
]

district_out_westmead = [7650,
7690,
7410,
8140,
8290,
8440,
8590,
8740,
8890,
9040,
9190,
9330,
9480,
9630,
9780,
9930,
10080,
10220,
10370,
10520,
10670,
10810,
10960,
11110
]

for i in range(len(year_val)):
	data = (district[2], year_val[i], district_pred_parra[i], pop_prediction[i], district_out_westmead[i],district_in_westmead[i])
	cursor.execute(add_user_data, data)

cnx.commit()
cursor.close()
cnx.close()