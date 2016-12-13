'''
In this demo, "All done" is displayed before "T1 end"
'''

import threading
import time


def thread_fun():
    # print "This is an added thread, number is %s" % threading.current_thread()
    print "T1 start\n"
    for i in xrange(10):
        time.sleep(0.1)
    print "T1 end\n"


def thread_fun2():
    print "T2 start\n"
    print "T2 end\n"



def main():
    added_thread = threading.Thread(target=thread_fun, name="T1")
    thread2 = threading.Thread(target=thread_fun2, name="T2")
    added_thread.start()
    thread2.start()


    # without join(), "All done" is displayed before "T1 end"
    # join() force main thread to wait for T1 finish.  join() means insert T1 into main thread
    # added_thread.join()
    thread2.join()
    print "All done\n"


if __name__ == '__main__':
    main()
