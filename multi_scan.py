from concurrent.futures import ThreadPoolExecutor, as_completed
<<<<<<< HEAD
from scanner_core import scan_port
import time

def scan_ports(host: str, ports: list, max_workers: int = 100, timeout: float = 0.6):
    results = []
    start = time.time()
    with ThreadPoolExecutor(max_workers=min(max_workers, len(ports))) as ex:
        futures = {ex.submit(scan_port, host, p, timeout): p for p in ports}
        for fut in as_completed(futures):
            try:
                results.append(fut.result())
            except Exception as e:
                results.append({"port": futures[fut], "open": False, "error": str(e)})
    elapsed = time.time() - start
    results.sort(key=lambda r: r["port"])
=======
from scanner_core import scan_port_resolve
import time

def scan_ports(host: str, ports: list, max_workers: int = 100, timeout: float = 0.8):
    results = []
    start = time.time()

    with ThreadPoolExecutor(max_workers=min(max_workers, len(ports))) as executor:
        futures = {executor.submit(scan_port_resolve, host, p, timeout): p for p in ports}
        for fut in as_completed(futures):
            port = futures[fut]
            try:
                res = fut.result()
                results.append(res)
            except Exception as e:
                results.append({"port": port, "open": False, "error": str(e)})

    elapsed = time.time() - start
    results.sort(key=lambda r: r.get("port", 0))
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
    return {"host": host, "scanned_ports": len(ports), "elapsed": elapsed, "results": results}

if __name__ == "__main__":
    host = "192.168.0.1"
<<<<<<< HEAD
    ports = list(range(20, 1025))
    summary = scan_ports(host, ports, max_workers=200, timeout=0.5)
    print(f"Scan de {summary['scanned_ports']} portas em {summary['elapsed']:.2f}s")
    open_ports = [r for r in summary['results'] if r['open']]
    print("Open ports:", [r['port'] for r in open_ports])
=======
    ports = list(range(20, 1025)) 
    summary = scan_ports(host, ports, max_workers=200, timeout=0.6)
    print(f"Scan de {summary['scanned_ports']} portas em {summary['elapsed']:.2f}s")
    open_ports = [r for r in summary["results"] if r.get("open")]
    print("Open ports:", [r["port"] for r in open_ports])
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
