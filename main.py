import os
from dotenv import load_dotenv
import requests
import config.configuracoes as configuracoes
import time
import pandas as pd
from datetime import datetime 
from api.api_consultar_protocolo import consultar_protocolo

load_dotenv()
login = configuracoes.Login()
token = os.getenv("TOKEN_SAFE2PAY")

lerPlanilha = pd.read_excel(login.get_caminho_planilha(), login.get_pagina_planilha(), dtype={'Documento': str, 'Protocolo': str})

lerPlanilha['Protocolo'] = lerPlanilha['Protocolo'].astype(str)

# Aqui crio as colunas vazias
lerPlanilha["VALOR PAGO"] = ""  
lerPlanilha["DATA PAGAMENTO"] = ""
lerPlanilha["STATUS"] = ""

for linha in lerPlanilha.itertuples():
    protocolo = linha.Protocolo

    consulta = consultar_protocolo(protocolo, token)
    try:
        print(f"Nome do Cliente: {consulta['cliente_nome']}")
        print(f"Valor do Boleto: {consulta['valor_boleto']}")
        print(f"Data do Pagamento: {consulta['data_pagamento']}")

        match consulta['status']:
            case 'Pendente':
                print(f"Status do Boleto: {consulta['status']}")
                pendente = login.adicionaPendente()
                lerPlanilha.at[linha.Index, 'VALOR PAGO'] = str(00.00)
            case 'Baixado':
                print(f"Status do Boleto: {consulta['status']}")
                baixado = login.adicionaBaixado()
                lerPlanilha.at[linha.Index, 'VALOR PAGO'] = str(00.00)
            case 'Liberado':
                print(f"Status do Boleto: {consulta['status']}")
                liberado = login.adicionaLiberado()
                lerPlanilha.at[linha.Index, 'VALOR PAGO'] = str(consulta['valor_boleto'])        
            case _:
                print(f"Status do Boleto: {consulta['status']}")
                pago = login.adicionaPago()
                lerPlanilha.at[linha.Index, 'VALOR PAGO'] = str(consulta['valor_boleto'])     
        lerPlanilha.at[linha.Index, 'STATUS'] = consulta['status']
        lerPlanilha.at[linha.Index, 'DATA PAGAMENTO'] = consulta['data_pagamento']             
    except Exception as e:
        print('none')

nome_arquivo = f"Planilha Finalizada {datetime.now().strftime('%d-%m-%Y__%H-%M-%S')}.xlsx"

lerPlanilha.to_excel(nome_arquivo, index=False)

print(login.mostrarDados())


