import requests
import webbrowser
import youtube_dl
from pprint import pprint
 
 
def get_daily(url):
    global ydl
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
 
    with ydl:
        result = ydl.extract_info(
        url,
        download=False
        )
 
    if 'entries' in result:
        video = result['entries'][0]
    else:
        video = result
 
    video_url = video['url']
    return video_url
 
 
def scrape(url):
    var = requests.get(url)
    spl = var.text.split("'")
    link = [x for x in spl if x.find("clip") != -1 or x.find("dailymotion") != -1]
 
    link = link[0]
    if "clip" in link:
        var = requests.get(link).text
        spl = var.split('"')
        link_final = [x for x in spl if "mp4" in x][0]
   
    if "daily" in link:
        link_final = get_daily(link)
   
 
    html = f"""<video width="640" height="480" controls>
      <source src="{link_final}" type="video/mp4">
      <source src="{link_final}" type="video/ogg">
    Your browser does not support the video tag.
    </video>
    """
 
    arquivo = open("html.html", "w")
    arquivo.write(html)
    arquivo.close()
 
    webbrowser.open("html.html", new=2)
 
link = input('Seu link: ')
scrape(link)
