import requests
import os
import sys
import json

REPO = os.environ.get('GITHUB_REPOSITORY') 
TOKEN = os.environ.get('GITHUB_TOKEN')    

SITIOS = ["https://www.google.com", "https://github.com", "https:santi.com"]

print(f"Iniciando para: {REPO}")

errores = []

for url in SITIOS:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            errores.append(f"{url} respondio con código {r.status_code}")
    except Exception as e:
        errores.append(f"{url} ERROR DE CONEXION")

if errores and REPO and TOKEN:
    print(f"Se detectaron {len(errores)} fallos. Creando Issue...")
    
    titulo = f" Reporte de Incidente: {len(errores)} servicios caídos"
    cuerpo = "### El monitor detecto problemas:\n\n" + "\n".join([f"- {e}" for e in errores])
    cuerpo += "\n\n*Por favor revisar.*"

    api_url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"title": titulo, "body": cuerpo, "labels": ["bug", "auto-generated"]}

    try:
        r = requests.post(api_url, json=data, headers=headers)
        if r.status_code == 201:
            print("Issue creada")
        else:
            print(f"Error creando issue: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"Falló la conexion con GitHub: {e}")

elif errores:
    print("ERROR")
else:
    print("Todo funciona perfecto")