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
print(len(url)-1)



status_msg = 'OK'
link_href = '#'
if url.find('#') == len(url)-1:
    status_msg = 'TMEP'
    print(status_msg)

if url.find('#') < 0:
    print(url.find('mailto:'))
    print('ni ma')
