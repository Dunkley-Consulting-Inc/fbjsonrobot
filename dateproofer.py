from daterobot import lstnuevafecha
import datetime
import time

#print lstnuevafecha
diadef=[]
for date in lstnuevafecha:
	datelst=[]
	fecha=date.split('-')
	dia=fecha[0]
	mes=fecha[1]
	yyear=fecha[2]
	strdate=dia+','+mes+','+yyear
	for i in range(0, len(fecha)):
		date1=datetime.datetime.strptime(strdate, "%d,%m,%Y")
		date2=date1.strftime('%A')
	if date2=="Friday":
		diadef.append(date)

	elif date2=="Saturday":
		for i in range(0,6):
			diadef.append(date)
		
	elif date2=="Sunday":
		for i in range(0,2):
			diadef.append(date)
		
	elif date2=="Tuesday":
		for i in range(0,4):
			diadef.append(date)
				
	else:
		for i in range(0,5):
			diadef.append(date)
		

#print diadef
#print len(diadef)