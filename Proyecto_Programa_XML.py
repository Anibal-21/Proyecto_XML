from Proyecto_Funciones_XML import *

estructura=leer_xml("ejercicioProyecto.xml")

#Ejercicio 1: Lista de localizacion.
for lista in localizacion(estructura):
    print (lista)

#Ejercicio 2:¿Cuantos equipos aparecen?.
for numero in equipos(estructura):
    print (numero)

#Ejercicio 3: 
