import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def obtener_sorteos_jps():
    url = "https://www.jps.go.cr/resultados"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    sorteos = []
    for item in soup.select(".resultado-sorteo"):  # Ajustar selector real
        fecha_texto = item.select_one(".fecha").get_text(strip=True)
        numeros_texto = item.select_one(".numeros").get_text(strip=True)

        fecha = datetime.strptime(fecha_texto, "%d/%m/%Y").strftime("%Y-%m-%d")
        numeros = [int(n) for n in numeros_texto.split(",")]
        sorteos.append({"fecha": fecha, "numeros": numeros})
    return sorteos

def obtener_sorteos_loto():
    url = "https://www.lotonicaragua.com/resultados"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    sorteos = []
    for item in soup.select(".resultado-sorteo"):  # Ajustar selector real
        fecha_texto = item.select_one(".fecha").get_text(strip=True)
        numeros_texto = item.select_one(".numeros").get_text(strip=True)

        fecha = datetime.strptime(fecha_texto, "%d/%m/%Y").strftime("%Y-%m-%d")
        numeros = [int(n) for n in numeros_texto.split(",")]
        sorteos.append({"fecha": fecha, "numeros": numeros})
    return sorteos

if __name__ == "__main__":
    todos = obtener_sorteos_jps() + obtener_sorteos_loto()
    with open("resultados.json", "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)
    print("Resultados guardados en resultados.json")
