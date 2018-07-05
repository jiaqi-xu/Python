import csv
from Services.customercontext import CustomerContext as CC

cc = CC(555028)

KENT_STORE_ID = 360137

target_file = open('/Users/jiaqixu/PycharmProjects/PythonLearning/customerhomehardware_kent_delete.csv', 'r')

verification_backups = []

# get all the skus in the bad matches file
sku_list = [r["Your SKU"] for r in csv.DictReader(target_file, delimiter=",")]

# list contains all sku has error during progress
error_list = []

# get all the documents which are verified and save into a list
verification_documents_list = list(cc.db.match_verification.find(
    {'store': KENT_STORE_ID, 'verifications.verified': True})
)


for document in verification_documents_list:
    # document id
    _id = document.get('_id')

    # sku for kent.ca
    _sku = document.get('sku')

    # reference to related customer's document
    verifications_list = document.get('verifications')
    # filter list in case of more than one element
    verification = filter(
        lambda ver: ver.get('store') == 555028, verifications_list
    )
    verification_id = verification[0].get('_id')

    # sku for customer homehardware
    customer_sku = document.get('verifications')[0].get('sku')

    # check if the sku is in the sku list from bad matches file
    if customer_sku in sku_list:
        try:
            # backup before removing
            verification = cc.db.match_verification.find_one(
                {'_id': verification_id}
            )
            verification_backups.append(verification)
            # remove element from customer perspective
            cc.db.match_verification.update(
                {'_id': verification_id},
                {'$pull': {'verifications': {'_id': _id}}}
            )
            # delete document for kent.ca in collection
            cc.db.match_verification.remove({'_id': _id})
            print(
                '%s removes verification for sku %s successfully'
                % (customer_sku, _sku)
            )
        except:
            error_list.append(customer_sku)
            print('error happens for sku %s' % customer_sku)


