import requests
from datetime import datetime 


def consultar_protocolo(protocolo, token):
    url = f"https://api.safe2pay.com.br/v2/transaction/Reference?reference={protocolo}"

    headers = {
        'x-api-key': token
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

            return {
                "cliente_nome": cliente_nome,
                "valor_boleto": valor_boleto,
                "status": status,
                "data_pagamento": data_padrao
            }
    else:
        return f"Falha ao consultar Boleto para o protocolo {protocolo}. Detalhes:", response.text