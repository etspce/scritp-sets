import time
from threading import Thread
from time import ctime


def fun(name, sec):
    print('-----start-----', name, ctime())
    time.sleep(sec)
    print('-----end-----', name, ctime())


if __name__ == '__main__':
    for i in range(3):
        t1 = Thread(target=fun, args=('线程1', 3))
        t2 = Thread(target=fun, args=('线程2', 3))

        t1.start()
        time.sleep(2)
        t2.start()

        t1.join()
        t2.join()

