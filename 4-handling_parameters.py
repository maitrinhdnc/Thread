import threading 

def operation(x):
    for i in range(x):
        print(threading.current_thread().name + ' - ' + str(i))

# Print MainThread 
t = threading.Thread(target=operation(10), name="Thread #1")
t.start()
# Print thread
t = threading.Thread(target=operation, name="Thread #1", args=(10,))
t.start()