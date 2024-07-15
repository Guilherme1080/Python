class NF:
    def __init__(self,numero,tipo,serie,cnpj,razao_social,data,valor,icms,frete,ipi,valor_total):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor = valor
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor2 = valor_total

    def obter_Numero(self):
        return self.numero
    
    def obter_DataEmissao(self):
        return self.data
    
    def alterar_RazaoSocial(self,nova_razao_social):
        self.razao_social = nova_razao_social
        return self.razao_social
    
    def calcular_Valor_Total(self):
        valor_total = self.valor + self.frete + self.icms + self.ipi
        self.valor2 = valor_total
        return self.valor2
    
nota_fiscal = NF(1,"saída",1,"123456","145252000/09","Empresa Abobrinha","28-06-2024",1000,180,50,20)
print(f"Número da NF: {nota_fiscal.obter_Numero()}")
print(f"Data: {nota_fiscal.obter_DataEmissao()}")
print(f"Razão Social inicial: {nota_fiscal.razao_social}")
nota_fiscal.alterar_RazaoSocial('963852741')
print(f"Razão Social depois da alteração: {nota_fiscal.razao_social}")