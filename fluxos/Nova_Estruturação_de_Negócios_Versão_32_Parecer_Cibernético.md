# Fluxo: Parecer Cibernético (PARECERCIBER) — versão 32
Caminho: Fluxos > Nova Estruturação de Negócios Versão 32 Parecer Cibernético
XML: `XMLs para teste/Nova_Estruturação_de_Negócios_Versão_32_Parecer_Cibernético.xml` | Supravizio 19.1.1 | SubProcessoId 20713 | DesenhoProcessoId 2906 | ProcessoId 79
Órgão dono: 3000009431 - SETOR DE SUPERVISAO DOS SERVICOS COMPARTILHADOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [329822] Tarefa "Inserir Parecer" {Responsável atual} → [329824] Aviso de encaminhamento de anexo 
- [329823] EventoIntermediarioMensagem "Parecer Cibernético" → [329819] Analisar Solicitação 
- [329819] Tarefa "Analisar Solicitação " {Fila Oportunidade Cyber} → [329822] Inserir Parecer
- [329820] LinkInicial "" → [329823] Parecer Cibernético
- [329821] EventoFinal "" → (fim)
- [329824] EventoIntermediarioMensagem "Aviso de encaminhamento de anexo " → [329821] 

## Atividades

### [329822] Tarefa "Inserir Parecer"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Parecer Cibernético — RequeridoInicial=true

### [329823] EventoIntermediarioMensagem "Parecer Cibernético"
Config: ListaDestinatarios=cyber@bbts.com.br
ModeloComunicado: Novos Negócios - Parecer Cibernético
Corpo do comunicado: Prezados,
Seguem anexas às informações de nova oportunidade de negócio referente ao Projeto OrdemServico.Assunto, conduzida pelo chamado de número OrdemServico.Numero ( Link.Edicao Worklist ).
Estamos em processo de assinatura do contrato desse novo negócio e solicitamos a avaliação pertinente aos Riscos Cibernético na minuta contratual.
Estamos à disposição para quaisquer esclarecimentos.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
OrdemServico.AdicionaComentario("Notificação 1 enviada com sucesso", False)
```

### [329819] Tarefa "Analisar Solicitação "
Responsável: Fila Oportunidade Cyber (papel 1216)

### [329820] LinkInicial ""
Config: Codigo=PARECER_CIBER; TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=778; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Portal de Estruturação de Negócios -> Parecer Cibernético
- Associação de subprocesso: AssociacaoId=1581; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Alvo: Parecer Cibernético

### [329821] EventoFinal ""

### [329824] EventoIntermediarioMensagem "Aviso de encaminhamento de anexo "
Destinatário: Cliente (papel 18)
ModeloComunicado: Anexar Parecer Cibernético para envio via e-mail
Corpo do comunicado: Prezado(a),
Na ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Foi anexado o item "Parecer Cibernético".
Para maiores informações Link.Workspace . 
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
#OrdemServico.AdicionaComentario("Notificação 1 enviada com sucesso", False)
```

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
### papel 1216: Fila Oportunidade Cyber
Tipo=RelacaoPessoas | pessoas: Fila Oportunidade Cyber
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
