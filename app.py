<<<<<<< HEAD
from flask import Flask, request, render_template_string, redirect, url_for, send_file
from multi_scan import scan_ports   # função que faz o scan paralelo
=======
#Bloco A

from flask import Flask, request, render_template_string, redirect, url_for, send_file
from multi_scan import scan_ports
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
import json
from io import BytesIO

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<title>Mini Port Scanner</title>
<h1>Mini Port Scanner</h1>

<form method="post">
<<<<<<< HEAD
  Host/IP: <input name="host" value="{{ host or '127.0.0.1' }}" required><br>
=======
  Host/IP: <input name="host" value="{{ host or '192.168.0.1' }}" required><br>
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
  Ports (ex: 20-1024 or 22,80,443): <input name="ports" value="{{ ports or '20-1024' }}"><br>
  Threads: <input name="threads" value="{{ threads or '100' }}"><br>
  Timeout(s): <input name="timeout" value="{{ timeout or '0.6' }}"><br>
  <button type="submit">Scan</button>
</form>

{% if scan %}
  <h2>Resultados para {{ scan.host }} — {{ "%.2f"|format(scan.elapsed) }}s</h2>
  <a href="{{ url_for('export_json') }}">Exportar JSON</a>
  <ul>
  {% for r in scan.results %}
    <li>{{ r.port }} — <strong style="color:{{ 'green' if r.open else 'gray' }}">{{ 'OPEN' if r.open else 'closed' }}</strong>
        {% if r.get('banner') %} — {{ r.banner[:120] }}{% endif %}</li>
  {% endfor %}
  </ul>
{% endif %}
"""
<<<<<<< HEAD
# app.py (bloco B)
LAST_SCAN = None  # guarda em memória o último scan para export

def parse_ports(ports_raw: str):
    """Converte string tipo '20-1024' ou '22,80,443' em lista de ints."""
=======

#Bloco B

# app.py (bloco B)
LAST_SCAN = None 

def parse_ports(ports_raw: str):
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
    s = ports_raw.strip()
    ports = []
    if "-" in s and "," not in s:
        a, b = s.split("-", 1)
        a, b = int(a), int(b)
<<<<<<< HEAD
        # limite razoável para evitar scans gigantes
=======
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
        if b - a > 5000:
            b = a + 5000
        ports = list(range(a, b + 1))
    else:
        parts = [p.strip() for p in s.split(",") if p.strip()]
        for p in parts:
            if "-" in p:
                pa, pb = p.split("-", 1)
                ports.extend(range(int(pa), int(pb) + 1))
            else:
                ports.append(int(p))
<<<<<<< HEAD
    # cap total
=======
    
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
    if len(ports) > 8000:
        ports = ports[:8000]
    return ports

@app.route("/", methods=["GET", "POST"])
def index():
    global LAST_SCAN
    scan = None
<<<<<<< HEAD
    host = "192.168.0.1"
=======
    host = "198.162.0.1"
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
    ports_str = "20-1024"
    threads = 100
    timeout = 0.6

    if request.method == "POST":
        host = request.form.get("host", host).strip()
        ports_str = request.form.get("ports", ports_str).strip()
        try:
            threads = int(request.form.get("threads", threads))
        except:
            threads = 100
        try:
            timeout = float(request.form.get("timeout", timeout))
        except:
            timeout = 0.6

        ports = parse_ports(ports_str)
<<<<<<< HEAD
        # limitar para segurança / performance
        if len(ports) > 3000:
            ports = ports[:3000]

        # === AQUI chamamos o scanner (síncrono) ===
=======
        if len(ports) > 3000:
            ports = ports[:3000]
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
        scan = scan_ports(host, ports, max_workers=threads, timeout=timeout)
        LAST_SCAN = scan

    return render_template_string(INDEX_HTML, scan=scan, host=host, ports=ports_str, threads=threads, timeout=timeout)

<<<<<<< HEAD

=======
# Bloco C
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
@app.route("/export.json")
def export_json():
    global LAST_SCAN
    if not LAST_SCAN:
        return redirect(url_for("index"))
    data = {
        "host": LAST_SCAN.host,
        "elapsed": LAST_SCAN.elapsed,
        "results": LAST_SCAN.results,
    }
    buf = BytesIO()
    buf.write(json.dumps(data, indent=2).encode("utf-8"))
    buf.seek(0)
    return send_file(buf, mimetype="application/json", as_attachment=True, download_name="scan_results.json")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
