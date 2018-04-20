from urllib import request
Google_link = "http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv"


def file_downloader(url):
    response = request.urlopen(url)
    ft = response.read()
    fr = str(ft)
    lines = fr.split("\\n")
    fx = open(r"goog.csv" , 'w')
    for line in lines:
            fx.write(line + "\n")
    fx.close()


file_downloader(Google_link)
