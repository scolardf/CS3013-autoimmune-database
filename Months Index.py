import sys
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import decimal
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="hellogoodbye",
                     db="test3")
cur = db.cursor();

cur.execute("SELECT * FROM visit")

MonthsList = [[] for y in range (200)]
Averages = [0,0,0,0,0,0,0,0,0,0,0,0]
NoOfAverages = [0,0,0,0,0,0,0,0,0,0,0,0]

for row in cur.fetchall():
    if(row[21]!=None):
        MonthsList[row[5].month-1].append(row[21])

for x in range(0, 12):
    for y in range(0, len(MonthsList[x])):
        Averages[x]+= MonthsList[x][y]
        NoOfAverages[x]+=1

for x in range(0, 12):
    Averages[x] = Averages[x]/NoOfAverages[x]

if(len(sys.argv) == 1):
    #barchart
    width = 0.5
    N = 12
    ind = np.arange(N)
    p = [12]
    offset = 1
    p0 = plt.bar(offset, Averages[0], width, color='b')
    offset+=1
    p1 = plt.bar(offset, Averages[1], width, color = 'g')
    offset+=1
    p2 = plt.bar(offset, Averages[2], width, color = 'y')
    offset+=1
    p3 = plt.bar(offset, Averages[3], width, color = 'r')
    offset+=1
    p4 = plt.bar(offset, Averages[4], width, color = 'c')
    offset+=1
    p5 = plt.bar(offset, Averages[5], width, color = 'm')
    offset+=1
    p6 = plt.bar(offset, Averages[6], width, color = 'y')
    offset+=1
    p7 = plt.bar(offset, Averages[7], width, color = 'k')
    offset+=1
    p8 = plt.bar(offset, Averages[8], width, color = '#6495ed')
    offset+=1
    p9 = plt.bar(offset, Averages[9], width, color = '#adff2f')
    offset+=1
    p10 = plt.bar(offset, Averages[10], width, color = '#cd5c5c')
    offset+=1
    p11 = plt.bar(offset, Averages[11], width, color = '#ffa500')
    offset+=1
    plt.title('Average health index of patients per month')
    plt.xticks(ind+1, ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
    plt.show()
if(len(sys.argv)>1):
        print Averages[sys.argv[1]]