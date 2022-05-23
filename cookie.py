import urllib
import http.cookiejar


def extract_cookies():
cookie_jar = http.cookiejar.cookiejar()

url_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

