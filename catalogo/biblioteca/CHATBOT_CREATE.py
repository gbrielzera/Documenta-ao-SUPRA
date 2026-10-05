# CHATBOT_CREATE
# Caminho: Catálogo > Biblioteca de scripts > CHATBOT_CREATE
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr

from System import *

from System.Text import StringBuilder

clr.AddReference("Supravizio.Custom")

from Venki.Supravizio.Recurso.Custom import Pessoa

from Venki.Supravizio.Processo.Custom import OrdemServico

  

def ObtemOSPorCliente(usuarioRede):

   xml = StringBuilder()  

   try:

       cliente = Pessoa.Carrega("UsuarioRede", usuarioRede)

       if cliente != None:  

           dt = DB.ExecuteDataTable("SELECT ID_OCORRENCIA FROM OCORRENCIA WHERE ID_CLIENTE = " + cliente.Id.ToString() + " AND SITUACAO = 'Aberto'")

           if dt.Rows.Count > 0:

               xml.AppendLine("<ORDEMSERVICO>")  

               for dr in dt.Rows:

                   os = OrdemServico.Carrega(Convert.ToInt32(dr["ID_OCORRENCIA"]))

                   xml.AppendFormat("<NUMERO>{0}</NUMERO>", os.Numero)

                   xml.AppendFormat("<ASSUNTO>{0}</ASSUNTO>\r\n", os.Assunto)

               xml.AppendLine("</ORDEMSERVICO>")

           else:

               xml.Append("Não foi encontrada nenhuma Ordem de Serviço")

       else:

           xml.Append("Usuário não encontrado")

   except Exception, e:

       xml.Append("Erro ao executar Web Service")

   return xml.ToString()
