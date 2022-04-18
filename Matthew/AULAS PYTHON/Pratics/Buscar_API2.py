import requests
import json
from requests.models import HTTPBasicAuth

                                #     GET
# nome = requests.get('https://teste-67f75-default-rtdb.firebaseio.com/.json')
# nomeJson = nome.json()
# print(nome.json())

                                    #  POST
token = '49695f1e5a1b0b84807f53b376061783'   
key = '0e317f2998c09bd3b093e05167e8b4da'
url_site = "https://www.minaristore.com.br/api/categorias/buscar/todos"


requisicao = requests.post(url=url_site,auth=HTTPBasicAuth(token,key))
res = requisicao.json()
print(res)

        


        


                                         #   PATCH
# informacao = '{"Nome": "Beatriz", "Sobrenome": "Santos", "idade": "20"}'
# mudanca = requests.patch('https://teste-67f75-default-rtdb.firebaseio.com/-Mn6FggheX8G27sz6aQu.json',data=informacao)
# mudaca = mudanca.json()
# print(mudanca)

                                #  DELETE

# mudanca = requests.delete('https://teste-67f75-default-rtdb.firebaseio.com/3.json')
# print(mudanca)
 

        # como especificar a informação que quero pegar
# cotacao_dolar = nome['USDBRL'] ['bid']
