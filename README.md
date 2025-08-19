# 🤖 RPA - Consulta de Pagamentos Safe2Pay

Este projeto é um **RPA orientado a API** que automatiza a consulta de pagamentos de clientes da Certsempre.  
Com base em uma planilha de protocolos, o sistema consulta a **API Safe2Pay**, extrai informações financeiras e gera uma nova planilha já preenchida, reduzindo drasticamente o tempo gasto em comparação ao processo manual.

---

## 📌 Problema
Antes da automação, o processo era **manual**:  
1. Acessar o sistema da Safe2Pay  
2. Copiar o protocolo da planilha  
3. Pesquisar o protocolo no sistema  
4. Copiar **valor**, **status** e **data de pagamento**  
5. Colar na planilha  
6. Repetir para cada cliente  

⏳ Esse fluxo levava **2 minuto por linha**, resultando em **horas de trabalho para planilhas grandes**.

---

## 🚀 Solução
Com a automação:  
- Para cada protocolo da planilha, o sistema consulta a **API Safe2Pay** (via `requests`).  
- Do **JSON de resposta**, o robô extrai automaticamente:  
  - Valor do boleto  
  - Status do boleto  
  - Data do pagamento  
- Esses dados são preenchidos diretamente em uma nova planilha Excel, organizada com as colunas:  

| VALOR PAGO | STATUS   | DATA PAGAMENTO |
|------------|----------|----------------|

---

## 📈 Benefícios
- **Automação total** do processo manual  
- **Redução de tempo de horas para segundos**  
- **Cada consulta leva menos de 1 segundo** (contra 2 minutos manuais)  
- **Eficiência > 6000%** em planilhas médias e grandes  
- **Precisão nos dados**, sem risco de erro humano  

Exemplo:  
- Planilha com **100 linhas** →  
  - **Manual:** ~100 minutos  
  - **Automatizado:** ~2 minutos

---

## ⚙️ Tecnologias Utilizadas
- **Python 3.10**
- **Pandas** (manipulação de planilhas)
- **Requests** (integração com API Safe2Pay)
- **Dotenv** (armazenamento seguro do token)

