
'''

下载必应首页图片,只下载当天的，一张。
'''

import requests
import re
import time
local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text
reg = r"(az/hprichbg/rb/.*?.jpg)"
a = re.findall(reg, content, re.S)[0]
print(a)
picUrl = url + a
read = requests.get(picUrl)
f = open('%s.jpg' % local, 'wb')
f.write(read.content)
f.close()