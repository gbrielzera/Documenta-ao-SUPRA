# obterosclienteteste
# Caminho: Catálogo > Biblioteca de scripts > obterosclienteteste
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

import clr
from System import *
from System.Text import StringBuilder
clr.AddReference("Supravizio.Custom")


from Newtonsoft.Json import JsonConvert
from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
 
def geraLicitacao():
    try:
        novaOS = OrdemServico.Nova(OrdemServico.Carrega("Numero", 1), "ROTINAAVALIACAO", "TESTEROTINAPEDROX", "Abertura Automática", Servico.Carrega(1299), Pessoa.Carrega(5), Pessoa.Carrega(5))
        novaOS.Salva()
        
        
        json_data = JsonConvert.SerializeObject([novaOS.Numero.ToString()])
        return json_data
    except Exception as e:
        Utils.LogError("Erro ao realizar chamada: "+ e.Message, 'a')
