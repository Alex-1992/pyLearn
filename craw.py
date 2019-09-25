import requests
import re
import os


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        return ''


def parsePid(html, plist):
    # 拿出前100的 id 与 采集数
    # 取前10个放入list
    #idlist = re.findall(r'"pin_id":/d+', html)[:100]
    idlist = re.findall(r'"pin_id":\d+', html)[:search_num]
    picklist = re.findall(r'"repin_count":\d+', html)[:search_num]
    for i in range(0, len(idlist)):
        plist[idlist[i].split(':')[1]] = picklist[i].split(':')[1]
    plist = sorted(plist.items(), key=lambda item: item[1], reverse=True)
    # print(plist[:pick_num])
    return plist[:pick_num]


def writePicData(url, pid):
    html = getHTMLText(url)
    # reg = re.compile(pid + r'.*?", "type"$')
    reg = re.compile(r'"pin_id":'+pid+r'.*?", "type"')
    str1 = reg.search(html)
    code = str1.group(0).split('"key":"')[1].split('", "type"')[0]
    down_url = 'https://hbimg.huabanimg.com/' + code
    r = requests.get(down_url)
    with open(dir+pid+'.png', 'wb') as f:
        f.write(r.content)


# 1.https://huaban.com/search/?q=原画 搜索前一百个资源 根据采集次数排序取前10
# 2.根据拿到的pid 去 https://huaban.com/pins/ + pid + /  找到主图code
# 3.根据链接https://hbimg.huabanimg.com/ + code  下载主图片  保存下载的图片到本地
search_num = 100
pick_num = 10
dir = 'pics/'
pidlist = {}
# print(sorted(d.items(), key=lambda item: item[1]))
start_url = 'https://huaban.com/search/?q=原画'
html = getHTMLText(start_url)
parsePid(html, pidlist)
print(pidlist)
for k, v in pidlist.items():
    pic_url = 'https://huaban.com/pins/' + k + '/'
    print(pic_url)
    print(k)
    writePicData(pic_url, k)
