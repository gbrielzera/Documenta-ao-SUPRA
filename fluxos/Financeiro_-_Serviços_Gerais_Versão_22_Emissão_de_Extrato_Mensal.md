# Fluxo: Emissão de Extrato Mensal (EMISEXTMENSAL) — versão 22
Caminho: Fluxos > Financeiro - Serviços Gerais Versão 22 Emissão de Extrato Mensal
XML: `XMLs para teste/Financeiro_-_Serviços_Gerais_Versão_22_Emissão_de_Extrato_Mensal.xml` | Supravizio 19.1.1 | SubProcessoId 21151 | DesenhoProcessoId 2796 | ProcessoId 150
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [337176] EventoInicialRegra " Emissão de Extrato Mensal - Conta de Investimento" → [337183] Abertura automática de OS por Solucionador
- [337182] SubProcesso "Abertura automática de OS por Solucionador" {Sistema} → [337180] Sucesso
- [337179] EventoInicialRegra "Emissão de Extrato Diário - Conta Corrente" → [337177] Abertura automática de OS por Solucionador
- [337180] EventoFinal "Sucesso" → (fim)
- [337181] EventoInicialRegra "Emissão de Extrato Mensal - Conta Corrente" → [337182] Abertura automática de OS por Solucionador
- [337177] SubProcesso "Abertura automática de OS por Solucionador" {Sistema} → [337178] Sucesso
- [337178] EventoFinal "Sucesso" → (fim)
- [337173] Tarefa "Emitir extrato." {Fila CSC - Pagamentos} → [337174] Anexar extrato no sharepoint.
- [337174] Tarefa "Anexar extrato no sharepoint." {Responsável atual} → [337185] Sucesso
- [337175] EventoFinal "Sucesso" → (fim)
- [337184] LinkInicial "" → [337173] Emitir extrato.
- [337185] EventoFinal "Sucesso" → (fim)
- [337183] SubProcesso "Abertura automática de OS por Solucionador" {Sistema} → [337175] Sucesso

## Atividades

### [337176] EventoInicialRegra " Emissão de Extrato Mensal - Conta de Investimento"
Config: Configuracao={"ServicoIniciador":"EMISSAOEXTRATOMENINVES"}
**Regra**
```python
DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.CONTA_CORRENTE_NUMERO From OCORRENCIA INNER JOIN CPE_CSC ON CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA where OCORRENCIA.ASSUNTO = 'Emissão de Extrato Mensal - Conta de Investimento' AND TRUNC(OCORRENCIA.DATA_HORA_SOL,'MM')=TRUNC(SYSDATE,'MM') AND CPE_CSC.CONTA_CORRENTE_NUMERO IN ('7020-3','6530-7','6518-8','7252-4','6534-x','6980-9','7250-8','6984-1','7229-x','6992-2','6972-8','6896-9','6968-X','6651-6','7247-8','6561-7','7236-2','6499-8','6951-5','6952-3','6953-1','6954-X','6583-8','7251-6','7006-8','6632-x','6527-7','6987-6','6624-9','7249-4','205826-x','205393-4','200000-8')").Rows.Count < 33 and DateTime.Now.ToString("dd") == "01"
```

### [337182] SubProcesso "Abertura automática de OS por Solucionador"
Responsável: Sistema (papel 1)
Config: ChamadaAssincrona=true; AssociacaoId=1507
**ScriptInicio**
```python
#Lista de solucionadores que não possuem OS de conformidade
contas = ['7020-3','6530-7','6518-8','7252-4','6534-x','6980-9','7250-8','6984-1','7229-x','6992-2','6972-8','6896-9','6968-X','6651-6','7247-8','6561-7','7236-2','6499-8','6951-5','6952-3','6953-1','6954-X','6583-8','7251-6','7006-8','6632-x','6527-7','6987-6','6624-9','7249-4','205826-x','205393-4','200000-8']

listaOSContas = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.CONTA_CORRENTE_NUMERO From OCORRENCIA INNER JOIN CPE_CSC ON CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA where OCORRENCIA.ASSUNTO = 'Emissão de Extrato Mensal - Conta Corrente' AND TRUNC(OCORRENCIA.DATA_HORA_SOL,'MM')=TRUNC(SYSDATE,'MM') AND CPE_CSC.CONTA_CORRENTE_NUMERO IN ('7020-3','6530-7','6518-8','7252-4','6534-x','6980-9','7250-8','6984-1','7229-x','6992-2','6972-8','6896-9','6968-X','6651-6','7247-8','6561-7','7236-2','6499-8','6951-5','6952-3','6953-1','6954-X','6583-8','7251-6','7006-8','6632-x','6527-7','6987-6','6624-9','7249-4','205826-x','205393-4','200000-8')")

n = 0
for conta in contas:
    for listaConta in listaOSContas.Rows:
        if conta == listaConta['CONTA_CORRENTE_NUMERO']:
            n = 1
    if n == 0:
        if DateTime.Now.ToString("dd") == "01":
            sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
            sub.Assunto = "Emissão de Extrato Mensal - Conta Corrente"
            sub["CONTA_CORRENTE_NUMERO"]= conta
            sub.Salva()
            sub.AvancaAtividade()
        
        n = 0    
        AvancaProximaAtividade = True
```
- ValoresInputs:
  - CustomPropertyId=2148; CustomProperty=CONTA_CORRENTE_NUMERO
- Associação: Ativo=true; FraseAssociacao=Emissão de Extrato Mensal -> Emissão de Extrato Mensal; FraseInversaAssociacao=Emissão de Extrato Mensal <- Emissão de Extrato Mensal; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=EXTRATOMENSALCONTAINVESTIMENTO; SeparadorSequencial=. | fonte: Emissão de Extrato Mensal → alvo: Emissão de Extrato Mensal

### [337179] EventoInicialRegra "Emissão de Extrato Diário - Conta Corrente"
Config: Configuracao={"ServicoIniciador":"EMISSAOEXTRATODIARIO"}
**Regra**
```python
DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.CONTA_CORRENTE_NUMERO From OCORRENCIA INNER JOIN CPE_CSC ON CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA where OCORRENCIA.ASSUNTO = 'Emissão de Extrato Diário - Conta Corrente' AND TO_CHAR(OCORRENCIA.DATA_HORA_SOL, 'DDMM') = TO_CHAR(SYSDATE, 'DDMM') AND CPE_CSC.CONTA_CORRENTE_NUMERO IN ('205826-x','205393-4','200000-8')").Rows.Count < 3 and DateTime.Now.DayOfWeek != 'Sunday' and DateTime.Now.DayOfWeek != 'Saturday'
```

### [337180] EventoFinal "Sucesso"

### [337181] EventoInicialRegra "Emissão de Extrato Mensal - Conta Corrente"
Config: Configuracao={"ServicoIniciador":"EMISSAOEXTRATOMENSALCC"}
**Regra**
```python
DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.CONTA_CORRENTE_NUMERO From OCORRENCIA INNER JOIN CPE_CSC ON CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA where OCORRENCIA.ASSUNTO = 'Emissão de Extrato Mensal - Conta Corrente' AND TRUNC(OCORRENCIA.DATA_HORA_SOL,'MM')=TRUNC(SYSDATE,'MM') AND CPE_CSC.CONTA_CORRENTE_NUMERO IN ('7020-3','6530-7','6518-8','7252-4','6534-x','6980-9','7250-8','6984-1','7229-x','6992-2','6972-8','6896-9','6968-X','6651-6','7247-8','6561-7','7236-2','6499-8','6951-5','6952-3','6953-1','6954-X','6583-8','7251-6','7006-8','6632-x','6527-7','6987-6','6624-9','7249-4','205826-x','205393-4','200000-8')").Rows.Count < 33 and DateTime.Now.ToString("dd") == "01"
```

### [337177] SubProcesso "Abertura automática de OS por Solucionador"
Responsável: Sistema (papel 1)
Config: ChamadaAssincrona=true; AssociacaoId=1507
**ScriptInicio**
```python
#Lista de solucionadores que não possuem OS de conformidade
contas = ['205826-x','205393-4','200000-8']

listaOSContas = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.CONTA_CORRENTE_NUMERO From OCORRENCIA INNER JOIN CPE_CSC ON CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA where OCORRENCIA.ASSUNTO = 'Emissão de Extrato Diário - Conta Corrente' AND TRUNC(OCORRENCIA.DATA_HORA_SOL,'MM')=TRUNC(SYSDATE,'MM') AND CPE_CSC.CONTA_CORRENTE_NUMERO IN ('205826-x','205393-4','200000-8')")

for conta in contas:
    sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
    sub.Assunto = "Emissão de Extrato Diário - Conta Corrente"
    sub["CONTA_CORRENTE_NUMERO"]= conta
    sub.Salva()
    sub.AvancaAtividade()
       
AvancaProximaAtividade = True
```
- ValoresInputs:
  - CustomPropertyId=2148; CustomProperty=CONTA_CORRENTE_NUMERO
- Associação: Ativo=true; FraseAssociacao=Emissão de Extrato Mensal -> Emissão de Extrato Mensal; FraseInversaAssociacao=Emissão de Extrato Mensal <- Emissão de Extrato Mensal; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=EXTRATOMENSALCONTAINVESTIMENTO; SeparadorSequencial=. | fonte: Emissão de Extrato Mensal → alvo: Emissão de Extrato Mensal

### [337178] EventoFinal "Sucesso"

### [337173] Tarefa "Emitir extrato."
Responsável: Fila CSC - Pagamentos (papel 705)
**ScriptInicio**
```python
OrdemServico.AdicionaComentario(DateTime.Now.DayOfWeek.ToString(), False)
```
- Operação PR0001 Preencher Campos
  - CONTA_CORRENTE_NUMERO "Conta Corrente" [TextBox String → CPE_CSC.CONTA_CORRENTE_NUMERO] obrigatório
    - coluna CONTA obrigatório
  - MESANOREF "Mês/Ano" [TextBox String → CPE_CSC.MESANOREF] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Anexo — RequeridoInicial=true

### [337174] Tarefa "Anexar extrato no sharepoint."
Responsável: Responsável atual (papel 36)

### [337175] EventoFinal "Sucesso"

### [337184] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=1507; FraseAssociacao=Emissão de Extrato Mensal -> Emissão de Extrato Mensal; Nome=EXTRATOMENSALCONTAINVESTIMENTO

### [337185] EventoFinal "Sucesso"

### [337183] SubProcesso "Abertura automática de OS por Solucionador"
Responsável: Sistema (papel 1)
Config: ChamadaAssincrona=true; AssociacaoId=1507
**ScriptInicio**
```python
#Lista de solucionadores que não possuem OS de conformidade
contas = ['7020-3','6530-7','6518-8','7252-4','6534-x','6980-9','7250-8','6984-1','7229-x','6992-2','6972-8','6896-9','6968-X','6651-6','7247-8','6561-7','7236-2','6499-8','6951-5','6952-3','6953-1','6954-X','6583-8','7251-6','7006-8','6632-x','6527-7','6987-6','6624-9','7249-4','205826-x','205393-4','200000-8']

listaOSContas = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.CONTA_CORRENTE_NUMERO From OCORRENCIA INNER JOIN CPE_CSC ON CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA where OCORRENCIA.ASSUNTO = 'Emissão de Extrato Mensal - Conta de Investimento' AND TRUNC(OCORRENCIA.DATA_HORA_SOL,'MM')=TRUNC(SYSDATE,'MM') AND CPE_CSC.CONTA_CORRENTE_NUMERO IN ('7020-3','6530-7','6518-8','7252-4','6534-x','6980-9','7250-8','6984-1','7229-x','6992-2','6972-8','6896-9','6968-X','6651-6','7247-8','6561-7','7236-2','6499-8','6951-5','6952-3','6953-1','6954-X','6583-8','7251-6','7006-8','6632-x','6527-7','6987-6','6624-9','7249-4','205826-x','205393-4','200000-8')")

n = 0
for conta in contas:
    for listaConta in listaOSContas.Rows:
        if conta == listaConta['CONTA_CORRENTE_NUMERO']:
            n = 1
    if n == 0:
        if DateTime.Now.ToString("dd") == "01":
            sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
            sub.Assunto = "Emissão de Extrato Mensal - Conta de Investimento"
            sub["CONTA_CORRENTE_NUMERO"]= conta
            sub.Salva()
            sub.AvancaAtividade()
        
        n = 0    
        AvancaProximaAtividade = True
```
- ValoresInputs:
  - CustomPropertyId=2148; CustomProperty=CONTA_CORRENTE_NUMERO
- Associação: Ativo=true; FraseAssociacao=Emissão de Extrato Mensal -> Emissão de Extrato Mensal; FraseInversaAssociacao=Emissão de Extrato Mensal <- Emissão de Extrato Mensal; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=EXTRATOMENSALCONTAINVESTIMENTO; SeparadorSequencial=. | fonte: Emissão de Extrato Mensal → alvo: Emissão de Extrato Mensal

## Papéis usados
### papel 1: Sistema
Tipo=RelacaoPessoas | pessoas: Sistema
### papel 705: Fila CSC - Pagamentos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pagamentos
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### CONTA_CORRENTE_NUMERO — Numero da conta corrente.
TextBox String → CPE_CSC.CONTA_CORRENTE_NUMERO
Descrição: Numero da Conta Corrente

### MESANOREF — Mês e ano referência
TextBox String → CPE_CSC.MESANOREF

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
