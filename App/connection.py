import requests


class Connect():
    def __init__(self, url) -> None:
        self.url = url
    def ping():
        try:
            url = requests.get("http://fdcyt24.ddns.net:5000/v1/history")
            data = url.json()[:0]  # Obtener las primeras seis entradas"
        except Exception as e:
            print(f'Connection failed: {e}')
