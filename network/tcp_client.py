'''
https://www.youtube.com/watch?v=XiVVYfgDolU&t=1358s

'''
import socket


def main():
    host = "127.0.0.1"
    port = 9527

    s = socket.socket()
    s.connect((host, port))

    message = raw_input("-> ")
    while message:
        s.send(message)
        data = s.recv(1024)
        print "Received from server: ", str(data)
        message = raw_input("-> ")
    s.close()


if __name__ == "__main__":
    main()
