from threading import Thread
import os
 
 
class Counter(Thread):
 
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
 
    def run(self):
        for i in range(10):
            print('%s is running and belongs to process with ID  %s' % (self.name, str(os.getpid())))
 
 
t1 = Counter('Thread #1')
t2 = Counter('Thread #2')
t3 = Counter('Thread #3')
t4 = Counter('Thread #4')
t5 = Counter('Thread #5')
 
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

"""
 this is why synchronization is needed because these threads are 
 using the same resources of the same process - such as memory.
"""