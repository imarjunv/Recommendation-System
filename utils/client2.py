import socket


def Server2():
    host = '192.168.43.141'
    port = 5002

    s = socket.socket()
    s.connect((host, port))

    message = 'trigger'

    s.send(message.encode())
    data = s.recv(1024).decode('utf-8')
    print('Received from Server ' + str(data))
    s.close()
    return data


if __name__ == '__main__':
    data = Server2()