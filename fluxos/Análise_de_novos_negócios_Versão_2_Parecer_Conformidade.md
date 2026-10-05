# Fluxo: Parecer Conformidade (PARECERDERISCO) — versão 2
Caminho: Fluxos > Análise de novos negócios Versão 2 Parecer Conformidade
XML: `XMLs para teste/Análise_de_novos_negócios_Versão_2_Parecer_Conformidade.xml` | Supravizio 19.1.1 | SubProcessoId 20581 | DesenhoProcessoId 2896 | ProcessoId 390
Órgão dono: 3000009431 - SETOR DE SUPERVISAO DOS SERVICOS COMPARTILHADOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Novos negócios (JUSNEGOCIOS)

## Grafo do fluxo
- [328100] Tarefa "Analisar Solicitação
" {Fila Conformidade} → [328101] Emitir parecer de conformidade 
- [328101] Tarefa "Emitir parecer de conformidade " {Responsável atual} → [328104] Aviso de encaminhamento de anexo 
- [328102] LinkInicial "" {Responsável atual} → [328105] Aviso de Abertura do Chamado 
- [328103] EventoFinal "Sucesso " → (fim)
- [328104] EventoIntermediarioMensagem "Aviso de encaminhamento de anexo " → [328103] Sucesso 
- [328105] EventoIntermediarioMensagem "Aviso de Abertura do Chamado " → [328100] Analisar Solicitação


## Atividades

### [328100] Tarefa "Analisar Solicitação
"
Responsável: Fila Conformidade (papel 447)

### [328101] Tarefa "Emitir parecer de conformidade "
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo - Geric " classes: Anexo - Geric — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [328102] LinkInicial ""
Responsável: Responsável atual (papel 36)
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=777; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Portal de Estruturação de negócios -> Parecer de Risco do Negócio
- Associação de subprocesso: AssociacaoId=1022; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Assinatura de Novos Contratos e Aditivos -> Parecer Conformidade
- Associação de subprocesso: AssociacaoId=1272; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Assinatura de Novos Contratos e Aditivos ATA -> Parecer Conformidade
- Associação de subprocesso: AssociacaoId=1585; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Alvo: Parecer de Risco
- Associação de subprocesso: AssociacaoId=1586; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Alvo: Parecer de Risco

### [328103] EventoFinal "Sucesso "

### [328104] EventoIntermediarioMensagem "Aviso de encaminhamento de anexo "
Config: ListaDestinatarios=controlesinternos@bbts.com.br
ModeloComunicado: Anexar parecer jurídico para envio no e-mail
Corpo do comunicado: Prezado(a),
Na ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Foi anexado o item "Anexo - Geric", o qual consta o parecer jurídico.
Para maiores informações Link.Workspace . 
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
OrdemServico.AdicionaComentario("Notificação 1 enviada com sucesso", False)
```

### [328105] EventoIntermediarioMensagem "Aviso de Abertura do Chamado "
Config: ListaDestinatarios=controlesinternos@bbts.com.br
ModeloComunicado: Comunicado Contas a Pagar - Boleto Previdência Privada
Corpo do comunicado: Prezado(a),
Consta Ordem de Serviço para para Boleto Previdência Privada:
 Nº de RI: OrdemServico.Customizado.CSC_NUMERO 
Para acessar a solicitação OrdemServico.Numero - OrdemServico.Assunto acesse o link Link.Workspace .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
OrdemServico.AdicionaComentario("Notificação 1 enviada com sucesso", False)
```

## Papéis usados
### papel 447: Fila Conformidade
Tipo=RelacaoGrupos
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
