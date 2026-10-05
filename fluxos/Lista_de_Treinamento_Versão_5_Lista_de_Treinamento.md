# Fluxo: Lista de Treinamento (LISTREI) — versão 5
Caminho: Fluxos > Lista de Treinamento Versão 5 Lista de Treinamento
XML: `XMLs para teste/Lista_de_Treinamento_Versão_5_Lista_de_Treinamento.xml` | Supravizio 19.1.1 | SubProcessoId 20842 | DesenhoProcessoId 2929 | ProcessoId 692
Órgão dono: 2000004017 - GERENCIA DE REDE DE SERVICOS | Responsável: CARLOS ALBERTO REZENDE SOUZA NETO
Classe do subprocesso: DescricaoCliente=Lista de Treinamento; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Cadastro de Lista de treinamento (CADLISTATREINAMENTO)

## Grafo do fluxo
- [331856] Tarefa "Dados da FQ
" {Fila Assistência Técnica} → [331855] 
- [331855] EventoFinal "" → (fim)
- [331857] EventoInicial "" {Lista de treinamento - Equipes} → [331856] Dados da FQ


## Atividades

### [331856] Tarefa "Dados da FQ
"
Responsável: Fila Assistência Técnica (papel 1076)
**ScriptInicio**
```python
# Avança automaticamente para a próxima atividade

AvancaProximaAtividade = True
```

### [331855] EventoFinal ""

### [331857] EventoInicial ""
Responsável: Lista de treinamento - Equipes (papel 1440)
Config: PermiteCancelamentoAA=true; PermitirRascunho=true; Configuracao={"ServicoIniciador":"CADLISTATREINAMENTO"}
TipoSolicitacao: Lista de Treinamento
**ScriptValidacao**
```python
grid = OrdemServico.GetCustom('LISTA_PARTICIPANTES')

if grid.Rows.Count == 0:
    Criticas.AdicionaPendencia('Não foi registrado nenhum participante.')
    
grid2 = OrdemServico.GetCustom('LISTA_TREINAMENTO2')

if grid2.Rows.Count == 0:
    Criticas.AdicionaPendencia('Não foi registrado nenhum treinamento.')
    
if grid2.Rows.Count > 1:
    Criticas.AdicionaPendencia('Você só deve cadastrar um treinamento por vez.')
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=EXCEL
  - LABEL111 "<iframe width="1500" height="500" frameborder="0" scrolling="no" src="https://bbtecno.sharepoint.com/teams/Treinamento735/_layouts/15/Doc.aspx?sourcedoc={2f54373e-e58d-4d0d-a1d0-85a18b4d8384}&action=embedview&AllowTyping=True&ActiveCell='TRANSFERENCIA'!A2&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True&wdInConfigurator=True"></iframe>" [Label String(2000) → CPE_CONTRATOS.LABEL111] obrigatório
  - LABEL2 "<b style="font-size: 18px;">Precisa de Ajuda? Clique <a href="https://bbtecno.sharepoint.com/:v:/r/teams/Treinamento735/Documentos%20Compartilhados/Lista%20Supravizio/Abrir%20-%2018.1.1%20e%20mais%202%20p%C3%A1ginas%20-%20Trabalho%20%E2%80%94%20Microsoft_%20Edge%202025-04-08%2014-45-38.mp4?csf=1&web=1&e=CeG8hc" target="_blank"> AQUI </a> e veja um Tutorial!</b>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=ARQUIVO01
  - anexo "Planilha para atualização de Cursos" classes: Arquivo 01 — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=ARQUIVO; Configuracao={"FiltroArea":false}
  - anexo "Anexe AQUI a Lista de Treinamento Preenchida" classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Adicionar Treinamento
  - LISTA_TREINAMENTO2 "Treinamento realizado" [DataGrid RecordList → Z_00143_LISTA_TREINAMENTO2.LISTA_TREINAMENTO2] obrigatório — FormaEdicaoWeb=JanelaPopup; QtdColunasFormulario=3; PosicaoRotulo=Topo
**LISTA_TREINAMENTO2.ScriptAdicionado**
```python
NovoRegistro['MULTIPLICADOR2'] = 'N/A'
```
    - coluna NOME_PARTICIPANTE obrigatório
**LISTA_TREINAMENTO2.NOME_PARTICIPANTE.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if FormularioRegistro['NOME_PARTICIPANTE'].Valor != "":
    id_func = FormularioRegistro["NOME_PARTICIPANTE"].Valor
    funcionario = Pessoa.Carrega(Convert.ToInt32(id_func))

    query = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE PESSOA.ID_PESSOA = " + id_func + "")
    
    pes = Convert.ToInt32(FormularioRegistro['NOME_PARTICIPANTE'].Valor)
    pessoa = Pessoa.Carrega(pes)
    
    uor = DB.ExecuteScalar("Select ORGAO.DESCRICAO From PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO where PESSOA.NOME LIKE '"+ pessoa.ToString() +"'")
    
    if uor != None or uor != "":
        FormularioRegistro['UOR'].Valor = uor
        FormularioRegistro['UOR'].Habilitado = False
    else:
        FormularioRegistro['UOR'].Habilitado = True
    

    for i in query.Rows:
        matricula = i["MATRICULA"]
        
        if matricula != "":
            FormularioRegistro["MATRICULA"].Valor = matricula
            FormularioRegistro["MATRICULA"].Habilitado = False
        else:
            FormularioRegistro["MATRICULA"].Valor = ""
            FormularioRegistro["MATRICULA"].Habilitado = True
            
    FormularioRegistro['MODALIDADE'].Habilitado = False
    FormularioRegistro['ID_CURSO'].Habilitado = False
```
    - coluna MULTIPLICADOR2 obrigatório
    - coluna LOCALIDADE obrigatório
    - coluna HORARIO obrigatório
    - coluna MATRICULA obrigatório
    - coluna LOCAL_TRABALHO obrigatório
    - coluna DATA_FIM obrigatório
    - coluna MODALIDADE obrigatório
    - coluna SUPER obrigatório
    - coluna DATA obrigatório
    - coluna ID_CURSO obrigatório
    - coluna MULTIPLICADOR obrigatório
    - coluna UOR obrigatório
    - coluna APROVEITAMENTO obrigatório
    - coluna NOME_CURSO obrigatório
**LISTA_TREINAMENTO2.NOME_CURSO.ScriptModificado**
```python
curso = FormularioRegistro['NOME_CURSO']
id = FormularioRegistro['ID_CURSO']
modalidade = FormularioRegistro['MODALIDADE']
prof = FormularioRegistro['MULTIPLICADOR2']

nomes = ["Andre Luis de Sena Jacinto", "Andre Luiz Nunes", "Andre Luiz Pires de Oliveira", "Antonio Veloso de Alencar", "Ayrton Silva de Macedo", "Bruno Antunes Camargo", "Cesar Adriano Georgetti", "Claudio Silva dos Santos", "Claudionor Rabelo Pamplona", "Denise Cassol de Campos", "Douglas Natario dos Santos", "Edson Henrique Vives Junior", "Eduardo Cesar Netto Duarte", "Eduardo Malta Fernandes", "Fabian Favaro", "Fabio Correa", "Fabio Gomes de Souza", "Fabio Muller", "Francisco de Assis Araujo Suzart", "Gerardo Caleb Ortiz Elgueta", "Gilson Horst", "Ivson Soares Pereira", "Joao Cesar Levandowski", "Josue Jorge Andrade", "Jupira Tarima de Carvalho Roncaglio", "Leonardo Roberto da Paixao", "Livingstone Pacheco dos Santos", "Louise Amanda dos Santos", "Luciano Izidoro Goncalves", "Luiz Gomes Fernandes", "Magno Almeida Cadengue", "Marcelo Henrique Braga da Luz", "Marco Antonio Zago", "Marcos Jose Barboza da Paz Junior", "Mario da Mota Rocumback", "Paris Anderson Geraldo Correa", "Patricio Lofy", "Paulo Aldebara Santana dos Anjos", "Rejane Dolores Vieira", "Renato Bastos Ferreira", "Risocleide Batista da Silva", "Ruth Cristina de Oliveira Ferraz Martins", "Sebastiao Pires de Freitas Neto", "Tony Itiro Tamaru", "Vanderley Pereira dos Santos", "Yasmim Fonseca Vianna", "--"]


if curso.Valor == "CDO - COMUNICAÇÃO COM A O CLIENTE CEMAN - ONLINE":
    id.Valor = "A001"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "CONTROLE DE CHAMADOS EBS/TOA - ONLINE":
    id.Valor = "A002"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DOCA - CONTROLE ACESSO - PRESENCIAL":
    id.Valor = "A003"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "DOCA - CONTROLE ACESSO - ONLINE":
    id.Valor = "A004"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DODR - GERADOR DE NEBLINA E LUZ ESTROBOSCÓPICA - PRESENCIAL":
    id.Valor = "A005"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "DODR - GERADOR DE NEBLINA E LUZ ESTROBOSCÓPICA - TRILHA 1 - ONLINE":
    id.Valor = "A006"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DODR - GERADOR DE NEBLINA E LUZ ESTROBOSCÓPICA - TRILHA 2 - ONLINE":
    id.Valor = "A007"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DODR - GERADOR DE NEBLINA E LUZ ESTROBOSCÓPICA - TRILHA 3 - ONLINE":
    id.Valor = "A008"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DOSA - PRESENCIAL":
    id.Valor = "A009"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "DOSI - PRESENCIAL":
    id.Valor = "A010"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "DOSI - TRILHA 1 - ONLINE":
    id.Valor = "A011"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DOSI - TRILHA 2 - ONLINE":
    id.Valor = "A012"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DOSI - TRILHA 3 - ONLINE":
    id.Valor = "A013"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DOSI - TRILHA 4 - ONLINE":
    id.Valor = "A014"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DOSI - TRILHA 5 - ONLINE":
    id.Valor = "A015"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "IMPLANTAÇÃO DO PVV - PRESENCIAL":
    id.Valor = "A016"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "IMPRESSÃO 3D - ONLINE":
    id.Valor = "A017"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "MIGRAÇÃO DE SUPRIDORA - ONLINE":
    id.Valor = "A018"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "OFICINA DAS ESTRUTURAS PGDM - PRESENCIAL":
    id.Valor = "A019"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "ORGANIZAÇÃO E MANUTENÇÃO DE SALA ONLINE - PRESENCIAL":
    id.Valor = "A020"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "PROCEDIMENTO DE ESTOQUES - ONLINE":
    id.Valor = "A021"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "SUPORTE AO CLIENTE: CHATBOT TAATI E MÉTRICAS DE SATISFAÇÃO - ONLINE":
    id.Valor = "A022"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA DIEBOLD 2014 COM ENTINTAMENTO - PRESENCIAL":
    id.Valor = "A024"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA OKI NMD E WINCOR V2019 E 2012 - PRESENCIAL":
    id.Valor = "A025"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA PERTO TMF - 21 V13 - PRESENCIAL":
    id.Valor = "A026"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA PERTO TS2100F V 19 - PRESENCIAL":
    id.Valor = "A027"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA PERTO TS2100F V 19 - ONLINE":
    id.Valor = "A028"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA TAAMC FULL TRASEIRO OKI ATM FULL 1502 C/ENTINTAMENTO - PRESENCIAL":
    id.Valor = "A029"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA TAAMC SUPERFULL TRASEIRO PERTO TMD 2100 V 20 - PRESENCIAL":
    id.Valor = "A030"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA TAAMC SUPERFULL TRASEIRO PERTO TMD 2100 V 20 - ONLINE":
    id.Valor = "A031"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA TAART TRASEIRO PERTO TMR2200 V19 - PRESENCIAL":
    id.Valor = "A032"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA TAART TRASEIRO PERTO TMR2200 V19 - ONLINE":
    id.Valor = "A033"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA PERTO TMR 21 V22 - FRONTAL / TMRD 2200 V22 - CHEQUE - PRESENCIAL":
    id.Valor = "A034"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TAA PERTO TMR 21 V22 - FRONTAL / TMRD 2200 V22 - CHEQUE - ONLINE":
    id.Valor = "A035"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 - PRESENCIAL":
    id.Valor = "A036"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 - ONLINE":
    id.Valor = "A037"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 - EXPLORAÇÃO DE JIG - PRESENCIAL":
    id.Valor = "A038"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 - VÍDEOS AULAS - ONLINE":
    id.Valor = "A039"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "TAATI - PRESENCIAL":
    id.Valor = "A040"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "VCOM - VISUAL CAPACITY OPTIMIZATION MANAGER - ONLINE":
    id.Valor = "A041"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "CDB (I) - ONLINE":
    id.Valor = "A042"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "CFTV (I) - PRESENCIAL":
    id.Valor = "A043"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "TERMINAL RECICLADOR TAART DIEBOLD V17 - EXPLORAÇÃO DE JIG (FORNECEDOR) - PRESENCIAL":
    id.Valor = "A044"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "NOBREAKE - PRESENCIAL":
    id.Valor = "A045"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "OKI ENTINTADO 2015 / 2016 - PRESENCIAL":
    id.Valor = "A046"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "PERTO 2013/2014 HÍBRIDO (INTERNO) - PRESENCIAL":
    id.Valor = "A047"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "PERTO RECICLADOR (FORNECEDOR) - PRESENCIAL":
    id.Valor = "A048"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "PERTO SUPERFULL (FORNECEDOR) (TMD2100 V20) - PRESENCIAL":
    id.Valor = "A049"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "PERTO TS2100 (FORNECEDOR) (TAA Saque Frontal) - PRESENCIAL":
    id.Valor = "A050"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "PILOTO EAD ALARME - ONLINE":
    id.Valor = "A051"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "SISTEMAS DE ALARMES VIAWEB - PRESENCIAL":
    id.Valor = "A052"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 (FORNECEDOR) - PRESENCIAL":
    id.Valor = "A053"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "WORKSHOP - DOSA Sensores Bosch (FORNECEDOR) - PRESENCIAL":
    id.Valor = "A054"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "WORKSHOP CATRACAS (FORNECEDOR) - PRESENCIAL":
    id.Valor = "A055"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "WORKSHOP FECHADURA DO COFRE (FORNECEDOR) - PRESENCIAL":
    id.Valor = "A056"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "WORKSHOP FECHADURAS (FORNECEDOR) - PRESENCIAL":
    id.Valor = "A057"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "DOSA ALARME V.2 - ONLINE":
    id.Valor = "A058"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "DOSA ALARME V.2 - PRESENCIAL":
    id.Valor = "A059"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "RASTREADOR DE ATIVOS - PRESENCIAL":
    id.Valor = "A060"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "DOSI V.2 - ONLINE":
    id.Valor = "A061"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "IMPRESSORA 3D CREALITY K1 MAX - PRESENCIAL":
    id.Valor = "A062"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

elif curso.Valor == "PGDM/ECLUSA – Detectores de Metais - ONLINE":
    id.Valor = "A063"
    id.Habilitado = False
    modalidade.Valor = "ONLINE"
    modalidade.Habilitado = False

elif curso.Valor == "PGDM/ECLUSA – Detectores de Metais - PRESENCIAL":
    id.Valor = "A064"
    id.Habilitado = False
    modalidade.Valor = "PRESENCIAL"
    modalidade.Habilitado = False

else:
    Formulario.ExibeMensagem("Nenhuma opção informada")

modalidade_detectada = (
    modalidade.Valor if modalidade.Valor
    else ("ONLINE" if "ONLINE" in curso.Valor else ("PRESENCIAL" if "PRESENCIAL" in curso.Valor else ""))
)

if modalidade_detectada == "PRESENCIAL":
    FormularioRegistro['MULTIPLICADOR2'].Habilitado = False
    
elif modalidade_detectada == "ONLINE":
    FormularioRegistro['MULTIPLICADOR2'].Habilitado = True
    FormularioRegistro['MULTIPLICADOR2'].Valor = ""
    FormularioRegistro['MULTIPLICADOR2'].Itens = nomes
```
  - LABEL1 "<p style="display: flex; color: yellow; font-weight: 800; background-color: blue; border-radius: 16px; padding: 2%; justify-content: center; text-align: center; font-weight: 600;">Prezado(a), <br>Para garantir o sucesso na importação da lista para o Supravizio, é imprescindível que todas as informações estejam preenchidas de forma completa e correta. <br>  Ressaltamos que campos em branco podem impedir a conclusão do fluxo, sendo essencial revisar os dados antes do envio.</p>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Adicionar participante
  - LISTA_PARTICIPANTES "Lista de Participantes" [DataGrid RecordList → Z_00143_LISTA_PARTICIPANTES.LISTA_PARTICIPANTES] obrigatório — PosicaoRotulo=Topo
    - coluna NOME_PARTICIPANTE obrigatório
**LISTA_PARTICIPANTES.NOME_PARTICIPANTE.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if FormularioRegistro['NOME_PARTICIPANTE'].Valor != "":
    id_func = FormularioRegistro["NOME_PARTICIPANTE"].Valor
    funcionario = Pessoa.Carrega(Convert.ToInt32(id_func))
 
    query = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE PESSOA.ID_PESSOA = " + id_func + "")
    pes = Convert.ToInt32(FormularioRegistro['NOME_PARTICIPANTE'].Valor)
    pessoa = Pessoa.Carrega(pes)
    uor = DB.ExecuteScalar("Select ORGAO.DESCRICAO From PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO where PESSOA.NOME LIKE '"+ pessoa.ToString() +"'")
    if uor != None or uor != "":
        FormularioRegistro['UOR'].Valor = uor
        #FormularioRegistro['UOR'].Habilitado = False
        FormularioRegistro['UOR'].Visivel = True
    else:
        FormularioRegistro['UOR'].Habilitado = True

 
    for i in query.Rows:
        matricula = i["MATRICULA"]
        if matricula != "":
            FormularioRegistro["MATRICULA"].Valor = matricula
            FormularioRegistro["MATRICULA"].Habilitado = False
        else:
            FormularioRegistro["MATRICULA"].Valor = ""
            FormularioRegistro["MATRICULA"].Habilitado = True
```
    - coluna MATRICULA obrigatório
    - coluna UOR obrigatório
    - coluna APROVEITAMENTO obrigatório

## Papéis usados
### papel 1076: Fila Assistência Técnica
Tipo=RelacaoPessoas | pessoas: Fila Assistência Técnica
### papel 1440: Lista de treinamento - Equipes
Tipo=RelacaoOrgaos

## Campos customizados usados (definição global)

### LABEL111 — Texto Informativo
Label String(2000) → CPE_CONTRATOS.LABEL111
Descrição: Texto informativo

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

### LISTA_TREINAMENTO2 — Lista de Treinamento
DataGrid RecordList → Z_00143_LISTA_TREINAMENTO2.LISTA_TREINAMENTO2
Colunas do registro:
- NOME_CURSO "Nome do Curso" [DropDownList String]
**NOME_CURSO.LookupScript**
```python
cursos = ["CDO - COMUNICAÇÃO COM A O CLIENTE CEMAN - ONLINE", "CONTROLE DE CHAMADOS EBS/TOA - ONLINE", "DOCA - CONTROLE ACESSO - PRESENCIAL", "DOCA - CONTROLE ACESSO - ONLINE", "DODR - GERADOR DE NEBLINA E LUZ ESTROBOSCÓPICA - PRESENCIAL", "DODR - GERADOR DE NEBLINA E LUZ ESTROBOSCÓPICA - TRILHA 1 - ONLINE", "DODR - GERADOR DE NEBLINA E LUZ ESTROBOSCÓPICA - TRILHA 2 - ONLINE", "DODR - GERADOR DE NEBLINA E LUZ ESTROBOSCÓPICA - TRILHA 3 - ONLINE", "DOSA - PRESENCIAL", "DOSI - PRESENCIAL", "DOSI - TRILHA 1 - ONLINE", "DOSI - TRILHA 2 - ONLINE", "DOSI - TRILHA 3 - ONLINE", "DOSI - TRILHA 4 - ONLINE", "DOSI - TRILHA 5 - ONLINE", "IMPLANTAÇÃO DO PVV - PRESENCIAL", "IMPRESSÃO 3D - ONLINE", "MIGRAÇÃO DE SUPRIDORA - ONLINE", "OFICINA DAS ESTRUTURAS PGDM - PRESENCIAL", "ORGANIZAÇÃO E MANUTENÇÃO DE SALA ONLINE - PRESENCIAL", "PROCEDIMENTO DE ESTOQUES - ONLINE", "SUPORTE AO CLIENTE: CHATBOT TAATI E MÉTRICAS DE SATISFAÇÃO - ONLINE", "T-10 TAA DIEBOLD 2014 COM ENTINTAMENTO - PRESENCIAL", "T-10 TAA OKI NMD E WINCOR V2019 E 2012 - PRESENCIAL", "T-10 TAA PERTO TMF - 21 V13 - PRESENCIAL", "T-10 TAA PERTO TS2100F V 19 - PRESENCIAL", "T-10 TAA PERTO TS2100F V 19 - ONLINE", "T-10 TAA TAAMC FULL TRASEIRO OKI ATM FULL 1502 C/ENTINTAMENTO - PRESENCIAL", "T-10 TAA TAAMC SUPERFULL TRASEIRO PERTO TMD 2100 V 20 - PRESENCIAL", "T-10 TAA TAAMC SUPERFULL TRASEIRO PERTO TMD 2100 V 20 - ONLINE", "T-10 TAA TAART TRASEIRO PERTO TMR2200 V19 - PRESENCIAL", "T-10 TAA TAART TRASEIRO PERTO TMR2200 V19 - ONLINE", "T-10 TAA PERTO TMR 21 V22 - FRONTAL / TMRD 2200 V22 - CHEQUE - PRESENCIAL", "T-10 TAA PERTO TMR 21 V22 - FRONTAL / TMRD 2200 V22 - CHEQUE - ONLINE", "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 - PRESENCIAL", "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 - ONLINE", "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 - EXPLORAÇÃO DE JIG - PRESENCIAL", "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 - VÍDEOS AULAS - ONLINE", "TAATI - PRESENCIAL", "VCOM - VISUAL CAPACITY OPTIMIZATION MANAGER - ONLINE", "CDB (I) - ONLINE", "CFTV (I) - PRESENCIAL", "TERMINAL RECICLADOR TAART DIEBOLD V17 - EXPLORAÇÃO DE JIG (FORNECEDOR) - PRESENCIAL", "NOBREAKE - PRESENCIAL", "OKI ENTINTADO 2015 / 2016 - PRESENCIAL", "PERTO 2013/2014 HÍBRIDO (INTERNO) - PRESENCIAL", "PERTO RECICLADOR (FORNECEDOR) - PRESENCIAL", "PERTO SUPERFULL (FORNECEDOR) (TMD2100 V20) - PRESENCIAL", "PERTO TS2100 (FORNECEDOR) (TAA Saque Frontal) - PRESENCIAL", "PILOTO EAD ALARME - ONLINE", "SISTEMAS DE ALARMES VIAWEB - PRESENCIAL", "T-10 TERMINAL RECICLADOR TAART DIEBOLD V17 (FORNECEDOR) - PRESENCIAL", "WORKSHOP - DOSA Sensores Bosch (FORNECEDOR) - PRESENCIAL", "WORKSHOP CATRACAS (FORNECEDOR) - PRESENCIAL", "WORKSHOP FECHADURA DO COFRE (FORNECEDOR) - PRESENCIAL", "WORKSHOP FECHADURAS (FORNECEDOR) - PRESENCIAL", "DOSA ALARME V.2 - ONLINE", "DOSA ALARME V.2 - PRESENCIAL", "RASTREADOR DE ATIVOS - PRESENCIAL", "DOSI V.2 - ONLINE", "IMPRESSORA 3D CREALITY K1 MAX - PRESENCIAL", "PGDM/ECLUSA ¿ Detectores de Metais - ONLINE", "PGDM/ECLUSA ¿ Detectores de Metais - PRESENCIAL"]



Itens = cursos
```
- ID_CURSO "ID Curso" [TextBox String]
- MODALIDADE "Modalidade" [TextBox String]
- MULTIPLICADOR "MULTIPLICADOR" [DropDownList String]
**MULTIPLICADOR.LookupScript**
```python
nomes = ["Andre Luis de Sena Jacinto", "Andre Luiz Nunes", "Andre Luiz Pires de Oliveira", "Antonio Veloso de Alencar", "Ayrton Silva de Macedo", "Bruno Antunes Camargo", "Cesar Adriano Georgetti", "Claudio Silva dos Santos", "Claudionor Rabelo Pamplona", "Denise Cassol de Campos", "Douglas Natario dos Santos", "Edson Henrique Vives Junior", "Eduardo Cesar Netto Duarte", "Eduardo Malta Fernandes", "Fabian Favaro", "Fabio Correa", "Fabio Gomes de Souza", "Fabio Muller", "Francisco de Assis Araujo Suzart", "Gerardo Caleb Ortiz Elgueta", "Gilson Horst", "Ivson Soares Pereira", "Joao Cesar Levandowski", "Josue Jorge Andrade", "Jupira Tarima de Carvalho Roncaglio", "Leonardo Roberto da Paixao", "Livingstone Pacheco dos Santos", "Louise Amanda dos Santos", "Luciano Izidoro Goncalves", "Luiz Gomes Fernandes", "Magno Almeida Cadengue", "Marcelo Henrique Braga da Luz", "Marco Antonio Zago", "Marcos Jose Barboza da Paz Junior", "Mario da Mota Rocumback", "Paris Anderson Geraldo Correa", "Patricio Lofy", "Paulo Aldebara Santana dos Anjos", "Rejane Dolores Vieira", "Renato Bastos Ferreira", "Risocleide Batista da Silva", "Ruth Cristina de Oliveira Ferraz Martins", "Sebastiao Pires de Freitas Neto", "Tony Itiro Tamaru", "Vanderley Pereira dos Santos", "Yasmim Fonseca Vianna"]

Itens = nomes
```
- MULTIPLICADOR2 "MULTIPLICADOR2" [DropDownList String]
**MULTIPLICADOR2.LookupScript**
```python
nomes = ["Andre Luis de Sena Jacinto", "Andre Luiz Nunes", "Andre Luiz Pires de Oliveira", "Antonio Veloso de Alencar", "Ayrton Silva de Macedo", "Bruno Antunes Camargo", "Cesar Adriano Georgetti", "Claudio Silva dos Santos", "Claudionor Rabelo Pamplona", "Denise Cassol de Campos", "Douglas Natario dos Santos", "Edson Henrique Vives Junior", "Eduardo Cesar Netto Duarte", "Eduardo Malta Fernandes", "Fabian Favaro", "Fabio Correa", "Fabio Gomes de Souza", "Fabio Muller", "Francisco de Assis Araujo Suzart", "Gerardo Caleb Ortiz Elgueta", "Gilson Horst", "Ivson Soares Pereira", "Joao Cesar Levandowski", "Josue Jorge Andrade", "Jupira Tarima de Carvalho Roncaglio", "Leonardo Roberto da Paixao", "Livingstone Pacheco dos Santos", "Louise Amanda dos Santos", "Luciano Izidoro Goncalves", "Luiz Gomes Fernandes", "Magno Almeida Cadengue", "Marcelo Henrique Braga da Luz", "Marco Antonio Zago", "Marcos Jose Barboza da Paz Junior", "Mario da Mota Rocumback", "Paris Anderson Geraldo Correa", "Patricio Lofy", "Paulo Aldebara Santana dos Anjos", "Rejane Dolores Vieira", "Renato Bastos Ferreira", "Risocleide Batista da Silva", "Ruth Cristina de Oliveira Ferraz Martins", "Sebastiao Pires de Freitas Neto", "Tony Itiro Tamaru", "Vanderley Pereira dos Santos", "Yasmim Fonseca Vianna"]

Itens = nomes
```
- DATA "Data Início" [DatePicker DateTime]
- DATA_FIM "Data Fim" [DatePicker DateTime]

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### LISTA_PARTICIPANTES — Lista de Participantes
DataGrid RecordList → Z_00143_LISTA_PARTICIPANTES.LISTA_PARTICIPANTES
Colunas do registro:
- NOME_PARTICIPANTE "Nome do Participante" [DropDownList String]
**NOME_PARTICIPANTE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```
- MATRICULA "Matricula" [TextBox String]
- UOR "UOR" [DropDownList String]
**UOR.LookupScript**
```python
#
```
- APROVEITAMENTO "Aproveitamento" [TextBox String]

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
