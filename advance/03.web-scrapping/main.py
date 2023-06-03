# -*- coding: utf-8 -*-

import requests, bs4, re


pattern = r"(дизайн|фото|web|python)"

base_url = "https://habr.com/"
full_url = base_url+"ru/all/"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.2.1759597955.1662321260; _ym_uid=1662321261736426690; _ym_d=1662321261; hl=ru; fl=ru; _ym_isad=1; habr_web_home_feed=/all/; _gid=GA1.2.796973414.1672327721; visited_articles=513966:226521:186608:482464:684720:149077; _gat_gtag_UA_726094_1=1",
    "Host": "habr.com",
    "If-None-Match": "W/e171-OAyTmotS4Zo2oWwnUGMcLDrLURo",
    "Referer": "https://habr.com/ru/all/",
    "sec-ch-ua": "Not?A_Brand;v=8, Chromium;v=108, Microsoft Edge;v=108",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    "x-app-version": "2.105.0"
    }
text = requests.get(url=full_url, headers=headers).text

soup = bs4.BeautifulSoup(text, features="html.parser")
previews = soup.find_all(class_="tm-article-snippet tm-article-snippet")
for preview in previews:
    result = re.findall(pattern, str(preview))

    if result != []:

        date = preview.find("time")
        date = re.findall(r"[\=]*(\d+\-\d+\-\d+)[\>]*", str(date))[0]

        title = preview.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").find("span").text

        href = preview.find(class_="tm-article-snippet__title tm-article-snippet__title_h2")
        href = re.findall(r"[\"](\S*)[\"]", str(href))[-1]

        print(date, title, base_url+href[1:])