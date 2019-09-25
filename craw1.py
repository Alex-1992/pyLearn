import requests
import re
from bs4 import BeautifulSoup
import traceback


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def getStockList(ilt, stockURL):
    print('')


def getStockInfo(list, stockURL, fpath):
    pass


def main():
    #     stock_list_url =

    # main()
    # http: // quote.eastmoney.com
