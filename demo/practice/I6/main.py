# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# 1.read dir
# 2. travel files
    #2.1 readFiles, count per word by wordCountMap
# compare wordMap
import os;
print(__name__)
def main (dir):
  wordCount = {}
  maxCount = 0
  maxRepeat = ''
  if (not os.path.isabs(dir)):
    dir = os.path.join(os.path.dirname(__file__), dir)
  print('---', dir)
  files = os.listdir(dir)
  for f in files:
    with(open(os.path.join(dir, f), 'r')) as file:
      content = file.read();
      words = content.split(' ')
      for w in words:
        wordCount[w] = wordCount.get(w, 0) + 1
  for k in wordCount:
    if (maxCount < wordCount[k]):
      maxCount = wordCount[k]
      maxRepeat = k
  print(wordCount)
  print('%s目录中所有日记中，最重要的词为%s,共使用%d次'%(dir, maxRepeat, maxCount))

if (__name__ == '__main__'):
  main('test')