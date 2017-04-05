import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import decimal
import string
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="password",
                     db="VasculitisDatabase")

cur = db.cursor()

cur.execute("SELECT * FROM visit")
ProphylaxisYesorNo = []
indexValue = []
total = 0
counter = 0
yesArray = []
noArray = []
wordList = set()

for row in cur.fetchall():
    if ((row[13]=='Non') or (row[13]=='No')):
        noArray.append(row[21])
    else:
        yesArray.append(row[21])
        wordArray = (row[13].split('+'))
        for i in range(0, len(wordArray)):
            wordList.add(string.strip(string.lower(wordArray[i])))

wordList.remove('')

yesAverage = decimal.Decimal(0)
for y in range(0, len(yesArray)):
    if(yesArray[y]!=None):
        yesAverage += decimal.Decimal(yesArray[y])

noAverage = decimal.Decimal(0)
for z in range(0, len(noArray)):
    if(noArray[z]!=None):
        noAverage += decimal.Decimal(noArray[z])

yesAverage = yesAverage/y
noAverage = noAverage/z
#barchart
width = 0.6
N = 2
ind = np.arange(N)
p1 = plt.bar(0.2, yesAverage, width, color = 'green')
p2 = plt.bar(1, noAverage, width, color = 'red')

plt.ylabel('Index average')
plt.title('Average index of those issued prophylaxis vs. \n those not issued prophylaxis')
plt.xticks(ind, ('Prophylaxis Average', 'No Prophylaxis Average'))
plt.yticks(np.arange(0,0.9,0.1))
print float(yesAverage)
print float(noAverage)
print len(noArray)
print len(yesArray)
print (wordList)
plt.show()