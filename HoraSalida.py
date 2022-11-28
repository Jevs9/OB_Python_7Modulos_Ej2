import datetime
import math

actual = datetime.datetime.now()
year = actual.year
mes = actual.month
dia = actual.day

salida = datetime.datetime(year, mes, dia, 19, 00, 00)

if actual.hour < 19:
    res = salida - actual
    horas = math.trunc(res.seconds/3600)
    minutos = math.trunc(((res.seconds/3600)-horas)*60)
    segundos = round(res.seconds - horas*3600 - minutos*60)
    print(f' Aún NO es hora de ir a casa, faltan: {horas} horas con {minutos} minutos y {segundos} segundos')
else:
    print("Ya es hora de ir a casa")
