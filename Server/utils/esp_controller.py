import socket

class Controller:
    def __init__(self) -> None:
        self.esp_ip = '192.168.108.11'
        self.esp_port = 80

    def send_data(self, data):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.esp_ip, self.esp_port))

            sock.sendall(data.encode('utf-8'))

            if data in ['1', '0']:
                sock.close()
            elif data in ['2']:
                response = sock.recv(1024)
                sock.close()
                return response.decode('utf-8')

        except Exception as e:
            print("Error:", e)


