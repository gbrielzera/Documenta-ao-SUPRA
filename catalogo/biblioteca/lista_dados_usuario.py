# lista_dados_usuario
# Caminho: Catálogo > Biblioteca de scripts > lista_dados_usuario
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

###PRONTO PARA API RH BBTS
import System
import clr
from System import *
clr.AddReference("System.Data")
from System.Data import DataSet 
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
from Newtonsoft.Json import * 
from Newtonsoft.Json.Linq import *
from System.Net.Http import *
from System.Net.Http.Headers import *
import re
 
def listaInformacoesUsuario(usuario):
# recebe como parâmetro o nome do funcionário
# retorna as informações MATRICULA,NOME,E_MAIL,ANIVERSARIO,CPF,MATRICULA_SUPERIOR,NOME_SUPERIOR,E_MAIL_SUPERIOR,TIPO,FUNCAO,CARGO,UOR,ESTABELECIMENTO,LOCAL
# para usar as informações do retorno deve usar uma variavel e apos o . seguido do atributo do retorno.
# exemplo de uso >>>func = listaInformacoesUsuario(leonam silva lima)
#                >>>OrdemServico.DescricaoDetalhada = func.MATRICULA.ToString()
    o='nada'
    link = 'http://10.213.0.74:8089/bbts/pessoa/hr/v1/nome/'+usuario

    c = HttpClient()
    c.Timeout = TimeSpan(0,0,15,0,0)
    c.DefaultRequestHeaders.Accept.Clear()
    c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
    response =  c.GetAsync(link)
    response.Wait()
    resultAsync =  response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result
    if result != None:
      o  = JsonConvert.DeserializeObject(result);
    return o["pessoa"][0]
