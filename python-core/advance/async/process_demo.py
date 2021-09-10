# -*- coding:utf-8 -*-
import multiprocessing
import time
import random
"""
    1.进程
      1.1 创建一个进程
          join()函数的作用
          守护进程
          杀死进程
      1.2 进程通信
          队列
          管道
      1.3 进程池
          Pool(进程数)类
            apply() 同步创建一个进程,会阻塞其他进程的执行
            apply_async() 异步创建一个进程，不会阻塞进程的执行                    
            get() 获取结果 
"""

# 1.1 创建一个进程
# def foo():
#     name = multiprocessing.current_process().name
#     print("start..." + name)
#     time.sleep(2)
#     print("end..." + name)
#
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=foo)
#     p1.daemon = True
#     p1.start()
#     # p1.join()
#     time.sleep(5)
#     print("Main Exixted")


# 1.2.1 进程通信之队列(生产者和消费者)
# class Producer(multiprocessing.Process):
#     """
#     """
#     def __init__(self, queue):
#         super().__init__()
#         self.queue = queue
#
#     def run(self):
#         for i in range(10):
#             item = random.randint(0, 256)
#             self.queue.put(item)
#             print("Process Producer : item %d appended to queue %s" % (item, self.name))
#             time.sleep(1)
#             print("The size of queue is %s" % self.queue.qsize())
#
#
# class Consumer(multiprocessing.Process):
#     """
#     """
#     def __init__(self, queue):
#         super().__init__()
#         self.queue = queue
#
#     def run(self):
#         while True:
#             if(self.queue.empty()):
#                 print("Process Consumer: the queue is empty")
#                 break
#             else:
#                 time.sleep(2)
#                 item = self.queue.get()
#                 print('Process Consumer : item %d popped from by %s \n' % (item, self.name))
#
#
# if __name__ == '__main__':
#     queue = multiprocessing.Queue()
#     producer = Producer(queue)
#     consumer = Consumer(queue)
#     producer.start()
#     consumer.start()
#     producer.join()
#     consumer.join()
#     print("Main exixted")
#

# class Producer(multiprocessing.Process):
#     """
#     """
#     def __init__(self, pipe_producer):
#         super().__init__()
#         self.pipe_producer = pipe_producer
#
#     def run(self):
#         for i in range(10):
#             item = random.randint(0, 256)
#             self.pipe_producer.send(item)
#             print("Process Producer : item %d send by %s" % (item, self.name))
#             time.sleep(1)
#             # print("The size of queue is %s" % self.queue.qsize())
#
#
# class Consumer(multiprocessing.Process):
#     """
#     """
#     def __init__(self, pipe_consumer):
#         super().__init__()
#         self.pipe_consumer = pipe_consumer
#
#     def run(self):
#         while True:
#             time.sleep(1)
#             item = self.pipe_consumer.recv()
#             print('Process Consumer : item %d popped from by %s \n' % (item, self.name))
#
#
# if __name__ == '__main__':
#     pipe = multiprocessing.Pipe()
#     producer = Producer(pipe[0])
#     consumer = Consumer(pipe[1])
#     producer.start()
#     consumer.start()
#     producer.join()
#     consumer.join()
#     print("Main exixted")

# 1.3 进程池
def worker(name):
    print("msg: hello " + str(name))
    time.sleep(2)
    print("end " + str(name))


if __name__ == "__main__":
    pool = multiprocessing.Pool(3)
    msg = "123"
    for i in range(4):
        pool.apply_async(func=worker, args=(i,))

    print("主进程内部输出......")
    pool.close()
    pool.join()
    print("主进程退出")
