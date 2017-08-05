# -*- coding:utf-8 -*-
import urllib
import urllib2
import httplib2
import bs4


TIMEOUT = 30

DEFAULT_HEADERS = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Cache-Control' : 'max-age=0',
    'Connection' : 'keep-alive',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}



def update_cookie(response):
    global DEFAULT_HEADERS

def http_get(url):
    conn = httplib2.Http(timeout=TIMEOUT)
    response, content = conn.request(url, headers=DEFAULT_HEADERS)
    print 's'



class ZhiHu(object):
    def __init__(self):
        self._xsrf = ''


    def get_xsrf(self):
        http_get('https://www.zhihu.com')


if __name__ == '__main__':
    ZhiHu().get_xsrf()


