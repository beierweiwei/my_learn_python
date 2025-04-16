# 第 0008 题： 一个HTML文件，找出里面的正文。
import os;
import re;
def parseHtml(html):
  # tagReg = re.compile(r'<[a-zA-z]+>.*</\1>')
  body = re.findall(r'<body>[\S\s]*</body>', html)[0]
  if not body:
    return ''
  return re.sub(r'</?[a-zA-Z]+[^>]*>', '', body)
def readDir(dir):
  if not os.path.isabs(dir):
    dir = os.path.join(os.path.dirname(__file__), dir)
  result = []
  for root, _dir, files in os.walk(dir):
    for _file in files:
      with open(os.path.join(root, _file)) as file:
        html = file.read()
        result.append(html)
  return result
def getHtml(dir):
  pass;


def getLocalHtmlContent(dir):
  contentList = []
  htmlList = readDir(dir)
  for html in htmlList:
    content = parseHtml(html)
    if content:
      contentList.append(content)
    return contentList
if __name__ == '__main__':
  files = getLocalHtmlContent('test')
  print(files)