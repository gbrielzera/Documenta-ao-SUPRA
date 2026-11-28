# gsc
# Caminho: Catálogo > Biblioteca de scripts > gsc
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml (2 variantes entre os XMLs; esta é a mais recente)

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
        
        
        
        
def useToken():
    return "TESTE_JEFF_999999"
