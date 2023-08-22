# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# 1.read dir
# 2. travel files
    #2.1 readFiles, count per word by wordCountMap
# compare wordMap
from collections import Counter
import os;
import re;
print(__name__)
def main (dir):
  wordCount = {}
  maxCount = 0
  maxRepeat = ''
  if (not os.path.isabs(dir)):
    dir = os.path.join(os.path.dirname(__file__), dir)
  files = os.listdir(dir)
  for root, _dir, files in os.walk(dir):
    for f in files:
      with(open(os.path.join(root, f), 'r')) as file:
        content = file.read();
        words = re.findall(r'\b\w+\b', content.lower())
        word_count = Counter(words)
        print(word_count)
        most_common_word, frequency = word_count.most_common(1)[0] 
  print('%s目录中所有日记中，最重要的词为%s,共使用%d次'%(dir, most_common_word, frequency))

if (__name__ == '__main__'):
  main('test')