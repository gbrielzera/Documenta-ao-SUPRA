# Testes em Qualidade (roteiro e resultados)
Caminho: Guias > Testes em Qualidade

Roteiro para comprovar, no ambiente de **Qualidade**, os comportamentos que só aparecem como "assinatura confirmada" ou
"observado". Os scripts abaixo são de **diagnóstico** (têm `try/except` e comentários na OS de propósito); a regra do script
mínimo vale para os scripts de entrega, não para estes. Cada um só escreve um comentário na OS: nada é alterado.

## Montagem (uma vez, ~15 minutos)
Fluxo de teste "TESTE_SKILL" em Qualidade, com Evento Inicial → Tarefa A → Tarefa B → Tarefa C (aprovação, Código `APROV`,
você como aprovador) → Evento de mensagem (destinatário: você) → Final. Você abre a OS pelo Portal ou Workspace,
anda pelas tarefas e, no fim, copia os comentários da OS (aba Comentários) que começam por "T".

## Scripts
**T1 — consulta parametrizada.** Script Início da Tarefa A. Descobre qual sintaxe de marcador o `DB` aceita.
```python
for sql, nomes in [("SELECT NOME FROM PESSOA WHERE ID_PESSOA = :ID", ["ID"]),
                   ("SELECT NOME FROM PESSOA WHERE ID_PESSOA = :ID", [":ID"]),
                   ("SELECT NOME FROM PESSOA WHERE ID_PESSOA = @ID", ["@ID"])]:
    try:
        r = DB.ExecuteScalar(sql, nomes, [OrdemServico.ClienteId])
        OrdemServico.AdicionaComentario("T1 OK " + str(nomes) + " " + sql[-6:] + ": " + str(r), False)
    except Exception as e:
        OrdemServico.AdicionaComentario("T1 ERRO " + str(nomes) + ": " + str(e), False)
```

**T2 — importar `Pessoa` é necessário?** Script Início da Tarefa A, em outra linha do mesmo script ou na Tarefa B,
**sem** nenhum `from ... import Pessoa`.
```python
try:
    p = Pessoa.Carrega(OrdemServico.ClienteId)
    OrdemServico.AdicionaComentario("T2 OK sem import: " + str(p.Nome), False)
except Exception as e:
    OrdemServico.AdicionaComentario("T2 ERRO sem import: " + str(e), False)
```

**T3 — esconder campo fora do formulário.** Escolha um campo inofensivo (ex.: `OBS1`) que esteja na Entrada de Dados das
Tarefas B e C. Script Início da Tarefa B e Script Formulário carregado da Tarefa C:
```python
OrdemServico.ModificaCampoFormularioVisivel("OBS1", False)
OrdemServico.AdicionaComentario("T3 executou", False)
```
Observação a anotar: ao abrir cada tarefa, o campo `OBS1` aparece ou não?

**T4 — `PossuiAprovacao` com a aprovação pendente.** Na Tarefa C (aprovação, Código `APROV`): Script Início e Script Fim.
```python
OrdemServico.AdicionaComentario("T4 PossuiAprovacao: " + str(OrdemServico.PossuiAprovacao("APROV")), False)
```
Esperado: `False` no Script Início (pendente) e `True` no Script Fim se você aprovar. Anote os dois valores.

**T5 — cancelar o envio da mensagem.** Script Evento do Evento de mensagem (destinatário: você mesmo):
```python
Mensagem.Cancelar = True
OrdemServico.AdicionaComentario("T5 script evento executou", False)
```
Observação a anotar: o e-mail chegou? (espere alguns minutos). Para comparar, rode uma segunda OS sem o `Cancelar`.
(Contexto: uma aula usou `if OrdemServico.ClasseSubProcesso.Sigla != "SIGLA": Mensagem.Cancelar = True` para barrar a mensagem
de outros subprocessos e a mensagem deixou de ser gerada; falta confirmar o e-mail na caixa e na versão 19.1.1.)

**T6 (opcional) — chamada assíncrona.** Só se já houver um par de fluxos de teste ligados por Link Inicial. Na atividade
Subprocesso, rode uma OS com `Chamada assíncrona` marcada e outra desmarcada. Anote: a OS chamadora avançou sem esperar a
filha terminar? (a documentação se contradiz; as aulas, com a tela à vista, mostram `False` = a principal espera e `True` =
segue. Falta confirmar na 19.1.1.)

## Como relatar
Mande em texto, uma linha por teste, copiando o texto do comentário ou da mensagem de erro:
```
T1: OK com ["ID"] -> nome retornado (sem escrever o nome)
T2: ERRO: ...
T3: Início = campo continuou visível; Formulário carregado = sumiu
T4: Início = False; Fim = True
T5: e-mail não chegou
```
Nunca cole nomes reais: troque por "(nome)". Se der erro com código (ex.: PR0029), mande o código e a mensagem.

## Resultados
| Teste | Data | Resultado | Conclusão incorporada |
|---|---|---|---|
