import sys
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import decimal
import string

def barchartIndices(IndicesTuple):
    average = 0
    MonthsList = [[] for y in range(200)]
    Averages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    NoOfAverages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(0, len(IndicesTuple)):
        average += IndicesTuple[x][0]
        Averages[IndicesTuple[x][1]-1]+=IndicesTuple[x][0]
        NoOfAverages[IndicesTuple[x][1]-1]+=1
        MonthsList[IndicesTuple[x][1]-1].append(IndicesTuple[x][0])
    average = average/len(IndicesTuple)
    MonthsList = filter(None, MonthsList)
    for y in range (0, 12):
        Averages[y] = Averages[y]/NoOfAverages[y]
    print average
    print Averages
    print NoOfAverages
    # barchart
    width = 0.5
    N = 12
    ind = np.arange(N)
    p = [12]
    offset = 1
    p0 = plt.bar(offset, Averages[0], width, color='b')
    offset += 1
    p1 = plt.bar(offset, Averages[1], width, color='g')
    offset += 1
    p2 = plt.bar(offset, Averages[2], width, color='y')
    offset += 1
    p3 = plt.bar(offset, Averages[3], width, color='r')
    offset += 1
    p4 = plt.bar(offset, Averages[4], width, color='c')
    offset += 1
    p5 = plt.bar(offset, Averages[5], width, color='m')
    offset += 1
    p6 = plt.bar(offset, Averages[6], width, color='y')
    offset += 1
    p7 = plt.bar(offset, Averages[7], width, color='k')
    offset += 1
    p8 = plt.bar(offset, Averages[8], width, color='#6495ed')
    offset += 1
    p9 = plt.bar(offset, Averages[9], width, color='#adff2f')
    offset += 1
    p10 = plt.bar(offset, Averages[10], width, color='#cd5c5c')
    offset += 1
    p11 = plt.bar(offset, Averages[11], width, color='#ffa500')
    offset += 1
    plt.title('Average health index of patients per month')
    plt.xticks(ind + 1, (
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
    'December'))
    plt.show()

    return


db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="hellogoodbye",
                     db="test3")
cur = db.cursor();

cur.execute("SELECT * FROM visit")
x=set()

activeIndices = []
remissionIndices = []
lowIndices = []

activeCount = 0
remissionCount = 0
lowCount = 0

activeAverage = 0
remissionAverage = 0
lowAverage = 0

for row in cur.fetchall():
    if(row[21]!=None):
        indexAndMonth = (row[21], row[5].month)
        if(string.lower(row[15])=='active'):
            activeIndices.append(indexAndMonth)
            activeCount+=1
        if(string.lower(row[15])=='remission'):
            remissionIndices.append(indexAndMonth)
            remissionCount+=1
        if(string.lower(row[15])=='low disease activity'):
            lowIndices.append(indexAndMonth)
            lowCount+=1


print activeCount
print remissionCount
print lowCount
if(sys.args[1]==1):
    barchartIndices(activeIndices)
if(sys.args[1]==2):
    barchartIndices(remissionIndices)
if(sys.args[1]==3):
    barchartIndices(lowIndices)
