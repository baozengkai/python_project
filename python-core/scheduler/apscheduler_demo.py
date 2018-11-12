# - * - coding:utf-8 - * -
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

"""
    定时触发库
        APScheduler是基于Quartz的Python定时任务库。
        实现了基于日期、时间间隔以及crontab类型的定时任务。
    实例:
        1.使用blocking实现，每2秒输出一次内容，会阻塞主线程
        2.使用background实现，不阻塞主线程
"""

# # 1.使用blocking实现，每2秒输出一次内容
# # def block_job():
# #     print 'I am blockingScheduler'
# #
# # scheduler = BlockingScheduler()
# # scheduler.add_job(block_job, 'interval', seconds=2)
# # scheduler.start()
#
# # 2.使用backgroundScheduler实现，每2秒输出一次内容
# def background_job():
#     print 'I am blockingScheduler'
#
# scheduler = BackgroundScheduler()
# scheduler.add_job(background_job, 'interval', seconds=2)
# scheduler.start()


# 2.使用background实现，不阻塞主线程
def backgroud_job():
    print('I am background_job')

if __name__=='__main__':

    sched = BackgroundScheduler()
    sched.add_job(backgroud_job, 'interval', seconds=3)
    sched.start()

    while(True):
        print('main 1s')
        time.sleep(1)
