import sys

def print_res(key, values):
    flag = [0, 0, 0, 0]
    for i in range(4):
        for j in range(len(values)):
            flag[i] += int(values[j][i])
        if flag[i] >= 10:
            flag[i] = "1"
        else:
            flag[i] = "0"
    print("\t".join([key, flag[0], flag[1], flag[2], flag[3]]))

prev_key = None
values = []

for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key != prev_key and prev_key is not None:
        print_res(prev_key, values)
        values = []
    prev_key = key
    values.append(value)

if prev_key is not None:
    print_res(prev_key, values)
