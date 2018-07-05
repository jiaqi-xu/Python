TITLE = "BUILD YOUR OWN GREE TRI ZONE MINI-SPLIT SYSTEM"

option_data = [{"opt":[{"price":2295.95,"sku":"3534","text":"GreeMultiZoneInverterHeatPump-36,000BTU","zone":"HeatPumpCondenser"},{"price":2495.95,"sku":"3535","text":"GreeMultiZoneInverterHeatPump-42,000BTU","zone":"HeatPumpCondenser"}]},{"opt":[{"price":349.95,"sku":"3536","text":"GreeVireoMultiZoneWallMountUnit-9,000BTU","zone":"Zone1"},{"price":395.95,"sku":"3531","text":"GreeVireoMultiZoneWallMountUnit-12,000BTU","zone":"Zone1"},{"price":445.95,"sku":"3537","text":"GreeVireoMultiZoneWallMountUnit-18,000BTU","zone":"Zone1"}]},{"opt":[{"price":349.95,"sku":"3538","text":"GreeVireoMultiZoneWallMountUnit-9,000BTU","zone":"Zone2"},{"price":395.95,"sku":"3539","text":"GreeVireoMultiZoneWallMountUnit-12,000BTU","zone":"Zone2"},{"price":445.95,"sku":"3532","text":"GreeVireoMultiZoneWallMountUnit-18,000BTU","zone":"Zone2"}]},{"opt":[{"price":349.95,"sku":"3540","text":"GreeVireoMultiZoneWallMountUnit-9,000BTU","zone":"Zone3"},{"price":395.95,"sku":"3541","text":"GreeVireoMultiZoneWallMountUnit-12,000BTU","zone":"Zone3"},{"price":445.95,"sku":"3533","text":"GreeVireoMultiZoneWallMountUnit-18,000BTU","zone":"Zone3"}]}]
option_data = [data['opt'] for data in option_data]

# get the total number of options the result should have
len_opts = len(option_data)
total_opts = 1
for i in xrange(0, len_opts):
    total_opts *= len(option_data[i])

# generate a list of lists - each list looks like [1,1,1,...] up to the number of option dropdowns
first_indexes = [1 for t in option_data]
indexes = []
for i in xrange(0,total_opts):
    indexes.append(common.deepcopy(first_indexes))

# mutate the indexes list to have every possible combination of indexes corresponding to each option in option_data
for level, option in enumerate(option_data):
    seq = list(xrange(0, len(option)))
    seq = seq * (total_opts/len(seq))
    for i, index in enumerate(indexes):
        index[level] = seq[i]
    indexes.sort(key=lambda x: x[level])

options = {}
for i in xrange(0, total_opts):
    skus = []
    option = {
        'sku':[],
        'availability': True,
        'options': {},
        'price': 0,
        'title': [],
    }
    for j, item in enumerate(option_data):
        opt_item = item[indexes[i][j]]
        option['sku'].append(opt_item['sku'])
        option['options'].update({opt_item['zone']: opt_item['text']})
        option['price'] += opt_item['price']
        option['title'].append(opt_item['text'])
    sku = '_'.join(option.pop('sku'))
    option['title'] = TITLE + ' [ ' + ', '.join(option['title']) + ' ]'
    options[sku] = option

print options