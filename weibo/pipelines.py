# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from weibo import session
from weibo.models import User

class WeiboPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        user = User(
            item.get('uid') or '',
            item.get('name') or '',
            item.get('gender') or '',
            item.get('location') or '',
            item.get('intro') or '',
            item.get('signin') or '',
            item.get('school') or '',
            item.get('company') or ''
        )
        logging.info(user)
        if session.query(User).filter_by(uid=user.uid).first() is None:
            session.add(user)
            try:
                session.commit()
            except:
                session.rollback()
            return item
        else:
            logging.info('已存在User')
