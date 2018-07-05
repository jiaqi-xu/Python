import sys

drugs_list = []
results = []
blankline_counter = 0
results_counter = 0

for line in sys.stdin:
    if line == '\n':
        break

    line = line.strip()
    drugs_list.append(line)

while True:
    match_key = sys.stdin.readline().strip()

    follow_key = []
    for letter in match_key:
        follow_key.append(chr(ord(letter)+1))

    follow_key = "".join(follow_key)

    for drug in drugs_list:
        if drug.startswith(match_key) or drug.startswith(follow_key):
            results.append(drug)
            results_counter += 1
            if results_counter == 2:
                break

    if results:
        for index in range(results_counter):
            print(results[index])
    else:
        print("<NONE>")

