import urllib2

def internet_on():
    try:
        urllib2.urlopen('http://google.de', timeout=1)
        return True
    except urllib2.URLError as err:
        return False