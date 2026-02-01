import requests
# 访问服务器 地址（URL）
# 数据处理    抓包：在混乱的数据中找到想要的数据

url='https://m804.music.126.net/20260127230301/e8f3dcb7bad4db61aa066a1e3f776747/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/28481679009/b727/c642/c82d/0c1114f676e5182b81bd4403482c574a.m4a?vuutv=aqjqA7fp28kFIujWUkf9PXz1ffHffTUh50gNt8MC8XU9UYgmFg2jsl7iz9c7Fh+cUe4It5LVPGq09gU+WbojlKGCcMljlcICDCUA7XIWyuA=&authSecret=0000019bffe3d9ca0c6c0a6498140006&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g'
requests.get(url)
# 所有的数据->二进制数据
res=requests.get(url).content

# 下载数据
# 创建一个mp3格式文件 音乐数据写进去
with open('于是.mp3', 'wb') as f:
     f.write(res)