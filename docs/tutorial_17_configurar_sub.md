# Configurar o Subprocesso

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 15: Iniciar Ordens de Serviço por Arquivos > Configurar o Subprocesso

Para configurar o Subprocesso em questão, utilizaremos no Macroprocesso "Administrativo" um novo processo denominado "Bancário" e o Subprocesso denominado "Processamento de Arquivo de Retorno":

Configuração do Subprocesso

E na aba de Serviços disponíveis, adicione um novo (apenas o serviço "Financeiro" de "Sistemas Administrativos":

Restrição de Serviços

No novo subprocesso vamos configurar conforme o fluxo abaixo:

Fluxo do Subprocesso

No iniciador por regra, modifique a propriedade de Regra para:

Directory.GetFiles("D:\\temp")

E a propriedade de Script Evento para:

OrdemServico.AnexaArquivo(Regra.ToString(), "ANALISEPRECO", True)

Portanto as propriedades seriam:

**Propriedades do iniciador por Evento**

Para concluir a edição** ative a versão** de processo contendo nosso novo subprocesso.
