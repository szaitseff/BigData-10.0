#!/opt/anaconda/envs/bd9/bin/python3
import sys

def main():
    for line in sys.stdin:
        record = line.strip().split('\t')
        # check filter on user id
        uid = record[0]
        if uid=='-':
            continue
        # check existence of url
        try:
            url = record[2]
        except IndexError:
            continue
        # output
        print(url + '\t1')

if __name__ == "__main__":
    main()
