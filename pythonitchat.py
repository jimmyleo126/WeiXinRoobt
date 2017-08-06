#coding=utf8
import itchat, time
import requests
import random
import os
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

@itchat.msg_register([TEXT])
def tuling_reply(msg):
    defaultReply = ''
    if msg['Type'] == 'Picture':
        reply = u'发毛线图片，说人话!(表情已收藏)'
    else:
        defaultReply = 'I received: ' + msg['Text']
        reply = get_response(msg['Text'])
    itchat.send_msg( reply or defaultReply, msg['FromUserName'])
    #return reply or defaultReply

@itchat.msg_register([TEXT], isGroupChat=True)
def group_reply_text(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    print(msg['Text'])
    print(reply)
    print(msg['FromUserName'])
    #if msg['IsAt']:
    itchat.send(reply or defaultReply, msg['FromUserName'])

@itchat.msg_register([PICTURE], isGroupChat=True)
def group_reply_img(msg):
    if 3 == random.randint(1, 4):
        msg.download(msg.fileName)
        itchat.send(u'你妹的，看我模仿!', msg['FromUserName'])
        time.sleep(1)
        itchat.send_image(msg.fileName, msg['FromUserName'])
    else:
        itchat.send(u'发毛线图片，说人话!(表情已收藏)', msg['FromUserName'])

@itchat.msg_register([PICTURE])
def tuling_reply_img(msg):
    if 3 == random.randint(1, 4):
        msg.download(msg.fileName)
        itchat.send(u'你妹的，看我模仿!', msg['FromUserName'])
        time.sleep(1)
        itchat.send_image(msg.fileName, msg['FromUserName'])
        # file = msg.fileName
        # if os.path.exists(file):
        #     os.remove(file)
        # else:
        #     print 'no such file:%s' % file
    else:
        itchat.send(u'发毛线图片，说人话!(表情已收藏)', msg['FromUserName'])

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT])
# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)
# @itchat.msg_register([PICTURE,TEXT], isGroupChat=True)
# def group_reply_text(msg):
#     chatroom_id = msg['FromUserName']
#     username = msg['ActualNickName']
#     if not chatroom_id in chatroom_ids:
#         return
#     if msg['Type'] == TEXT:
#         content = msg['Content']
#     elif msg['Type'] == SHARING:
#         content = msg['Text']
#
#     if msg['Type'] == TEXT:
#         for item in chatrooms:


itchat.auto_login(hotReload=True)
itchat.run(debug=True)
#itchat.send_msg('kjkjkjkj',u'@281c279c4c977720dde758c4a1eff4356c2634f60383786a98bc73ae22102b24')
#itchat.send_msg('kjkjkjkj','filehelper')
#users = itchat.search_friends(name=u'Single Dogs')

# print(users[0]['UserName'])
# # itchat.send_msg('11','filehelper')
# for i in range(3):
#     itchat.send(u'卧槽,wocao', users[0]['UserName'])
#     time.sleep(1)

