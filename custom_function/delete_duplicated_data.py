from Services.customercontext import  CustomerContext as CC
cc = CC(555062)

go_masters = []
masters = cc.db.masters.find({'products': {'$elemMatch': {'store': 555062}}}, {'products.$': 1})

for master in masters:
    count = 0
    ts_list = []
    master_id = master.get('_id')
    prices = master.get('products')[0].get('prices')
    for price in prices:
        if count == 2:
            go_masters.append({
                master_id: ts_list
            })
            break

        ts = price.get('ts')
        if ts.year == 2018 and ts.month == 4 and ts.day == 9:
            ts_list.append(ts)
            count += 1

for go_master in go_masters:
    _id = go_master.keys()[0]
    time_entry = go_master.get(_id)[0]
    cc.db.masters.update(
        {'_id': _id, 'products.store': 555062},
        {'$pull': {'products.$.prices': {'ts': time_entry}}}
    )
