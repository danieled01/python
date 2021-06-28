#at this point you need to inspect the web page using your browser view-source and start to make a note of how the page comes together and where is the data that you want to pull out which will store in a pandas dataframe later on.

#This is the simple script that will gather the data
import requests
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")

#now we will use the find_all() method and look for the propertyRow class that we discovered when we inspected it using our web browser.  This will return all the divs
all=soup.find_all("div",{"class":"propertyRow"})

#all will now store the divs, which have a class propertyRow assigned to them, in a list.  So what you can do is use the list to iterate through them.  However before we do that we will use the find_all() method and grab some more data out of each item.
all[0].find_all("h4",{"class":"propPrice"})

#once you know that you are able to grab the data that you need you can turn that data into a string and remove unneeded text using string methods such as replace.  The code below is a bit rudementary but its there just to show how we can manipulate the string.
print(str(all[0].find_all("h4",{"class":"propPrice"})).replace('\n','').replace('[<h4 class="propPrice">','').replace('<span class="IconPropertyFavorite16"></span></h4>]','').replace(' ',''))
