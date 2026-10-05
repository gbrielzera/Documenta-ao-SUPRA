# apiDados
# Caminho: Catálogo > Biblioteca de scripts > apiDados
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
import System
clr.AddReference("System.Data")
from System.Data import DataSet 
clr.AddReference("Newtonsoft.Json")
from Newtonsoft.Json import * 
from System.Text import StringBuilder
from System.Web import *

from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
        

def enviaDadosDiv():
    try:
        uors = [];
        
#       ExecuteReader retorna um conjunto de resultados
        result_table2 = DB.ExecuteDataTable("SELECT DISTINCT f.organizacao, f.numero_subcr_nivel1, f.descricao_subcr_nivel1, c.scr_sigla FROM CAD_FUNCIONARIO_V F INNER join cob_gl_centro c on c.scr = f.numero_subcr_nivel1")
        
        for row in result_table2.Rows:
            uor = {
                "organizacao": row["ORGANIZACAO"],
                "numero": row["NUMERO_SUBCR_NIVEL1"],
                "descricao": row["DESCRICAO_SUBCR_NIVEL1"],
                "sigla": row["SCR_SIGLA"]
            }
            uors.append(uor)
            
        
#       Verificar se a lista de uors está vazia
        if len(uors) == 0:
            return "Nenhuma solicitação encontrada."

#       Serializar a lista de uors para JSON
    
    
        json_data = JsonConvert.SerializeObject(uors)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)


        
def enviaDadosCad():
    try:
        pessoas = [];
        
#       ExecuteReader retorna um conjunto de resultados
        result_table2 = DB.ExecuteDataTable("SELECT f.status_matricula, f.nome, f.matricula, f.gestor_posicao, f.cargo_funcional, f.funcao_gratificada, f.supervisor, f.organizacao, f.unidade_negocio, f.local_cidade, f.local_estado, f.numero_subcr_nivel1, f.descricao_subcr_nivel1, f.numero_subcr_nivel2, f.descricao_subcr_nivel2, f.numero_subcr_nivel3, f.descricao_subcr_nivel3, cp.matricula, cp.funcao_gratificada, cp.cargo_funcional, cp.data_nascimento, cp.data_de_admissao, p.email, p.usuario_rede, p.bloqueado, c.scr_sigla as siglaNv1, c2.scr_sigla as siglaNv2, c3.scr_sigla as siglaNv3 FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa INNER join cob_gl_centro c on c.scr = f.numero_subcr_nivel1 INNER join cob_gl_centro c2 on c2.scr = f.numero_subcr_nivel2 INNER join cob_gl_centro c3 on c3.scr = f.numero_subcr_nivel3")
        
        
        
        
        for row in result_table2.Rows:
            pessoa = {
                "nome": row["NOME"],
                "matricula": row["MATRICULA"],
                "status": row["STATUS_MATRICULA"],
                "organizacao": row["ORGANIZACAO"],
                "numeroUorNv1": row["NUMERO_SUBCR_NIVEL1"],
                "siglaUorNv1": row["SIGLANV1"],
                "descricaoUorNv1": row["DESCRICAO_SUBCR_NIVEL1"],
                "unidade": row["UNIDADE_NEGOCIO"],
                "localCidade": row["LOCAL_CIDADE"],
                "localEstado": row["LOCAL_ESTADO"],
                "cargoFuncional": row["CARGO_FUNCIONAL"],
                "funcaoGratificada": row["FUNCAO_GRATIFICADA"],
                "supervisor": row["SUPERVISOR"],
                "gestor": row["GESTOR_POSICAO"],
                "numeroUorNv2": row["NUMERO_SUBCR_NIVEL2"],
                "descricaoUorNv2": row["DESCRICAO_SUBCR_NIVEL2"],
                "siglaUorNv2": row["SIGLANV2"],
                "numeroUorNv3": row["NUMERO_SUBCR_NIVEL3"],
                "descricaoUorNv3": row["DESCRICAO_SUBCR_NIVEL3"],
                "siglaUorNv3": row["SIGLANV3"],
                "dataNascimento": row["DATA_NASCIMENTO"],
                "admissao": row["DATA_DE_ADMISSAO"],
                "email": row["EMAIL"],
                "usuarioRede": row["USUARIO_REDE"],
                "bloqueado": row["BLOQUEADO"]
            }
            
            pessoas.append(pessoa)
            
        
#       Verificar se a lista de pessoas está vazia
        if len(pessoas) == 0:
            return "Nenhuma solicitação encontrada."

#       Serializar a lista de pessoas para JSON
        json_data = JsonConvert.SerializeObject(pessoas)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        
        
        
        
        
        
        
        
        
def enviaDadosDue():
    try:
        dues = [];
    
        result_table2 = DB.ExecuteDataTable("Select CP_ORDEM_SERVICO.CNPJ, CP_ORDEM_SERVICO.SIM_NAO, CP_ORDEM_SERVICO.FAVORECIDO_COBRA, CP_ORDEM_SERVICO.ACAO_TOMADA, OCORRENCIA.ASSUNTO, CP_ORDEM_SERVICO.NOME_FORNECEDOR, CPE_CONTRATOS.OBS5, CPE_CSC.TE_NOME_EMPREGADO, CPE_CSC.CSC_VALOR1_A, CPE_CSC.DIRETORIA_GERENCIA, CPE_CONTRATOS.DIVISAO_DUEDILIGENCE, CPE_CSC.FUNDAMENTACAO, CPE_CONTRATOS.MODALIDADE_DE_CONTRATACAO, CPE_CSC.NUMERO_DGCO, CPE_FINANCEIRO.OBJETO_QUALIF, CPE_DESLOCAMENTO.VALOR_DESPESAS, CPE_DESLOCAMENTO.VALIDADE_PASSAGEM, CPE_FINANCEIRO.VALOR_QUALIF, CPE_CSC.OBS6, CPE_CSC.DATA_HORA_FIM, CPE_CONTRATOS.GRAUDERISCO_DUEDILIGENCE, CPE_CSC.OBS21, CPE_CSC.SIM_NAO1, OCORRENCIA.ID_CLASSE_SUB_PROC From CP_ORDEM_SERVICO Inner Join OCORRENCIA On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_CONTRATOS On CP_ORDEM_SERVICO.ID_OCORRENCIA = CPE_CONTRATOS.ID_OCORRENCIA Inner Join CPE_CSC On CPE_CONTRATOS.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CPE_FINANCEIRO On CPE_CSC.ID_OCORRENCIA = CPE_FINANCEIRO.ID_OCORRENCIA Inner Join CPE_DESLOCAMENTO On CPE_FINANCEIRO.ID_OCORRENCIA = CPE_DESLOCAMENTO.ID_OCORRENCIA Where OCORRENCIA.ID_CLASSE_SUB_PROC = 805")

        
        json_data = JsonConvert.SerializeObject(result_table2)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        
        
def enviaDadosAvaliacaoFornecedor():
    try:
    
        result_table2 = DB.ExecuteDataTable("Select OCORRENCIA.ASSUNTO, OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO, CP_ORDEM_SERVICO.COMBOBOX As TIPO_AVALIACAO, CPE_CSC.CSC_DGCO As DGCO, CP_ORDEM_SERVICO.NOME_FORNECEDOR As EMPRESA_CONTRATADA, CPE_CSC.CSC_OBS As OBJ_CONTRATACAO, CPE_CSC.CSC_DATA_FIM As VIGENCIA_CONTRATO, CP_ORDEM_SERVICO.COMBOBOX1 As FISCAL_AVALIADOR, CPE_PESSOAS.GESTOR_SOLICITA As GESTOR_DO_CONTRATO, CPE_CSC.CSC_COMBOBOX As PERIODO_DA_AVALIACAO, CP_ORDEM_SERVICO.ANO As ANO_DA_AVALIACAO, CP_ORDEM_SERVICO.VALOR As MEDIA_TRIMESTRAL, CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO, Z_00143_AVALIACAO_FORNECEDOR.ITEM As ITEM, Z_00143_AVALIACAO_FORNECEDOR.NOTA As NOTA From OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CPE_PESSOAS On OCORRENCIA.ID_OCORRENCIA = CPE_PESSOAS.ID_OCORRENCIA Inner Join CLASSE_SUB_PROCESSO On OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO Inner Join Z_00143_AVALIACAO_FORNECEDOR On OCORRENCIA.ID_OCORRENCIA = Z_00143_AVALIACAO_FORNECEDOR.ID_OCORRENCIA Where CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = 575")

        
        json_data = JsonConvert.SerializeObject(result_table2)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
