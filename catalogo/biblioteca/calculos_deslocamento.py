# calculos_deslocamento
# Caminho: Catálogo > Biblioteca de scripts > calculos_deslocamento
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

import clr 
import re
import datetime
import System.Text


zero = 0

valorRefIntegral = 67.47
valorRefReduzida = 19.28


refeicoes=0
valores = 0

daysOffText = System.Text.StringBuilder()
##RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
    #feriados = 0
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            #feriados += 2
            return True
    return False
def countHolidays(firstDate, lastDate):
    totalHolidays = 0
    currentDay = firstDate
    while currentDay <= lastDate:
        if isHoliday(currentDay):
            totalHolidays += 1
        currentDay = currentDay.AddDays(1)
    return totalHolidays
def workingDays(totalDays, firstDate):
    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff
def countSaturdays(firstDate, lastDate):
    saturdays = 0
    currentDay = firstDate
    while currentDay <= lastDate:
        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
            saturdays += 2
        currentDay = currentDay.AddDays(1)  
        # Avance para o próximo dia
    return saturdays
#FUNCAO PARA O CALCULO DA QUANTIDADE DE REFEICOES
def qtdRefeicoes(dtSaida,dtRetorno,hrSaida,hrRetorno):
    # recebe como parâmetros na sequencia campo data de saída, campo data do retorno, campo hora da saída, campo hora do retorno
    # retorna Array com os indices integral e reduzida
    firstDate = dtSaida
    lastDate = dtRetorno

    totalDays = (lastDate - firstDate).TotalDays
    count = 0

    totalWorkingDays = workingDays(totalDays,firstDate)
    holidaysCount = countHolidays(firstDate, lastDate)
    saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2

    #Quantidade de refeições Reduzias e integrais
    quantRed = totalWorkingDays
    quantInt = saturdays + totalWorkingDays 

    #Atribuindo valor a variável
    saidaHora = hrSaida 
    retornoHora = hrRetorno

    #Split de horário, separando hora de minuto
    hora = saidaHora.Split(':');     
    horaRetorno = retornoHora.Split(':');

    #Atribuindo valor de horário e minuto de acordo com o índice da variável
    horarioSaida = hora[0]
    minutoSaida = hora[1]

    horarioRetorno = horaRetorno[0] 
    minutoRetorno = horaRetorno[1]

    #DIAS UTEIS

    if workingDays(0,firstDate):
        if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
            quantRed = quantRed - 1
        if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
            quantInt = quantInt - 1
    if workingDays(0,lastDate):    
        if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
            quantRed = quantRed - 1
        if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
            quantInt = quantInt - 1
    
    ###############################################################
        
    #SAÍDA FINAIS DE SEMANA E/OU FERIADOS

    if not  workingDays(0,firstDate):
        if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
            quantInt = quantInt - 1
        if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
            quantInt = quantInt - 1
    if not  workingDays(0,lastDate):
        if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
            quantInt = quantInt - 1
        if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
            quantInt = quantInt - 1   
    refeicoes=[{'integral':quantInt,'reduzida':quantRed}]
    return refeicoes

############# calculo valor total

def valorRefeicoes(qtdRefInt, qtdRefRed):
    # retorna Array com os indices integral, reduzida e total
    #qtdRef = qtdRefeicoes(dtSaida, dtRetorno, hrSaida, hrRetorno) 
    refIntegral = qtdRefInt * valorRefIntegral
    refReduzida = qtdRefRed * valorRefReduzida
    valorTotalRefeicoes = refIntegral + refReduzida

    valores=[{'integral':refIntegral,'reduzida':refReduzida,'total':valorTotalRefeicoes}]
    return valores
