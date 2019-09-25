import re
import requests
import os


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        return ''


# reg = re.compile(r'^"pin_id":"'+pid+r'.*?", "type"$')
k = '1220293694'
url = 'https://huaban.com/pins/' + k + '/'
html = getHTMLText(url)
reg = re.compile(r'"pin_id":'+k+r'.*?", "type"')
# reg = re.compile(r'"pin_id":1220293694.*?", "type"$')
#reg = re.compile(r'1220293694.*$')
str1 = reg.search(html.replace("\n", ""))
print(str1.group(0))
