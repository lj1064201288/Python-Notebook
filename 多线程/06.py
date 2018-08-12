import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Min thread")

t1 = threading.Thread(target=fun, args=())

t1.start()

time.sleep(1)

print("Main thread end")