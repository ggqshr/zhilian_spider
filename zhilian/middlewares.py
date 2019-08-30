# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import time
from .utils.agents import AGENTS
from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
from scrapy import log

class RandomUserAgentMiddleware():
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers.setdefault('User-Agent', agent)


class CustomRetryMiddleware(RetryMiddleware):

    def process_response(self, request, response, spider):
        if response.status == 503:
            log.msg("Server down: %s, waiting for 30min" % response.url, level=log.INFO)
            reason = '503'
            time.sleep(1800)
            return self._retry(request, reason, spider) or response

        return response

