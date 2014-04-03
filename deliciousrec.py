# coding:utf-8
__author__ = 'shn'

from pydelicious import get_popular,get_userposts,get_urlposts
import time

def initializeUserDict(tag, count=5):
    user_dict={}

    # popularな投稿をcount件目まで取得
    for p1 in get_popular(tag=tag)[0:count]:

        # このリンクを投稿したすべてのユーザを取得
        for p2 in get_urlposts(p1['url']):
            user=p2['user']
            user_dict[user]={}

        return user_dict

def fillItems(user_dict):
    all_items={}

    # 全てのユーザによって投稿されたリンクを取得
    for user in user_dict:
        try:
            posts = get_userposts(user)
            break
        except:
            print "Failed user " + user + ", retrying"
            time.sleep(4)

    for post in posts:
        url = post['url']
        user_dict[user][url] = 1.0
        all_items[url] = 1

    # 空のアイテムを０で埋める
    for ratings in user_dict.value():
        for item in all_items:
            if item not in ratings:
                ratings[item] = 0.0

delusers = initializeUserDict('programming')
print(delusers)
delusers['tsegaran'] = {}
print(fillItems(delusers))