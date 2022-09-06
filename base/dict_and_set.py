d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])


# setValue
d['wang'] = 1000
print('wang score is', d['wang'])

# getValue
d['wang']
# 如果不存在会报错
# d['Mark']

# 使用get 可以设置默认值，不存在就使用默认值或返回None
print('Mark score is', d.get('Mark'))

print('Mark score default is', d.get('Mark', -1))

# dict key需要是不可变对象


# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
# set是无序的
# set中重复元素会被过滤
# set添加元素
s.add(4)
print(s)
# set remove 元素
s.remove(4)
print(s)

# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。