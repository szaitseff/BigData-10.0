#!/opt/anaconda/envs/bd9/bin/python3
import sys

def main():
    for line in sys.stdin:
        record = line.strip().split('\t')
        # check filters on user id
        uid = record[0]
        if uid=='-' or (int(uid) % 256)!=114:
            continue
        # transform timestamp records
        try:
            ts = int(float(record[1])*1000)
        except:
            print('cannot convert ts')
        # check existence and correctness of url
        try:
            url = record[2]
            if url.startswith('http')==False:
                continue
        except IndexError:
            continue
        # output
        print(uid + '\t' + str(ts) +'\t' + url)

if __name__ == "__main__":
    main()
