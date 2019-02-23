import requests
import json 


a = requests.get("https://md5.pinasthika.com/api/encrypt?value=md5api")


dicionario = json.loads(a.text) 
print('Md5:', dicionario['result'])


#SH