import threading    

# The MainThread will run everything sequentially

print(threading.current_thread().name) #return MainThread

def count_operation():
    for i in range(10):
        print(threading.current_thread().name+str(i))

# This is the sequential execution 
# count_operation()
# count_operation()

t1 = threading.Thread(target = count_operation, name='Adam')
t2 = threading.Thread(target = count_operation, name='Joe')

t1.start()
t2.start()
