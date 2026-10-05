# validarTamCampo
# Caminho: Catálogo > Biblioteca de scripts > validarTamCampo
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def validarTamCampo(valor, tam, int, dec):

#valor: valor a ser validado
#tam: quantidade de caracteres de campos alfanuméricos
#int: quantidade de caracteres de campos numéricos casa inteiro 
#dec: quantidade de caracteres de campos numéricos casa Decimais

#Se utilizar o campo tam, atribuir 0 (Zero) aos campos int e dec

#Se utilizar o campo int ou dec, atribuir 0 (Zero) aos campos tam 

#função utilizada no fluxo - Contas de Serviços Concessionários para Pagamento - CSC

    resultado = 'Ok'
    
    #validar tamanho de campos alfanuméricos ou inteiro
    if tam > 0:
        if len(valor) > tam :
                resultado = 'Erro'
                
    #validar tamanho de campos numéricos
    else:
        if valor.find(',') > 0:
            numero = valor.split(',')
            if len(numero[0]) > int :
                resultado = 'Erro'
                
            if len(numero[1]) > dec :
                resultado = 'Erro'
    
    return resultado
