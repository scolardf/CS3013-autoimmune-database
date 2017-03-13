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
steroidsYesorNo = []
indexValue = []
yes = 0
no = 0
total = 0
counter = 0
yesArray = []
noArray = []

for row in cur.fetchall():
    if (row[21] != 'NULL'):
        if (row[11] != ''):
            steroidsYesorNo.append(row[11])
            indexValue.append(row[21])

for x in range(0, len(steroidsYesorNo)):
    if (steroidsYesorNo[x] == 'Yes'):
        yes += 1
        yesArray.append(indexValue[x])
    else:
        no += 1
        noArray.append(indexValue[x])

yesAverage = decimal.Decimal(0)
for y in range (0, len(yesArray)):
    yesAverage=decimal.Decimal(yesAverage)+decimal.Decimal(yesArray[y])

yesAverage = yesAverage/y

noAverage = decimal.Decimal(0)
for z in range (0, len(noArray)):
    noAverage = decimal.Decimal(noAverage)+decimal.Decimal(noArray[z])

noAverage = noAverage/z
print yesAverage
print noAverage