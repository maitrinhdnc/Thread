from threading import Thread

class Counter(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    # When start Thread, this run() func will be called 
    def run(self):
        for i in range(100):
            print(f"thread is running: {self.name, str(i)}"  )

t1 = Counter('Hello')
t2 = Counter('Hi')

t1.start()
t2.start()