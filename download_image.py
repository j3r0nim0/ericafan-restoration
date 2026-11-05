#!/usr/bin/env python3
import urllib.request
import sys

url = "https://bkimg.cdn.bcebos.com/pic/a044ad345982b2b7d0a25240c9f4dcef76094a362da7?x-bce-process=image/resize,m_lfit,w_536,limit_1/quality,Q_70"
path = "/Users/jerry/Developer/ericafan-restoration/images/movie-poster.jpg"

try:
    urllib.request.urlretrieve(url, path)
    print(f"Downloaded successfully to {path}")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)