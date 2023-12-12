# pip install requests
import requests
import time
import os
#App  que cada 5 segundos me muestre el valor en dolares
#del BITCOIN
os.system("cls")
while True:
    peticion = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = peticion.json()
    valorBitcoinUSD = data["bpi"]["USD"]["rate"]
    print(f"El Valor del Bitcoin actualmente es: USD {valorBitcoinUSD}")
    time.sleep(5)