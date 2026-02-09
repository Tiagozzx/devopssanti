import requests
import time
from datetime import datetime

sitios = ["https://www.google.com", "https://github.com", "https://www.python.org", "https://www.openai.com"]
resultados = []

print("Iniciando Escaneo...")

for url in sitios:
    start_time = time.time()
    try:
        r = requests.get(url, timeout=5)
        latency = (time.time() - start_time) * 1000 # Convertir a milisegundos
        if r.status_code == 200:
            estado = "Online"
            clase = "success"
        else:
            estado = f"Error {r.status_code}"
            clase = "warning"
    except:
        estado = "Offline"
        latency = 0
        clase = "danger"
    
    resultados.append((url, estado, f"{latency:.2f} ms", clase))

# HTML CON ESTILOS MODERNOS (BOOTSTRAP)
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard DevOps</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #f8f9fa; padding: 20px; }}
        .card {{ box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">Monitor de Servicios</h1>
        <p class="text-center text-muted">Último escaneo: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        <div class="card p-4">
            <table class="table table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>Sitio Web</th>
                        <th>Estado</th>
                        <th>Latencia (Velocidad)</th>
                    </tr>
                </thead>
                <tbody>
"""

for url, estado, latencia, clase in resultados:
    html_content += f"""
                    <tr class="table-{clase}">
                        <td><strong>{url}</strong></td>
                        <td>{estado}</td>
                        <td>{latencia}</td>
                    </tr>
    """

html_content += """
                </tbody>
            </table>
        </div>
        <footer class="text-center mt-4">
            <small>Generado automáticamente por GitHub Actions</small>
        </footer>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Dashboard generado con éxito.")