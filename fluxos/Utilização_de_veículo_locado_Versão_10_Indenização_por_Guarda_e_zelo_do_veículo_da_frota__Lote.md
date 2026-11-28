# Fluxo: Indenização por Guarda e zelo do veículo da frota (Lote) (INDVEICULOFROTALOTE) — versão 10
Caminho: Fluxos > Utilização de veículo locado Versão 10 Indenização por Guarda e zelo do veículo da frota (Lote)
XML: `XMLs para teste/Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml` | Supravizio 19.1.1 | SubProcessoId 20510 | DesenhoProcessoId 2888 | ProcessoId 405
Órgão dono: 2000004019 - DIVISAO DE APOIO A REDE DE SERVICOS | Responsável: CARLOS ALBERTO REZENDE SOUZA NETO
Classe do subprocesso: Objetivo=Indenização por Guarda e zelo do veículo da frota (Lote); DescricaoCliente=Indenização por Guarda e zelo do veículo da frota (Lote); CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Orgao; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Indenização por guarda e zelo do veículo locado (INDENIZAGUARD)

## Grafo do fluxo
- [327200] EventoInicial "" → [327202] Abertura em Lote (Indenização por Lotação de Veícu
- [327201] EventoFinal "" → (fim)
- [327202] SubProcesso "Abertura em Lote (Indenização por Lotação de Veículo Locado)" {Responsável atual} → [327201] 

## Atividades

### [327200] EventoInicial ""
Config: Configuracao={"ServicoIniciador":"INDENIZAGUARD"}
TipoSolicitacao: Serviços para veículo locado
**ScriptValidacao**
```python
grid = OrdemServico.GetCustom('GRID_FROTA')
matricula = ''

for i in grid.Rows:
    matricula = i['MATRICULA'].ToString()
    query = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, PESSOA.NOME From CP_PESSOA Inner Join PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA = '"+ matricula +"'")
    if query.Rows.Count == 0 or query.Rows.Count == None:
        Criticas.AdicionaPendencia("ATENCÃO!\nA MATRICULA {} NÃO É VALIDA. POR FAVOR, REVISE.".format(matricula.ToString()))
```
**ScriptFormCarregado**
```python
Formulario['GRID_FROTA'].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Planilha Preenchida" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - LABEL_GRANDE "<div style="display: flex; align-items: center; width: 100%; background: linear-gradient(145deg,black, blue,black); border-radius: 16px; padding: 2%;"><b style="font-size: 22px; color: yellow;">Clique <a href="https://bbtecno-my.sharepoint.com/:x:/g/personal/ext-douglas_moura_bbts_com_br/EbsPhVToRm1PtH-p4pVyigYB4wvFK766FSrapeMdx9ciDQ?download=1" target="_blank" style="text-decoration: none; color: red;"> AQUI </a> para baixar a planilha modelo desse fluxo.</b></div>" [Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE] obrigatório
  - CHECKBOX10 "Clique aqui para carregar as informações" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX10] obrigatório
**CHECKBOX10.ScriptModificado**
```python
if Controle.Valor == True:
    if OrdemServico.PossuiItem("ARQUIVO"):
        
        import clr
        import System
        clr.AddReference("System.Data")
        from System.Data import DataSet
        from System.Data.OleDb import OleDbConnection, OleDbDataAdapter, OleDbCommand
        from System import Convert

        def readExcel(nomesCampos, nomeGrid):
        
            repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
            anexo = OrdemServico.ObtemItem("ARQUIVO")
            _Arquivo = repositorio + "\\" + anexo.Localizacao
            _StringConexao = String.Format(
                "Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties='Excel 12.0 Xml;HDR=YES;ReadOnly=False';",
                _Arquivo
            )

            conexao = OleDbConnection(_StringConexao)
            adapter = OleDbDataAdapter('SELECT * FROM [LOTE$]', conexao)

            ds = DataSet()
            conexao.Open()
            adapter.Fill(ds)

            
            
            for linha in ds.Tables[0].Rows:
                linhaVazia = (not linha["MATRICULA"] and not linha["DIAS"] and not linha["MÊS REFERENCIA"] and not linha["ANO REFERENCIA"] and not linha["VALOR"])
                if linhaVazia:
                    continue

                if (not linha["MATRICULA"] and not linha["DIAS"] and not linha["MÊS REFERENCIA"] and not linha["ANO REFERENCIA"] and not linha["VALOR"]):
                    continue

                matricula =     Convert.ToDecimal(linha["MATRICULA"])
                dias =          linha['DIAS'].ToString()
                mes =           linha['MÊS REFERENCIA'].ToString()
                ano =           linha['ANO REFERENCIA'].ToString()
                valor =         round(Convert.ToDecimal(linha['VALOR']), 2).ToString()
                int_pro =       linha['INTEGRAL OU PROPORCIONAL'].ToString()

                Formulario.ExibeMensagem(matricula.ToString())
                dados = DB.ExecuteDataTable("Select Distinct To_Char(p.ID_PESSOA) As id_pessoa, p.NOME || ' (' || p.USUARIO_REDE || ') - ' || f.status_matricula As nomemat, ORGAO.DESCRICAO From CAD_FUNCIONARIO_V f Inner Join CP_PESSOA cp On f.matricula = cp.matricula Inner Join PESSOA p On cp.ID_PESSOA = p.id_pessoa Inner Join ORGAO On p.ID_ORGAO = ORGAO.ID_ORGAO Where cp.MATRICULA = '"+ matricula.ToString() +"' Order By nomemat")

                
                for i in dados.Rows:
                    id = i['ID_PESSOA'].ToString()
                    funcionario = i['NOMEMAT'].ToString()
                    uor = i['DESCRICAO'].ToString()

                valores = [id, funcionario, matricula, uor, dias, mes, ano, valor, int_pro]
                OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, valores)

            Formulario["CHECKBOX10"].Habilitado = False
            conexao.Close()

        readExcel(["ID_FUNCIONARIO","FUNCIONARIO", "MATRICULA", "UOR", "DIAS", "MES_REFERENCIA","ANO_REFERENCIA","VALOR", "INT_PRO"], 'GRID_FROTA')
        Formulario.ExibeMensagem("Importação feita com sucesso!\nTotal de linhas importadas: "+ OrdemServico.GetCustom('GRID_FROTA').Rows.Count.ToString())
    else:
        Formulario.ExibeMensagem("Não tem Arquivo anexado para importação.")
        Controle.Valor = False

# =====================================================================================
```
  - GRID_FROTA "Informações da Frota" [DataGrid RecordList → Z_00143_GRID_FROTA.ID_ITEM] obrigatório
    - coluna DIAS obrigatório
    - coluna MES_REFERENCIA obrigatório
    - coluna ANO_REFERENCIA obrigatório
    - coluna VALOR obrigatório
    - coluna FUNCIONARIO obrigatório
    - coluna UOR obrigatório
    - coluna ID_FUNCIONARIO obrigatório
    - coluna INT_PRO obrigatório
    - coluna MATRICULA obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Nota Técnica" classes: Anexo — RequeridoInicial=true

### [327201] EventoFinal ""

### [327202] SubProcesso "Abertura em Lote (Indenização por Lotação de Veículo Locado)"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1470; Configuracao={"ExibirBotaoNovaSubprocessos":false, "ValidacaoFinalizacao":"Finaliza\u00e7\u00e3o da ocorr\u00eancia"}
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
grid = OrdemServico.GetCustom('GRID_FROTA')

#OrdemServico.AdicionaComentario(id.ToString(), True)
    
for linha in grid.Rows:
    matricula = linha['MATRICULA']

    dados = DB.ExecuteDataTable("Select P.NOME, CP.MATRICULA, ORGAO.DESCRICAO, P.ID_PESSOA From PESSOA P Inner Join CP_PESSOA CP On P.ID_PESSOA = CP.ID_PESSOA Inner Join ORGAO On ORGAO.ID_ORGAO = P.ID_ORGAO Where CP.MATRICULA = '"+ matricula.ToString()+ "'")
    
    id = 0
    for i in dados.Rows:
        id = Convert.ToInt32(i['ID_PESSOA'])
        
    #OrdemServico.AdicionaComentario(Pessoa.Carrega(id).ToString(), True)    

    sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
    
    sub.Cliente = Pessoa.Carrega(id)
    sub.Assunto = "Indenização por Guarda e zelo de veículo Locado (Lote)"
    
    #Preenchimento dos campos:
    #sub["NOME_NOME"] =          linha["FUNCIONARIO"].ToString() # ok
    sub['TE_MATRICULA'] =       linha['MATRICULA'].ToString()   # ok
    sub['TE_UOR'] =             linha['UOR'].ToString()         # ok
    sub['VALOR_QUALIF'] =       Convert.ToDecimal(linha['DIAS'])    # ok
    sub['MES_REFERENCIA'] =     linha['MES_REFERENCIA'].ToString()  # 
    sub['ANO_REF'] =            linha['ANO_REFERENCIA'].ToString()  # 
    sub['TE_VALOR_REEMBOLSO'] = Convert.ToDecimal(linha['VALOR'].ToString())    #ok
    sub['ID_PERSON'] =          linha['ID_FUNCIONARIO'].ToString()
    sub['SIM_NAO'] =            linha['INT_PRO'].ToString()
    
    
    sub.Salva()
    sub.AvancaAtividade()
    
    

AvancaProximaAtividade = True
```
- Associação: Ativo=true; FraseAssociacao=Ind. Guarda e Zelo (LOTE) --> Base; FraseInversaAssociacao=Ind. Guarda e Zelo (BASE) --> Lote; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=INDLOTEPARABASE; SeparadorSequencial=. | fonte: Indenização por Guarda e zelo do veículo da frota (Lote) → alvo: Indenização por Guarda e Zelo do Veículo Locado

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

## Campos customizados usados (definição global)

### LABEL_GRANDE — Label Grande
Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE

### CHECKBOX10 — Checkbox10
CheckBox Boolean → CPE_PESSOAS.CHECKBOX10

### GRID_FROTA — Grid Frota
DataGrid RecordList → Z_00143_GRID_FROTA.ID_ITEM
Colunas do registro:
- FUNCIONARIO "Funcionário" [TextBox String]
- MATRICULA "Matrícula" [TextBox String]
- DIAS "Dias" [TextBox String]
- MES_REFERENCIA "Mês de referência" [TextBox String]
- ANO_REFERENCIA "Ano de Referência" [TextBox String]
- VALOR "Valor" [TextBox String]
- UOR "UOR" [TextBox String]
- INT_PRO "Integral ou Proporcional" [TextBox String]
- ID_FUNCIONARIO "ID_FUNCIONARIO" [TextBox Integer]

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
