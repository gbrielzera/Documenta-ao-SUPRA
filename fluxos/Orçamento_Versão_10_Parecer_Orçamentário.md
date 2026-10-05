# Fluxo: Parecer Orçamentário (PARECERORCAMETARIO) — versão 10
Caminho: Fluxos > Orçamento Versão 10 Parecer Orçamentário
XML: `XMLs para teste/Orçamento_Versão_10_Parecer_Orçamentário.xml` | Supravizio 19.1.1 | SubProcessoId 13899 | DesenhoProcessoId 2036 | ProcessoId 189
Órgão dono: 3000009431 - SETOR DE SUPERVISAO DOS SERVICOS COMPARTILHADOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: DescricaoCliente=Parecer Orçamentário; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [212282] Tarefa "Analisar solicitação" {Fila Controladoria} → [212283] Emitir parecer

- [212283] Tarefa "Emitir parecer
" {Responsável atual} → [212284] 
- [212284] EventoFinal "" → (fim)
- [212285] EventoIntermediarioMensagem "Orçamento para Investimento" → [212282] Analisar solicitação
- [212286] LinkInicial "" → [212285] Orçamento para Investimento

## Atividades

### [212282] Tarefa "Analisar solicitação"
Responsável: Fila Controladoria (papel 372)

### [212283] Tarefa "Emitir parecer
"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Parecer Orçamentário" classes: Parecer Orçamentário — RequeridoInicial=true

### [212284] EventoFinal ""

### [212285] EventoIntermediarioMensagem "Orçamento para Investimento"
Config: ListaDestinatarios=dioge@bbts.com.br;beatriz.vieira@bbts.com.br;fernando.guedes@bbts.com.br; AnexarTodosDocumentos=true
ModeloComunicado: Novos Negócios - Orçamento para Investimento
Corpo do comunicado: Prezados,
Seguem anexas às informações de nova oportunidade de negócio referente ao Projeto OrdemServico.Assunto, conduzida pelo chamado de número OrdemServico.Numero (Link.Edicao Worklist).
Estamos em processo de estruturação desse novo negócio e solicitamos apoio quanto a avaliação da viabilidade orçamentária, tendo como referência o volume de investimento necessário para atender a essa oportunidade de negócio.
Segue anexa a DRE, para avaliação e indicação quanto a viabilidade orçamentária ou os ajustes necessários no cronograma de investimentos, para que seja viável a continuidade dessa oportunidade de negócio.
Estamos à disposição para quaisquer esclarecimentos.
Atenciosamente,
Central d…

### [212286] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=961; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Portal de Estruturação de Negócios (Projeto) -> Parecer Orçamentário
- Associação de subprocesso: AssociacaoId=1582; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Alvo: Parecer Jurídico

## Papéis usados
### papel 372: Fila Controladoria
Tipo=RelacaoPessoas | pessoas: Fila Controladoria
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
