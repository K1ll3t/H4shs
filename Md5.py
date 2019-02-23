import hashlib 
import time
# -*- coding: utf-8 -*-


  
print("1 para codificar em md5:") 
print("2 para decodificar em md5")
time.sleep(0.5)

sair = False
while not sair:
    escolha = input("Qual opcao? ")
    if escolha == "1":
        codificar = input("Codificar: ")
        time.sleep(1.4)
        cod = hashlib.md5(codificar.encode())
        print("Codificador: ", end="")
        print(cod.hexdigest())
    
    else:
        print("Deu erro")

"""
result = hashlib.md5(str.encode()) 
  

print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 
"""