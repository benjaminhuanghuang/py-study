'''
https://www.youtube.com/watch?v=XiVVYfgDolU&t=1358s

'''
import socket


def main():
    host = "127.0.0.1"
    port = 9527

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print "UDP Server is started"

    while True:
        data, addr = s.recvfrom(1024)
        print "Message from:" + str(addr)
        print "From connected user: ", str(data)
        data = str(data).upper()
        print "Sending:", data
        s.sendto(data, addr)
    s.close()


if __name__ == "__main__":
    main()
