import socket

class esp32:
    def __init__(self):
        self.esp32_ip = "192.168.120.101"
        self.esp32_port = 80

    def turn_relay(self, state):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.esp32_ip, self.esp32_port))
                if state == 0:
                    s.sendall('0'.encode())
                elif state == 1:
                    s.sendall('1'.encode())
                
            
    def info(self):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.esp32_ip, self.esp32_port))
                s.sendall("2".encode())
                response = s.recv(1024)
                return response.decode()
