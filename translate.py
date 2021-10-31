import urllib.request
import urllib.parse
import time
import json
import os


def translate(url,a):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'
    }
    data = {
        'i':a,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    d = json.loads(html)
    res = print('翻译结果：{}'.format(d['translateResult'][0][0]['tgt']))
    response.close()
    return res

def result():
    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    while True:
        print('{:=^50}'.format("(按q!退出/按c!清屏)"),end='  ')
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        a = input("翻译内容：")
        if a == 'q!':
            exit()
        elif a == 'c!':
            os.system('cls')
        else:
            translate(url,a)

if __name__ == '__main__':
    result()