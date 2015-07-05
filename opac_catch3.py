#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
with urllib.request.urlopen('https://opac.icu.ac.jp/opac/opac_search.cgi?smode=1') as response:
    html = response.read()
html = str(html)
print(html.encode('utf8'))
f = open('./test.html','w+')
f.write(html)
