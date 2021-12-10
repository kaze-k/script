import urllib.request
import urllib.parse
import time
import json
import os


# 清屏的函数
def clean():
    # 判断系统类别
    # windows
    if os.name == 'nt':
        os.system('cls')
    # linux
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("未知系统")


# 伪装成浏览器访问网易在线翻译的函数
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


# 输入和输出的函数
def result():
    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    while True:
        print('{:=^50}'.format("(按q!退出/按c!清屏)"),end='  ')
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        a = input("翻译内容：")
        if a == 'q!':
            exit()
        elif a == 'c!':
            clean()
        elif a == '':
            print('',end='\n')
            result()
        else:
            translate(url,a)


# 主程序入口
if __name__ == '__main__':
    result()
