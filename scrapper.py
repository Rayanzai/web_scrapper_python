from bs4 import BeautifulSoup
import requests

#Recebe o conteudo da requisição http do site
site = requests.get("https://www.climatempo.com.br/").content
#Baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

#transforma o html em STR e printa o html
print(soup.prettify())


#print(soup.title.string)
#print(soup.a)
#print(soup.p.string)
#print(soup.find('admin'))


