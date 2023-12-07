import os
import requests


def download(src_list, website, catalog="noCatalog"):
    dir_name = "./" + website
    if catalog != "noCatalog":
        dir_name += "/" + catalog
    # Create a new directory or not
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    for _, src in enumerate(src_list):
        response = requests.get(src)
        file_name = src.split('/')[-1]
        with open(dir_name + "/" + file_name, "wb") as f:
            f.write(response.content)
        f.close()
        print(file_name + " has been download...")