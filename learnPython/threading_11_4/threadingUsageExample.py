import threading
import time

def threading_usage_example():
    func_name = "threading_usage_example - "
    print(func_name + "start")
    # Create new threads
    thread1 = MyThread(1, "Thread-1", 4)
    thread2 = MyThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(func_name + "end")


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, sec_to_sleep):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.sec_to_sleep = sec_to_sleep

    def run(self):
        print("Starting " + self.name)
        sec_to_sleep = 3
        print(self.name + " - sleeping for " + str(self.sec_to_sleep) + " seconds")
        time.sleep(sec_to_sleep)
        print ("Exiting " + self.name)
