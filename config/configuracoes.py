import pandas as pd

class Login:
    def __init__(self) -> None:
        self._caminhoPlanilha = 'C:\\Users\\Pessoal\\Desktop\\Emissões Video Agosto.xlsx'
        self._paginaPlanilha = 'Plan1'
        self.pago = 0
        self.liberado = 0
        self.baixado = 0
        self.pendente = 0
    
    def get_caminho_planilha(self):
        return self._caminhoPlanilha
    
    def get_pagina_planilha(self):
        return self._paginaPlanilha
    
    def adicionaPago(self):
        self.pago += 1
    def adicionaLiberado(self):
        self.liberado += 1
    def adicionaBaixado(self):
        self.baixado += 1
    def adicionaPendente(self):
        self.pendente += 1
    
    def mostrarDados(self):
        return(f'''
            DADOS:
            {self.pago} - Boletos pagos 🟢
            {self.liberado} - Boletos liberados 🔵
            {self.baixado} - Boletos baixados 🔴
            {self.pendente} - Boletos pendentes ⚪
            '''
        )
    
lerPlanilha = pd.read_excel(Login().get_caminho_planilha(), Login().get_pagina_planilha())
