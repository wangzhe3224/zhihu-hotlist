import json
import requests


def load(path: str):
    """"""
    with open(path, 'r') as f:
        data = json.load(f)
        return data


def fetch():
    """"""
    sess = requests.Session()
    headers = {
        'cookie': '_zap=9668ac0c-74f9-4af6-be21-cc8d7c9c2cdb; d_c0="APDk7o04vA2PTj_y96Se8FV5FbVz_05am3E=|1528749591"; __gads=ID=c72d1d689ec0e945:T=1541199454:S=ALNI_MavWeGdIDHu6X47EaCrZcSybUn7Cg; __utmv=51854390.100-1|2=registration_date=20140130=1^3=entry_date=20140130=1; _xsrf=0wwKkhC59EnUCRoI3bPd73PH5hJ5PJrC; q_c1=204693cc3aab45168abe23a751d10530|1569016398000|1528749589000; __utma=51854390.502800493.1566734222.1570000041.1570305900.9; __utmz=51854390.1570305900.9.9.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/wangzhetju/collections; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1570905859,1570905873,1570906370,1570906425; tshl=; capsion_ticket="2|1:0|10:1570910735|14:capsion_ticket|44:OGIwZGZkNjZlZDdlNDliNWJjZWU1N2MxOWU1MjhkMWI=|9c0b1b11433c7942365d8e26d2fec7387f79cdc2eddaf3624622664525cab7a2"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1570910737; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b',
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    res = requests.get('https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total')
    print(res)
    return res.json()


if __name__ == '__main__':

    import time

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get("http://www.python.org")

    time.sleep(60)