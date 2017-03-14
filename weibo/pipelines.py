# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from weibo.models import Base, User


class WeiboPipeline(object):
    def __init__(self):
        engine = create_engine('sqlite:///test.db')
        Base.metadata.create_all(engine)
        SessionCls = sessionmaker(bind=engine)
        self.session = SessionCls()

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
        print(user)
        self.session.add(user)
        self.session.commit()
        return item
