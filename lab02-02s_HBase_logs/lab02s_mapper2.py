#!/opt/anaconda/envs/bd9/bin/python3
import sys

def main():
    lst1 = []
    for line in sys.stdin:
        url, num = line.strip().split('\t')
        # check filter on user id
        lst1.append([int(num), url])
    # output
    lst2 = sorted(lst1, reverse=True)[:350]
    for item in lst2:
        print(item[1] + '\t' + str(item[0]))

if __name__ == "__main__":
    main()
