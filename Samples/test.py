import json
import datetime

from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException


client = ZhihuClient()
client.load_token('/home/wz/ZheProject/Zhihu/Samples/token.pkl')
# try:
#     client.login('wangzhetju@gmail.com', 'xiao3224')
# except NeedCaptchaException:
#     # 保存验证码并提示输入，重新登录
#     with open('./a.gif', 'wb') as f:
#         f.write(client.get_captcha())
#     captcha = input('please input captcha:')
#     client.login('wangzhetju@gmail.com', 'xiao3224', captcha)
#     client.save_token('./token.pkl')

res = client.test_api(method="GET", url="https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total")
data = res.json()['data']
now = datetime.datetime.now().isoformat()
with open('/home/wz/ZheProject/Zhihu/Data/Hotlist_%s.json' % now, 'w') as f:
    json.dump(data, f)
