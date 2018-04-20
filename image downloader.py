import random
import urllib.request


def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url , full_name)




download_image("https://upload.wikimedia.org/wikipedia/commons/3/38/Arduino_Uno_-_R3.jpg")