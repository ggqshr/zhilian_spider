from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


client = MongoClient()
db = client['zhilian']
cl = db['campus_180420_181207']
ocl = db["tmp"]

for n, item in enumerate(cl.find()):
    print(n)
    link_id = item.get("link").split("/")[-1]
    item["_id"] = link_id
    try:
        ocl.insert(item)
    except DuplicateKeyError:
        pass

# for day in range(23, 28):
#     day = str(day)
#     if len(day) == 1:
#         day = '0' + day
#     date = '2017-11-' + day
#     print('Processing:' + date)
#     count = db['sociaty_1120'].count({'post_time':date})
#     print(date + ':' + str(count))
#
# client.close()