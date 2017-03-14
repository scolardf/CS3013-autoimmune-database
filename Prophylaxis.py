import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import decimal
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="hellogoodbye",
                     db="test3")

cur = db.cursor()

cur.execute("SELECT * FROM visit")
ProphylaxisYesorNo = []
indexValue = []
yes = 0
no = 0
total = 0
counter = 0
yesArray = []
noArray = []

for row in cur.fetchall():
    if (row[21] != None):
        if (row[11] != ''):
            ProphylaxisYesorNo.append(row[11])
            indexValue.append(row[21])

for x in range(0, len(ProphylaxisYesorNo)):
    if (ProphylaxisYesorNo[x] == 'Yes'):
        yes += 1
        yesArray.append(indexValue[x])
    else:
        no += 1
        noArray.append(indexValue[x])

yesAverage = decimal.Decimal(0)
for y in range (0, len(yesArray)):
    yesAverage+= decimal.Decimal(yesArray[y])

yesAverage = yesAverage/y
noAverage = decimal.Decimal(0)
for z in range (0, len(noArray)):
    noAverage = decimal.Decimal(noAverage)+decimal.Decimal(noArray[z])
noAverage = noAverage/z
#barchart
width = 0.6
N = 2
ind = np.arange(N)
p1 = plt.bar(0.2, yesAverage, width, color = 'green')
p2 = plt.bar(1, noAverage, width, color = 'red')

plt.ylabel('Index average')
plt.title('Average index of steroid and non-steroid users')
plt.xticks(ind, ('Steroid Average', 'Non-Steroid Average'))
plt.yticks(np.arange(0,0.9,0.1))
print float(yesAverage)
print float(noAverage)

plt.show()