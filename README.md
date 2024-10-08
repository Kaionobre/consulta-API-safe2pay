﻿# Projeto de RPA - Consulta e Liberação de Boletos via API

Este projeto foi desenvolvido para automatizar o processo de consulta e liberação de boletos através de uma integração com a API da Safe2Pay. Utilizando bibliotecas como **Requests** e **Pandas**, foi possível economizar horas de trabalho, processando em média 80 requisições a cada 5 minutos.

Algumas informações sensíveis, como credenciais de login e a chave da API, foram removidas ou alteradas para garantir a segurança dos dados da empresa **Certsempre** e de seus clientes.

## Tecnologias Utilizadas

- **Pandas**: Para leitura e manipulação dos dados da planilha.
- **Requests**: Para realizar as consultas via API.
- **Orientação a Objetos (OO)**: Utilizada para encapsular dados sensíveis, como senhas e tokens, garantindo a segurança das informações.

## Funcionalidades

1. **Leitura da Planilha**: O sistema lê uma planilha Excel contendo informações de clientes e boletos a serem consultados.
2. **Consulta de Boletos**: Para cada protocolo listado na planilha, o sistema faz uma requisição à API Safe2Pay para verificar o status do boleto.
3. **Atualização da Planilha**: A planilha é atualizada com informações de pagamento, data de pagamento e o status atual do boleto.
4. **Liberação de Boletos**: O sistema também permite a liberação de boletos diretamente via API, conforme necessário.
5. **Logs e Relatórios**: Após a execução, o sistema gera logs com o número de boletos pagos, liberados, baixados e pendentes.

## Segurança

Neste projeto, foram tomadas medidas de segurança para proteger informações sensíveis:

- **Credenciais e Chaves de API**: As senhas, tokens e chaves de API foram movidas para variáveis privadas e não estão expostas no código principal.
- **Omissão de Dados**: Informações sensíveis relacionadas a clientes e à empresa **Certsempre** foram removidas para garantir a privacidade e a segurança dos dados.

## Fluxo do Processo

1. O sistema lê a planilha e inicia a consulta dos boletos via API Safe2Pay.
2. Para cada boleto, o status e os dados de pagamento são retornados e processados.
3. Caso o boleto esteja pendente, baixado, liberado ou pago, as colunas correspondentes da planilha são atualizadas.
4. Ao final, é gerado um resumo com a quantidade de boletos processados, pagos, liberados, baixados e pendentes.
