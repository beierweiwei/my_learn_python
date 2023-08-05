# 第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 优惠券规则 /d{4}-[a-z]{8}-{date}
import random
from datetime import datetime

now = datetime.now()
# create 100 len Arr
arr = [0] * 10
new_arr = []
strs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for x in arr:
  randNums = random.randint(100000, 999999)
  randStrs = list(map(lambda x: strs[random.randint(0, len(strs ) -1)], range(4)))
  dateStr = "{:04d}{:02d}{:02d}".format(now.year, now.month, now.day)
  new_arr.append((str(randNums)+ "".join(randStrs) + dateStr))

print(new_arr)