#!/opt/anaconda/envs/bd9/bin/python3
import sys
import re
from urllib.parse import urlparse, unquote

def main():
    for line in sys.stdin:
        record = line.strip().split('\t')
        # check existence of user id
        uid = record[0]
        if uid=='-':
            continue
        # check existence of url
        try:
            url = record[2]
        except IndexError:
            continue
        # extract domain from url
        domain = url2domain(url)
        # check if auto-user
        if domain in {u'cars.ru', u'avto-russia.ru', u'bmwclub.ru'}:
            a = "1"
        else:
            a = "0"
        # output of non-empty domain:
        print("\t".join([uid, a, domain]))

def url2domain(url):
    try:
        a = urlparse(unquote(url.strip()))
        if (a.scheme in ['http','https']):
            b = re.search("(?:www\.)?(.*)",a.netloc).group(1)
            if b is not None:
                return str(b).strip()
            else:
                return ''
        else:
            return ''
    except:
        return

if __name__ == "__main__":
    main()
