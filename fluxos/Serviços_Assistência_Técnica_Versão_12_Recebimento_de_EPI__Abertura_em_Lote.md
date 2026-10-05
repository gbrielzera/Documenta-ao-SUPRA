# Fluxo: Recebimento de EPI (Abertura em Lote) (RECEBIMENTOEPILOTE) — versão 12
Caminho: Fluxos > Serviços Assistência Técnica Versão 12 Recebimento de EPI (Abertura em Lote)
XML: `XMLs para teste/Serviços_Assistência_Técnica_Versão_12_Recebimento_de_EPI_(Abertura_em_Lote).xml` | Supravizio 19.1.1 | SubProcessoId 21091 | DesenhoProcessoId 2947 | ProcessoId 31
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Recebimento de EPI (RECEBIMENTOEPI)

## Grafo do fluxo
- [336290] EventoFinal "" → (fim)
- [336288] EventoInicial "" {Dires} → [336289] 
- [336289] SubProcesso "" {Dires} → [336290] 

## Atividades

### [336290] EventoFinal ""

### [336288] EventoInicial ""
Responsável: Dires (papel 1380)
TipoSolicitacao: Recebimento de EPI
- Operação PR0001 Preencher Campos
  - EQUIP_EPI_LOTE "Equipamentos EPI Lote" [DataGrid RecordList → Z_00143_EQUIP_EPI_LOTE.EQUIP_EPI_LOTE] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna UOR obrigatório
    - coluna CA obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna UNIDADE obrigatório
    - coluna RETIRADA obrigatório
    - coluna CARGO obrigatório
    - coluna FUNCAO obrigatório
    - coluna NOME obrigatório
    - coluna ITEM obrigatório
    - coluna CODIGO obrigatório
    - coluna DESCRICAO obrigatório
    - coluna MATRICULA obrigatório
  - CHECKBOX1 "Clique aqui para ler a planilha" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1] obrigatório
**CHECKBOX1.ScriptModificado**
```python
if Controle.Valor == True:
    if OrdemServico.PossuiItem("ARQUIVO"):

        import clr
        import System
        clr.AddReference("System.Data")
        from System.Data import DataSet
        from System.Data.OleDb import OleDbConnection, OleDbDataAdapter
        from System import String, DBNull

        def readExcel(nomesCampos, nomeGrid):

            repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
            anexo = OrdemServico.ObtemItem("ARQUIVO")
            _Arquivo = repositorio + "\\" + anexo.Localizacao

            _StringConexao = String.Format(
                "Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties='Excel 12.0 Xml;HDR=YES;ReadOnly=False';",
                _Arquivo
            )

            #Formulario.ExibeMensagem("teste 1")
            conexao = OleDbConnection(_StringConexao)

            cmd_text = ("SELECT [NOME],[ITEM],[RETIRADA],[QUANTIDADE] FROM [EPI$] WHERE [NOME] IS NOT NULL AND [ITEM] IS NOT NULL AND [RETIRADA] IS NOT NULL AND [QUANTIDADE] IS NOT NULL")
            adapter = OleDbDataAdapter(cmd_text, conexao)

            ds = DataSet()
            conexao.Open()
            adapter.Fill(ds)
            
            total_linhas = 0
            adicionadas = 0
            sem_match = 0
            erros = 0

            tbl = ds.Tables[0]
            #Formulario.ExibeMensagem("teste 2")
            for linha in tbl.Rows:
                total_linhas += 1

                def get_val(row, col):
                    try:
                        if row.IsNull(col):
                            return None
                        return str(row[col]).strip()
                    except:
                        return None

                favorecido = get_val(linha, "NOME")
                item = get_val(linha, "ITEM")
                retirada = get_val(linha, "RETIRADA")
                quantidade = get_val(linha, "QUANTIDADE")
                
    
                if item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026888 - 34':
                    codigo  = '026888'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026889 - 35':
                    codigo  = '026889'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026890 - 36':
                    codigo  = '026890'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026891 - 37':
                    codigo  = '026891'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026892 - 38':
                    codigo  = '026892'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026893 - 39':
                    codigo  = '026893'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026894 - 40':
                    codigo  = '026894'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026895 - 41':
                    codigo  = '026895'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026896 - 42':
                    codigo  = '026896'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026897 - 43':
                    codigo  = '026897'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026898 - 44':
                    codigo  = '026898'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026899 - 45':
                    codigo  = '026899'
                    ca  = '34550'
                    descricao = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

                elif item == 'Óculos Proteção Carbografite Pro Vision Incolor | R$ 7,77 - 003432':
                    codigo  = '003432'
                    ca  = '6942'
                    descricao = 'Óculos de segurança constituído de armação e visor confeccionados em uma única peça de policarbonato com meia borda superior e meia borda lateral, hastes tipo espátula confeccionadas do mesmo material da armação com seis fendas fixadas à armação através de pinos plásticos. Certificado de Aprovação: 6942'

                elif item == 'Óculos Proteção Libus Argon Anti Risco Incolor | R$ 6,47 - 033504':
                    codigo  = '033504'
                    ca  = '35765'
                    descricao = 'Óculos de segurança, constituídos de um arco de material plástico preto com um pino central e uma fenda em cada extremidade, utilizadas para o encaixe de um visor de policarbonato na cor incolor, com apoio nasal e proteção lateral injetados do mesmo material, com um orifício na parte frontal superior e uma fenda em cada extremidade para o encaixe no arco. O arco possui borda superior com meia-proteção nas bordas. As hastes, do tipo espátula, são confeccionadas do mesmo material do arco e são compostas de duas peças; uma semi-haste vazada, com uma das extremidades fixadas ao arco por meio de parafuso metálico e outra semi-haste com um pino plástico em uma das extremidades e que se encaixa na semi-haste anterior e que permite o ajuste do tamanho. Certificado de Aprovação; 35765'

                elif item == 'Óculos Proteção Libus Ecoline Antiembaçante Incolor | R$ 10,30 - 033509':
                    codigo  = '033509'
                    ca  = '36032'
                    descricao = 'Óculos de segurança, constituídos de armação e visor confeccionado em uma única peça de policarbonato incolor, com ponte e apoio nasal injetado do mesmo material. As hastes, do tipo espátula, são confeccionadas de material plástico preto e são fixadas às extremidades do visor através de parafusos metálicos. Possui tratamento anti embaçante. Certificado de Aprovação; 36032'

                elif item == 'Óculos Proteção Libus Ecoline Anti Risco Incolor | R$ 5,15 - 033508':
                    codigo  = '033508'
                    ca  = '36032'
                    descricao = 'Óculos de segurança, constituídos de armação e visor confeccionado em uma única peça de policarbonato incolor com ponte e apoio nasal injetado do mesmo material. As hastes, do tipo espátula, são confeccionadas de material plástico preto e são fixadas às extremidades do visor através de parafusos metálicos. Certificado de Aprovação; 36032'

                elif item == 'Óculos Proteção Sobrepor Libus Visita Cinza | R$ 7,77 - 041784':
                    codigo  = '041784'
                    ca  = '35763'
                    descricao = 'Óculos de segurança constituídos de armação e visor confeccionados em uma única peça de policarbonato disponível nas cores incolor e cinza com meia borda superior, hastes tipo espátula confeccionadas do mesmo material da armação na cor cinza com seis fendas para ventilação e fixadas à armação através de pinos plásticos. Proteção dos Olhos do usuário contra impactos de partículas volantes, contra raios ultravioleta (U) e, no caso da lente de cor cinza, contra luz intensa. CA Nº 35.763'

                elif item == 'Óculos Proteção Sobrepor Libus Visita Incolor | R$ 7,77 - 033513':
                    codigo  = '033513'
                    ca  = ''
                    descricao = 'Óculos de segurança'

                elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela EG 1PAR | R$ 3,36 - 053989':
                    codigo  = '053989'
                    ca  = '51147'
                    descricao = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

                elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela G 1PAR | R$ 3,36 - 053988':
                    codigo  = '053988'
                    ca  = '51147'
                    descricao = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

                elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela M 1PAR | R$ 3,36 - 053987':
                    codigo  = '053987'
                    ca  = '51147'
                    descricao = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

                elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela P1PAR | R$ 3,36 - 053986':
                    codigo  = '053986'
                    ca  = '51147'
                    descricao = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

                elif item == 'Luva Látex Volk Slim Multiuso Forrada Amarela M | R$ 3,36 - 025338':
                    codigo  = '025338'
                    ca  = '51147'
                    descricao = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

                elif item == 'Luva Poliamida Volk Tátil PU Palma e Dedos Preta M | R$ 3,40 - 025306':
                    codigo  = '025306'
                    ca  = '30916'
                    descricao = 'Luva de segurança confeccionada em fibras sintéticas, revestimento da face palmar e ponta dos dedos em poliuretano (PU), punho com inserções de fibras elásticas e acabamento em fibras sintéticas. Luva para proteção contra agentes mecânicos. Certificado de Aprovação; 30916'

                elif item == 'Luva Tricotada Volk Black Tractor Térmica Banho Borracha G | R$ 10,44 - 050908':
                    codigo  = '050908'
                    ca  = '37981'
                    descricao = 'Luva de segurança confeccionada em fibras sintéticas e fibras naturais, revestimento de face palmar, face palmar dos dedos e ponta dos dedos em borracha vulcanizada; punho com fibras elásticas e acabamento em fibras sintéticas. CA 37981'


                nome_fav = (favorecido or "").split('(')[0].strip()
                nome_like = nome_fav.replace("'", "''") + "%"
                #Formulario.ExibeMensagem("Nome: {0}".format(nome_like))

                sql = ("Select Distinct CP_PESSOA.CARGO_FUNCIONAL, CP_PESSOA.MATRICULA, CP_PESSOA.FUNCAO_GRATIFICADA, ORGAO.DESCRICAO From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO WHERE PESSOA.NOME LIKE UPPER('"+nome_like+"')")

                try:
                    dados = DB.ExecuteDataTable(sql)

                    if dados.Rows.Count > 0:
                        row = dados.Rows[0]
                        cargo = row['CARGO_FUNCIONAL'].ToString()
                        matricula = row['MATRICULA'].ToString()
                        funcao = row['FUNCAO_GRATIFICADA'].ToString() if not String.IsNullOrEmpty(row['FUNCAO_GRATIFICADA'].ToString()) else cargo
                        uor = row['DESCRICAO'].ToString()
                        unidade = "UNIDADE-QUANTIDADE"
                        
                        valores = [nome_fav, matricula, cargo, funcao, uor, retirada, item, codigo, ca, quantidade, unidade, descricao]
                        
                        OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, valores)
                        adicionadas += 1
                    else:
                        sem_match += 1

                except Exception as ex:
                    Formulario.ExibeMensagem("Erro: {0}".format(str(ex)))
                    erros += 1
                    continue
                    
            conexao.Close()

            qtd = 0
            try:
                qtd = OrdemServico.GetCustom(nomeGrid).Rows.Count
            except:
                pass

            resumo = (
                "Importação concluída!\n\n"
                "Linhas lidas: {0}\n"
                "Adicionadas: {1}\n"
                "Funcionário ou Base não encontrada: {2}\n"
                "Erros: {3}\n"
                "Total na GRID agora: {4}"
            ).format(total_linhas, adicionadas, sem_match, erros, qtd)
            
            #Formulario.ExibeMensagem("teste 6")
            Formulario.ExibeMensagem(resumo)
            #Formulario["CHECKBOX2"].Habilitado = False

        readExcel(
            ["NOME","MATRICULA", "CARGO", "FUNCAO", "UOR", "RETIRADA","ITEM", "CODIGO", "CA", "QUANTIDADE", "UNIDADE", "DESCRICAO"],
            "EQUIP_EPI_LOTE"
        )

        
        #Formulario['CHECKBOX1'].Visivel = True
        #Formulario['CHECKBOX1'].Habilitado = True
        
        
    else:
        Formulario.ExibeMensagem("Não tem Arquivo anexado para importação.")
        Controle.Valor = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Planilha Preenchida" classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- ClientesAutorizados:
  - PapelProcessoId=67037; PapelAutorizado=Dires

### [336289] SubProcesso ""
Responsável: Dires (papel 1380)
Config: AssociacaoId=1642
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
grid = OrdemServico.GetCustom('EQUIP_EPI_LOTE')

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
    sub.Assunto = "Recebimento de EPI(LOTE)"
    
#    item = FormularioRegistro['ITEM'].Valor.ToString()
#    
#    if item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026888 - 34':
#        sub['CODIGO']  = '026888'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026889 - 35':
#        sub['CODIGO']  = '026889'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026890 - 36':
#        sub['CODIGO']  = '026890'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026891 - 37':
#        sub['CODIGO']  = '026891'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026892 - 38':
#        sub['CODIGO']  = '026892'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026893 - 39':
#        sub['CODIGO']  = '026893'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026894 - 40':
#        sub['CODIGO']  = '026894'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026895 - 41':
#        sub['CODIGO']  = '026895'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026896 - 42':
#        sub['CODIGO']  = '026896'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026897 - 43':
#        sub['CODIGO']  = '026897'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026898 - 44':
#        sub['CODIGO']  = '026898'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026899 - 45':
#        sub['CODIGO']  = '026899'
#        sub['NUM_ITEM']  = '34550'
#        sub['DESCRICAO_DETALHADA'] = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'
#
#    elif item == 'Óculos Proteção Carbografite Pro Vision Incolor | R$ 7,77 - 003432':
#        sub['CODIGO']  = '003432'
#        sub['NUM_ITEM']  = '6942'
#        sub['DESCRICAO_DETALHADA'] = 'Óculos de segurança constituído de armação e visor confeccionados em uma única peça de policarbonato com meia borda superior e meia borda lateral, hastes tipo espátula confeccionadas do mesmo material da armação com seis fendas fixadas à armação através de pinos plásticos. Certificado de Aprovação: 6942'
#
#    elif item == 'Óculos Proteção Libus Argon Anti Risco Incolor | R$ 6,47 - 033504':
#        sub['CODIGO']  = '033504'
#        sub['NUM_ITEM']  = '35765'
#        sub['DESCRICAO_DETALHADA'] = 'Óculos de segurança, constituídos de um arco de material plástico preto com um pino central e uma fenda em cada extremidade, utilizadas para o encaixe de um visor de policarbonato na cor incolor, com apoio nasal e proteção lateral injetados do mesmo material, com um orifício na parte frontal superior e uma fenda em cada extremidade para o encaixe no arco. O arco possui borda superior com meia-proteção nas bordas. As hastes, do tipo espátula, são confeccionadas do mesmo material do arco e são compostas de duas peças; uma semi-haste vazada, com uma das extremidades fixadas ao arco por meio de parafuso metálico e outra semi-haste com um pino plástico em uma das extremidades e que se encaixa na semi-haste anterior e que permite o ajuste do tamanho. Certificado de Aprovação; 35765'
#
#    elif item == 'Óculos Proteção Libus Ecoline Antiembaçante Incolor | R$ 10,30 - 033509':
#        sub['CODIGO']  = '033509'
#        sub['NUM_ITEM']  = '36032'
#        sub['DESCRICAO_DETALHADA'] = 'Óculos de segurança, constituídos de armação e visor confeccionado em uma única peça de policarbonato incolor, com ponte e apoio nasal injetado do mesmo material. As hastes, do tipo espátula, são confeccionadas de material plástico preto e são fixadas às extremidades do visor através de parafusos metálicos. Possui tratamento anti embaçante. Certificado de Aprovação; 36032'
#
#    elif item == 'Óculos Proteção Libus Ecoline Anti Risco Incolor | R$ 5,15 - 033508':
#        sub['CODIGO']  = '033508'
#        sub['NUM_ITEM']  = '36032'
#        sub['DESCRICAO_DETALHADA'] = 'Óculos de segurança, constituídos de armação e visor confeccionado em uma única peça de policarbonato incolor com ponte e apoio nasal injetado do mesmo material. As hastes, do tipo espátula, são confeccionadas de material plástico preto e são fixadas às extremidades do visor através de parafusos metálicos. Certificado de Aprovação; 36032'
#
#    elif item == 'Óculos Proteção Sobrepor Libus Visita Cinza | R$ 7,77 - 041784':
#        sub['CODIGO']  = '041784'
#        sub['NUM_ITEM']  = '35763'
#        sub['DESCRICAO_DETALHADA'] = 'Óculos de segurança constituídos de armação e visor confeccionados em uma única peça de policarbonato disponível nas cores incolor e cinza com meia borda superior, hastes tipo espátula confeccionadas do mesmo material da armação na cor cinza com seis fendas para ventilação e fixadas à armação através de pinos plásticos. Proteção dos Olhos do usuário contra impactos de partículas volantes, contra raios ultravioleta (U) e, no caso da lente de cor cinza, contra luz intensa. CA Nº 35.763'
#
#    elif item == 'Óculos Proteção Sobrepor Libus Visita Incolor | R$ 7,77 - 033513':
#        sub['CODIGO']  = '033513'
#        sub['NUM_ITEM']  = ''
#        sub['DESCRICAO_DETALHADA'] = 'Óculos de segurança'
#
#    elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela EG 1PAR | R$ 3,36 - 053989':
#        sub['CODIGO']  = '053989'
#        sub['NUM_ITEM']  = '51147'
#        sub['DESCRICAO_DETALHADA'] = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'
#
#    elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela G 1PAR | R$ 3,36 - 053988':
#        sub['CODIGO']  = '053988'
#        sub['NUM_ITEM']  = '51147'
#        sub['DESCRICAO_DETALHADA'] = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'
#
#    elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela M 1PAR | R$ 3,36 - 053987':
#        sub['CODIGO']  = '053987'
#        sub['NUM_ITEM']  = '51147'
#        sub['DESCRICAO_DETALHADA'] = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'
#
#    elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela P1PAR | R$ 3,36 - 053986':
#        sub['CODIGO']  = '053986'
#        sub['NUM_ITEM']  = '51147'
#        sub['DESCRICAO_DETALHADA'] = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'
#
#    elif item == 'Luva Látex Volk Slim Multiuso Forrada Amarela M | R$ 3,36 - 025338':
#        sub['CODIGO']  = '025338'
#        sub['NUM_ITEM']  = '51147'
#        sub['DESCRICAO_DETALHADA'] = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'
#
#    elif item == 'Luva Poliamida Volk Tátil PU Palma e Dedos Preta M | R$ 3,40 - 025306':
#        sub['CODIGO']  = '025306'
#        sub['NUM_ITEM']  = '30916'
#        sub['DESCRICAO_DETALHADA'] = 'Luva de segurança confeccionada em fibras sintéticas, revestimento da face palmar e ponta dos dedos em poliuretano (PU), punho com inserções de fibras elásticas e acabamento em fibras sintéticas. Luva para proteção contra agentes mecânicos. Certificado de Aprovação; 30916'
#
#    elif item == 'Luva Tricotada Volk Black Tractor Térmica Banho Borracha G | R$ 10,44 - 050908':
#        sub['CODIGO']  = '050908'
#        sub['NUM_ITEM']  = '37981'
#        sub['DESCRICAO_DETALHADA'] = 'Luva de segurança confeccionada em fibras sintéticas e fibras naturais, revestimento de face palmar, face palmar dos dedos e ponta dos dedos em borracha vulcanizada; punho com fibras elásticas e acabamento em fibras sintéticas. CA 37981'

    
    
    #Preenchimento dos campos:
    #sub["NOME_NOME"] =          linha["FUNCIONARIO"].ToString() # ok
    sub['TE_NOME_EMPREGADO'] =       linha['NOME'].ToString()
    sub['TE_MATRICULA'] =           linha['MATRICULA'].ToString()   # ok
    sub['TE_CARGO'] =               linha['CARGO'].ToString()
    sub['TE_UOR'] =                 linha['UOR'].ToString()
    sub['TEXT'] =                   linha['RETIRADA'].ToString() # ok
    sub['TEXT_1'] =                 linha['ITEM'].ToString()    # ok
    sub['CODIGO'] =                 linha['CODIGO'].ToString()  # 
    sub['NUM_ITEM'] =               linha['CA'].ToString()  # 
    sub['QUANTIDADE_ESTIMADA'] =    linha['QUANTIDADE'].ToString()   #ok
    sub['TEXT2'] =                  linha['UNIDADE'].ToString()
    sub['DESCRICAO_DETALHADA'] =    linha['DESCRICAO'].ToString()
    
    
    sub.Salva()
    sub.AvancaAtividade()
    
    

AvancaProximaAtividade = True
```
- Associação: Ativo=true; FraseAssociacao=EPI (Lote) -> EPI; FraseInversaAssociacao=EPI -> EPI (Lote); CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=RECEBIMENTOEPILOTE; SeparadorSequencial=. | fonte: Recebimento de EPI (Abertura em Lote) → alvo: Recebimento de EPI

## Papéis usados
### papel 1380: Dires
Tipo=RelacaoOrgaos

## Campos customizados usados (definição global)

### EQUIP_EPI_LOTE — Equipamentos EPI Lote
DataGrid RecordList → Z_00143_EQUIP_EPI_LOTE.EQUIP_EPI_LOTE
Colunas do registro:
- RETIRADA "Retirada" [DatePicker DateTime]
- NOME "NOME" [TextBox String]
- ITEM "Item" [DropDownList String]
**ITEM.LookupScript**
```python
combobox = [
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026888 - 34',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026889 - 35',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026890 - 36',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026891 - 37',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026892 - 38',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026893 - 39',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026894 - 40',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026895 - 41',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026896 - 42',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026897 - 43',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026898 - 44',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026899 - 45',
    'Óculos Proteção Carbografite Pro Vision Incolor | R$ 7,77 - 003432',
    'Óculos Proteção Libus Argon Anti Risco Incolor | R$ 6,47 - 033504',
    'Óculos Proteção Libus Ecoline Antiembaçante Incolor | R$ 10,30 - 033509',
    'Óculos Proteção Libus Ecoline Anti Risco Incolor | R$ 5,15 - 033508',
    'Óculos Proteção Sobrepor Libus Visita Cinza | R$ 7,77 - 041784',
    'Óculos Proteção Sobrepor Libus Visita Incolor | R$ 7,77 - 033513',
    'Luva Látex Flocada Go Safety Multiuso Amarela EG 1PAR | R$ 3,36 - 053989',
    'Luva Látex Flocada Go Safety Multiuso Amarela G 1PAR | R$ 3,36 - 053988',
    'Luva Látex Flocada Go Safety Multiuso Amarela M 1PAR | R$ 3,36 - 053987',
    'Luva Látex Flocada Go Safety Multiuso Amarela P1PAR | R$ 3,36 - 053986',
    'Luva Látex Volk Slim Multiuso Forrada Amarela M | R$ 3,36 - 025338',
    'Luva Poliamida Volk Tátil PU Palma e Dedos Preta M | R$ 3,40 - 025306',
    'Luva Tricotada Volk Black Tractor Térmica Banho Borracha G | R$ 10,44 - 050908'
]

Itens = combobox
```
- CODIGO "CODIGO" [TextBox String]
- CA "CA" [TextBox Integer]
- QUANTIDADE "Quantidade" [TextBox String]
- UNIDADE "UNIDADE" [TextBox String]
- DESCRICAO "Descrição do Equipamento" [Memo String]
- MATRICULA "MATRICULA" [TextBox String]
- UOR "UOR" [TextBox String]
- CARGO "CARGO" [TextBox String]
- FUNCAO "FUNCAO" [TextBox String]

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
