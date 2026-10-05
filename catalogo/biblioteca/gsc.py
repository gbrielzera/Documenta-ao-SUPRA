# gsc
# Caminho: Catálogo > Biblioteca de scripts > gsc
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
import System

clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

clr.AddReference("System.Data")
from System.Data import DataSet 
clr.AddReference("Newtonsoft.Json")
from Newtonsoft.Json import * 
from System.Text import StringBuilder
from System.Web import *

from System import Convert

from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa


from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import JArray, JValue

def enviaDadosItens():
    try:
        # ExecuteReader retorna um conjunto de resultados
        result_table2 = DB.ExecuteDataTable("SELECT segment1 || ' - ' || segment2 || ' - ' || description as produto FROM mtl_system_items_b WHERE organization_id = '88' AND enabled_flag = 'Y'")

        json_data = JsonConvert.SerializeObject(result_table2)
        return json_data

        # Serializar a lista de pessoas para JSON
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
