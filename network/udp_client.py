'''
https://www.youtube.com/watch?v=XiVVYfgDolU&t=1358s

'''
import socket


def main():
    host = "127.0.0.1"
    port = 9999

    server = ('127.0.0.1', 9527)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = raw_input("-> ")

    while message != "q":
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)
        print "Message from server:" + str(data)
        message = raw_input("-> ")

    s.close()


if __name__ == "__main__":
    main()
