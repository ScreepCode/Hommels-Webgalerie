import os
import json

data = '{"title": "Wales; Bucht bei St Annes Head","year": "2018","format": "80 x 60 cm","technic": "Oel auf Leinwand"}'

jsonData = json.loads(data)
name = jsonData["title"].replace(" ", '_') + "_" + jsonData["year"].replace(" ", '_') + "_" + jsonData["format"].replace(" ", '_') + "_" + jsonData["technic"].replace(" ", '_')

path = os.path.abspath(".")+ "/"
files=os.listdir(path)
for x in files:
    print(x)

os.rename(path + "Kachel.jpg", path + name+ "_Kachel.jpg")
os.rename(path + "mittel.jpg", path + name+ "_mittel.jpg")
os.rename(path + "groß.jpg", path + name+ "_groß.jpg")
