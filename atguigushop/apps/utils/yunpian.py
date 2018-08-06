import requests
import json

class YunPian(object):
    def __init__(self,apikey):
        self.apikey=apikey
        self.sms_send_url='https://sms.yunpian.com/v2/sms/single_send.json'


    def set_msg(self,mobile,code):

        data={
            'apikey':self.apikey,
            'mobile':mobile,
            'text':"【杨光福】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response=requests.post(self.sms_send_url,data=data)
        text=response.text
        print(text)
        dicjson=json.loads(text)
        print(dicjson)


if __name__=="__main__":
    yp=YunPian('4f70824dde066067241393c80c291ea6')

    yp.set_msg("18601042258","2018")
