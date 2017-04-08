from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from weibo.models import Base

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/weibo?charset=utf8mb4')
Base.metadata.create_all(engine)
SessionCls = sessionmaker(bind=engine)
session = SessionCls()