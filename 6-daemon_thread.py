import threading
def normal_operation():
    for _ in range(100):
        print('Normal thread is running...')

def daemon_operation():
    while True:
        print('Daemon thread is running...')

t1 = threading.Thread(target=normal_operation, name="Thread #1")
t2 = threading.Thread(target=daemon_operation, name="Thread #2", daemon=True)
t1.start()
t2.start()