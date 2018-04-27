import multiprocessing
from threading import Thread
import sys
import time

COUNTDOWN = 5

class Th(Thread):

    def __init__ (self, num):
        sys.stdout.write("Making thread number " + str(num) + "n")
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num
        self.countdown = COUNTDOWN

    def run(self):

        while self.countdown:
            sys.stdout.write("Thread " + str(self.num) + " (" + str(self.countdown) + ")\n")
            sys.stdout.flush()
            self.countdown -= 1


def worker():
    """worker function"""
    print('Worker')
    return


if __name__ == '__main__':
    jobs = []
    t0 = time.time()
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
    t1 = time.time()

    # t2 = time.time()
    for thread_number in range(5):
        thread = Th(thread_number)
        thread.start()

    t2 = time.time()


    print("tempo do Multiprocessamento: " + str(t1-t0))  
                                                            
    print("tempo do Thread: " + str(t2-t1))  
