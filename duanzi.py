import re
import requests  # 如果没这模块运行CMD pip  install requests

response = requests.get('http://baijiahao.baidu.com/s?id=1598724756013298998&wfr=spider&for=pc')  # 这个编辑器的长度关系没法放一行
data = response.text
# 按F12选择自己想要的内容所在的位置copy出来
new_list = re.findall('<span class="bjh-p">(.*?)</span></p><p>', data)  # (.*?)是我们要的内容

for a in new_list:
    with open(r'/mnt/段子.txt', 'a') as fw:
        fw.write(a)
        fw.flush()
