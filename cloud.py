# -*- coding: utf-8 -*-
__author__ = 'lateink'

# coding: utf-8
import leancloud
from django.core.wsgi import get_wsgi_application
from leancloud import Engine, LeanEngineError

from fetch import Fetcher
from settings import LEAN_CLOUD_ID, LEAN_CLOUD_SECRET

engine = Engine(get_wsgi_application())


@engine.define
def fetch(**params):
    leancloud.init(LEAN_CLOUD_ID, LEAN_CLOUD_SECRET)
    query = leancloud.Query('JDqs')
    query.limit(1000)
    query.skip(0)
    resultList = query.find()
    # 清除旧数据
    leancloud.Object.destroy_all(resultList)
    # 重新获取数据
    fetcher = Fetcher()
    fetcher.fetch_douyu()
    fetcher.fetch_panda()
    fetcher.fetch_quanmin()
    fetcher.fetch_longzhu()
    fetcher.fetch_huya()

    for jdqs in fetcher.djqes:
        try:
            jdqs.save()
        except Exception as e:
            print("FUck")


@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')
