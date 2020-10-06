# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["tittle", "link", "date"])   
    for article in articles:       
#       print(article.find("a").get_text())
#       title = article.find("a").get_text()
#       print(title)
#       href = article.find("a").attrs['href']
#       print(href)
#       date = article.find("time").attrs['datetime']
#       print(date)
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
        print(title, url, date)
    

