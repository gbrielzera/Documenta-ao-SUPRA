# Fluxo: Pré-Notificação do Índice de Desempenho de Fornecedores (IDF)  (IDFINDIVIDUAL) — versão 3
Caminho: Fluxos > Gabriel Teste Ativações Versão 3 Pré-Notificação do Índice de Desempenho de Fornecedores (IDF) 
XML: `XMLs para teste/Gabriel_Teste_Ativações_Versão_3_Pré-Notificação_do_Índice_de_Desempenho_de_Fornecedores_(IDF)_.xml` | Supravizio 19.1.1 | SubProcessoId 21929 | DesenhoProcessoId 3019 | ProcessoId 781
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Pré-Notificação do Índice de Desempenho de Fornecedores (IDF); CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [348235] EventoIntermediarioMensagem "E-mail avaliação Fiscal" → [348236] 
- [348236] EventoFinal "" → (fim)
- [348231] Tarefa "Preenchimeneto dos campos" {Responsável atual} → [348230] Aprovação
- [348227] LinkInicial "" {Fila CSC - Contratos} → [348231] Preenchimeneto dos campos
- [348228] EventoIntermediarioMensagem "E-mail avaliação Fiscal" → [348235] E-mail avaliação Fiscal
- [348230] Tarefa "Aprovação" {Responsável atual} → [G78666] Aprovado?
- [G78666] Gateway "Aprovado?" → «Aprovado» [348228] E-mail avaliação Fiscal | «Reprovado» [348231] Preenchimeneto dos campos

## Gateways
### [G78666] Aprovado? (DataBasedExclusiveDecision)
Codigo=TESTE
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("TESTE")
```
- alternativa → [348228] E-mail avaliação Fiscal: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Aprovado
**ValorComparacaoDecision**
```python
True
```
- alternativa → [348231] Preenchimeneto dos campos: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Reprovado
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [348235] EventoIntermediarioMensagem "E-mail avaliação Fiscal"
Destinatário: Favorecido Cobra 1 (papel 1125)
ModeloComunicado: IDF - Notificação
Corpo do comunicado: Prezado Fornecedor OrdemServico.Customizado.FORNECEDOR1 
Contrato DGCO: OrdemServico.Customizado.DGCO_BB 
Último período apurado: OrdemServico.Customizado.PERIODO01 
Informamos que, na última Avaliação Trimestral de Fornecedores, o desempenho apresentado ficou abaixo do esperado, conforme evidenciado pelas notas atribuídas e pelas respectivas ocorrências registradas abaixo.
Esclarecemos que a avaliação realizada pelos fiscais do contrato possui caráter exclusivamente informativo, tendo por finalidade pré-notificar o fornecedor acerca dos pontos que necessitam de melhoria no cumprimento das obrigações contratuais.
Ressalta-se, ainda, que a referida avaliação possui caráter interno e não impli…

### [348236] EventoFinal ""

### [348231] Tarefa "Preenchimeneto dos campos"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
grid = OrdemServico.GetCustom('GRID_IDF')
nome_fornecedor = ""

for i in grid.Rows:
    nome_fornecedor = i["FORNECEDOR"].strip()
    nome_fornecedor.ToString()
    break
    
OrdemServico.AdicionaComentario(nome_fornecedor, False)
```
**ScriptFormCarregado**
```python
campos = ['COMBOBOX', 'COMBOBOX_I', 'DESCRICAO_UM', 'DESCRICAO_DOIS', 'PENF_EMAIL', 'FAVORECIDO_COBRA', 'FAVORECIDO_COBRA1']
for i in campos:
    Formulario[i].Habilitado = True

Formulario['COMBOBOX'].Itens = "1- Não atendimento às exigências contratuais;2- Atendimento parcial às exigências contratuais;3-Pleno atendimento às exigências contratuais"

Formulario['COMBOBOX_I'].Itens = "1- Não atendimento às exigências contratuais;2- Atendimento parcial às exigências contratuais;3-Pleno atendimento às exigências contratuais"
```
- Operação PR0001 Preencher Campos
  - COMBOBOX "Nota de Avaliação do Fiscal de Serviço" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
  - DESCRICAO_UM "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_UM] obrigatório
  - COMBOBOX_I "Nota de Avaliação do Fiscal Administrativo" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório
  - DESCRICAO_DOIS "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_DOIS] obrigatório
  - PENF_EMAIL "E-mails do Fornecedor que serão notificados sobre o IDF abaixo do esperado (separados por ponto e vírgula):" [TextBox String(2000) → CPE_PENF.PENF_EMAIL] obrigatório
  - FAVORECIDO_COBRA "Fiscal de Serviço" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - FAVORECIDO_COBRA1 "Gestor do Contrato" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_COBRA1] obrigatório
- Operação PR0001 Preencher Campos
  - GRID_IDF "Dados capturados" [DataGrid RecordList → Z_00143_GRID_IDF.GRID_IDF] — LarguraJanelaPopup=500
    - coluna FORNECEDOR obrigatório
**GRID_IDF.FORNECEDOR.ScriptModificado**
```python
OrdemServico['FORNECEDOR'] = FormularioRegistro['FORNECEDOR'].Valor
```
    - coluna DGCO obrigatório
    - coluna STATUS obrigatório
    - coluna IDF obrigatório
    - coluna ULTIMO_PERIODO obrigatório
    - coluna RISCO_APURADO
    - coluna QUALIDADE_IDF

### [348227] LinkInicial ""
Responsável: Fila CSC - Contratos (papel 688)
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=1662; Nome=RONY BALDOINO DA SILVA; FraseAssociacao=IDF Lote -> IDF Individual

### [348228] EventoIntermediarioMensagem "E-mail avaliação Fiscal"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: IDF - Notificação
Corpo do comunicado: Prezado Fornecedor OrdemServico.Customizado.FORNECEDOR1 
Contrato DGCO: OrdemServico.Customizado.DGCO_BB 
Último período apurado: OrdemServico.Customizado.PERIODO01 
Informamos que, na última Avaliação Trimestral de Fornecedores, o desempenho apresentado ficou abaixo do esperado, conforme evidenciado pelas notas atribuídas e pelas respectivas ocorrências registradas abaixo.
Esclarecemos que a avaliação realizada pelos fiscais do contrato possui caráter exclusivamente informativo, tendo por finalidade pré-notificar o fornecedor acerca dos pontos que necessitam de melhoria no cumprimento das obrigações contratuais.
Ressalta-se, ainda, que a referida avaliação possui caráter interno e não impli…
**ScriptEvento**
```python
if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
    
remetente = (OrdemServico.Responsavel).ToString()
Mensagem.Remetente = remetente
#OrdemServico.AdicionaComentario(Mensagem.Remetente, False)
result = "".join(Mensagem.Destinatarios)
#OrdemServico.AdicionaComentario(result, False)
```

### [348230] Tarefa "Aprovação"
Responsável: Responsável atual (papel 36)
Config: Codigo=TESTE
**ScriptFormCarregado**
```python
import clr
import System

from System import Convert, DBNull


def Texto(valor):
    try:
        if valor is None or valor == DBNull.Value:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


def DesabilitarCampo(campo):
    try:
        controle = Formulario[campo]
        controle.Habilitado = False
        return True

    except:
        return False


def PreencherCampo(campo, valor):
    try:
        controle = Formulario[campo]
        valorTexto = Texto(valor)

        if valorTexto != "":
            controle.Valor = valorTexto

        controle.Habilitado = False
        return True

    except:
        return False


# ============================================================
# DESABILITA OS CAMPOS DA TAREFA
# ============================================================

campos_desabilitados = [
    "COMBOBOX",
    "COMBOBOX_I",
    "PENF_EMAIL",
    "DESCRICAO_UM",
    "DESCRICAO_DOIS",
    "FAVORECIDO_COBRA",
    "FAVORECIDO_COBRA1"
]

for campo in campos_desabilitados:
    DesabilitarCampo(campo)


# ============================================================
# RECUPERA OS DADOS DA PRIMEIRA LINHA DA GRID_IDF
# ============================================================

nome_fornecedor = ""
numero_dgco = ""
ultimo_periodo = ""
erro_grid = ""

try:
    grid = OrdemServico.GetCustom("GRID_IDF")

    for linha in grid.Rows:

        nome_fornecedor = Texto(
            linha["FORNECEDOR"]
        )

        numero_dgco = Texto(
            linha["DGCO"]
        )

        ultimo_periodo = Texto(
            linha["ULTIMO_PERIODO"]
        )

        # Cada associada possui somente uma linha.
        break

except Exception as ex:
    erro_grid = Texto(ex)


# ============================================================
# PREENCHE OS CAMPOS DA TAREFA
# ============================================================

campos_nao_encontrados = []


if not PreencherCampo(
    "FORNECEDOR1",
    nome_fornecedor
):
    campos_nao_encontrados.append(
        "FORNECEDOR1"
    )


if not PreencherCampo(
    "DGCO_BB",
    numero_dgco
):
    campos_nao_encontrados.append(
        "DGCO_BB"
    )


if not PreencherCampo(
    "PERIODO01",
    ultimo_periodo
):
    campos_nao_encontrados.append(
        "PERIODO01"
    )


# ============================================================
# DIAGNÓSTICO
# ============================================================

mensagens = []

if erro_grid != "":
    mensagens.append(
        "Erro ao consultar a GRID_IDF: " +
        erro_grid
    )


if len(campos_nao_encontrados) > 0:
    mensagens.append(
        "Os seguintes controles não foram encontrados "
        "no formulário da tarefa corrente: " +
        ", ".join(campos_nao_encontrados) +
        ". Verifique se os campos foram adicionados à tarefa "
        "e confirme os nomes técnicos."
    )


if len(mensagens) > 0:
    try:
        Formulario.ExibeMensagem(
            "\n\n".join(mensagens)
        )
    except:
        pass
```
- Operação PR0002 Aprovar
  - (aprovação) COMBOBOX "Nota de Avaliação do Fiscal de Serviço" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
  - (aprovação) DESCRICAO_UM "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_UM]
  - (aprovação) COMBOBOX_I "Nota de Avaliação do Fiscal Administrativo" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I]
  - (aprovação) DESCRICAO_DOIS "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_DOIS]
  - (aprovação) DESCRICAO1 "E-mails do Fornecedor que serão notificados sobre o IDF abaixo do esperado (separados por ponto e vírgula):" [Memo String → CP_ORDEM_SERVICO.DESCRICAO1]
  - (aprovação) FAVORECIDO_COBRA "Fiscal de Serviço" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - (aprovação) FAVORECIDO_COBRA1 "Gestor do Contrato" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_COBRA1]
  - aprovador: Superior Imediato do Responsável (Unico)
- Operação PR0001 Preencher Campos
  - FORNECEDOR1 "Nome do fornecedor" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1] obrigatório
  - DGCO_BB "DGCO_BB" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
    - coluna BANCO obrigatório
    - coluna AGENCIA obrigatório
    - coluna CONTA_CORR obrigatório
    - coluna TIPO_CHAVE obrigatório
    - coluna CHAVE_PIX obrigatório
  - PERIODO01 "Último Período Avaliado" [TextBox String → CPE_CONTRATOS.PERIODO01] obrigatório
  - COMBOBOX "Nota de Avaliação do Fiscal de Serviço" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
  - DESCRICAO_UM "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_UM] obrigatório
  - COMBOBOX_I "Nota de Avaliação do Fiscal Administrativo" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório
  - DESCRICAO_DOIS "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_DOIS] obrigatório
  - FAVORECIDO_COBRA "Fiscal de Serviço" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - FAVORECIDO_COBRA1 "Gestor do Contrato" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_COBRA1] obrigatório
  - PENF_EMAIL "E-mails" [TextBox String(2000) → CPE_PENF.PENF_EMAIL] obrigatório

## Papéis usados
### papel 1125: Favorecido Cobra 1
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))

    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 688: Fila CSC - Contratos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Contratos
### papel 277: Favorecido Cobra
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))

    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```
### papel 601: Superior Imediato do Responsável
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
gestor = OrdemServico.Responsavel.Orgao.OrgaoPai.Gestor
Utils.LogError(gestor.ToString(), "erro")

Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Responsavel.ToString())
```

## Campos customizados usados (definição global)

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX

### DESCRICAO_UM — Descrições gerais
Memo String(2000) → CPE_CSC.DESCRICAO_UM

### COMBOBOX_I — COMBOBOX_I
DropDownList String → CPE_BOOTCAMP.COMBOBOX_I

### DESCRICAO_DOIS — Descrições gerais
Memo String(2000) → CPE_CSC.DESCRICAO_DOIS

### PENF_EMAIL — E-mails que serão notificados sobre o andamento da ordem de serviço (separados por ponto e vírgula)
TextBox String(2000) → CPE_PENF.PENF_EMAIL

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### FAVORECIDO_COBRA1 — Colaborador BBTS
DropDownList String → CPE_CONTRATOS.FAVORECIDO_COBRA1
Descrição: Para pesquisa rápida faça:
1 - Clique na seta à direita do campo para abrir a relação de nomes;
2 - Com a lista ABERTA, pressione as teclas Ctrl + F (no IE aparece uma caixa de texto na parte superior esquerda e no Chrome na parte superior direita);
3 -  Digite o nome (ou parte dele) a ser pesquisado (serão marcados todas ocorrências que correspondam ao texto digitado);
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### GRID_IDF — GRID_IDF
DataGrid RecordList → Z_00143_GRID_IDF.GRID_IDF
Colunas do registro:
- FORNECEDOR "FORNECEDOR" [TextBox String]
- DGCO "DGCO" [TextBox String]
- STATUS "STATUS" [TextBox String]
- IDF "IDF" [TextBox Integer]
- ULTIMO_PERIODO "Último Período Avaliado" [TextBox String]
- RISCO_APURADO "Risco Apurado" [TextBox String]
- QUALIDADE_IDF "Qualidade do IDF" [TextBox String]

### DESCRICAO1 — Caixa de texto
Memo String → CP_ORDEM_SERVICO.DESCRICAO1

### FORNECEDOR1 — Fornecedor
TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1

### DGCO_BB — DGCO
TextBox String(300) → CPE_FINANCEIRO.DGCO_BB

### PERIODO01 — Período 01
TextBox String → CPE_CONTRATOS.PERIODO01

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
