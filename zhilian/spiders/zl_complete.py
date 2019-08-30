# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy import log
from zhilian.settings import PER, AIM_DATE
from zhilian.items import ZhilianItem, XiaozhaoItem

from ..utils.list1 import CityList
from ..utils.cleaner import content_cleaner, redundancy_cleaner, get_num, salary_formater

import re


class ZlJobsSpider(scrapy.Spider):
    name = 'zl_complete'
    allowed_domains = ['zhaopin.com']
    handle_httpstatus_list = [301, 302]

    def start_requests(self):
        for city in CityList:
            url = 'http://jobs.zhaopin.com/{0}/pd{1}/'.format(city, PER)
            yield scrapy.Request(url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        selector = Selector(response)
        num = selector.xpath('//div[@class="jobs-inforamation"]/span/text()').extract_first()
        if num:
            num = re.search('\d+', num, re.S)
            num = int(num.group(0))
            if num > 6000:
                # 单一搜索条件最多显示6000个职位信息，因此当职位数大于6000时，递归子分类爬取当前城市不同行业下的信息
                yield from self.parse_subcat(selector, '//div[@id="search_dom2"]/a/@href', self.parse_industry)
            else:
                yield from self.loop(response)

        else:
            print('Web page have changed, please manually check %s' % response.url)

    def parse_industry(self, response):
        selector = Selector(response)
        num = selector.xpath('//div[@class="jobs-inforamation"]/span/text()').extract_first()
        if num:
            num = re.search('\d+', num, re.S)
            num = int(num.group(0))
            if num > 6000:
                # 该行业下职位数大于6000时，递归子分类爬取当前城市当前行业下大职能类别的信息
                yield from self.parse_subcat(selector, '//div[@class="content"]/div[4]/div[@class="listcon height48"]/a/@href', self.parse_cat_job_1)
            else:
                yield from self.loop(response)
        else:
            print('Web page have changed, please manually check %s' % response.url)

    def parse_cat_job_1(self, response):
        selector = Selector(response)
        num = selector.xpath('//div[@class="jobs-inforamation"]/span/text()').extract_first()
        if num:
            num = re.search('\d+', num, re.S)
            num = int(num.group(0))
            if num > 6000:
                # 该行业下职位数大于6000时，递归子分类爬取当前城市当前行业下小职能类别的信息
                yield from self.parse_subcat(selector, '//div[@class="sublist"]/a/@href',self.parse_cat_job_2)
            else:
                yield from self.loop(response)
        else:
            print('Web page have changed, please manually check %s' % response.url)

    def parse_cat_job_2(self, response):
        selector = Selector(response)
        num = selector.xpath('//div[@class="jobs-inforamation"]/span/text()').extract_first()
        if num:
            num = re.search('\d+', num, re.S)
            num = int(num.group(0))
            if num > 6000:
                # 该职能下职位数大于6000时，递归子分类爬取不同学历
                yield from self.parse_subcat(selector, '//div[@class="search_xlyq"]/a/@href', self.loop)
            else:
                yield from self.loop(response)

        else:
            print('Web page have changed, please manually check %s' % response.url)

    def parse_subcat(self, selector, xpath, cb):
        cat_li = selector.xpath(xpath).extract()
        if 'dom2' in xpath:
            cat_li = ['http://jobs.zhaopin.com/' + cat for cat in cat_li]
        try:
            for cat_url in cat_li:
                yield scrapy.Request(cat_url, callback=cb, dont_filter=True)
        except:
            log.msg("Failed to get into %s" % cat_url, level=log.WARNING)
            return None

    def loop(self, response):
        selector = Selector(response)
        obj = selector.xpath('//ul[@class="search_list"]/li/div[contains(@class,"details_container")]')
        for each in obj:
            post_time = each.xpath('span[@class="release_time"]/text()').extract_first()
            each_url = each.xpath('span[@class="post"]/a/@href').extract_first()
            if not each_url:
                continue

            if AIM_DATE:
                if post_time in AIM_DATE:
                    yield scrapy.Request(each_url, callback=self.parse_item, priority=2,
                                         meta={'post_time': post_time})
            else:
                yield scrapy.Request(each_url, callback=self.parse_item, priority=2,
                                     meta={'post_time': post_time})

        nextlink = response.xpath('//div[@class="searchlist_page"]/span[@class="search_page_next"]/a/@href').extract_first()
        if nextlink:
            nextlink = 'http://jobs.zhaopin.com' + nextlink
            yield scrapy.Request(nextlink, callback=self.loop, dont_filter=True)

    def parse_item(self, response):
        # 校园招聘遇301重定向
        if response.status == 301:
            newurl = response.headers['Location'].decode('utf8')
            yield scrapy.Request(newurl, callback=self.parse_item, dont_filter=True, priority=3,
                                 meta={'post_time': response.meta['post_time']})


        # 网页解析
        elif response.status == 200:
            try:
                selector = Selector(response)
                link = response.url
                place = 'Null'

                if '//xiaoyuan' in link:
                    # 解析校园招聘详情页
                    job_name = selector.xpath('//div[@class="cJobDetailInforWrap"]/h1/text()').extract_first()
                    if job_name:
                        _id = ''.join(re.findall('com/job/(.*)', link))

                        job_data = selector.xpath('//ul["@class=cJobDetailInforBotWrap clearfix c3"]/li[@class="cJobDetailInforWd2 marb"]/text()').extract()
                        place, job_kind, job_number, post_time, job_nature, education = \
                            job_data[0], job_data[1], job_data[2], job_data[3], job_data[4], job_data[5]
                        place = place.split('-')[0]
                        job_content = selector.xpath('//div[@class="cJob_Detail f14"]/p//text()').extract()
                        company_name = selector.xpath('//li[@id="jobCompany"]/a/text()').extract_first()
                        company_industry = selector.xpath('//ul[@class="cJobDetailInforTopWrap clearfix c3"]/li[4]/@title').extract_first()
                        company_size = selector.xpath('//ul[@class="cJobDetailInforTopWrap clearfix c3"]/li[6]/text()').extract_first()
                        company_nature = selector.xpath('//ul[@class="cJobDetailInforTopWrap clearfix c3"]/li[8]/text()').extract_first()
                        job_place = selector.xpath('//div[@class="clearfix p20"]/p[@class="c9"]/text()').extract_first()
                        company_address = selector.xpath('//div[@class="clearfix p20"]/p[@class="c9"]/text()').extract_first()
                        company_homepage = selector.xpath('//div[@class="clearfix p20"]/p[@class="c9 mt5"]/a/@href').extract_first()
                        item = XiaozhaoItem()
                    else:
                        return

                else:
                    # 解析社会招聘详情页
                    job_name = selector.xpath('//h3[@class="summary-plane__title"]/text()').extract_first()
                    if job_name:
                        _id = ''.join(re.findall('com/(.*?).htm', link))
                        salary = selector.xpath('//span[@class="summary-plane__salary"]/text()').extract_first()
                        place = selector.xpath('//ul[@class="summary-plane__info"]/li[1]/a/text()').extract_first()
                        experience = selector.xpath('//ul[@class="summary-plane__info"]/li[2]/text()').extract_first()
                        education = selector.xpath('//ul[@class="summary-plane__info"]/li[3]/text()').extract_first()
                        job_number = selector.xpath('//ul[@class="summary-plane__info"]/li[4]/text()').extract_first()
                        job_kind = selector.xpath('//span[@class="pos-name"]/a/text()').extract_first()  # miss
                        job_content = selector.xpath('//div[@class="describtion__detail-content"]//text()').extract()
                        job_place = selector.xpath('//span[@class="job-address__content-text"]/text()').extract_first()
                        company_name = selector.xpath('//a[@class="company__title"]/text()').extract_first()
                        advantage = selector.xpath('//div[@class="highlights__content"]//text()').extract()
                        company_industry = selector.xpath('//button[@class="company__industry"]//text()').extract_first()
                        company_nature = selector.xpath('//ul[@class="promulgator-ul cl"]/li[2]/strong/text()').extract_first() # miss
                        company_size = selector.xpath('//button[@class="company__size"]/text()').extract_first()
                        company_homepage = selector.xpath('//a[@class="company__home-page"]/@href').extract_first()
                        company_address = selector.xpath('//ul[@class="promulgator-ul cl"]/li[5]/strong/text()').extract_first() # miss
                        job_content = ''.join(job_content).strip()
                        post_time = response.meta['post_time']
                        post_time = '20' + post_time if post_time else 'NULL'
                        job_nature = "全职"
                        salary = salary_formater(redundancy_cleaner(salary, '元/月'))
                        advantage = '/'.join(advantage)

                        item = ZhilianItem()
                        item["salary"] = salary if salary else "NULL"
                        item["experience"] = experience if experience else "NULL"
                        item["advantage"] = advantage if advantage else "NULL"

                # 公有字段清洗
                place = redundancy_cleaner(place)
                job_content = content_cleaner(job_content)
                job_name = redundancy_cleaner(job_name)
                job_place = redundancy_cleaner(job_place)
                job_number = get_num(job_number)

                item["_id"] = _id
                item["job_name"] = job_name if job_name else "NULL"
                item["link"] = link if link else "NULL"
                item["place"] = place if place else "NULL"
                item["post_time"] = post_time
                item["job_number"] = job_number if job_number else "NULL"
                item["education"] = education if education else "NULL"
                item["job_nature"] = job_nature if job_nature else "NULL"
                item["job_kind"] = job_kind if job_kind else "NULL"
                item["job_place"] = job_place if job_place else "NULL"
                item["job_content"] = job_content if job_content else "NULL"
                item["company_size"] = company_size if company_size else "NULL"
                item["company_nature"] = company_nature if company_nature else "NULL"
                item["company_industry"] = company_industry if company_industry else "NULL"
                item["company_name"] = company_name if company_name else "NULL"
                item["company_homepage"] = company_homepage if company_homepage else "NULL"
                item["company_address"] = company_address.strip() if company_address else "NULL"

                yield item

            # except ValueError as ve:
            #     log.msg("Error: " + _id + ' ' + str(ve), level=log.ERROR)

            except Exception as ex:
                log.msg("Error when parsing {0}".format(response.url), level=log.ERROR)
                raise ex

        else:
            log.msg("Page Not Found, reason: {0}".format(response.status), level=log.WARNING)


    # 进入智联公司主页寻找官网地址
    def parse_company_page(self, response):
        item = response.meta['sz_item']
        if item["company_homepage"] != "NULL":
            yield item
        selector = Selector(response)
        company_homepage = selector.xpath('//p[@class="company-info__detail-info__url"]/a/text()').extract_first()
        item["company_homepage"] = company_homepage if company_homepage else "NULL"
        yield item

