import scrapy


class TataSpider(scrapy.Spider):
    name = 'tata'
    allowed_domains = ['https://www.carone.com.br/iogurte-tata-flocos-1000g']
    start_urls = ['https://www.carone.com.br/iogurte-tata-flocos-1000g']

    def parse(self, response):
        price = response.css('span.price::text').get()
        yield {
            'price': price
        }

'''
import scrapy
import requests
from scrapy import Request as rq
import json

import os
os.chdir('/home/arthur/GitHub/cebola/cebola/')
if not os.path.exists('new_salves'):
    os.makedirs('new_salves')
os.chdir('new_salves')



class AnaSpider(scrapy.Spider):
    name = 'ana'
    allowed_domains = ['www.famosasbrasil.net']
    start_urls = ['http://www.famosasbrasil.net/sexy/']
    
    def parse(self, response):
        url_total = response.url # local da url atual
        print("url_total primeira = %s" % url_total) 
        download = response.request.meta['download_slot'] # local da url de download
        links = response.css('img::attr(src)').getall() # lista de todas as fotos que existem na página
        qntDeImgs = len(links) # quantidade de fotos na página

        src = response.css('h1.titulopost > a::attr(href)').get()  # pega o cabeçalho do primeiro post
        print("SRC === %s" % src)
        qntDePosts = len(src) # costuma ser 10 posts por página

        if url_total == 'http://www.famosasbrasil.net/sexy/':
            for x in response.css('h1.titulopost > a::attr(href)'):
                yield {
                    'path' : 'http://'+download+x.get()
                }
    
        a = 0 # é o que faz mudar o nome da foto
        for y in links:  # y vai percorrer essa lista de imagens da página
            try:
                if not os.path.exists('/home/arthur/GitHub/cebola/cebola/new_salves/'+src): # tentando criar pastas separadas
                    os.makedirs('/home/arthur/GitHub/cebola/cebola/new_salves/'+src)
                    #print("FINAL SRC = %s" src[5])
                with open('/home/arthur/GitHub/cebola/cebola/new_salves/'+src+'imagemANA'+str(a)+'.jpg', 'wb') as f:
                    if not y[0] == 'h' : # tirando umas urls completas
                        f.write(requests.get('http://'+download+y).content) # corrigindo a url
                        f.close()
                        print("foto gravada com sucesso")
            except:
                print("deu algum problema")
                pass
            a = a+1 # atualiza o número

        print("FIM DO LOOP ==============")

        if url_total == 'http://www.famosasbrasil.net/sexy/':
            next_page_url = 'http://'+download+src
            print("NEXT_PAGE_URL === %s" %next_page_url)
            yield scrapy.Request(response.urljoin(next_page_url))
        else:
            url_total = url_total[:-len(src):] # encurta a url_total
            
            #new_response = response.replace(url='http://www.famosasbrasil.net/sexy/')

            #next_page_url = new_response.css('h1.titulopost > a::attr(href)').get()
            print("NEXT_PAGE_URL === %s" %next_page_url)
            yield scrapy.Request(response.urljoin(next_page_url))

'''
'''
import json
import os

print ("START")

# credentials to login to twitter api

try:
    os.system("echo OS START")
    os.system("rm /home/arthur/GitHub/cebola/cebola/new_salves/output.json")
    os.system("cd /home/arthur/GitHub/cebola/cebola/ && scrapy crawl ana -o output.json")
    os.system("echo OS END")
except:
    os.system("deu pau")
    pass

with open('/home/arthur/GitHub/cebola/cebola/new_salves/output.json') as f:
    data = json.load(f)
f.close
# conversion json -> float
path = data[0].get("path")
print(path)




'''