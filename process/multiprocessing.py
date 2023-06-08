import os

print('process (%s) starting...' % os.getpid())
# windows下没有fork
# pid = os.fork()
# if (pid == 0):
#  print('i m a child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#   print('i (%s) just orated a child process (%s)l' % (os.getpid(), pid))

