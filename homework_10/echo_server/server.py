# -*- coding: utf-8 -*-


import datetime
import socket
from http import HTTPStatus
from random import randint


class ServerInfo:
    LOCALHOST: str = '127.0.0.1'
    PORT_: int = randint(20000, 30000)


with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_:
    host_and_port = (ServerInfo.LOCALHOST, ServerInfo.PORT_)
    server_.bind(host_and_port)
    server_.listen(1)

    print(f'http://{host_and_port[0]}:{host_and_port[1]}/')

    while True:

        conn, addr = server_.accept()

        with conn:
            while True:
                try:
                    bytes_info = conn.recv(1024)
                    decode_data = bytes_info.decode('utf-8', errors='ignore')
                    print(f'Get data:\n"{decode_data}"\nfrom: {addr}')

                    request_data = decode_data.split('\r\n')
                    request_status_line = request_data[0]
                    request_method = request_data[0].split(' ')[0]
                    request_headers = request_data[1:-2]
                    try:
                        status = int(request_status_line.split('status=')[1].split(' HTTP')[0])
                        status = HTTPStatus(status)
                    except Exception as e:
                        print(e)
                        status = HTTPStatus(200)

                    body = (
                        f'<h1>Echo server</h1>'
                        f'<h3>Request time: {datetime.datetime.now()}</h3>'
                        f'<h3>Request info:</h3>'
                        f'<div>Request Method: {request_method}</div>'
                        f'<div>Request Source: {host_and_port}</div>'
                        f'<div>Response Status: {status.value} {status.name}</div>'
                    )

                    for header in request_headers:
                        body += f'<div>{header}</div>'

                    response_line = f'HTTP/1.1 {status.value} {status.name}'
                    headers = '\r\n'.join([
                        response_line,
                        f'Content-Length: {len(body)}',
                        'Content-Type: text/html',
                        *request_headers,
                    ])
                    response = '\r\n\r\n'.join([
                        headers,
                        body,
                    ])

                    conn.send(response.encode('utf-8'))

                except Exception as e:
                    print(e)
                    conn.close()
