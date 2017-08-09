# -*- coding: utf-8 -*-
__author__ = 'lateink'
import re
import sys
import urllib3

import requests
import leancloud
from settings import LEAN_CLOUD_ID, LEAN_CLOUD_SECRET

urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)
leancloud.init(LEAN_CLOUD_ID, LEAN_CLOUD_SECRET)


class Fetcher():
    JDqs = leancloud.Object.extend('JDqs')

    def __init__(self):
        self.djqes = []

    def append_model(self, id, href, title, name, img, num):
        jdqs = self.JDqs()
        try:
            jdqs = self.JDqs()
            jdqs.set('type', 'panda')
            jdqs.set('href', href)
            jdqs.set('id', id)
            jdqs.set('title', title)
            jdqs.set('name', name)
            jdqs.set('img', img)
            jdqs.set('num', num)
            jdqs.save()
            self.djqes.append(jdqs)
        except Exception as e:
            print("FUck")

    def change_num(self, num):
        if '万' in num:
            num = int(round(float(num.replace('万', '').replace('\r', '').replace('\n', '')) * 10000))
        else:
            num = int(num)
        return num

    def fetch_panda(self):
        print('fetch pandaTv')
        url = 'https://www.panda.tv/cate/pubg'
        session = requests.Session()
        response = session.get(url, verify=False)
        base_url = 'https://www.panda.tv/'
        for each_content in re.finditer('<a href=".*?" class="video-list-item-wrap"([\s\S]*?)<\/a>',
                                        response.content.decode('utf8')):
            group = each_content.group()
            href = re.search('href=".*?"', group).group().lstrip('href="/').rstrip('"')
            id = 'panda_' + href.lstrip('/')
            href = base_url + href
            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            img = re.search('data-original=".*?"', group).group().lstrip('data-original="').rstrip('"')
            try:
                name = re.search('</i>[\s\S]*?</span>', group).group().lstrip('</i>').rstrip('</span>')
            except:
                name = "FUck"
            name = name.strip()
            num = re.search('<span class="video-number">.*?</span>', group).group().lstrip(
                '<span class="video-number">').rstrip('</span>')
            num = num.replace('人', '')
            num = self.change_num(num)
            # print(title, name, href, ' ', img, num)
            self.append_model(id, href, title, name, img, num)

    def fetch_douyu(self):
        print('fetch douyu')
        url = 'https://www.douyu.com/directory/game/jdqs'
        session = requests.Session()
        response = session.get(url, verify=False)
        base_url = 'https://www.douyu.com/'
        for each_content in re.finditer('<a class="play-list-link" .*?>([\s\S]*?)<\/a>',
                                        response.content.decode("utf8")):
            group = each_content.group()
            href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
            id = 'douyu_' + href.lstrip('/')
            href = base_url + href
            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            img = re.search('data-original=".*?"', group).group().lstrip('data-original="').rstrip('"')
            name = re.search('<span class="dy-name ellipsis fl">.*?</span>', group).group().\
                lstrip('<span class="dy-name ellipsis fl">').rstrip('</span>')
            num = re.search('<span class="dy-num fr.*?</span>', group).group().\
                lstrip('<span class="dy-num" fr>').rstrip('</span>')
            num = self.change_num(num)
            # print(title, name, href, img, num)
            self.append_model(id, href, title, name, img, num)

    def fetch_quanmin(self):
        print('fetch quanmin')
        url = 'http://www.quanmin.tv/json/categories/juediqiusheng/list.json?t=24468018'
        session = requests.Session()
        response = session.get(url, verify=False)
        base_url = 'https://www.quanmin.tv/'
        for each_content in response.json()['data']:
            id = each_content['uid']
            id = 'quanmin_' + str(id)
            title = each_content['title']
            href = base_url + each_content['uid']
            img = each_content['thumb']
            name = each_content['nick']
            num = self.change_num(each_content['follow'])
            # print(title, name, href, img, num)
            self.append_model(id, href, title, name, img, num)

    def fetch_huya(self):
        print('fetch huya')
        url = 'http://www.huya.com/g/2793'
        session = requests.Session()
        response = session.get(url, verify=False)
        for each_content in re.finditer('<li class="game-live-item">([\s\S]*?)<\/li>',
                                        response.content.decode("utf8")):
            group = each_content.group()
            href = 'h' + re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
            id = 'huya_' + href.lstrip('http://www.huya.com/')
            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            img = re.search('data-original=".*?"', group).group().lstrip('data-original="').rstrip('"')
            name = re.search('<i class="nick" title=".*?">', group).group().\
                lstrip('<i class="nick" title="').rstrip('">')
            num = re.search('<i class="js-num.*?</span>', group).group(). \
                lstrip('<i class="js-num">').rstrip('</i></span')
            num = self.change_num(num)
            # print(title, name, href, img, num)
            self.append_model(id, href, title, name, img, num)

    def fetch_longzhu(self):
        print('fetch longzhu')
        url = 'http://longzhu.com/channels/jdqs?from=figame'
        session = requests.Session()
        response = session.get(url, verify=False)
        for each_content in re.finditer('<a href=".*? class="livecard"([\s\S]*?)<\/a>',
                                        response.content.decode("utf8")):
            group = each_content.group()
            href = re.search('href=".*?"', group).group().lstrip('href=').strip('"')
            id = 'longzhu_' + href.replace('/', '').lstrip('http://star.longzhu.com/').rstrip('?from=challcontent')
            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            img = re.search('<img src=".*?"', group).group().lstrip('<img src="').rstrip('"')
            name = re.search('<strong class="livecard-modal-username">.*?</strong>', group).group().\
                lstrip('<strong class="livecard-modal-username">').rstrip('</strong>')
            num = re.search('<span class="livecard-meta-item-text">.*?</span>', group).group().\
                lstrip('<span class="livecard-meta-item-text">').rstrip('</span>')
            num = self.change_num(num)
            # print(title, name, href, img, num)
            self.append_model(id, href, title, name, img, num)

if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.fetch_douyu()
    fetcher.fetch_panda()
    fetcher.fetch_quanmin()
    fetcher.fetch_longzhu()
    fetcher.fetch_huya()
    print(len(fetcher.djqes))
