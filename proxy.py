#!/usr/bin/env python
import socket
import select
import threading

HOST = ''
PORT = 50007
PROXYHOST = 'your proxy addr'
PROXYPORT = 50009


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(0)
    while True:
        conn, addr = s.accept()
        print 'Connected by', addr, '#active', threading.active_count()
        p = threading.Thread(target=tunnel, args=(conn,))
        p.start()

    s.close()


def tunnel(conn):
    provy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    provy.connect((PROXYHOST, PROXYPORT))

    sent = threading.Thread(target=forwarder, args=(conn, provy))
    recv = threading.Thread(target=forwarder, args=(provy, conn))
    sent.start()
    recv.start()

    recv.join()
    sent.join(10)
    
    provy.close()
    conn.close()


def forwarder(r_s, w_s):
    try:
        while True:
            select.select([r_s], [], [])
            data = r_s.recv(1024)
            if not data: break
            select.select([], [w_s], [])
            w_s.sendall(data)
    except Exception, e:
        pass
    r_s.close()
    w_s.close()


if __name__ == '__main__':
    main()
