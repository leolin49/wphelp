import progressbar
import requests
import time
import re
import os


def download(pbar, src_list, website, catalog="noCatalog"):
    dir_name = "./" + website
    if catalog != "noCatalog":
        dir_name += "/" + catalog
    # Create a new directory or not
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    # total = 100
    # widgets = ['Download: ', progressbar.Percentage(),\
    #             ' ', progressbar.Bar('#'),\
    #             ' ', progressbar.Timer(),\
    #             ' ', progressbar.FileTransferSpeed()]
    # download photos
    # print(src_list)
    for i in range(0, len(src_list)):
        # pbar = progressbar.ProgressBar(widgets=widgets, maxval=total)
        # pbar.start()
        respon = requests.get(src_list[i])
        file_name = src_list[i].split('/')[-1]
        with open(dir_name + "/" + file_name, "wb") as f:
            f.write(respon.content)
        f.close()
        step = ((i + 1)/len(src_list))*100
        pbar.setValue(step)
        # pbar.finish()
        print(file_name + " has been download...")


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


def bing():
    '''Bing Wallpapers'''
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/76.0.3809.132 Safari/537.36'
    }
    for page in range(1, 2):
        # Request website
        website = 'https://bing.ioliu.cn/ranking?p=' + str(page)
        response = requests.get(website, headers=head)
        html_code = response.text
        # Resolve website and get the photo website
        urls_list = re.findall('<a class="mark" href="(.*?)"></a>', html_code)
        # Get the photo's name by split in the photo website
        photoname_list = \
            [url.split('?')[0].split('/')[-1] for url in urls_list]
        # Splice to get the real picture address
        start_str = 'http://h1.ioliu.cn/bing/'
        end_str = '_1920x1080.jpg'
        realsite_list = \
            [start_str + photoname + end_str for photoname in photoname_list]
        download(realsite_list, "bing")


def main():
    wallpaperscraft("art")


if __name__ == "__main__":
    main()
