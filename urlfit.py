#!/usr/bin/env python2

import urllib2, urllib
import json
import sys
import pyperclip
from cookielib import CookieJar

def shorten(link):
    api = "https://developer.url.fit/api/shorten?long_url={link}"
    base = "https://url.fit"
    code = ""
    cj = CookieJar()

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = \
        [("User-agent", "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")]
    try:
        u = opener.open(api.format(link=urllib.quote_plus(link)))
    except urllib2.HTTPError, msg:
        print "Error shortening \"{link}\": {msg} ".format(link=link, msg=str(msg))
        return None
    code = (json.loads(u.read()))['url']

    return urllib.basejoin(base, code)
result = []
if len(sys.argv) > 1:
    result = []
    for url in sys.argv[1:]:
        if "http" not in url[:5]:
            url = "http://"+url
        u = shorten(url)
        if u is not None:
            print "Link \"{link}\" -> \"{short}\"".format(link=url, short=u)
            result += [u]

else:
    print "Getting url from clipboard..."
    for url in pyperclip.paste().split():
        if "http" not in url[:5]:
            url = "http://"+url
        u = shorten(url)
        if u is not None:
            print "Link \"{link}\" -> \"{short}\"".format(link=url, short=u)
            result += [u]

if len(result) > 0: pyperclip.copy("\n".join(result))
