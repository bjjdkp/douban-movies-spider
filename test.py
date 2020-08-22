# --*-- coding:utf-8 --*--

import requests

headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'douban-fav-remind=1; gr_user_id=692a78cb-e45c-42f2-9623-7db60a1ceca2; push_doumail_num=0; douban-profile-remind=1; __utmv=30149280.15796; _ga=GA1.2.1678134300.1547994934; __utma=30149280.1678134300.1547994934.1561079942.1572576353.136; viewed="1292405_3852290_3667744_1133907_30259573_26912767_1230413_10546925_26297606_26979890"; push_noty_num=0; ll="119088"; bid=9RIXPQoXnak; ct=y; talionusr="eyJpZCI6ICIxNTc5NjUwODUiLCAibmFtZSI6ICJcdTVjMGZcdTk0YzFcdTc0ZGMifQ=="; ap_v=0,6.0',
    # 'Host': 'm.douban.com',
    # 'Origin': 'https://movie.douban.com',
    'Referer': 'https://movie.douban.com/subject/1292849/?from=subject-page',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}

url = "https://m.douban.com/rexxar/api/v2/gallery/subject_feed"

params = {
    # 'start': '0',
    # 'count': '4',
    'subject_id': '305739',
    # 'ck': 'null',
}

res = requests.get(url, headers=headers, params=params)

print(res.text)
