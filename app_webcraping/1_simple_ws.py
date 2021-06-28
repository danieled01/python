#In order to webscrape the web for data we must load webpages and grab the contents out of them.

#we do this via the requests and beatifulsoup (bs4) libraries
import requests
from bs4 import BeautifulSoup

#requests.get grabs the web page and stores is as a variable - the headers impersonates a web browser which makes the script more effective
r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
#we map the contents of r to another variable which allows us to view it
c=r.content

#BeautifulSoup allows us to parse the contents
parsed_text=BeautifulSoup(c,"html.parser")

#we now start diving into the html code and start to grab data
cities=parsed_text.find_all("div",{"class":"cities"})
cities_first=parsed_text.find_all("div",{"class":"cities"})[0]

#to grab just the h2 tags from dic class and strips all of the unrequired data
h2_tags=cities[0].find_all("h2")[0].text
print(h2_tags)

#to loop through all of the h2 h2_tags
for item in cities:
    print(item.find_all("h2")[0].text)

#This is for the paragrap h2_tags
for item in cities:
    print(item.find_all("p")[0].text)
