from bs4 import BeautifulSoup
import requests
import os
url="https://www.pexels.com/search/cars/"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
page=requests.get(url,headers=header)
soup=BeautifulSoup(page.text,'html.parser')
links=[]
images=soup.select('img[src^="https://images.pexels.com/photos/"]')
for image in images:
    links.append(image['src'])
#for l in links:
    #print(l)

os.mkdir("images")
i=1
for index,image_link in enumerate(links):
    if i<=10:
        image_data=requests.get(image_link).content
        with open("images/"+str(index+1)+".jpg",'wb+') as f:
            f.write(image_data)
        i=i+1
    else:
        f.close()
        break
