import threading 
from threading import Lock
x = 0
lock = Lock()
def increment():
    global x
    # lock.acquire()
    x = x + 1
    # lock.release()

def operation():
    for _ in range(1000000):
        increment()

t1 = threading.Thread(target=operation)
t2 = threading.Thread(target=operation)
t1.start()
t2.start()
t1.join()
t2.join()
print('The value of x: '+str(x))