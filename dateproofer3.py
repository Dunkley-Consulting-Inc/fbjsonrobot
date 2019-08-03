from daterobot import lstnuevafecha
import datetime
import time

diadef = []
# print lstnuevafecha

# for matchdays with three sunday matches. Frozenset items must be adapted each season
specialMD = frozenset([4, 7, 9, 15])

for date in lstnuevafecha:
    jornada = len(diadef) / 9
    jornada += 1
    # print jornada
    # datelst=[]
    fecha = date.split('-')
    dia = fecha[0]
    mes = fecha[1]
    yyear = fecha[2]
    strdate = dia + ',' + mes + ',' + yyear
    for i in range(0, len(fecha)):
        date1 = datetime.datetime.strptime(strdate, "%Y,%m,%d")
        date2 = date1.strftime('%A')

    if jornada in specialMD:
        if date2 == "Friday":
            diadef.append(date)

        elif date2 == "Saturday":
            for i in range(0, 5):
                diadef.append(date)
        else:
            for i in range(0, 3):
                diadef.append(date)

    # for the last two matchdays of each tournament,
    # all matches in one day
    # to be verified at the end of this tournament
    elif jornada > 32:
        for i in range(0, 9):
            diadef.append(date)

    # only for season 2016/2017. MD on Easter Week. Delete or adjust for other seasons
    # elif jornada == 29:
        # for i in range(0,6):
            # diadef.append(date)

    elif date2 == "Friday":
        diadef.append(date)

    elif date2 == "Saturday":
        for i in range(0, 6):
            diadef.append(date)

    elif date2 == "Sunday":
        for i in range(0, 2):
            diadef.append(date)

    elif date2 == "Tuesday":
        for i in range(0, 4):
            diadef.append(date)

    # for wednesday matches on english weeks
    else:
        for i in range(0, 5):
            diadef.append(date)


# print diadef
# print len(diadef)