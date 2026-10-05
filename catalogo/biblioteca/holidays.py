# holidays
# Caminho: Catálogo > Biblioteca de scripts > holidays
# Fonte: Financeiro_-_Serviços_Gerais_Versão_38_Comprovantes_de_Valores_Pagos_a_Fornecedores Gabriel.xml

def isHoliday(day):
    holidays = DB.ExecuteDataTable("select data from feriado ")
    for holiday in holidays.rows:
        if day == holiday["data"].date:
            return True
    return False
