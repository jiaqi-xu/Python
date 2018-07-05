from bson import ObjectId
import csv
from Services.customercontext import CustomerContext as CC
cc =CC(4)
sku_list = []
with open('/home/jiaqi/Jiaqi_list.csv') as r:
    sku_reader = csv.reader(r)
    sku_list = [r[0] for r in sku_reader]

counter = 0
skus_without_avail = []
skus_get_avail = []
error_list = []

for sku in sku_list:
    counter += 1
    customer_product_id = cc.db.products.find_one({'sku': sku, 'store':4}).get('_id')
    master_id = cc.db.masters.find_one(
        {'products.product': customer_product_id}
    ).get('_id')

    products = cc.db.masters.find_one(
        {'products.product': customer_product_id},
        {'products': {'$elemMatch': {'store': 3066}}}
    ).get('products')

    if products is None:
        continue

    if products[0]['prices'][-1].get('available') is None:
        skus_without_avail.append(sku)
        print("{sku} avail is None".format(sku=sku))
    else:
        skus_get_avail.append(sku)
        print("{sku} gets avail value".format(sku=sku))


