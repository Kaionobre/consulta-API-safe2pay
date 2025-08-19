import os
from dotenv import load_dotenv
import requests
import configuracoes
import pandas as pd
from datetime import datetime 

load_dotenv()
login = configuracoes.Login()
token = os.getenv("TOKEN_SAFE2PAY")

lerPlanilha = pd.read_excel(login.get_caminho_planilha(), login.get_pagina_planilha(), dtype={'Documento': str, 'Protocolo': str})

lerPlanilha['Protocolo'] = lerPlanilha['Protocolo'].astype(str)

# Aqui crio as colunas vazias
lerPlanilha["VALOR PAGO"] = ""  
lerPlanilha["DATA PAGAMENTO"] = ""
lerPlanilha["STATUS"] = ""
lerPlanilha["RESULTADO"] = ""

for linha in lerPlanilha.itertuples():
    protocolo = linha.Protocolo

    url = f"https://api.safe2pay.com.br/v2/transaction/Reference?reference={protocolo}"

    headers = {
        'X-API-KEY': token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200 and not response.json().get('HasError'):
        json_data = response.json()

        if "ResponseDetail" in json_data and "Objects" in json_data["ResponseDetail"] and json_data["ResponseDetail"]["TotalItems"] > 0:
            transaction_data = json_data["ResponseDetail"]["Objects"][0]

            cliente_nome = transaction_data["Customer"]["Name"]
            valor_boleto = transaction_data["Amount"]
            status = transaction_data.get("Message", "N/A")
            data_pagamento = transaction_data.get("PaymentDate", "N/A")

            if data_pagamento != "N/A":
                data_padrao = datetime.strptime(data_pagamento, "%Y-%m-%d").strftime("%d/%m/%Y")
            else:
                data_padrao = "N/A"

            print("Nome do Cliente:", cliente_nome)
            print(f"Valor do Boleto: {valor_boleto:.2f}")
            print("Data do Pagamento:", data_padrao)
            print("Status do Boleto:", status)

            if status == 'Pendente':
                print("Boleto Pendente 🔘")
                pendente = login.adicionaPendente()
                lerPlanilha[linha.Index, 'VALOR PAGO'] = str(00.00)
            elif status == 'Baixado':
                print("Boleto Baixado 🔴")
                baixado = login.adicionaBaixado()
                lerPlanilha.at[linha.Index, 'VALOR PAGO'] = str(00.00)
            elif status == 'Liberado':
                print("Boleto Liberado 🔵")
                liberado = login.adicionaLiberado()
                lerPlanilha.at[linha.Index, 'VALOR PAGO'] = str(valor_boleto)
            else:
                print("Boleto pago com sucesso 🟢")
                pago = login.adicionaPago()
                lerPlanilha.at[linha.Index, 'VALOR PAGO'] = str(f'{valor_boleto:.2f}')

            lerPlanilha.at[linha.Index, 'DATA PAGAMENTO'] = data_padrao
            lerPlanilha.at[linha.Index, 'STATUS'] = status
    else:
        print(f"Falha ao consultar Boleto para o protocolo {protocolo}. Detalhes:", response.text)

nome_arquivo = f"Planilha Finalizada {datetime.now().strftime('%d-%m-%Y__%H-%M-%S')}.xlsx"

lerPlanilha.to_excel(nome_arquivo, index=False)
print(login.mostrarDados())


