import sys
selling_dict = {}
while True:
    line = sys.stdin.readline()
    if line == '\n':
        break

    sell_date, quantity, product_id = line.split(",")
    if sell_date not in selling_dict.keys():
        selling_dict.update({
            sell_date: [(quantity, product_id)]
        })
    else:
        selling_dict[sell_date].append((quantity, product_id))


for sell_time in selling_dict.keys():
    items_atm = selling_dict.get(sell_time)
    item_counter = len(items_atm)
    total_quantities = 0
    for item in items_atm:
        total_quantities += int(item[0])
    average_quantities = round(total_quantities/item_counter, 3)
    result = [
        sell_time, str(total_quantities),
        "%.2f" % average_quantities, str(item_counter)
    ]
    print(",".join(result))








