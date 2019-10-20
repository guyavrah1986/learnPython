import time
from threading import Thread
from abc import ABCMeta, abstractmethod



def threading_usage_example():
    func_name = "threading_usage_example - "
    print(func_name + "start")
    # Create new threads
    thread_list = []
    thread_list.append(MyThread1("Thread-1", 4))
    thread_list.append(MyThread1("Thread-2", 2))

    # Start new Threads and wait for both of them to terminate
    for t in thread_list:
        t.start()

    for t in thread_list:
        ret_val = t.join()
        print(func_name + "thread:" + t.name + " returned:" + str(ret_val))

    print(func_name + "end")


class MyThreadInterface(metaclass=ABCMeta):
    @abstractmethod
    def pre_run_start(self):
        pass

    @abstractmethod
    def post_run_actions(self):
        pass


class MyBaseThread(Thread):
    def __init__(self, thread_name):
        func_name = "MyBaseThread::__init__ - "
        Thread.__init__(self, name=thread_name)
        self.thread_name = thread_name
        self._return = None
        print(func_name + "got thread name:" + self.thread_name)

    def join(self, *args):
        func_name = "MyBaseThread::join - "
        Thread.join(self, *args)
        return self._return


class MyThread1(MyBaseThread, MyThreadInterface):

    def __init__(self, thread_name, sec_to_sleep):
        func_name = "MyThread1::__init__ - "
        MyBaseThread.__init__(self, thread_name)
        self.sec_to_sleep = sec_to_sleep
        print(func_name + "got " + str(sec_to_sleep) + " seconds to sleep")

    def run(self):
        func_name = "MyThread1::run - "
        self.pre_run_start()
        print(func_name + "starting " + self.name)
        print(func_name + self.name + " - sleeping for " + str(self.sec_to_sleep) + " seconds")
        time.sleep(self.sec_to_sleep)
        print(func_name + self.name + " exiting")
        self.post_run_actions()
        self._return = 12 + self.sec_to_sleep

    def pre_run_start(self):
        func_name = "MyThread1::pre_run_start - "
        num_sec_to_add_to_sleep = 1
        print(func_name + "adding " + str(num_sec_to_add_to_sleep))
        self.sec_to_sleep += num_sec_to_add_to_sleep

    def post_run_actions(self):
        func_name = "MyThread1::post_run_actions - "
        print(func_name)


