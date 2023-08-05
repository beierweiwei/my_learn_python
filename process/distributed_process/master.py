# 分布式进程
import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
# 发送任务队列
task_queue = queue.Queue()
# 接收队列
result_queue = queue.Queue()

def ret_task_queue():
  global task_queue
  return task_queue
def ret_result_queue():
  global result_queue
  return result_queue
# 从baseManage继承的QueueMange
class QueueMange(BaseManager):
  pass
def test():
  # 把两个queue都注册到网络上，callable参数关联了Queue对象
  QueueMange.register('get_task_queue',   callable=ret_task_queue)
  QueueMange.register('get_result_queue',   callable=ret_result_queue)

  # 绑定端口5000，验证码 ‘abc’
  manager = QueueMange(address=('127.0.0.1', 5000),   authkey=b'abc')

  # 启动queue
  manager.start()
  # 获取通过网络访问的Queue对象
  task = manager.get_task_queue()
  result = manager.get_result_queue()
  for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
  print('Try get results...')
  for i in range(11):
    try:
      r = result.get(timeout=10)
      print('Result:%s' % r)
    except queue.Empty:
      print('result queue is empty.')
  # 关闭
  manager.shutdown()
  print('master exit')

if __name__ == '__main__':
  freeze_support()
  print("Start!")
  test()