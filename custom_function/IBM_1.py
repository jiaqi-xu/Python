import sys
for line in sys.stdin:
    # print(line)
    N, p, q = line.strip().split(" ")
    N = int(N)
    p = int(p)
    q = int(q)
    results = []
    for index in range(N):
        num = N - index
        if num % p == 0 and str(q) not in str(num):
            results.append("OUT")
        elif num % p != 0 and str(q) in str(num):
            results.append("THINK")
        elif num % p == 0 and str(q) in str(num):
            results.append("OUTTHINK")
        else:
            results.append(str(num))

    print(",".join(results))
