# pip install requests or
# python -m  pip install requests
import requests
r = requests.get('https://www.baidu.com/') # 豆瓣首页
r.status_code
print(r.status_code)
print(r.text)