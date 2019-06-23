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

    while True:
        print('--------------------------------------------------')
        print('Start listening...')
        print()

        conn, addr = s.accept()
        print('Connection established: ')
        print('Connection address: ', addr)
        print()

        data = conn.recv(BUFFER_SIZE)

        if not data:
            response = 'ee'
            print('--------------------------------------------------')
            print('No command received.')
            print()
            conn.send(response.encode('utf-8'))  # echo
            server_status = 'read empty'
        else:
            cmd = data.decode('utf-8')
            print('Command received: ' + cmd)

            if cmd == 'start':
                response = 'ok'
                conn.send(response.encode('utf-8'))  # echo
                server_status = 'read data'
                print('--------------------------------------------------')
                print('Valid command received. Start processing...')
                print()
                break
            elif cmd == 'stop':
                response = 'stopped listening.'
                conn.send(response.encode('utf-8'))  # echo
                server_status = 'read stop'
                print('--------------------------------------------------')
                print('Stop command received. Program will be terminated.')
                print('--------------------------------------------------')
                print()
                break
            else:
                response = 'ew'
                conn.send(response.encode('utf-8'))  # echo
                server_status = 'read misc'
                print('--------------------------------------------------')
                print('Invalid command received.')
                print()

        conn.close()

    del s

    return server_status
