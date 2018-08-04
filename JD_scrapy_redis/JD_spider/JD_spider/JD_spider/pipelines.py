# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from pymongo import MongoClient
# class JdSpiderPipeline(object):
#     def open_spider(self,spider):
#         client = MongoClient('127.0.0.1',27017)
#         self.jd_collection = client.JD.jd
#         self.jd_collection.drop()
#     def process_item(self, item, spider):
#         if item['count'] == 20:
#             dict1 = {}
#             dict1.update(item.__dict__['_values'])
#             self.jd_collection.insert(dict1)
#         return item
# from scrapy_redis.pipelines import RedisPipeline,deferToThread
# import json
# class JDRedisPipeline(RedisPipeline):
#     def _process_item(self, item, spider):
#         key = self.item_key(item, spider)
#         data = self.serialize(item)
#         self.server.rpush(key, data)
#         # self.duplicate(key)
#         return item
    # def duplicate(self,key):
        # list1 = self.get_list(key)
        # print('1',len(list1))
        # print(len(self.server.lrange(key, 0, -1)))
    #     for index,_ in enumerate(list1):
    #         redis_rate1 = json.loads(_.decode())
    #         for i in list1[index+1:-1]:
    #             redis_rate2 = json.loads(i.decode())
    #             if redis_rate1['item_id'] == redis_rate2['item_id']:
    #                 for i in redis_rate2:
    #                     redis_rate1['rate'].append(i)
    #                 self.server.lrem(key, 0, i)
    #         data = self.serialize(redis_rate1)
    #         print('3',len(self.server.lrange(key, 0, -1)))
    #         self.server.lrem(key, 0, _)
    #         print('4',len(self.server.lrange(key, 0, -1)))
    #         self.server.lpush(key, data)
    #         print('5',len(self.server.lrange(key, 0, -1)))
    #     print('2',len(list1))
    #     # print(len(self.server.lrange(key, 0, -1)))
    # def get_list(self,key):
    #     return self.server.lrange(key, 0, -1)

