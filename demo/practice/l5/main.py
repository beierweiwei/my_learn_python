# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
import os
from PIL import Image
iphone5_resolution = (640, 1136)
def transformDirImgs (dir):
  saveDir = os.path.join(dir, 'transform')
  os.mkdir(saveDir)
  items = os.listdir(dir)
  for file in items:
    clipImg(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imgs', file), saveDir)

def clipImg (fileName, saveDir):
  baseName = os.path.basename(fileName)
  name, suffix = os.path.splitext(baseName)
  originImg = Image.open(fileName)
  width, height = originImg.size
  clipWidth = min(iphone5_resolution[0], width)
  clipHeight = min(iphone5_resolution[1], height)
  left = (clipWidth - width) // 2
  top = (clipHeight - height) // 2
  right = left + clipWidth
  bottom = top + clipHeight
  clipedImg = originImg.crop((left, top, right, bottom))
  resizedImg = clipedImg.resize(iphone5_resolution)
  resizedImg.save(os.path.join(saveDir, name + '@iphone5' + suffix))

  
if __name__ == '__main__':
  transformDirImgs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imgs'))