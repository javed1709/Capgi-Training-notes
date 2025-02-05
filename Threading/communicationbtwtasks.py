import threading
import time
import queue
def producer(q):
    for i in range(1,6):
        time.sleep(1)
        q.put(i)
        print(f"Produces :{i}")
    q.put(None)

def consumer(q):
    while True:
        item=q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(2)

q=queue.Queue()

producer_thread=threading.Thread(target=producer,args=(q,))
consumer_thread=threading.Thread(target=consumer,args=(q,))
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()