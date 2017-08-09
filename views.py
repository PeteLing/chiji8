import leancloud
from django.shortcuts import render, redirect

from settings import LEAN_CLOUD_ID, LEAN_CLOUD_SECRET
from fetch import Fetcher
# Create your views here.


def get_index(request):
    leancloud.init(LEAN_CLOUD_ID, LEAN_CLOUD_SECRET)
    query = leancloud.Query('JDqs')

    jdqes = []
    for jdqs in query.add_descending('num').find():
        jdqes.append(jdqs.attributes)

    return render(request, "index.html", {
        'jdqes': jdqes,
    })


def fetch(request):
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
    return redirect("/")
