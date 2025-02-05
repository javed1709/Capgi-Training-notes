import threading
import time

def task1():
    for i in range(1,10,2):
        print(f"Odd number: {i}")
        time.sleep(1)

def task2():
    for i in range(2,10,2):
        print(f"Even number: {i}")
        time.sleep(1)

thread1=threading.Thread(target=task1)
thread2=threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# tasks are performinig one after the other
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()

        
