"""
Title: tcp_server.py
Author: Dominik Limbach
Date: 08.06.2019
Description:
    - script is handling the server functionality
    - will listen to a certain port
    - upon receiving a certain command from the matlab client
      it will notify the main program that there is a new data file that can be processed
"""
import socket


def wait_for_new_data():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8632

    BUFFER_SIZE = 20

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)


    # loop = True
    while True:
        print('listening...')
        conn, addr = s.accept()
        print('Connection address:', addr)

        data = conn.recv(BUFFER_SIZE)

        if not data:
            response = 'ee'
            print('No data received.')
            conn.send(response.encode('utf-8'))  # echo
        else:
            cmd = data.decode('utf-8')
            print('Data received: ' + cmd)

            if cmd == 'start':
                response = 'ok'
                conn.send(response.encode('utf-8'))  # echo
                # loop = False
                break
            else:
                response = 'ew'
                conn.send(response.encode('utf-8'))  # echo
                # loop = True
                continue

        conn.close()

    del s

    return cmd
