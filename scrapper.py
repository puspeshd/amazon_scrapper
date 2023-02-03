from bs4 import BeautifulSoup       #for scrappng
import pandas as pd                 #for excel file operations
import requests                     #for opening web pages
                          # for formatting the data
import time
from  fake_useragent import UserAgent

listed=[] 
for i in range(2,21):
 #baseurl="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"
 pageno="page="+str(i)+"&"
 baseurl="https://www.amazon.in/s?k=bags&"+pageno+"crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"+str(i)
 print(baseurl)   
 user_agent = UserAgent()
 time.sleep(2)
 page=requests.get(baseurl,headers={'User-Agent': 'chrome' },allow_redirects=True,timeout=8000) 
 
 soup = BeautifulSoup(page.text, 'html.parser')  
 
                
 for j in range(2,26):
   time.sleep(2)
   purl=''   
   if j==7 or j==4 or j==8 or j==17 or j==18 or j==14 :
        continue
   else:                       
        #will loop here
        tags=''
        title=''
        purl=''
        price=''
        stars=''
        reviews=''
        desc=''
        #asin=''
        proddesc=''
        #manufacturer='' 
        try:
                jj=str(j)
                dict1={'data-index':jj}      
                 
                tags=soup.find("div", attrs=dict1)
          
                #print(tags)
                title=tags.find("h2").text
                
                xxx=tags.find("div", class_="a-row a-size-small")
                stars=xxx.find("span").text
                
                print(stars.encode("utf-8"))
                print(jj)
                reviews=xxx.find("span", class_="a-size-base s-underline-text").text
                
                purl=tags.find("h2")
                purl=purl.find("a")
                purl=purl.get("href")
                purl='https://www.amazon.in'+purl
               
               
                price=tags.find("span", class_="a-offscreen").text
                
                user_agent = UserAgent()
                page1=requests.get(purl,headers={'User-Agent': 'chrome' },allow_redirects=True,timeout=6000)
                
                soup1 = BeautifulSoup(page1.text, 'html.parser')
                
        except:
                continue        
        #try: 
                        #listofdetails=soup1.find("div", attrs={"id":"detailBullets_feature_div"}).text
                        #print(listofdetails)
                        #manufacturer=listofdetails.find("span",string=="Manufacturer")
                       # manufacturer=listofdetails.findNext("li")
                        
                           
                       # manufacturer=manufacturer.findNext("li")
                        #manufacturer=manufacturer.findNext("li")
                       # manufacturer=manufacturer.findNext("li").text
                       # asin=manufacturer.findNext("li").text
                       # print(manufacturer.encode("utf-8"))
                        #asin=asin.match("ASIN")
                       # manufacturer=manufacturer.text
                        #manufacturer=manufacturer.encode("utf-8")
                        #asin=asin.encode("utf-8")
                        #print(manufacturer.encode("utf-8"))
                        #print(asin.encode("utf-8"))
        #except:   
                 
                 #listofdetails=soup1.find("table", attrs={"id":"productDetails_techSpec_section_2"})
                 #manufacturer=listofdetails.find("th",text="Manufacturer :").find_next_sibling("td").gettext
                        #listofdetails=soup1.find("table", attrs={"id":"productDetails_techSpec_section_2"})
                 #asin=listofdetails.find("th",text="ASIN :").find_next_sibling("td").gettext
                        

        try:                
                proddesc=soup1.find("div", attrs={"data-a-expander-name":"aplus-module-expander"})
                proddesc=proddesc.find("div", attrs={"aria-expanded": "false"}).text
                #proddesc=proddesc.encode("utf-8")
                #print(proddesc)
        except:
                pass
        try:        
                desc=soup1.find("div",attrs={"id":"feature-bullets"}).text.strip()
                
        except:
                pass        
                
                

        if(purl!=''):
                        listed.append([purl,title,price,stars,reviews,desc,proddesc])   
                         


df=pd.DataFrame(listed)

head=['url','name','price','rating','reviews','description','product desc']
df.to_csv('Output.csv',index=False,header=head,sep=',')        


