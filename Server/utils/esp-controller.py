import socket

class Controller:
    def __init__(self) -> None:
        self.esp_ip = '0.0.0.0'
        self.esp_port = 0

    def send_data(self, data):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.esp_ip, self.esp_port))

            sock.sendall(data.encode('utf-8'))

            response = sock.recv(1024)
            return response.decode('utf-8')

        except Exception as e:
            print("Error:", e)

        finally:
            sock.close()
