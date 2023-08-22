# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
import re;
import os;
commentCount = 0
blankCount = 0
codeCount = 0
def countLines(content):
  # 空行 \s,注释 \s*#\s*.*
  # codes = re.findall(r'^\s*([^#^\s]+')
  for line in content.split('\n'):
    if re.findall(r'^\s+$', line):
      global blankCount
      blankCount = blankCount + 1 ;
    elif re.findall(r'^\s*#', line):
      global commentCount
      commentCount = commentCount + 1;
    else:
      global codeCount
      codeCount = codeCount + 1;
def readFiles (dir, handle):
  if not os.path.isabs(dir):
    dir = os.path.join(os.path.dirname(__file__), dir);
  for root, _dir, files in os.walk(dir):
    for file in files:
      with open(os.path.join(root, file)) as f:
        content = f.read()
        handle(content)

if __name__ == '__main__':
  readFiles('test', countLines)
  print(f'test目录中包含空行{blankCount}行，包含注释{commentCount}行，包含代码{codeCount}行')