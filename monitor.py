import requests
from datetime import datetime

sitios = ["https://www.google.com", "https://github.com", "https://www.python.org"]
resultados = []

print("🚀 Iniciando Escaneo...")

for url in sitios:
    try:
        r = requests.get(url, timeout=5)
        estado = "🟢 FUNCIONANDO" if r.status_code == 200 else f"🔴 ERROR {r.status_code}"
    except:
        estado = "⚫ CAÍDO"
    resultados.append((url, estado))

html_content = f"""
<html>
<body style="font-family: Arial; padding: 20px;">
    <h1>📊 Reporte de Salud DevOps</h1>
    <p>Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <ul>
"""
for url, est in resultados:
    html_content += f"<li><strong>{url}</strong>: {est}</li>"
html_content += "</ul></body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("✨ Reporte index.html creado.")