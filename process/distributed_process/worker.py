import time, sys, queue
from multiprocessing.managers import BaseManager

# 场景类似的QueueManager
class QueueManager(BaseManager):
  pass

# 由于这个QueueManager只从网络上获取Queue,所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器
server_addr = '127.0.0.1'
print('Connect to server %s' % server_addr)

m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
  try:
    n = task.get(timeout=1)
    print('run task %d * %d...' % (n, n))
    r = '%d * %d = %d' % (n, n, n*n)
    time.sleep(1)
    result.put(r)
  except queue.Empty:
    print('task queue is empty')
print('worker exit')