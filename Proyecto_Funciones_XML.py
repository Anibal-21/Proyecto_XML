from lxml import etree
import sys
def leer_xml(fichero):
    try:
        with open(fichero) as f:
            datos=etree.parse(fichero)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

#Ejercicio 1:Lista de localizacion.
def localizacion(estructura):
    lista = estructura.xpath('/repose/sports/sportsItem/name/id/type/leagues/leaguesItem/name/abbreviation/id/groupId/shortName/groups/groupsItem/id/name/abbreviation/competitors/competitorsItem/id/location')
    return lista


#Ejercio 2: ¿Cuantos equipos aparecen?.
def equipos(estructura):
    numero = estructura.xpath('count(/repose/sports/sportsItem/name/id/type/leagues/leaguesItem/name/abbreviation/id/groupId/shortName/groups/groupsItem/id/name)')
    return numero

