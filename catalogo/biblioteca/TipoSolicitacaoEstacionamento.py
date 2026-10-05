# TipoSolicitacaoEstacionamento
# Caminho: Catálogo > Biblioteca de scripts > TipoSolicitacaoEstacionamento
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def VerificaTipo(opcao):
    if opcao == "Inclusão na Fila de Espera do Estacionamento" or opcao == "Solicitar Posição na Fila de Espera":
        return "Inclusão na Fila de Espera do Estacionamento ou Solicitar Posição na Fila de Espera"
    elif opcao == "Inclusão na Fila de Espera do Estacionamento" or opcao == "Solicitar Posição na Fila de Espera":
        return "Inclusão na Fila de Espera do Estacionamento ou Solicitar Posição na Fila de Espera"
    elif opcao == "Atualização de Cadastro do Estacionamento" or opcao == "Desistência da Fila de Espera do Estacionamento":
        return "Atualização de Cadastro do Estacionamento ou Desistência da Fila de Espera do Estacionamento"
    else:
        return opcao
