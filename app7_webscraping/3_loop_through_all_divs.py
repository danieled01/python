#we now iterate through all the items and get the price

import requests
import re
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

#At this point we are starting to work through the items in the soup list and pulling data out in a way which we can use and iterpret.  The example below does so with a for loop and applies a bunch of replace methods to remove characters from strings which arent needed.

for item in all:
    print(str(item.find("h4",{"class":"propPrice"})).replace('\n','').replace('<h4 class="propPrice">','').replace(' ','').replace('<spanclass="IconPropertyFavorite16"></span></h4>',''))
    name = (str(item.find_all("span",{"class","propAddressCollapse"})).replace('[<span class="propAddressCollapse" title="','').replace('</span>, <span class="propAddressCollapse">','').replace('</span>]',''))
    name = (re.sub(r'.*>', '>', name))
    print(name.replace('>',''))
    try:
        print(str(item.find('span',{'class','infoBed'})).replace('<span class="infoBed"><b>','').replace('</b> Beds','').replace('</span>',''))
    except:
        print('None')
    try:
        print(str(item.find('span',{'class','infoSqFt'})).replace('<span class="infoSqFt"><b>','').replace('</b> Sq. Ft','').replace('</span>',''))
    except:
        print('None')
    try:
        print(str(item.find('span',{'class','infoValueFullBath'})).replace('<span class="infoValueFullBath"><b>','').replace('</b> Full Baths','').replace('</span>',''))
    except:
        print('None')
    try:
        print(str(item.find('span',{'class','infoValueHalfBath'})).replace('<span class="infoValueHalfBath"><b>','').replace('</b> Half Bath','').replace('</span>',''))
    except:
        print('None')
    print('')
