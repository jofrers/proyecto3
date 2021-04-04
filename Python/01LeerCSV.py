#Jofre Rolong
#Lectura de fichero CSV

import csv

with open('./Python/01LeerCSV.csv') as File:
    misDatosReunion = csv.DictReader(File, delimiter=";")
    for asistente in misDatosReunion:
        print (asistente['Nombre'] + '-' + asistente['Correo'] + '-' + asistente['Rol'])
    