from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48'

#opening page
uClient = uReq(myurl)
page_html=uClient.read()

uClient.close()

#soup
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"})