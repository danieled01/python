#If there are multiple pages on the website we will scrape through all of them and grab the data that we need.  We will do this in the script below.  In the previous script we grabbed the base page an grabbed the data out of it in this script we ill build intelligence to get the page range dynamically and crawl through them.
#The trick here is to understand how the url changes as we browse through the pages.  So what we did was find out the baseurl for the first page and then loop through the rest of them.

#By inspecting the web page it was gathered that page 1 had a url of 'http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=0.html', with the 0.html incrementing by 10.  So as a rudementary first step we created a foor loop with a base url of 'http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=' with the 0.html increasing as 10.html, 20.html etc.

import requests
import re
from bs4 import BeautifulSoup
import pandas

l=[]
base_url='http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='

#So now what we have is a loop that loop through the pages using the base url as a starting point and then adds the range in intervals of 10 as the subsequent pages.  This loop grabs the propertyRow class and allows us to extract the data that we need which will be fed into a list of dicts and then into a pandas df.
for item in range(0,30,10):
    r=requests.get(base_url+str(item)+'.html', headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,'html.parser')
    all=soup.find_all("div",{"class":"propertyRow"})

#Within that we have a nested for loop which loops through all of the propertyRow which were gathered in the for loop above.
    for item in all:
        d={}
        name = str(item.find_all("span",{"class","propAddressCollapse"})).replace('[<span class="propAddressCollapse" title="','').replace('</span>, <span class="propAddressCollapse">','').replace('</span>]','')
        name = (re.sub(r'.*>', '>', name))
        d['Name']=name.replace('>','')
        d['Price']=str(item.find("h4",{"class":"propPrice"})).replace('\n','').replace('<h4 class="propPrice">','').replace(' ','').replace('<spanclass="IconPropertyFavorite16"></span></h4>','')
        try:
            d['Beds']=str(item.find('span',{'class','infoBed'})).replace('<span class="infoBed"><b>','').replace('</b> Beds','').replace('</span>','')
        except:
            d['Beds']=None
        try:
            d['Sq Feet']=str(item.find('span',{'class','infoSqFt'})).replace('<span class="infoSqFt"><b>','').replace('</b> Sq. Ft','').replace('</span>','')
        except:
            d['Sq Feet']=None
        try:
            d['Full Baths']=str(item.find('span',{'class','infoValueFullBath'})).replace('<span class="infoValueFullBath"><b>','').replace('</b> Full Baths','').replace('</span>','')
        except:
            d['Full Baths']=None
        try:
            d['Half Baths']=str(item.find('span',{'class','infoValueHalfBath'})).replace('<span class="infoValueHalfBath"><b>','').replace('</b> Half Bath','').replace('</span>','')
        except:
            d['Half Baths']=None

        for column_group in item.find_all('div',{'class':'columnGroup'}):
            for feature_group, feature_name in zip(column_group.find_all('span',{'class':'featureGroup'}),column_group.find_all('span',{'class':'featureName'})):
                if 'Lot Size' in feature_group.text:
                    d['Lot Size']=feature_name.text
                else:
                    pass
        l.append(d)

df=pandas.DataFrame(l)
df.to_csv('output.csv')
