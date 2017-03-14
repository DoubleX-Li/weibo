import json
import logging

from scrapy import Request
from scrapy import Spider

from weibo.items import WeiboItem


class WeiboSpider(Spider):
    name = 'weibo'

    cookie = input('请输入cookie')

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cookie": cookie,
        "Connection": "keep-alive",
        "Host": "m.weibo.cn",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    getSecond = 'http://m.weibo.cn/container/getSecond'
    getIndex = 'http://m.weibo.cn/container/getIndex'

    def __init__(self, uid):
        self.uid = uid

    def start_requests(self):
        logging.debug('start_request')

        yield Request(
            url='{0}?containerid=100505{1}_-_FOLLOWERS'.format(self.getSecond, self.uid),
            headers=self.headers,
            callback=self.parse_followers
        )

    def parse_person(self, response):
        """
        解析个人信息
        :param response:
        :return:
        """
        jsonObj = json.loads(response.text)

        # 获取信息出错
        if jsonObj.get('msg'):
            # 再次调用parse_person
            yield Request(
                url=response.url,
                headers=self.headers,
                callback=self.parse_person
            )
        item = WeiboItem()
        # 从response.url中截取uid
        item['uid'] = response.url.split('_')[0].split('=')[1][6:]

        # 遍历cards
        cards = jsonObj.get('cards') or []
        for something in cards:
            card_group = something.get('card_group') or []

            # 遍历card_group，逐项寻找感兴趣的信息
            for card in card_group:
                item_name = card.get('item_name')
                # logging.debug(item_name)
                if '昵称' == item_name:
                    item['name'] = card.get('item_content')
                elif '性别' == item_name:
                    item['gender'] = card.get('item_content')
                elif '所在地' == item_name:
                    item['location'] = card.get('item_content')
                elif '简介' == item_name:
                    item['intro'] = card.get('item_content')
                elif '注册时间' == item_name:
                    item['signin'] = card.get('item_content')
                elif '学校' == item_name:
                    item['school'] = card.get('item_content')
                elif '公司' == item_name:
                    item['company'] = card.get('item_content')

        yield item

    def parse_followers(self, response):
        """
        解析关注者信息
        :param response:
        :return:
        """
        logging.debug('parse_followers')

        jsonObj = json.loads(response.text)

        # 解析cards中朋友信息
        try:
            cards = jsonObj.get('cards')
            for card in cards:
                uid = card.get('user').get('id')
                logging.info(card.get('user').get('screen_name'))
                yield Request(
                    url='{0}?containerid=230283{1}_-_INFO'.format(self.getIndex, uid),
                    headers=self.headers,
                    callback=self.parse_person
                )
        # 没有粉丝
        except:
            msg = jsonObj['msg']
            print(msg)
            return

        # 解析下一页中的朋友信息
        try:
            next_page = jsonObj['cardlistInfo']['page']
            yield Request(
                url='{0}?containerid=100505{1}_-_FOLLOWERS&page={2}'.format(self.getSecond, self.uid, next_page),
                headers=self.headers,
                callback=self.parse_followers
            )
        except:
            print('没有了')
            return
