from collections import Counter
import re
import mysql.connector as MySQLdb

 
def token(text):
    wordToRemove = " c’est - + * qui = « tu mes quoi le se la les à est et si sur mon de du des par pour même a afin donc vous pas un il une en avec ça dans au ils je ! ? tout toute tous  sont que mai plus leur ce mais : ; ,   "
    wordlist = text.split()
    newtext = [x for x in wordlist if x not in wordToRemove]
    for x in newtext:
        mots = re.findall(r'\w+', x)
    return Counter(newtext)
def trending():
    connexion = MySQLdb.connect(host="tp-epu",port=3308, user="besbesa", password="n28yzv9n", database="besbesa",charset='utf8')
    curseur=connexion.cursor()
    curseur.execute("Select region,text from Tweets;")
    region={}
    tweets=curseur.fetchall()
    for tweet in tweets :
        if not(tweet[0] in region.keys()):
            region[tweet[0]]=[tweet[1]]
        else:
            region[tweet[0]].append(tweet[1])

    text=""
    for i in region.keys():
        for j in region[i] :
            text=text+j
        region[i]=text
        text=""
    first_three=[]
    regions=list(region.keys())
    for i in region.keys():
        region[i]=token(region[i].lower())
        first_three.append(list(region[i])[:3])
    for i in range(len(regions)):
        print("the first 3 words trending in", regions[i] ," are ",first_three[i])
    
trending()