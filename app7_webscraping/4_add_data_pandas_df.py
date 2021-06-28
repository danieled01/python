#we are now at a point where we grab the data and want to append it to a pandas dataframe.  A time efficient way of doing this is to create dictionaries for each key value pair for each item(ie Price $75000, Bedrooms 4 etc).  We then append this to a list.  Once we have a list of dictionaries we import that in pandas and save it as a csv.

import requests
import re
from bs4 import BeautifulSoup
import pandas

r=requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

l=[]

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
