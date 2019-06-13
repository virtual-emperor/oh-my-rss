# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from rssfeeds.utils import *
from scrapy.exceptions import DropItem
from rssapi.models import *


class ValidPipeline(object):
    """
    合法性判断
    """
    def process_item(self, item, spider):

        if item['title'] and item['content'] and item['url'] and item['name']:
            return item
        else:
            raise DropItem("数据校验失败：%s" % item)


class TodbPipeline(object):
    """
    插入数据库
    """
    def process_item(self, item, spider):
        site_obj = Site.objects.get(name=item['name'])

        if site_obj.status == 'active':
            article_obj = Article(site=site_obj, title=item['title'], uindex=current_ts(), content=item['content'],
                                  remark='', readtime=cal_readtime(item['content']), src_url=item['url'])
            article_obj.save()

            # 更新标记
            set_crawled_url(item['url'])
        else:
            # TODO 站点被下线处理
            pass
