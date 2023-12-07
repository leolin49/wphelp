import requests
import re
import common as comm


class Wallhaven:
    @staticmethod
    def run():
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        for page in range(2, 4):
            src_list = []
            website = 'https://wallhaven.cc/search?q=id%3A37&resolutions=1920x1080&page=' + str(page)
            response = requests.get(website, headers=head)
            html_code = response.text
            id_list = re.findall('data-wallpaper-id="([^"]+)"', html_code)
            for _, wallpaper_id in enumerate(id_list):
                png_website = 'https://wallhaven.cc/w/' + str(wallpaper_id)
                html_code = requests.get(png_website, headers=head).text
                src = re.findall('<div[^>]+class="scrollbox"[^>]*>\s*<img[^>]+src="([^"]+)"', html_code)
                if len(src) > 0:
                    src_list.append(src[0])
            comm.download(src_list, "WallHaven")


def run():
    Wallhaven.run()
