CityList = [
    'chongqing',
    'hongkong',
    'macao',
    'taiwan',
    'guangzhou', 'shaoguan', 'shenzhen', 'zhuhai', 'shantou', 'foshan', 'jiangmen', 'zhanjiang', 'maoming', 'zhaoqing', 'huizhou', 'meizhou', 'shanwei', 'heyuan', 'yangjiang', 'qingyuan', 'dongguan', 'zhongshan', 'chaozhou', 'jieyang', 'yunfu',
    'wuhan', 'huangshi', 'shiyan', 'yichang', 'xiangyang', 'ezhou', 'jingmen', 'xiaogan', 'jingzhou', 'huanggang', 'xianning', 'suizhou', 'enshitujiazumiaozuzizhizhou', 'gongan', 'wuxue', 'tianmen', 'xiantao', 'qianjiang', 'yicheng', 'shennongjia',
    'xian', 'tongchuan', 'baoji', 'xianyang', 'weinan', 'yanan', 'hanzhong', 'yulin', 'ankang', 'shangluo', 'xingping', 'yangling', 'xixianxinqu',
    'chengdu', 'zigong', 'panzhihua', 'luzhou', 'deyang', 'mianyang', 'guangyuan', 'suining', 'neijiang', 'leshan', 'nanchong', 'meishan', 'yibin', 'guangan', 'dazhou', 'yaan', 'bazhong', 'ziyang', 'aba', 'ganzi', 'liangshan', 'emei', 'xichang', 'jianyang',
    'dalian', 'shenyang', 'anshan', 'fushun', 'benxi', 'dandong', 'jinzhou', 'yingkou', 'fuxin', 'liaoyang', 'panjin', 'tieling', 'chaoyang', 'huludao', 'xingcheng', 'haicheng', 'changtu', 'donggang', 'kaiyuan',
    'changchun', 'hunchun', 'siping', 'liaoyuan', 'tonghua', 'baishan', 'songyuan', 'baicheng', 'yanbian', 'jilinshi', 'gongzhuling',
    'taicang', 'zhangjiagang', 'lianyungang', 'nanjing', 'suzhou', 'kunshan', 'changshu', 'wuxi', 'xuzhou', 'changzhou', 'nantong', 'huaian', 'yancheng', 'yangzhou', 'zhenjiang', 'taizhou', 'suqian',
    'jinan', 'qingdao', 'zibo', 'zaozhuang', 'dongying', 'yantai', 'weifang', 'jining', 'taian', 'weihai', 'rizhao', 'laiwu', 'linyi', 'dezhou', 'liaocheng', 'heze', 'binzhou',
    'fangjiashan', 'hangzhou', 'ningbo', 'wenzhou', 'jiaxing', 'huzhou', 'shaoxing', 'jinhua', 'quzhou', 'zhoushan', 'taizhou', 'lishui',
    'fangchenggang', 'nanning', 'liuzhou', 'guilin', 'wuzhou', 'beihai', 'qinzhou', 'guigang', 'yulin', 'baise', 'hezhou', 'hechi', 'laibin', 'chongzuo',
    'maanshan', 'hefei', 'wuhu', 'bengbu', 'huainan', 'huaibei', 'tongling', 'anqing', 'huangshan', 'chuzhou', 'suzhou', 'liuan', 'bozhou', 'chizhou', 'xuancheng', 'fengyang', 'fuyang', 'guangde', 'susong',
    'shijiazhuang', 'qinhuangdao', 'zhangjiakou', 'tangshan', 'handan', 'xingtai', 'baoding', 'chengde', 'cangzhou', 'langfang', 'hengshui', 'zunhua',
    'yongji', 'taiyuan', 'datong', 'yangquan', 'changzhi', 'jincheng', 'shuozhou', 'jinzhong', 'yuncheng', 'xinzhou', 'linfen', 'lvliang',
    'huhehaote', 'baotou', 'wuhai', 'chifeng', 'tongliao', 'eerduosi', 'hulunbeier', 'xingan', 'xilinguole', 'wulanchabu','bayannaoer','alashan','wushenqi','manzhouli',
    'haerbin', 'qiqihaer', 'shuangyashan', 'jiamusi', 'qitaihe', 'mudanjiang', 'daxinganling', 'suifenhe', 'zhaodongshi', 'jixi', 'hegang', 'daqing', 'yichun', 'heihe', 'suihua', 'anda', 'shuangcheng',
    'fuzhou', 'xiamen', 'putian', 'sanming', 'quanzhou', 'zhangzhou', 'nanping', 'longyan', 'ningde',
    'jingdezhen', 'nanchang', 'pingxiang', 'jiujiang', 'xinyu', 'yingtan', 'ganzhou', 'jian', 'yichun', 'fu3zhou', 'shangrao',
    'sanmenxia', 'zhumadian', 'pingdingshan', 'zhengzhou', 'kaifeng', 'luoyang', 'anyang', 'hebi', 'xinxiang', 'jiaozuo', 'xuchang', 'luohe', 'nanyang', 'shangqiu', 'xinyang', 'zhoukou', 'puyang', 'jiyuan', 'xiping',
    'zhangjiajie', 'changsha', 'zhuzhou', 'xiangtan', 'hengyang', 'shaoyang', 'yueyang', 'changde', 'yiyang', 'chenzhou', 'yongzhou', 'huaihua', 'loudi', 'xiangxi',
    'yangpu','wuzhishan','haikou','sanya','qionghai','danzhou','wenchang','wanning','dongfang','anding','tunchang','chengmai','lingao','qiongzhonglizumiaozuzizhi','baotinglizumiaozuzizhi','baishalizuzizhi', 'changjianglizuzizhi', 'ledonglizuzizhi', 'lingshuilizuzizhi',
    'liupanshui', 'qiandongnan', 'qianxinan', 'guiyang', 'zunyi', 'anshun', 'tongren', 'bijie', 'qiannan',
    'xishuangbanna', 'kunming', 'qujing', 'yuxi', 'baoshan', 'zhaotong', 'chuxiong', 'honghe', 'wenshan', 'dali', 'dehong', 'lijiang', 'nujiang', 'lincang', 'puer',
    'rikeze', 'lasa', 'changdu', 'shannan', 'naqu', 'ali', 'linzhi',
    'jiayuguan', 'lanzhou', 'jinchang', 'baiyin', 'tianshui', 'wuwei', 'zhangye', 'pingliang', 'jiuquan', 'qingyang', 'dingxi', 'longnan', 'gannan', 'linxia',
    'hainan', 'xining', 'haidong', 'haibei', 'huangnan', 'guoluo', 'yushu', 'haixi',
    'yinchuan', 'shizuishan', 'wuzhong', 'guyuan', 'zhongwei',
    'wulumuqi', 'kelamayi', 'tulufan', 'hami', 'changji', 'boertala', 'bayinguoleng', 'akesu', 'kezilesukeerkezi', 'kashen', 'hetian', 'yili', 'tacheng', 'aletai', 'shihezi', 'kuitunshi', 'wusu', 'alaer', 'tumushuke', 'wujiaqu', 'beitunqu',
    'beijing', 'diqing', 'keshen', 'su4zhou', 'shanghai', 'tai4zhou', 'yi1chun', 'yu4lin',
]

# CityList = ['beijing', 'diqing', 'keshen', 'su4zhou', 'shanghai', 'tai4zhou', 'yi1chun', 'yu4lin']


IndustryList = ['in210500', 'in160400', 'in160000', 'in160500', 'in160200', 'in300100', 'in160100', 'in160600',
                'in180000', 'in180100', 'in300500', 'in300900', 'in140000', 'in140100', 'in140200', 'in200300',
                'in200302', 'in201400', 'in201300', 'in300300', 'in120400', 'in120200', 'in170500', 'in170000',
                'in300700', 'in201100', 'in120800', 'in121000', 'in129900', 'in121100', 'in121200', 'in210600',
                'in120700', 'in121300', 'in121500', 'in300000', 'in150000', 'in301100', 'in121400', 'in200600',
                'in200800', 'in210300', 'in200700', 'in130000', 'in120500', 'in130100', 'in201200', 'in200100',
                'in120600', 'in100000', 'in100100', 'in990000']

Catagory = ['bj4010200',
            'bj7001000',
            'bj7002000',
            'bj70020001',
            'bj4000000',
            'bj40000001',
            'bj40000002',
            'bj4082000',
            'bj4084000',
            'bj40840001',
            'bj7004000',
            'bj70040001',
            'bj2060000',
            'bj20600001',
            'bj20600002',
            'bj5002000',
            'bj3010000',
            'bj30100001',
            'bj30100002',
            'bj201300',
            'bj2013001',
            'bj2023405',
            'bj20234051',
            'bj1050000',
            'bj160000',
            'bj1600001',
            'bj1600002',
            'bj160300',
            'bj160200',
            'bj1602001',
            'bj160400',
            'bj1604001',
            'bj1604002',
            'bj200500',
            'bj2005001',
            'bj200300',
            'bj5001000',
            'bj50010001',
            'bj141000',
            'bj1410001',
            'bj1410002',
            'bj140000',
            'bj1400001',
            'bj1400002',
            'bj1400003',
            'bj142000',
            'bj2071000',
            'bj2070000',
            'bj20700001',
            'bj20700002',
            'bj20700003',
            'bj7006000',
            'bj200900',
            'bj2009001',
            'bj2009002',
            'bj2009003',
            'bj4083000',
            'bj40830001',
            'bj4010300',
            'bj4010400',
            'bj40104001',
            'bj121100',
            'bj1211001',
            'bj160100',
            'bj1601001',
            'bj1601002',
            'bj1601003',
            'bj7003000',
            'bj7003100',
            'bj5003000',
            'bj5003001',
            'bj5003002',
            'bj7005000',
            'bj7005001',
            'bj7005002',
            'bj7005003',
            'bj5004000',
            'bj5004001',
            'bj121300',
            'bj121301',
            'bj121302',
            'bj120500',
            'bj2120000',
            'bj2120001',
            'bj2120002',
            'bj2120003',
            'bj2100708',
            'bj2100709',
            'bj2140000',
            'bj2140001',
            'bj2140002',
            'bj2140003',
            'bj2090000',
            'bj2090001',
            'bj2080000',
            'bj2080001',
            'bj2080002',
            'bj2120500',
            'bj5005000',
            'bj5005001',
            'bj5005002',
            'bj5005003',
            'bj4040000',
            'bj4040001',
            'bj4040002',
            'bj201100',
            'bj201101',
            'bj201102',
            'bj2050000',
            'bj2050001',
            'bj2050002',
            'bj2050003',
            'bj2051000',
            'bj2051001',
            'bj2051002',
            'bj6270000',
            'bj6270001',
            'bj6270002',
            'bj130000',
            'bj130001',
            'bj130002',
            'bj2023100',
            'bj2023101',
            'bj100000',
            'bj100001',
            'bj100002',
            'bj100003',
            'bj200100',
            'bj200101',
            'bj200102',
            'bj5006000',
            'bj5006001',
            'bj5006002',
            'bj200700',
            'bj200701',
            'bj300100',
            'bj300101',
            'bj300200']



# CityList = CityList[:2]
