# Aulas de Supravizio — conhecimento prático por tema
Caminho: Guias > Aulas

Síntese, com as nossas palavras e organizada por tema, de seis aulas gravadas de treinamento. Fonte: as transcrições e as
revisões detalhadas feitas por um colega (que autorizou o uso), conferidas por nós contra a documentação e as DLLs quando
possível. Minutos entre parênteses (A3 01:27 = aula 3, 1h27). Material de aula: sem nomes de participantes nem credenciais.

**Limites.** As aulas usam uma instalação de treinamento histórica (versão 11.1.2, 2020), não a 19.1.1 do cliente: as telas e
os comportamentos podem ter mudado. Os exemplos são didáticos, não foram executados no ambiente da empresa, e a transcrição
automática erra palavras e nomes de método. Cada item vem marcado: **[aula]** demonstrado ou explicado na aula, **[doc]** a
documentação confirma, **[api]** a DLL confirma a assinatura. Em dúvida, teste em Qualidade (`guias/testes_qualidade.md`).

## 1. Acesso, interfaces e permissões
- Portal (cliente), Workspace/Worklist (solucionador) e Editor de Processos têm funções e permissões diferentes. Acesso de
  solucionador não prova permissão para modelar processos [aula A1].
- **Filtros do Workspace persistem** ao recarregar (responsável, aprovador, pessoa envolvida, situação, paginação) e são a
  causa mais comum de "a OS sumiu"; a opção Todos não prova acesso irrestrito [aula A1 00:16]. Uma OS que parece ter perdido
  campos pode estar numa aba secundária (ex.: SLA).
- Cancelar não é encerrar com sucesso (o assistente pede o motivo do cancelamento) [aula].
- **Ausência**: período, substituto e três permissões independentes (modificar OS, redirecionar encaminhamentos, aprovar em
  nome do titular). Escolher um substituto não habilita as três [aula A1 00:19].
- Perfis de acesso complementam-se (os customizados somam aos nativos); perfil de cliente não é perfil de acesso; o modo do
  Worklist (desativado, todos, só autorizados) é configuração do ambiente, separada do perfil da pessoa [aula A1].
- Registrar um comunicado não prova que o e-mail saiu: a rotina de envio precisa estar ativa (a aba Comunicados mostra
  "Pendente" quando não está) [aula A1 00:28].
- O protocolo/número guardado em um campo customizado não é o identificador nativo da OS: não misturar em consultas [aula A1].

## 2. Grupos, filas e papéis
- Área (órgão), grupo de trabalho, fila e papel são coisas diferentes; nome parecido não cria vínculo [aula A1 + doc].
- **Membros de um grupo**: `TECNICO` (`ID_GRUPO_TRABALHO`, `ID_PESSOA`, `ATIVO`); o coordenador está em
  `GRUPO_TRABALHO.ID_COORDENADOR`. Cada solucionador tem uma lotação ativa por vez; as regras de operação do grupo (cancelar,
  encaminhar, classificar...) não descem aos subgrupos [doc `dados_grupo_trabalho`, `dados_tecnico`].
- Criar fila: Grupo de Trabalho > Solucionadores e Filas > Criar Fila. Autorizar o acesso a filas de outros grupos é outra
  coisa. **Assumir** a OS da fila a atribui ao usuário [aula A1 02:24, A5 00:00].
- **Papéis são compartilhados em toda a base.** Antes de reutilizar ou editar um papel, confira tipo, filtros e processos
  que o usam; nome sugestivo ("Aprovador") não garante a configuração [aula A5 00:15].
- Papel por **filtro no cadastro de pessoas**: as condições se somam (área + perfil de cliente VIP deixa de fora o VIP de outra
  área) [aula A5 00:33]. Selecionar várias pessoas pode pedir que se escolha um responsável; isso não é uma fila.
- Papel que recupera **quem concluiu uma tarefa anterior**: tipo "Execução de Tarefa do Processo" (Solucionador finalizador da
  atividade), com o **Código** da tarefa e "Somente última execução" [aula A5 00:15 + doc `tipos_papeis`].
- Papel por script: `Atores.Adiciona(Pessoa.Carrega("Id", linha["ID_PESSOA"]))`; a consulta precisa trazer o identificador
  que o `Carrega` usa, e o script popula objetos `Pessoa`, não nomes [aula A5 00:48; `Pessoa.Carrega(string, object)` confirmada em [api]].
- Um papel recém-criado pode não aparecer no editor: fechar e reabrir o editor resolveu no caso observado [aula].

## 3. Construir, versionar e importar fluxos
- Hierarquia: macroprocesso > processo > subprocesso (o fluxo desenhado). Toolbox: **clicar no elemento e depois no desenho**;
  fixar a Toolbox evita que ela se recolha. Ligar com o item Fluxo, de um conector ao outro, respeitando a direção
  (erro frequente: ligar o final à tarefa) [aula A2 00:00].
- Entrada de Dados (laranja) e Aprovação (verde) são Data Objects ligados ao elemento; não viram tarefas nem se ligam com a
  seta de fluxo. Objeto "órfão": copiar e colar sobre o destinatário resolveu [aula A3 00:15].
- Validar subprocesso, validar versão e **ativar** são operações diferentes; validar não comprova a regra de negócio [aula A2].
- **Nova versão**: abra o subprocesso da versão nova (duplo clique) e confira o número na aba antes de editar; criar a versão
  não troca a aba aberta. Ativar uma versão nova **não migra** as OS existentes. Tornar obrigatório um campo em versão já
  usada por OS pode bloquear o avanço de quem não o preencheu [aula A2 00:40, A5 00:15].
- Sigla/nome abreviado repetido dá erro de gravação; salve em etapas para achar o erro cedo [aula A2 02:40].
- **Importação** [aula A2 02:40, A3 00:00]: Importar na versão em edição do destino, escolher os subprocessos. A versão 3 da
  origem entrou como versão 1 (o histórico não vem). O papel importado ficou **sem pessoa válida** porque a pessoa da origem não
  existe no destino: atribuir uma local. A caixa "Atualizar configuração de papéis" altera papéis do destino. O XML não garante as
  dependências (faltou o grupo envolvido no macroprocesso). Um tipo de subprocesso cadastrado pode não estar no Process Explorer
  da versão: adicione o existente e complete o desenho.
- Base copiada de outro ambiente mantém a URL dele: links dos comunicados levam ao ambiente errado, e corrigir a configuração não
  corrige os links já gerados [aula A4 00:21]. Separe desenvolvimento, homologação e produção e transfira por XML.

## 4. Gateways e aprovação
- Gateway "Dados ou fórmula": **Regra de desvio = Aprovação** na tarefa (nativo) ou uma fórmula. O texto escrito na seta é só
  legenda; quem decide o caminho é o **valor de comparação** da alternativa. Erro real da aula: duas alternativas ambas com
  "Reprovado" [aula A3 02:32]. O Código da tarefa e o Código do gateway são distintos.
- Os dados da aprovação (aprovadores, Iniciar automaticamente, obrigatoriedade do motivo) ficam na **configuração da aprovação**
  (folha verde), não na atividade. "Campos para Aprovação" (o que se analisa; "Complementar a partir de" copia da Entrada de
  Dados) é diferente de "Campos para Preenchimento" (o que o aprovador informa). Aprovação sem dados configurados gera pendência.
- **Quantos precisam aprovar** [aula A4 00:00 + doc]: hierarquia *Única* com dois aprovadores exige os dois; *Inicial/Final* é
  sequencial (a segunda pessoa só vê a aprovação depois da primeira); **Mínimo aprovadores = 1** deixa uma decisão favorável
  bastar; **Reprovar imediatamente = True** encerra negativamente a uma reprovação (com False, a reprovação total vem quando já
  não dá para atingir o mínimo). O mínimo conta **pessoas**: dois papéis que resolvem a mesma pessoa não cumprem "dois".
- **Cancelar a versão da aprovação** não é reprovar, nem cancelar a OS, nem criar nova versão do processo [aula A2 03:48].
- Pré-aprovação: "Utilizar identidade do solicitante" (aproveita quem abriu a OS) é diferente de "Iniciar automaticamente"
  (inicia ao entrar na tarefa) e não vale para aprovação incremental por hierarquia [aula A2, A3 03:38].
- Aprovação pendente impede o avanço; campos aprovados ficam com cadeado. Reprovar pode levar a um caminho que não cancela a OS:
  o cancelamento nos exemplos é só o desenho escolhido.

## 5. Subprocesso chamado e associação
- **Chamada assíncrona** (atividade Subprocesso): **False** = a OS principal **espera** a filha finalizar (a principal mostra a
  pendência nativa e avança sozinha quando a filha termina); **True** = a principal segue sem esperar [aula A3 01:27, A4 00:11,
  A6 01:03 — telas com o valor visível + `docs/subprocessos.md`]. A frase "chamada síncrona" falada nas aulas e a descrição da
  propriedade na doc oficial estão trocadas: não as use como prova.
- **Sincronizar cancelamento**: propaga o cancelamento entre pai e filha nos dois sentidos (ao cancelar a filha com o pai aberto, o
  sistema avisa que o pai também será cancelado). Use só quando o requisito pede cancelamento conjunto [aula A4 00:11].
- **Associação**: nome único dentro da associação; frases direta e inversa são descrições, não comandos; cardinalidade (ex.: 1:1)
  e separador (gera numeração como 103.1). Configure-a na atividade chamadora e, no invocado, a leitura inversa no iniciador
  (mensagem entre processos / Link). Associar por engano ao próprio chamador é um erro de cadastro [aula A3 01:13].
- **Parâmetros de entrada** levam campos do pai ao filho (nativos como Propriedade; customizados na opção própria); para o filho
  exibi-los, inclua os campos na Entrada de Dados dele. **Parâmetros de saída** ficam no subprocesso invocado; marque o campo de
  entrada como opcional para não exigi-lo antes do retorno [aula A4 03:00].

## 6. Mensagens e comunicados
- O modelo de comunicado é editado **pela Web** (Processo > Processos > Modelo de comunicado), com campos dinâmicos da OS.
  Destinatários: papel e/ou lista fixa separada por `;`. "Temporalidade" é retenção, não prazo de envio [aula A4 00:21].
- Dois caminhos: **Tipo de Evento** (Abertura, Início aprovação, Aprovação, Reprovação, encaminhamento) ou **Evento
  Intermediário de Mensagem** no desenho. Não deixe os dois enviando o mesmo aviso. Salvar o iniciador não executa o evento
  [aula A6 00:02].
- *Início aprovação* avisa a pendência; *Aprovação* avisa a decisão favorável; *Reprovação* é outro evento. Se a aprovação já
  começou, trocar o evento não a reenvia: cancele a versão da aprovação ou abra outra OS [aula A4 01:10].
- Destinatário "Cliente" é o cliente da OS (não necessariamente quem abriu); destinatário vazio não recupera o último
  responsável; a pessoa precisa ter e-mail [aula A4, A6].
- **Script Evento** [aula A4 00:21, A6 00:02]: filtrar a mensagem por fluxo,
  `if OrdemServico.ClasseSubProcesso.Sigla != "SIGLA": Mensagem.Cancelar = True` (cancela só a mensagem, não a OS);
  `OrdemServico.AdicionaComentario("texto", False)` (o `False` não publica no Portal). Um script antigo que monta
  `Mensagem.Corpo` sobrepõe o modelo escolhido.
- **Quantidade máxima de execuções = 1** no evento evita mensagens repetidas quando a OS volta e avança de novo [aula A6 00:11].
- Relatório anexado ao comunicado: formato PDF; os parâmetros devem existir no relatório e ser usados na consulta. Teste a
  consulta em "Execução de Comandos SQL". Anexos enviados: informe o "Tipo de arquivos anexados" no evento.
- Falha no envio (e-mail inválido) pode deixar um indicativo de erro e ainda permitir o avanço; erro em Script Evento é outro
  caso, não testado até o fim [aula A6]. A aba Comunicados prova que foi gerado, não que foi entregue.

## 7. Iniciadores por Timer e por Regra
- **Timer** [aula A4 01:49]: ciclo diário (com dias da semana e horário), semanal, mensal (inclui "último dia do mês") ou
  anual. A **Máquina de Processos** (Utilitários > Gerenciamento de Ambiente) verifica os eventos; o ciclo do job não é o ciclo
  do Timer, e o horário não é garantia de pontualidade. Divergências aula x manual (não conciliar): a aula gerou OS retroativa no
  mesmo dia e OS atribuída ao Sistema sem responsável, enquanto o manual diz que só gera para data/hora maior ou igual à
  corrente e que sem responsável o iniciador é desconsiderado. Fluxo só com Timer não abre manualmente [doc]. Configure serviço
  e responsável reais e teste.
- **Regra** [aula A4 02:04 + doc `iniciador_por_regra`]: o retorno pode ser lógico (liga/desliga), `DataTable` (uma OS por
  registro), array ou lista (uma OS por item). Consulta em base externa: o segundo argumento do `DB` é o nome da conexão. No Script
  Evento, `OrdemServico["CAMPO"] = Regra["COLUNA"]` preenche a OS (o nome da coluna precisa bater com o da consulta). Vários
  registros num campo simples: o último sobrescreve; para várias linhas numa OS use grid.
- Sem **deduplicação**, o iniciador gera novas OS a cada ciclo para os mesmos registros: defina como marcar o que já foi
  processado. Atualizou a consulta no script mas não no iniciador: nascem OS a mais [aula A4 03:41].
- Para achar as OS geradas, o relatório da última execução do job pode já ter sido substituído; use a fila, a pesquisa ou a tabela
  dinâmica. Não use a tela de remoção de OS para procurar (ela é destrutiva).

## 8. ANS e ANO
- **ANS** acompanha a OS; **ANO** acompanha a atividade. Para o ANS ser escolhido, confira vigência, áreas atendidas (é a área do
  **cliente** da OS, não a do solucionador), serviços, perfis, horários e **Processos Acordados** (o subprocesso precisa estar
  associado). Vários acordos aplicáveis: vale a afinidade de serviço e, nos demais critérios, o menor tempo; filtro vazio amplia
  [aula A5 00:54 + doc].
- 1.440 minutos são 24 horas **contabilizadas**, não um dia corrido: com horários só na segunda (09-12 e 13-18, 8 horas por
  semana), 24 horas exigem três semanas. Confirme o que "um dia" significa antes de converter.
- ANO constante em minutos x **Percentual SLA**: veja a "Unidade de tempo" (120 em percentual vira 120%). ANO constante pode existir
  sem ANS; ANO percentual depende do ANS. Um ANO de 48 horas e um ANS VIP de 24 horas coexistem: são parâmetros diferentes.
- **Ações do ANO** disparam por percentual do tempo consumido (e-mail em 10%, categorização em 50%, encaminhamento em 80%);
  percentual zero não executa; ajuste o texto do e-mail ao limiar real. **Grupo de ANO**: atividades agrupadas **compartilham**
  prazo, unidade e ações; cumprir todos os ANO isolados não garante cumprir o ANS.
- **Pausa do ANS na aprovação**: o motivo (ex.: "Aguardando aprovação") deve estar permitido nas Interrupções do acordo **e**
  indicado no "Motivo de interrupção SLA" da atividade; a pausa nasce ao entrar na etapa e termina ao concluí-la. Não há pausa
  automática por existir o objeto de aprovação. A pausa gerada pelo processo não pode ser encerrada à mão. Alterar o motivo com a
  OS já na etapa não pausa na hora: teste numa OS nova [aula A5 01:15, 02:09].
- **Interrupção manual** (Mais Ações > Priorização e ANS) usa um motivo permitido pelo acordo; "Aguardando fornecedor" exigiu
  comentário e tem máximo de 2 horas (vale só para as manuais). Recalcular o ANS está no mesmo menu.
- Calendário: primeiro o do grupo do solucionador, depois o da localidade da unidade. Ausência de calendário explícito não permite
  afirmar contagem 24/7. Horário do ANS e calendário do ANO se conferem separadamente [doc].

## 9. Campos, formulários, grids e arquivos
- Rótulo (descrição resumida), nome técnico, coluna, tipo de dado e controle visual são coisas diferentes; a largura do controle
  não é o tamanho máximo do texto; nome técnico sem acento. Para o campo virar coluna do grid de OS, "Permitir inclusão em
  listagens" precisa estar ligado [aula A1 03:16, A6 01:49].
- **Combo por script**: `Itens = DB.ExecuteDataTable(...)`; para campo Inteiro, a 1ª coluna é o identificador gravado e as
  seguintes são o texto exibido; lista fixa vai separada por `;` [aula A6 + doc `controle_combobox`].
- **Copiar a Entrada de Dados para outra atividade preserva a referência ao mesmo campo** (mostra os mesmos dados da OS). Para dados
  independentes, use campos distintos [aula A6 01:49].
- Grid: permitir incluir, editar e excluir são opções independentes; as colunas podem misturar controles. Booleano: `GetCustom`
  devolve `False` quando o valor nunca foi gravado (use `None` para distinguir ausência) [doc].
- **Arquivo anexado** é um Item de Configuração (objeto azul) cujo tipo (Ativos > Tipos de Itens de Configuração) tem supertipo
  Artefato, situação Anexado e artefato do tipo Arquivo; defina o tamanho máximo (10 MB foi o exemplo; arquivo grande pesa no
  servidor). Associe pelo atalho Configurar > Associação de arquivo. Reutilizar um tipo altera um cadastro compartilhado. Vários
  tipos na mesma coleção deram erro na base do treinamento: use objetos azuis separados [aula A6 00:27].
- Campos de OS podem ficar em tabela `CPE_*` em vez de `CP_ORDEM_SERVICO` (`guias/sql.md`).

## 10. Pesquisa de satisfação
Cadastro em quatro passos: grupo de questões com escores, questões, classe de pesquisa (ativa, com as questões) e a associação da
classe ao **finalizador** do subprocesso (a pesquisa nasce quando a OS finaliza; pai e filha podem ter configurações diferentes).
**Percentual de envio = 100 significa probabilidade de 100% de enviar**, não "cem envios"; zero não envia. A resposta é dada no
Portal e acompanhada no Workspace e nos relatórios. Sequência e peso do escore são propriedades distintas [aula A6 01:00 + doc].

## 11. Scripts e SQL vistos nas aulas
- **Script Fim com grid** [aula A6 03:41]:
  ```python
  OrdemServico["REPROVADO"] = False
  for linha in OrdemServico["PRODUTOS"].Rows:
      if linha["STATUS"] == "Reprovado":
          OrdemServico["REPROVADO"] = True
          break
  ```
  O gateway usa a fórmula `OrdemServico["REPROVADO"]` com alternativas `True` e `False`. A linha que zera o booleano é a
  correção para a OS que **volta** e muda os status (sem ela o valor antigo permanece). Esse script diz se existe ao menos um
  reprovado; para **contar**, percorra todas as linhas sem `break`.
- `DB.ExecuteScalar` devolve a 1ª coluna da 1ª linha: para testar "existe", a consulta precisa devolver uma contagem.
  `DB.ExecuteDataTable` devolve uma tabela percorrida por `.Rows`; o segundo argumento opcional é o nome da conexão (sem ele, a
  base do Supravizio). Uma **view não garante somente leitura**: a restrição vem das permissões da conexão [aula A6 + Microsoft].
- Quem cria a OS por script (Início) carrega a pessoa por `UsuarioRede` e o serviço por sigla; confirme que existem no destino
  [aula A5 01:15].

## 12. Armadilhas de quem começa (aparecem em todas as aulas)
Ligação invertida entre tarefa e final; papel sem pessoa; filtro do Workspace esquecido; editar a versão ativa em vez de criar
outra (e conferir o número na aba); duas alternativas de gateway com o mesmo valor; achar que o rótulo da seta decide o caminho;
trocar o evento de mensagem depois de iniciada a aprovação; papel com nome sugestivo mas outra configuração; base copiada com URL
de outro ambiente; ANO em percentual quando se queria minutos; área do ANS diferente da do cliente; indentação misturada no
IronPython; esperar que "salvar" execute um evento. Use esta lista como checklist de revisão de fluxo (`guias/desenho_fluxos.md`).
