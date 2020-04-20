import socket
import time


class ClientError(BaseException):
    """ Class - ClientError for implementing custom exceptions"""


class Client(ClientError):
    """ Client """

    def __init__(self, host, port, timeout=None):
        self.timeout = timeout
        self.sock = socket.socket()
        self.sock.connect((host, int(port)))

    def get(self, data_key):
        """ The function for send data to server and processing answers"""

        if data_key == '*':
            self.sock.sendall('get *\n'.encode())
            data_r = self.sock.recv(1024)
        else:
            data = f'get {data_key}\n'
            self.sock.sendall(data.encode())
            data_r = self.sock.recv(1024)

        if data_r.decode() == "error\nwrong command\n\n":
            raise ClientError

        if data_r.decode() == "ok\n\n":
            return {}
        else:
            try:
                dic = {}
                data_r = data_r.decode().split('\n')
                for line in data_r:
                    if line and (line not in 'ok'):
                        metrica, numb_val, timestamp = line.split()
                        if dic.get(metrica):
                            dic[metrica].append((int(timestamp),
                                                 float(numb_val)))
                        else:
                            dic[metrica] = [(int(timestamp), float(numb_val))]
                for value in dic.values():
                    value.sort(key=lambda x: (x[0], x[1]))
                return dic
            except:
                raise ClientError

    def put(self, name_metric, value, timestamp=None):
        """ Sending a data to server for saving """

        timestamp = int(time.time() if timestamp == None else int(timestamp))
        data = f'put {str(name_metric)} {value} {timestamp}\n'
        self.sock.sendall(data.encode())
        answer = self.sock.recv(1024)
        if answer.decode() == "error\nwrong command\n\n":
            raise ClientError

# client = Client("127.0.0.1", 8888, timeout=15)
# print(client.get('*'))
# client.put("palm.cpu", 0.5, timestamp=1150864247)
