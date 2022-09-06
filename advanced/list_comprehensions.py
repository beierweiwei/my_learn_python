# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
  L.append(x * x)
print(L)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
res = [x * x for x in range(1, 11)]
print(res)
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
res = [x * x for x in range(1, 11) if x % 2 == 0]
print(res)
