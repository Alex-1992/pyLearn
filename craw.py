import requests
import re
import os

# -*- coding: utf-8 -*-


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        return ''


def parsePid(html):
    # 拿出前100的 id 与 采集数
    # 取前10个放入list
    #idlist = re.findall(r'"pin_id":/d+', html)[:100]
    list_p = {}
    idlist = re.findall(r'"pin_id":\d+', html)[:search_num]
    picklist = re.findall(r'"repin_count":\d+', html)[:search_num]
    for i in range(0, len(idlist)):
        list_p[idlist[i].split(':')[1]] = picklist[i].split(':')[1]
    list_p = sorted(list_p.items(), key=lambda item: int(
        item[1]), reverse=True)
    list_p = list_p[:10]
    list_p = sorted(list_p, key=lambda item: int(
        item[1]), reverse=True)
    return list_p


def writePicData(k):
    pic_url = 'https://huaban.com/pins/' + k + '/'
    html = getHTMLText(pic_url)
    # reg = re.compile(pid + r'.*?", "type"$')
    reg1 = re.compile(r'"pin_id":'+k+r'.*?", "urlname"')
    str1 = reg1.search(html).group(0)

    repin = re.search(r'"repin_count":\d+', str1).group(0).split(':')[1]
    like = re.search(r'"like_count":\d+', str1).group(0).split(':')[1]
    leibie = re.search(r'"raw_text":"[^"]+', str1).group(0).split(':"')[1]
    name = re.search(r'"username":"[^"]+', str1).group(0).split(':"')[1]
    print(repin, like, leibie, name)

    code = str1.split('"key":"')[1].split('", "type"')[0]
    down_url = 'https://hbimg.huabanimg.com/' + code
    r = requests.get(down_url)
    # coding:utf-8
    path = '主题:' + leibie + '||画师:'+name+'||采集:' + repin+'||喜欢:' + like+'.png'
    path = re.sub(r'(?u)[^-\w.]', '_', path)
    # path = ("%d--" % score) + author_name + "--" + question_title + ("--%d" % seq) + ".jpg"
    with open(os.path.join(dir, path), 'wb') as f:
        f.write(r.content)


# 1.https://huaban.com/search/?q=原画 搜索前一百个资源 根据采集次数排序取前10
# 2.根据拿到的pid 去 https://huaban.com/pins/ + pid + /  找到主图code
# 3.根据链接https://hbimg.huabanimg.com/ + code  下载主图片  保存下载的图片到本地
# 4.根据  用户名 种类 采集数，喜欢数 作为文件名保存
search_num = 100
pick_num = 10
pidlist = {}
key_word = '原画'
dir = 'pics/'

# 每页最多拿100个 超过100会被限制成20
start_url = 'https://huaban.com/search/?q='+key_word+'&per_page=100'
html = getHTMLText(start_url)
pidlist = parsePid(html)
# for k, v in pidlist.items():
#     pic_url = 'https://huaban.com/pins/' + k + '/'
#     writePicData(pic_url, k)
print(pidlist)
for k in pidlist:
    writePicData(k[0])
