# -*- coding: utf-8 -*-

import re


def content_cleaner(obj):
    try:
        new_str = ''
        for item in obj:
            if '工作地址：' in item:
                # 正文获取至工作地址前
                break
            if ('：' or ':') in item:
                item = '  ' + item
            else:
                item = ''.join(item.split())
            new_str += item
        return new_str
    except:
        return obj


def redundancy_cleaner(obj, *args):
    # 清洗冗余字
    if obj:
        for e in args:
            obj = obj.replace(e, '')
        obj = ''.join(obj.split())
    return obj


def get_num(obj):
    match_re = re.match(".*?(\d+).*", obj)
    if match_re:
        num = int(match_re.group(1))
    else:
        num = 0
    return num


def salary_formater(salary_string):
    if "-" in salary_string:
        old_salary_format = salary_string.split("-")
        new_salary_format = []
        for i in old_salary_format:
            if u"千" in i:
                new_salary_format.append(float(i.split(u"千")[0]) * 1000)
            elif u"万" in i:
                new_salary_format.append(float(i.split(u"万")[0]) * 10000)
        new_salary_string = str(int(new_salary_format[0])) + "-" + str(int(new_salary_format[1]))
        return new_salary_string
    return salary_string