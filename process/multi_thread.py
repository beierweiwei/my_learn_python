# _thread低级模块, threading对_thread进行了封装，大多数情况只需用到threading

import time, threading

def loop():
  print('thread %s is running' % threading.current_thread().name)
  n = 0 
  while n < 5:
    n = n + 1
    print('thread %s >>> %s' % (threading.current_thread().name, n))
    time.sleep(1)
  print('thread %s end' % threading.current_thread().name)

print('thread %s is running' % threading.current_thread().name)  
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread end %s' % threading.current_thread().name)
  
# 多线程是计算机cup核心在线程之间交替运行，运行部分代码，然后转到其他进程。所以多个进程对同样数据进行修改容易改乱，这个时候需要加线程锁
balance = 0
lock = threading.Lock()

def change_it (n):
  global balance
  balance = balance + n 
  balance = balance - n 

def run_thread(n):
    for i in range(10000):
      # 获取锁
      lock.acquire()
      try:
        change_it(n)
      finally:
        lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)