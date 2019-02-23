import requests
import json 
import time 

print("1 - Para Encrypt""\n")
print("2 - Para Decrypt""\n")
time.sleep(3)
escolha = input("Encrypt ou Decrypt? ")


if escolha == "1" or "Encrypt": 
    encryptar = input("Selecione a palavra a criptografar:")
    a = requests.get("https://md5.pinasthika.com/api/encrypt?value=" + encryptar)
    dicionario = json.loads(a.text) 
    print('Md5:', dicionario['result'])
    time.sleep(1.0)
elif escolha == "2" or "Decrypt":
    decryptar = input("Selecione a hash pra descriptografar::")
    a = requests.get("https://md5.pinasthika.com/api/encrypt?value=" + decryptar)
    dicionario = json.loads(a.text) 
    print('Resultado:', dicionario['result'])
    time.sleep(1.0)

else:
    print("Opções inválidas")


#SH

