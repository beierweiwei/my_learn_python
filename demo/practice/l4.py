## **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
import os
dirname = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dirname, 'source', 'en.txt')
print(file)
wordCount = 0
with open(file, 'r') as file:
  for line in file:
    for str in line.split(' '):
      if str != '\n':
        wordCount =  wordCount + 1
print('the file %s has %d word' % (file.name, wordCount))

