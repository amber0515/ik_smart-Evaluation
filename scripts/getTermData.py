#coding=utf-8
import requests
import io

def hello():

    content = '{ "content" : ['
    for i in range(1,195):
        url = "http://192.168.31.96:9200/test-iksmart-article/_doc/"+ str(i) +"/_termvectors?fields=content"
        req = requests.get(url)
        # print(req.content.decode("utf-8"))
        content += req.content.decode("utf-8")
        content += ','
        content += '\n'

    goldOffset = io.open('C:\\Users\\53238\\Desktop\\response.txt', 'w', encoding='utf-8')
    strr  = str(content)
    strr += ']}'
    goldOffset.write(strr)

    # res_data = urllib.urlopen(req)
    # res = res_data.read()
    # print(res)

hello()