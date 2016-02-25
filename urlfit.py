#!/usr/bin/env python2

import urllib2, urllib
import json
import sys
from cookielib import CookieJar

def shorten(link):
    api = "https://developer.url.fit/api/shorten?long_url={link}"
    base = "https://url.fit"
    code = ""
    cj = CookieJar()

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = \
        [("User-agent", "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")]
    u = opener.open(api.format(link=urllib.quote_plus(link)))
    code = (json.loads(u.read()))['url']

    return urllib.basejoin(base, code)

if len(sys.argv) > 1:
    for url in sys.argv[1:]:
        print shorten(url)
else:
    pass
