##importamos las librerias necesarias##
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

##usas una url donde este lista el producto que quieres ver##
my_url = 'https://www.weplay.cl/catalogsearch/result/?q=crash+4'

##leemos y cerramos la pagina con este comando##
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

##aqui tenemos toda la data##
page_soup = soup(page_html,"html.parser")

##buscamos data en especificosi inspeccionamos la pagina podemos encontrar en en httmlcosas que dicen class, entonces como es una pagina de venta yo quiero el nombre y el precio ##
containers = page_soup.findAll("div",{"class":"regular"})



print(len(containers))
##aqui revisas si containers agrego lo que querias esto lo pone en una lista##

print(containers[0])
containe = containers[0]
print(containe.a)
##dentro de container si encontramos a, que nos muestra el nombre del producto y la pagina del producto 0 ##

