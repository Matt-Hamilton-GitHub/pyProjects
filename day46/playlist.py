from bs4 import BeautifulSoup
import requests
url = 'https://www.billboard.com/charts/hot-100/'

def top_songs():
    date = input('Date (YYYY-MM-DD): ')
    url = f'https://www.billboard.com/charts/hot-100/{date}/'

    try:
        f = open(f"{date}.txt", 'x')
    except:
        f = open(f"{date}", 'w')
    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    scrap_titles = soup.select(selector='li ul li h3', class_='a-font-primary-bold-s', id='title-of-a-story')
    # singers = scrap_lists.select(selector='span', class_='c-label')
    scrap_singers = soup.select(selector='li ul li span',class_='c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')
    # print(scrap_singers)
    
    titles = [t.getText() for t in scrap_titles]
    singers = [t.getText() for t in scrap_singers]
    print(singers)
    
    title_arr = []
    singers_arr = []

    tmr = 100
    for t in titles:
        title = ""
        for txt in t:
            if txt.isalpha() or txt==' '  :
                title += txt
        if tmr > 0:
            # f.write(title + '\n')
            title_arr.append(title)
        tmr-=1

  
    for t in singers:
        title = ""
        for txt in t:
            if txt.isalpha() or txt==' ' :
                title += txt
        if len(title) > 0:
            # f.write(title + '\n')
            singers_arr.append(title)
       
    print( title_arr)
    print( singers_arr)
    for i in range(0,100):
        f.write(f"{singers_arr[i]}: {title_arr[i]} \n")
          

    

top_songs()