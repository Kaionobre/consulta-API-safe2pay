import requests
import Login

login = Login.Login()
token = login.get_token()

id_transacao = '00000000' #apenas o código do boleto

url = f"https://api.safe2pay.com.br/v2/BankSlip/ReleaseBankSlip?idTransaction={id_transacao}"

headers = {'x-api-key': token}

response = requests.get(url, headers=headers)

if response.status_code == 200 and response.json().get('HasError') is False:
    print("Boleto liberado com sucesso ✅")
else:
    print("Falha ao liberar o boleto. Detalhes:", response.text)

