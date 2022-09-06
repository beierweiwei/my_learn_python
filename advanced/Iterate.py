
# 在Python中，迭代是通过for ... in来完成的
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABC':
  print(ch)

# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断
from collections.abc import Iterable
print(isinstance('abc', Iterable))

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
  print(i, value)

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
  print(x, y)