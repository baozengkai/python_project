# -*- coding:utf-8 -*-
import threading
import _thread
import time
"""
    1.线程
      1.1 创建一个线程
      1.2 自定义线程类
      1.3 线程安全之使用Lock
      1.4 线程安全之使用RLock
      1.5 线程安全之使用信用量
      1.6 线程安全之使用条件
      1.7 线程安全之使用事件     
"""


# 1.1 创建一个线程
# def func(i):
#     print("%d threading is running" % i)
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=func, args=(i,))
#     threads.append(t)
#     t.start()
#     # t.join()
# print("Main exited")


# 1.2 自定义线程类
# exit_flag = 0
#
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("Starting " + self.name)
#         print_time(self.name, self.counter, 5)
#         print("Exiting " + self.name)
#
#
# def print_time(thread_name, delay, counter):
#     while counter:
#         # if exit_flag:
#         #     # 线程可以主动退出
#         #     _thread.exit()
#         time.sleep(delay)
#         print("%s: %s" % (thread_name, time.ctime(time.time())))
#         counter = counter - 1
#
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(123)
# print("Exiting Main Thread")


# 1.3 线程安全之Lock锁
# shared_with_lock = 0
# shared_with_no_lock = 0
# lock = threading.Lock()
#
#
# # 有锁的情况下
# def increment_with_lock():
#     global shared_with_lock
#     for i in range(10000):
#         lock.acquire()
#         shared_with_lock += 1
#         lock.release()
#
#
# def decrement_with_lock():
#     global shared_with_lock
#     for i in range(10000):
#         lock.acquire()
#         shared_with_lock -= 1
#         lock.release()
#
#
# # 无锁的情况下
# def increment_without_lock():
#     global shared_with_no_lock
#     for i in range(100000):
#         shared_with_no_lock += 1
#
#
# def decrement_whithout_lock():
#     global shared_with_no_lock
#     for i in range(100000):
#         shared_with_no_lock -= 1
#
#
# t1 = threading.Thread(target=increment_without_lock())
# t2 = threading.Thread(target=decrement_whithout_lock())
#
# t3 = threading.Thread(target=increment_with_lock())
# t4 = threading.Thread(target=decrement_with_lock())
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# print("无锁的情况下，共享变量为: %s" % shared_with_no_lock)
# print("有锁的情况下，共享变量为: %s" % shared_with_lock)
#
#
# # 1.4 线程安全之RLock锁
# rlock = threading.RLock()
#
# # 初始化共享资源
# abce = 0
#
# # 本线程访问共享资源
# rlock.acquire()
# abce = abce + 1
#
# # 这个线程访问共享资源会被阻塞
# rlock.acquire()
# abce = abce + 2
# rlock.release()
# rlock.release()
# print(abce)


# 1.5 线程安全之信号量
# semaphore = threading.Semaphore(2)
#
#
# def worker(id):
#     print("thread {0} acquire semaphore".format(id))
#     semaphore.acquire()
#     print("thread {0} do something".format(id))
#     time.sleep(2)
#     semaphore.release()
#     print("thread {0} release semahore".format(id))
#
#
# for i in range(10):
#     t = threading.Thread(target=worker, args=(i,))
#     t.start()

# 1.6 线程安全之条件
# item = []
# condition = threading.Condition()
#
#
# class consumer(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def consumer(self):
#         global item, condition
#         condition.acquire()
#         if len(item) == 0:
#             condition.wait()
#             print("conumser: 我释放了锁，我正在等待唤醒")
#         item.pop()
#         print("Consumer notify : consumed 1 item")
#         print("Consumer notify : items to consume are " + str(len(item)))
#         condition.notify()
#         condition.release()
#
#     def run(self):
#         for i in range(5):
#             time.sleep(2)
#             self.consumer()
#
#
# class producer(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def producer(self):
#         global item, condition
#         condition.acquire()
#         if len(item) == 4:
#             condition.wait()
#             print("producer: 我释放了锁，我正在等待唤醒")
#         item.append(1)
#         print("producer notify : consumed 1 item")
#         print("producer notify : items to consume are " + str(len(item)))
#         condition.notify()
#         condition.release()
#
#     def run(self):
#         for i in range(5):
#             time.sleep(1)
#             self.producer()
#
#
# t1 = consumer()
# t2 = producer()
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# 1.7 线程安全之使用事件
from threading import Thread, Event
import random
items = [1, 2, 3, 4, 5, 6]
event = Event()

def print_a():
    global items, event

    for i in range(1,3,5):
        event.wait()
        print(i)

def print_b():
    global items, event
    for i in range(2,4,6):
        event.wait()
        print(i)


t1 = threading.Thread(target=print_a)
t2 = threading.Thread(target=print_b)

t1.start()
t2.start()
t1.join()
t2.join()
event.set()