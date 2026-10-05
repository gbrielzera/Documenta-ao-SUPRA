# validaCNPJ
# Caminho: Catálogo > Biblioteca de scripts > validaCNPJ
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (3 variantes entre os XMLs; esta é a mais recente)

def valor_char(c):

    #Converte caractere alfanumérico em valor numérico.


    if c.isdigit():
        return int(c)
    return ord(c.upper()) - 48 
    


def validaCNPJ(valor):
    if String.IsNullOrEmpty(valor.ToString()):
        return 'Nulo'
    
    valor = str(valor).strip()
    
    # CNPJ alfanumérico deve ter 14 posições
    if len(valor) != 14:
        return valor
    
    cnpj = list(valor)
    
    # -------------------
    # Primeiro DV
    # -------------------
    pesos1 = [5,4,3,2,9,8,7,6,5,4,3,2]

    soma = 0
    for i in range(12):
        soma += valor_char(cnpj[i]) * pesos1[i]
    
    resto = soma % 11

    dv1 = 0 if resto < 2 else 11 - resto
    
    if dv1 != valor_char(cnpj[12]):
        return valor
    # -------------------7
    # Segundo DV
    # -------------------
    pesos2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]

    soma = 0
    for i in range(12):
        soma += valor_char(cnpj[i]) * pesos2[i]

    soma += dv1 * pesos2[12]

    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto

    if dv2 != valor_char(cnpj[13]):
        return valor

    return 'ok'

#def validaCNPJ(valor):
#    if String.IsNullOrEmpty(valor.ToString()):
#        return 'Nulo'
#
#    if len(valor) != 14 : 
#        return valor
#    algarismos = [5,4,3,2,9,8,7,6,5,4,3,2]
#    cnpj = list(valor)
#    # Calculo do primeiro DV - 03.662.630/0001-10
#    d1 = algarismos[0] * int(cnpj[0]) # 5 * 0 = 0
#    d2 = algarismos[1] * int(cnpj[1]) # 4 * 3 = 12
#    d3 = algarismos[2] * int(cnpj[2]) # 3 * 6 = 18
#    d4 = algarismos[3] * int(cnpj[3]) # 2 * 6 = 12
#    d5 = algarismos[4] * int(cnpj[4]) # 9 * 2 = 18
#    d6 = algarismos[5] * int(cnpj[5])
#    d7 = algarismos[6] * int(cnpj[6])
#    d8 = algarismos[7] * int(cnpj[7])
#    d9 = algarismos[8] * int(cnpj[8])
#    d10 = algarismos[9] * int(cnpj[9])
#    d11 = algarismos[10] * int(cnpj[10])
#    d12 = algarismos[11] * int(cnpj[11])
#    dv1 = 0
#    dv2 = 0
#    soma = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12
#    # modulo 11
#    restoDiv = soma % 11
#    if restoDiv > 1:
#       dv1 = 11 - restoDiv
#    
#    if dv1 != int(cnpj[12]):
#        #r = "dv1:" + dv1.ToString() + " e " + cnpj[12].ToString()
#        #return r
#        return valor
#    
#    
#    # Calculo do segundo DV
#    algarismos = [6,5,4,3,2,9,8,7,6,5,4,3,2]
#    d1 = algarismos[0] * int(cnpj[0])
#    d2 = algarismos[1] * int(cnpj[1])
#    d3 = algarismos[2] * int(cnpj[2])
#    d4 = algarismos[3] * int(cnpj[3])
#    d5 = algarismos[4] * int(cnpj[4])
#    d6 = algarismos[5] * int(cnpj[5])
#    d7 = algarismos[6] * int(cnpj[6])
#    d8 = algarismos[7] * int(cnpj[7])
#    d9 = algarismos[8] * int(cnpj[8])
#    d10 = algarismos[9] * int(cnpj[9])
#    d11 = algarismos[10] * int(cnpj[10])
#    d12 = algarismos[11] * int(cnpj[11])
#    dv1 = algarismos[12] * dv1
#    soma = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12+dv1
#    # modulo 11
#    restoDiv = soma % 11
#    if restoDiv > 1:
#       dv2 = 11 - restoDiv    
#    
#    if dv2 != int(cnpj[13]):
#        #r = "dv2:" + dv2.ToString() + " e " + cnpj[13].ToString()
#        #return r
#        return valor
#       
#    return 'ok'
