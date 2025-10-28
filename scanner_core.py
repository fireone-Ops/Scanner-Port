import socket

<<<<<<< HEAD
def scan_port(host: str, port: int, timeout: float = 0.8) -> dict:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = {"port": port, "open": False, "error": None}
=======
def scan_port_resolve(host, port, timeout=0.8):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = {'port': port, 'open': False, 'error': None}
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
    try:
        code = s.connect_ex((host, port))
        result["open"] = (code == 0)
    except Exception as e:
        result["error"] = str(e)
    finally:
        s.close()
    return result

if __name__ == "__main__":
    host = "192.168.0.1"
    for p in [22, 80, 443]:
<<<<<<< HEAD
        r = scan_port(host, p)
=======
        r = scan_port_resolve(host, p)
>>>>>>> 1db0ca9 (Primeiro commit — Mini Port Scanner)
        print(r)
