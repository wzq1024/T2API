import requests
import json
import  ssl
#忽略warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#verify=False忽略ssl验证

class BaseRequest:
    #post请求
    def send_post(self,url,data):
        res = requests.post(url=url,data=data,verify=False).text
        return res
    #get请求
    def send_get(self,url,data):
        res = requests.get(url=url,params=data,verify=False).text
        return res
    #执行方法，传参
    def run_main(self,method,url,data):
        if method == 'get':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        try:
            res =json.loads(res)#转换重新赋值
        except:
            print("text")
        return res

if __name__ == '__main__':
    url = "https://www.baidu.com"
    data = {'page': 1}
    #实例化类
    request = BaseRequest()
    res = request.run_main("get",url,data)
    print(res)