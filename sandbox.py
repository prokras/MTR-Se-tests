import requests
import sys

if len(sys.argv[1]) > 1:
    print(sys.argv[1])
else:
    raise

url = 'http://magentofinal.mytriorings.com/layaway-plan#'
r = requests.get(url)
print(r.status_code)
print(url.find('#'))
print(len(url))
