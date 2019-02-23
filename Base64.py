#/usr/bin / python3
import base64
import time 

print("1 para codificar em base64")
print("2 para decodificar em base64")
time.sleep(0.5)

sair = False
while not sair:
    escolha = input("Qual opção? ")
    if escolha == "1":
        codificar = input("Codificar: ")
        time.sleep(1.4)
        virar_bytes = codificar.encode("UTF-8")
        transformar = base64.b64encode(virar_bytes)
        base64_cod = transformar.decode("UTF-8")
        print(base64_cod)
    elif escolha == "2":
        decodificar =  input("Dedificar: ")
        time.sleep(1.4)
        virar_bytes = decodificar.encode("UTF-8")
        transformar = base64.b64decode(virar_bytes)
        base64_cod = transformar.decode("UTF-8")
        print(base64_cod)
    else:
        print("Algo invalido digitado infelizmente!")
        time.sleep(3)