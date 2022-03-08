import requests
import datetime

site = 'https://curso-jhon-django.herokuapp.com/'
resposta = requests.get(site)
if resposta.status_code == 200:
    print(f'Horário da requisição retornada foi: {datetime.datetime.today()}')
else:
    print('Requisição não concluida, o site está fora do ar!')

"Linhas 1 e 2 = foram importada as bibliotecas Requests e Datetime"
"Linha 4 = É apresentada o site que irá retornar os dados"
"Linha 5 = Recebe a resposta e armazena em sua variável"
"Linha 6 = Se a resposta retornar 200 é a resposta de status de sucesso que indica que a requisição foi bem sucedida"
"Linha 7 = Imprimirá na tela a hora da requisição através da biblioteca datetime que contém o today que detalha a hora"
"Linha 8 = Qualquer erro diferente do status 200 irá retornar que o site está fora do ar"
