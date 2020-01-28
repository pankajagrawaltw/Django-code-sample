# import json
# import urllib.request as urllib2


# def goo_shorten_url(url):
#     API_KEY='<API_KEY>'
#     post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=%s'%API_KEY
#     postdata = {'longUrl':url}
#     headers = {'Content-Type':'application/json'}
#     req = urllib2.Request(
#         post_url,
#         json.dumps(postdata),
#         headers
#     )
#     ret = urllib2.urlopen(req).read()
#     return json.loads(ret)['id']


import requests
import json

def goo_shorten_url(url):
    key='AIzaSyD_ZE6AxmW1GID7VljqjhR7q5en5CKu_v0'
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key='+key
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    return r.json()