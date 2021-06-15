import folium
import mysql.connector as MySQLdb
from mysql.connector import errorcode
france=[46.2276, 2.2137] 
map = folium.Map(location = france,title='Trending words ', zoom_start=6) 
folium.Marker([45.9026, 6.1275],  popup='Annecy').add_to(map)
connexion = MySQLdb.connect(host="tp-epu",port=3308, user="besbesa", password="n28yzv9n", database="besbesa",charset='utf8')
curseur=connexion.cursor()
curseur.execute("Select position_X,position_Y,text from Tweets;")
 
points=curseur.fetchall()

for point in points:
    folium.Marker([float(point[0]), float(point[1])],  popup=point[2]).add_to(map)
 

map.save('map.html')