import threading
import time


class acquire(object):
    def __init__(self, *locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, ty, val, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False


def philosopher(left, right):
    while True:
        with acquire(left,right):      
            time.sleep(0.5)  
            print(f'Philosopher at {threading.currentThread()} is eating.')


N_FORKS = 5
forks = [threading.Lock() for n in range(N_FORKS)]


phils = [threading.Thread(
    target=philosopher,
    args=(forks[n], forks[(n + 1) % N_FORKS])
) for n in range(N_FORKS)]


for p in phils:
    p.start()