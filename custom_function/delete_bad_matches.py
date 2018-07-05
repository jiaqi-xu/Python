import csv
from Services.customercontext import CustomerContext as CC
from Services.ProductService import DeleteProduct
cc = CC(555027)
error_list = []
target_file = open('/Users/jiaqixu/PycharmProjects/PythonLearning/customerhomehardware_kent_delete.csv', 'r')
sku_reader = csv.DictReader(target_file, delimiter=",")
sku_list = []
for row in sku_reader:
    sku_list.append(row.get("Your SKU"))

for sku in sku_list:
    customer_product_id = cc.db.products.find_one({'sku': sku}).get('_id')
    master_id = cc.db.masters.find_one({'products.product': customer_product_id}).get('_id')
    products = cc.db.masters.find_one(
        {'products.product': customer_product_id},
        {'products': {'$elemMatch': {'store': 360137}}}
    )
    if len(products) == 1:
        product_id = products[0].get('product')
    else:
        error_list.append(sku)
        print('%s is added to error list' % sku)
        continue

    DeleteProduct(master_id, product_id, 555027)
    print('delete from master for %sku successfully!' % sku)



