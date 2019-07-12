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
        dom = url2domain(url)
        # check user visits to the domain groups
        c1, c2, c3, c4 = "0", "0", "0", "0"
        if dom in [u'cars.ru', u'avto-russia.ru', u'bmwclub.ru']:
            c1 = "1"
        if dom in [u'fastpic.ru', u'fotoshkola.net', u'bigpicture.ru']:
            c2 = "1"
        if dom in [u'nirvana.fm', u'rusradio.ru', u'pop-music.ru']:
            c3 = "1"
        if dom in [u'snowmobile.ru', u'nastroisam.ru', u'mobyware.ru']:
            c4 = "1"
        # output of non-empty dom:
        if dom:
            print(uid + "\t" + c1 + c2 + c3 + c4)


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
