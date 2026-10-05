# Fluxo: Parecer da LGPD (PARECERLGPD) — versão 32
Caminho: Fluxos > Nova Estruturação de Negócios Versão 32 Parecer da LGPD
XML: `XMLs para teste/Nova_Estruturação_de_Negócios_Versão_32_Parecer_da_LGPD.xml` | Supravizio 19.1.1 | SubProcessoId 20714 | DesenhoProcessoId 2906 | ProcessoId 79
Órgão dono: 3000009431 - SETOR DE SUPERVISAO DOS SERVICOS COMPARTILHADOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [329825] EventoFinal "" → (fim)
- [329826] EventoIntermediarioMensagem "Aviso de encaminhamento de anexo " → [329825] 
- [329827] Tarefa "Emitir parecer " {Responsável atual} → [329826] Aviso de encaminhamento de anexo 
- [329828] EventoIntermediarioMensagem "Novos Negócios - Parecer da LGPD" → [329829] Analisar Solicitação 
- [329829] Tarefa "Analisar Solicitação " {Fila GovIT} → [329827] Emitir parecer 
- [329830] LinkInicial "" → [329828] Novos Negócios - Parecer da LGPD

## Atividades

### [329825] EventoFinal ""

### [329826] EventoIntermediarioMensagem "Aviso de encaminhamento de anexo "
Config: ListaDestinatarios=controlesinternos@bbts.com.br
ModeloComunicado: Anexar Parecer LGPD para envio via e-mail
Corpo do comunicado: Prezado(a),
Na ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Foi anexado o item "Parecer da LGPD".
Para maiores informações Link.Workspace . 
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
OrdemServico.AdicionaComentario("Notificação 1 enviada com sucesso", False)
```

### [329827] Tarefa "Emitir parecer "
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Parecer da LGPD — RequeridoInicial=true

### [329828] EventoIntermediarioMensagem "Novos Negócios - Parecer da LGPD"
Config: ListaDestinatarios=privacidade@bbts.com.br;ext-ramagalhaes@bbts.com.br
ModeloComunicado: Novos Negócios - Parecer da LGPD
ClasseAnexoResposta: Parecer da LGPD
Corpo do comunicado: Prezados,
Seguem anexas às informações de nova oportunidade de negócio referente ao Projeto OrdemServico.Assunto, conduzida pelo chamado de número OrdemServico.Numero ( Link.Edicao Worklist ).
Estamos em processo de assinatura do contrato desse novo negócio e solicitamos a avaliação pertinente as cláusulas LGPD da minuta contratual.
Estamos à disposição para quaisquer esclarecimentos.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
OrdemServico.AdicionaComentario("Notificação 1 enviada com sucesso", False)
```

### [329829] Tarefa "Analisar Solicitação "
Responsável: Fila GovIT (papel 1357)
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Parecer da LGPD — RequeridoInicial=true

### [329830] LinkInicial ""
Config: Codigo=XX; TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=779; FraseAssociacao=Portal de Estruturação de Negócios -> Parecer da LGPD; Nome=LGPDPARECER
- Associação de subprocesso: AssociacaoId=1579; FraseAssociacao=Alvo: Parecer da LGPD; Nome=PARECERLGPDASSINATURA

## Papéis usados
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 1357: Fila GovIT
Tipo=RelacaoPessoas | pessoas: Fila de Oportunidade LGPD

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
