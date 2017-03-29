import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import decimal
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="hellogoodbye",
                     db="test3")
cur = db.cursor();

cur.execute("SELECT * FROM visit WHERE HealthIndex is NULL ")

Index5L = []
Index3L = []
HealthIndex5L = []
HealthIndex3L = []

f=open('C:\Users\caolan\Desktop\Programming Project\DATABASE FILES\SQLupdate.txt', 'w')

for row in cur.fetchall():
    if(row[14]=='3L'):
        Index3L.append(row[20])
        HealthIndex3L.append((0.2472*(row[0]))+(0.2247*(row[1]))-(0.0034*(row[2])) + (0.025*(row[3])) + (0.0282*(row[4])))



    if(row[14]=='5L'):
        Index5L.append(row[20])
        HealthIndex5L.append((0.1107*(row[0])) + (0.2186*(row[1])) - (0.1367*(row[2])) + (0.0872*(row[3])) + (0.1945*(row[4])))
for i in range(0, len(Index3L)):
    f.write("\n UPDATE visit SET HealthIndex = '" + str(HealthIndex3L[i]) + "' WHERE ID = '"+ str(Index3L[i]) + "';")

for i in range(0, len(Index5L)):
    f.write("\n UPDATE visit SET HealthIndex = '" + str(HealthIndex5L[i]) + "' WHERE ID = '"+ str(Index5L[i]) + "';")

