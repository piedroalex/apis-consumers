# CONSUMINDO UMA API REST
import requests
from datetime import date

def consulta():
    response = requests.get('https://covid19-brazil-api.now.sh/api/report/v1')
    print('-------------------------------- INFORMAÇÕES DA COVID-19 NO BRASIL --------------------------------')
    print('DATA:', date.today().strftime('%d/%m/%Y'))
    print('---------------------------------------------------------------------------------------------------')
    dados = response.json();
    for info in dados['data']:
        print('UF:', info['state'], ', CONFIRMADOS:', info['cases'], ', MORTOS:', info['deaths'], ', SUSPEITOS:', info['suspects'])
    print('---------------------------------------------------------------------------------------------------')

consulta()