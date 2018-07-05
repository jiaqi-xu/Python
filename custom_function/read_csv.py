import csv

zip_code_list = []
with open('/Users/jiaqixu/Downloads/84-lumber_zipcodes.csv') as r:
    reader = csv.DictReader(r, delimiter=",")
    for row in reader:
        zip_code = row['ZIP CODE'].split('-')[0]
        zip_code_list.append(zip_code)



# remove the zip codes in customer database for specific competitor (run in customercontext)
count = 0
for zip in zip_code_list:
    cc.db.zones.remove({'store_id': 3136905, 'zone_name': zip})
    count += 1

print(count)







