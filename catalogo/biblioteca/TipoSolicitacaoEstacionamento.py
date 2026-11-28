# TipoSolicitacaoEstacionamento
# Caminho: Catálogo > Biblioteca de scripts > TipoSolicitacaoEstacionamento
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml (2 variantes entre os XMLs; esta é a mais recente)

def VerificaTipo(opcao):
    if opcao == "Inclusão na Fila de Espera do Estacionamento" or opcao == "Solicitar Posição na Fila de Espera":
        return "Inclusão na Fila de Espera do Estacionamento ou Solicitar Posição na Fila de Espera"
    elif opcao == "Inclusão na Fila de Espera do Estacionamento" or opcao == "Solicitar Posição na Fila de Espera":
        return "Inclusão na Fila de Espera do Estacionamento ou Solicitar Posição na Fila de Espera"
    elif opcao == "Atualização de Cadastro do Estacionamento" or opcao == "Desistência da Fila de Espera do Estacionamento":
        return "Atualização de Cadastro do Estacionamento ou Desistência da Fila de Espera do Estacionamento"
    else:
        return opcao
