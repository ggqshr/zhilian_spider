# -*- coding: utf-8 -*-
from scrapy import Item, Field


class XiaozhaoItem(Item):
    # 智联校招
    _id = Field()               # 职位ID
    post_time = Field()         # 发布日期
    link = Field()              # 职位链接
    place = Field()             # 工作城市
    job_place = Field()         # 工作地址
    job_nature = Field()        # 工作性质
    job_name = Field()          # 职位名称
    job_kind = Field()          # 职位类别
    education = Field()         # 最低学历
    job_number = Field()        # 招聘人数
    job_content = Field()       # 职位描述
    company_name = Field()      # 公司名称
    company_industry = Field()  # 公司行业
    company_size = Field()      # 公司规模
    company_nature = Field()    # 公司性质
    company_homepage = Field()  # 公司主页
    company_address = Field()   # 公司地址


class ZhilianItem(Item):
    # 智联社招
    _id = Field()               # 职位ID
    job_name = Field()          # 职位名称
    link = Field()              # 职位链接
    salary = Field()            # 职位薪酬
    post_time = Field()         # 发布日期
    place = Field()             # 工作城市
    job_nature = Field()        # 工作性质
    experience = Field()        # 工作经验
    education = Field()         # 最低学历
    job_number = Field()        # 招聘人数
    job_kind = Field()          # 职位类别
    job_content = Field()       # 职位描述
    job_place = Field()         # 工作地点(具体)
    company_name = Field()      # 公司名称
    advantage = Field()         # 公司福利
    company_size = Field()      # 公司规模
    company_nature = Field()    # 公司性质
    company_industry = Field()  # 公司行业
    company_homepage = Field()  # 公司主页
    company_address = Field()   # 公司地址

