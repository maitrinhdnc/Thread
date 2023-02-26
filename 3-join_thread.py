import threading 

def counting_operation():
    for i in range(10):
        print(i)

t1 = threading.Thread(target=counting_operation, name='Hello')
t2 = threading.Thread(target=counting_operation, name='Hi')

t1.start()
t2.start()
t1.join()
t2.join()
print("Finish with thread execution...")

# The Mainthread handle everthing
# join(): wait for all threads finish execution 
# We can block MainThread until all threads are finished