# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html


class ProxyMiddleWare(object):

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://111.23.10.123:8080'
