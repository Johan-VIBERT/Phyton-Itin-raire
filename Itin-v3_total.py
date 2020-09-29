import math
math.inf = float("inf")
from pyroutelib3 import Router
import os
os.fspath = lambda x : x
import folium
import webbrowser




input('Appuyer sur une touche pour commencer')
c= folium.Map(location=[47.651550,-2.083622],zoom_start=17)
router = Router("car")
depart = router.findNode(47.654522,-2.081007)
arrivee = router.findNode(47.648544,-2.085589)
status, route = router.doRoute(depart, arrivee)
if status == 'success':
    routeLatLons_car = list(map(router.nodeLatLon, route))
taille=len(routeLatLons_car)
coord1=routeLatLons_car[0]
coord2=routeLatLons_car[taille-1]

##--------------------------------------------------------

router = Router("foot")
depart = router.findNode(47.654522,-2.081007)
arrivee = router.findNode(47.648544,-2.085589)
status, route = router.doRoute(depart, arrivee)
if status == 'success':
    routeLatLons_foot = list(map(router.nodeLatLon, route))
taille=len(routeLatLons_foot)
coord3=routeLatLons_foot[0]
coord4=routeLatLons_foot[taille-1]

##---------------------------------------------------------

i=1
dist_car=dist_foot=0
while (i < taille):
    coord1=routeLatLons_car[i-1]
    coord2=routeLatLons_car[i]
    coord3=routeLatLons_foot[i-1]
    coord4=routeLatLons_foot[i]
    dist_car=dist_car + (router.distance(coord1,coord2))
    dist_foot=dist_foot + (router.distance(coord3,coord4))
    i+=1
    folium.PolyLine([coord1,coord2], weight = 4, tooltip=('voiture  ( ' + str(round(dist_car,3)) + 'km )'), color = 'blue').add_to(c)
    folium.PolyLine([coord3,coord4], weight = 4, tooltip =('A pied  ( ' + str(round(dist_foot,3)) + 'km )'), color = 'red', opacity=0.7).add_to(c)
c.save('maCarte2.html')
webbrowser.open('maCarte2.html')