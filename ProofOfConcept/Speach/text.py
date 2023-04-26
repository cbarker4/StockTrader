import requests


test = requests.get("https://www.joincolossus.com/episodes/84175166/varty-trail-magic").text
open("Temp.txt","w").write(test)