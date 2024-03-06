#Instalar na biblioteca do python, sempre colocar pip install:pandas, openpyxl, twilio
import pandas as pd
from twilio.rest import Client

account_sid = "AC266eafc7aa1e7f63173d1d3ac3df5a35"
auth_token = "620deaed556dc0cf342ca7e83c57d674"

client = Client(account_sid, auth_token)

#Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
  tabela_vendas=pd.read_excel(f'{mes}.xlsx')

  #Para cada arquivo: 
  if (tabela_vendas['Vendas']>55000).any():
    vendedor=tabela_vendas.loc[tabela_vendas['Vendas']>55000, 'Vendedor'].values[0]
    vendas=tabela_vendas.loc[tabela_vendas['Vendas']>55000, 'Vendas'].values[0]
    print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
    message = client.messages.create(

#Enviar mensagem para o número do vendedor
#Verificar se algum valor na coluna "vendas" daquele arquivo é maior que 55k
#Se for maior que 55k -> Enviar um SMS com o nome, o mês e as vendas do vendedor
        body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}',
        from_='+17795480749',
        to='+5511991902782')
    print(message.sid)
