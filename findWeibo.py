from bs4 import BeautifulSoup
import requests,json
import os


url = 'http://m.weibo.cn/container/getIndex?type=uid&value=1191262305&containerid=1076031191262305&page=1'
wb_data = requests.get(url)
aa = str(wb_data.content, encoding = "utf-8")
bb = json.loads(aa)
theWeiBos = bb['cards']

NewWeiBo = theWeiBos[0]
NewWeiBo_itemid = NewWeiBo['itemid']
NewWeiBo_scheme = NewWeiBo['scheme']
NewWeiBo_mblog = NewWeiBo['mblog']
old = '0.1'


def diff(new):
    global old
    if new == old:
        # 不继续下面操作
        print('meiyou old:{}'.format(old))
    else:
        # 继续下面操作，评价，并给自己发送邮件
        old = new
        print('gengxin old:{}'.format(old))


NewWeiBo_mblog_text = NewWeiBo_mblog['text']
NewWeiBo_mblog_user = NewWeiBo_mblog['user']
NewWeiBo_mblog_comments = NewWeiBo_mblog['comments_count']
# NewWeiBo_mblog_pics = NewWeiBo_mblog['pics']
NewWeiBo_mblog_retweeted = NewWeiBo_mblog['retweeted_status']

screen_name = NewWeiBo_mblog_user['screen_name']
profile_image_url = NewWeiBo_mblog_user['profile_image_url']

retweeted_text = NewWeiBo_mblog_retweeted['text']
retweeted_pics = NewWeiBo_mblog_retweeted['pics']
retweeted_pics_list = [x['large']['url'] for x in retweeted_pics]
retweeted_user = NewWeiBo_mblog_retweeted['user']
retweeted_user_name = retweeted_user['screen_name']

