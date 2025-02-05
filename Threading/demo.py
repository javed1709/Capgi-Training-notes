#single threading (single task)
import threading
import time
def single_taks():
    print("Task Stared")
    time.sleep(2)
    print("Task completed")

thread=threading.Thread(target=single_taks)

thread.start()
thread.join() #waits for the thread till it completes the task
print("Main thread execution completed")
