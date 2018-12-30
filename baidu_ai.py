from aip import AipSpeech


# 可在以下代码基础上爬取网页的文字并生成语音文件
def baidu_speech(title, text):
    """ 你的 APPID AK SK """
    APP_ID = '15306829'  # 替换成百度提供的,
    API_KEY = 'KYZd0rKokAop8exDIzg76TP1'
    SECRET_KEY = 'FW4uOn51rxBDjPQMQGE0Fc9vpIZYEuyl'
    mp3_name = title + '.mp3'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # client.setConnectionTimeoutInMillis()   通常不进行配置,
    # client.setSocketTimeoutInMillis()

    result = client.synthesis(text,
                              'zh',
                              1,
                              {
                                  'vol': 5,
                                  'per': 0
                              }
                              )

    # 识别正确返回语音二进制 错误则返回di,ct 参照下面错误码
    if not isinstance(result, dict):
        with open(mp3_name, 'ab') as f:
            f.write(result)

    print(result)
