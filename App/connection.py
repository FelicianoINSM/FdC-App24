import requests


class Connect():
    def __init__(self) -> None:
        self.url = "http://127.0.0.1:5000/v1/bomb"

    def bomb_test(self, state):
        data = {
            'value': f'{state}'
        }
        response = requests.post(self.url, json=data)
