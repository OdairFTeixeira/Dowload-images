import requests 
from bs4 import BeautifulSoup

url = input('Digite a URL do site para dowload: ')
class_a = input('Digite a classe das tags <a> que você deseja baixar: ')
count = 0
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

imagens = soup.find_all('a',class_=class_a)

def baixa_imagens(link):
    request = requests.get(link)
    with open(f'{count}img.jpg', 'wb') as f:
        f.write(request.content)

for imagem in imagens:
    print(imagem['href'])
    baixa_imagens(imagem['href'])
    count += 1
