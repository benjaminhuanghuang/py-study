'''
In CPython, the "global interpreter lock", or GIL, is a mutex that prevents multiple native threads
from executing Python bytecodes at once.

This lock is necessary mainly because CPython's memory management is not thread-safe.
(However, since the GIL exists, other features have grown to
depend on the guarantees that it enforces.)
'''

import threading
import time
from Queue import Queue
import copy


def job(l, q):
    res = sum(l)
    q.put(res)


def multithreading():
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name="T%i" % i)
        t.start()
        threads.append(t)

    [t.join() for t in threads]
    total = 0

    for _ in range(4):
        total += q.get()
    print total


def normal(l):
    total = sum(l)
    print total


if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l * 4)
    print "normal", time.time() - s_t
    s_t = time.time()
    multithreading()
    print "multithreading", time.time() - s_t
