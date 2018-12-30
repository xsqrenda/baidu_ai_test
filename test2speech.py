import requests,re,datetime,sys,baidu_ai

from bs4 import BeautifulSoup
# python test2speech.py http://www.chinatax.gov.cn/n810219/n810744/n3752930/n3752974/c3960115/content.html

pt = u"((?<=[\u4e00-\u9fa5])\s+(?=[\u4e00-\u9fa5])|^\s+|\s+$)"
urlpt = u'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
# 判断目标文本类型:1、在线网页（以国家税务总局为例）；2、本地文本
if re.match(urlpt,sys.argv[1]):
    url= sys.argv[1]
    r = requests.get(url)
    r.encoding='utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    title = soup.find(['title']).text.strip()
    baidu_ai.baidu_speech(title,title)
    content = soup.find('li', id='tax_content').find_all('p')
    for p in content:
        temp = re.split('，|。|？', p.text)
        for ptext in temp:
            text = re.sub(pt, ',', ptext)
            print(text+'\n')
            baidu_ai.baidu_speech(title,text)
else:
    # G:/python_test/baidu_ai_test/关于个人所得税自行纳税申报有关问题的公告.txt
    path = sys.argv[1]
    with open(path, "r",encoding='utf8') as f:  # 设置文件对象
        data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
        f.close()
        title = re.findall(r'[^\\/:*?"<>|\r\n]+$', path)[0].split('.')[0]
        print(title)
        baidu_ai.baidu_speech(title, title)
        for p in data:
            temp = p.split('，')
            for ptext in temp:
                text = re.sub(pt, ',', ptext)
                # print(text + '\n')
                baidu_ai.baidu_speech(title, text)




