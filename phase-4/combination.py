import itertools
'''
data_dict = options_dict
total_option = 1
longest_list = 0
option_dict = {}
colum = 0
for key, value in data_dict.iteritems():
    total_option *= len(value)
    if len(value) > longest_list:
        longest_list = len(value)

for i in xrange(0, total_option):
    option_dict[i] = {}

for key, value in data_dict.iteritems():
    num_of_opt = 0
    # to create colums
    for i in xrange(0, (total_option)):
        option_dict[i].update({
            key.replace('#', '').strip(): value[num_of_opt]
        })
        if num_of_opt < (len(value) - 1):
            num_of_opt += 1
        else:
            num_of_opt = 0

if option_dict:
    return option_dict
'''
data_dict ={
 "Color": [
  "Red",
  "Ultra Blue/White",
  "Black/Quirky Lime",
  "Royal"
 ],
 "Size": [
  "5",
  "6",
  "7",
  "8",
  "9",
  "10"
 ],
 "Width": [
  "Regular"
 ]
}

keys = data_dict.keys()
print keys
option_len = len(keys)
combination_list = []
for key in keys:
    combination_list.append(data_dict.get(key))


print combination_list

combination_result = list(itertools.product(*combination_list))
print combination_result
print len(combination_result)

options = []

for option_combination in combination_result:
    for option_key in en(option_combination)



