from urllib.request import Request,urlopen

from fake_useragent import UserAgent

base_url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20"
i = 0
while True:

    headers = {
        "User-Agent" :UserAgent().chrome
    }
    url = base_url.format(i * 20)       # 每20条，翻一页。 可以通过扩大每一页显示的数，就可以提高效率。
    request = Request(url,headers=headers)
    response = urlopen(request)
    info = response.read().decode()
    print(info)
    if info == "" or info is None:
        break
    i += 1