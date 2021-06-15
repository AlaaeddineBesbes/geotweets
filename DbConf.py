import json
import mysql.connector as MySQLdb
from mysql.connector import errorcode
import requests
class BD:
    def __init__(self,jsonFile):
        self.file=jsonFile


    def getLocation(self,lon,lat):
                solditems = requests.get('https://nominatim.openstreetmap.org/reverse.php?lat='+str(lat)+'&lon='+str(lon)+'&zoom=5&format=jsonv2') # (your url)
                data = solditems.json()
                return solditems.json()["name"]

    def insertData(self,connexion):
        curseur=connexion.cursor()
        tweets_file = open(self.file, "r",encoding='utf-8')
        for line in tweets_file.readlines():
            tweet= json.loads(line)
            id = tweet["id_str"]
            nom=tweet["user"]["screen_name"]
            text=tweet["text"]
            creation_date=tweet["created_at"]
            try:
                position_X = (tweet["place"]["bounding_box"]["coordinates"][0][0][1] +
                                            tweet["place"]["bounding_box"]["coordinates"][0][1][1]) / 2.0
                position_Y = (tweet["place"]["bounding_box"]["coordinates"][0][0][0] +
                                            tweet["place"]["bounding_box"]["coordinates"][0][2][0]) / 2.0
                region=self.getLocation(position_Y,position_X)
                position_X=str(position_X)
                position_Y=str(position_Y)
                print("INSERT INTO Tweets (id, nom, text, creation_date, position_X, position_Y,region) VALUES('{}' ,'{}' ,'{}','{}','{}','{}','{}');".format(id,nom,text,creation_date,position_X,position_Y,region))
                curseur.execute("INSERT INTO Tweets (id, nom, text, creation_date, position_X, position_Y,region) VALUES('{}' ,'{}' ,'{}','{}','{}','{}','{}');".format(id,nom,text,creation_date,position_X,position_Y,region))
                print('done')
            except:
                print("error : localisation doesn't exists")


dbconfig=BD('frenchTweets1.json')
connexion = MySQLdb.connect(host="tp-epu",port=3308, user="besbesa", password="n28yzv9n", database="besbesa",charset='utf8')
dbconfig.insertData(connexion)       

