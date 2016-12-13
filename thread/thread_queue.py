import threading
import time
from Queue import Queue  # The Queue module has been renamed to queue in Python 3


def job(l):
    for i in xrange(len(l)):
        l[i] = l[i] ** 2
    return l


def multiThread(data):
    q = Queue()
    thread =[]
    data = [[1,2,3],[3,4,5],[4,4,4],[1,2,3]]
    for i in range(4):
        t = threading.Thread(target=job, args=data[i])
        t.start()


def main():
    pass


if __name__ == '__main__':
    main()
