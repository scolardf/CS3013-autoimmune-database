from django.http import HttpResponse


def simple(request):	
	import MySQLdb
	import matplotlib.pyplot as plt
	import numpy as np
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	import matplotlib.pyplot as plt 
	import django

	db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="alexis",
                     db="test")

	cur = db.cursor()

	cur.execute("SELECT * FROM patients")
	year_of_birth = []
	year_of_diagnosis = []
	ageAtDiagnosis = []

	for row in cur.fetchall():

	    if((row[4])!=None):
	        year_of_birth.append(row[2])
	        year_of_diagnosis.append(row[4].year)

	for x in range(0, len(year_of_birth)):
	    ageAtDiagnosis.append(year_of_diagnosis[x]-year_of_birth[x])

	counter = 0
	average = 0
	birthYearMax = 0
	birthYearMin = 0
	min = 9999
	max = 0

	for counter in range (0, len(ageAtDiagnosis)):
	    if(ageAtDiagnosis[counter]<min):
	        min=ageAtDiagnosis[counter]
	    if(ageAtDiagnosis[counter]>max):
	        max=ageAtDiagnosis[counter]
	    print ageAtDiagnosis[counter]
	    average = average + ageAtDiagnosis[counter]
	average = average/counter
	list = []
	for number in range (0, max+1):
	    list.append(number)
	y = np.bincount(ageAtDiagnosis)
	z = np.nonzero(y)[0]
	plt.xlabel("Frequency of ages")
	plt.ylabel("Ages")
	plt.title("Frequency of ages at diagnosis")
	plt.plot(list, y)
	canvas = FigureCanvas(plt.figure(1))
	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response
	
