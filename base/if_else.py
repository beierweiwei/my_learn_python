# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
age = 20
if age > 18:
  print('your age is', age)
  print('adult')


age = 3
if age >= 18:
  print('your age is', age)
  print('adult')
elif age >= 6:
  print('teenager')
else:
  print('kid')

x = 0
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if x:
  print('True')

# 不同的数据类型需要转换成相同数据类型才能进行比较
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')