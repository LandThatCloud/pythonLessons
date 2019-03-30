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

file_name = "products.csv"
f = open(file_name,"w")

headers = "brand, product_name, shipping_details\n"

f.write(headers)

brands = page_soup.find_all("div", {"class": "item-info"})
for container in containers:
    #brand
    brand = brands[0].div.a.img["title"]

    #title containers
    title_containers = page_soup.findAll("a", {"class":"item-title"})
    product_name = title_containers[0].text

    #shipping
    shipping_details = page_soup.findAll("li", {"class":"price-ship"})
    shipping = shipping_details[0].text.strip()

    print("Brand:" + brand)
    print("Product: "+ product_name)
    print("Shipping:"+ shipping)
    f.write(brand + "," + product_name.replace(",","|") + "," + shipping +"\n")

f.close()