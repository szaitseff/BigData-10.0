#!/opt/anaconda/envs/bd9/bin/python3
import sys
import happybase

connection = happybase.Connection('master.cluster-lab.com')
table=connection.table('sergey.zaytsev')


def main():
    for line in sys.stdin:
        # input
        uid, ts, url = line.strip().split('\t')
        # output
        table.put(uid, {'data:url': url}, timestamp=int(ts))

if __name__ == "__main__":
    main()
