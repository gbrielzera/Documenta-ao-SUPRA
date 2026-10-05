# gscCont
# Caminho: Catálogo > Biblioteca de scripts > gscCont
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

import clr
import System
clr.AddReference("System.Data")
from System.Data import DataSet 
clr.AddReference("Newtonsoft.Json")
from Newtonsoft.Json import * 
from System.Text import StringBuilder
from System.Web import *

from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import JArray, JValue

from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
from System import Convert
        



def aberturaApiAvaliacao():
    try:
            
        import datetime
        import System

        novaOS = OrdemServico.Nova(OrdemServico.Carrega('Numero', 766), "AVALIACAOAPIABERT", "ABRIRAPIAVALIACAOFORNE", "Avaliação de Fornecedores - Trimestral API", Servico.Carrega(1749), Pessoa.Carrega(26902), Pessoa.Carrega(26902))
        

        novaOS.AdicionaComentario('Abertura API', True)
        
        novaOS.Salva()

        avancou = novaOS.AvancaAtividade()
        

        if avancou:
            novaOS.Salva()
            return JsonConvert.SerializeObject(meuObjeto) + ' Numero da OS: ' + str(novaOS.Numero) + ' (Atividade Avançada com Sucesso)'
        else:
            # Se não avançou, salve mesmo assim e retorne um aviso
            novaOS.Salva()
            return JsonConvert.SerializeObject(meuObjeto) + ' Numero da OS: ' + str(novaOS.Numero) + ' (AVISO: A OS foi criada mas a atividade NAO avancou. Verifique as condicoes de saida do fluxo.)'
        
        
        return JsonConvert.SerializeObject(meuObjeto) + ' Numero da OS: ' + str(novaOS.Numero)
    except Exception as e:
        import System # Garante que System está importado aqui também
        # Monta uma mensagem de erro mais completa
        erro_detalhado = "Erro na API: " + str(e) + System.Environment.NewLine
        erro_detalhado += "Tipo da Exceção: " + str(type(e)) + System.Environment.NewLine
        
        # Se for uma exceção do .NET, ela pode ter uma InnerException com mais detalhes
        if hasattr(e, 'InnerException') and e.InnerException is not None:
            erro_detalhado += "Inner Exception: " + str(e.InnerException)
            
        return erro_detalhado
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
