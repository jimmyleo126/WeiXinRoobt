#coding=utf8
import itchat, time
import requests
from itchat.content import *

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key' : KEY,
        'info' : msg,
        'userid' : 'wechat-robot'
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register([PICTURE,TEXT])
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    itchat.send_msg('kjkjkjkj','@281c279c4c977720dde758c4a1eff4356c2634f60383786a98bc73ae22102b24')
    #return reply or defaultReply


itchat.auto_login(hotReload=True)
#itchat.send_msg('kjkjkjkj',u'@281c279c4c977720dde758c4a1eff4356c2634f60383786a98bc73ae22102b24')
#itchat.send_msg('kjkjkjkj','filehelper')
users = itchat.search_friends(name=u'刘靖')
print(users[0]['UserName'])
itchat.send_msg('11',u'@281c279c4c977720dde758c4a1eff4356c2634f60383786a98bc73ae22102b24')
