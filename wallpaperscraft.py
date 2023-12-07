import re

import requests


def wallpaperscraft_prepare():
    _website = 'https://wallpaperscraft.com'
    _code = requests.get(_website).text
    # Get all catalog
    catalog_list = re.findall('<a class="filter__link" href="/catalog/(.*?)">', _code)
    return catalog_list


def wallpaperscraft(pbar, catalog="60_favorites", resolution="1920x1080"):
    for page in range(1, 2):
        website = 'https://wallpaperscraft.com/catalog/'+catalog+'/page' + str(page)
        # print(website)
        response = requests.get(website)
        html_code = response.text
        urls_list = re.findall('<img class="wallpapers__image" src="(.*?)" alt=', html_code)
        photoname_list = \
            [url.split('/')[-1].replace("300x168", resolution) for url in urls_list]
        start_str = "https://images.wallpaperscraft.com/image/"
        realsite_list = \
            [start_str + photoname for photoname in photoname_list]
        download(pbar, realsite_list, "wallpaperscraft", catalog)