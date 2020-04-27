import bs4
from urllib.request import urlopen as ureq
import urllib
from bs4 import BeautifulSoup as soup
user1=input("Make Folder Name as 'database' and if Yes then Press y : ")
user2=input("Make another folder inside database folder as 'images' and if Yes then Press y : ")
if(user1=='y'and user2=='y'):
    my_url='https://www.imdb.com/list/ls099318569/'
    #opening csv file for database
    filename="database/database.csv"
    f=open(filename,"w")
    #headers
    headers="Image_Location,Celebrity_Name,Profession,Personality traits\n"
    f.write(headers)
    #openeing up connection,grabbing the page
    uclint=ureq(my_url)
    page_html=uclint.read()
    uclint.close()
    #html parser
    page_soup=soup(page_html,"html.parser")
    #find the all div with class lister list detail sub-list in the page
    #grab each celebrity name
    containers=page_soup.findAll("div",{"class":"lister-item mode-detail"})
    print("\n")
    print(str(len(containers))+" Records found and Stored in database.csv File")
    #grabing only images of actors
    imgs=page_soup.find_all("div",{"class":"lister-item-image"})
    links=[]
    for imge in imgs:
        link=imge.a.img.get('src')
        if 'https://' not in link:
            link=url+link
        links.append(link)
    print('\nImages Detected: '+str(len(links)))
    print("Wait...")
    # variable for link number
    img_no=0
    #grabing only the information from lister-item-content
    for container in containers:
        #actor names
        content = container.find('div', attrs={'class': 'lister-item-content'})
        Actor_name = content.a.text.strip()
        #profession
        #removing span tag 
        if container.find('p'):
            profession=container.p.text.strip().split()
            pr=profession[0]
        else:
            #if data is not available on website
            pr="Not Specified"
        #grabbing personality traits
        if container.find('p') and container.p.next_sibling.next_sibling!=None:
            personality_traits=container.p.next_sibling.next_sibling
            person=personality_traits.text.strip()
        else:
            #if data is not available on website
            person="Not Specified"
        #saving image with the name of actor
        image_name=Actor_name+".png"
        filename="database/images/"+image_name
        urllib.request.urlretrieve(links[img_no],filename)
        #writing information into database.csv file
        f.write(filename+","+Actor_name+","+pr+","+person+"\n")
        img_no+=1
    f.close()
    print("Images are stored in images folder inside the database folder")
    print("Records are stored in database.csv file inside the database folder")
else:
    print("Make database folder and images folder inside the database folder to store the database")
    
    
    

