# import libraries
import requests, shelve
from bs4 import BeautifulSoup
def getKDA(id):

    quote_page ='https://www.dotabuff.com/players/'+str(id)
    page = requests.get(quote_page,headers = {'User-agent': 'my bot 0.1'})
    page.status_code
    soup = BeautifulSoup( page.content,features="html.parser" )
    kda = soup.find('span' , attrs = {'class':'kda-record'})
    return kda.text
