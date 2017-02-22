'''
https://www.youtube.com/watch?v=XiVVYfgDolU&t=1358s

'''
import socket


def main():
    host = "127.0.0.1"
    port = 9527

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print "Connection from ", str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "From connected user: ", str(data)
        data = str(data).upper()
        print "Sending:", data
        c.send(data)
    c.close()


if __name__ == "__main__":
    main()
