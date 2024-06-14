from bs4 import BeautifulSoup
import requests

# with open("website.html", encoding='UTF8') as file:
#     contents = file.read()

#BeatifulSoup(content, parser), can be lxml -> 'lxml' 
# requres installing lxml library

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)

# a_tags = soup.find_all(name='a')

# for tag in a_tags:
#     print(tag.get('href'))
#     print(tag.getText())

# header = soup.find(name='h3', class_='heading')
# # for nested elements: a inside p
# company_url = soup.select(selector='p a')


#Live Website
# res = requests.get('https://news.ycombinator.com/news')
# yc_web_page = res.text
# soup = BeautifulSoup(yc_web_page, 'html.parser')
# scrap = soup.find_all(name='span', class_='titleline')
# # scrap = soup.find_all(name='span', class_='titleline')

    

# data = [[s.text] for s in scrap]
# links = [c.find(name='a').get('href') for c in scrap]
# points = [int(p.text.split()[0]) for p in soup.find_all(name='span', class_='score')]


# for i in range(len(data) - 1):
#     data[i].append(links[i])
#     data[i].append(points[i])
# print(data)

# sorted_data = data.sort(key=lambda data: data[2] )
# print(sorted_data)


#TOP MOVIES

res = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2')

soup = BeautifulSoup(res.text, 'html.parser')


all_movies = [t.text for t in soup.find_all('h3', class_='title')]
all_movies = all_movies[::-1]
with open('movies.txt','w',encoding='UTF8') as file:

    for m in all_movies:
        file.write(m + '\n')
  

file.close()
