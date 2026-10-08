# Aulas de Supravizio — pontos práticos (resumo próprio)
Caminho: Guias > Aulas (uso local)

Resumo, com as nossas palavras, das seis aulas gravadas (transcrições automáticas em
`Supravizio-Estudos-Felipe/estudo-materiais/transcricoes/`). Cita o minuto para conferência.
Transcrição automática: pode errar palavras e nomes de métodos. Confirmar sempre na documentação.
**Uso local:** o material de origem é do Felipe e tem trechos de treinamento interno; por isso este
arquivo fica fora do GitHub (`.gitignore`). Só publicar com autorização dele e revisão.

## Aula 1 — acesso, filtros e visão do gestor
- Os **filtros do Workspace persistem**: ao recarregar a tela eles continuam marcados. É a principal causa de
  "sumiu uma OS" nos primeiros dias (00:16–00:17). Limpar filtros antes de dizer que a OS não existe.
- Para ver a fila de outra pessoa ou grupo, a própria pessoa precisa de **autorização** (aba de filas/grupos de
  trabalho do cadastro de pessoas, 02:32).
- Para pertencer a um **grupo de trabalho**, o usuário precisa de perfil de administrador ou solucionador (01:01).
- Colunas do Workspace (como "SLA restante") ajudam o gestor a acompanhar o andamento (00:47).
- O cliente do Windows e o Portal são acessos diferentes: o Portal não consome licença de solucionador (01:20).
- Derrubar a sessão de um usuário é registrado pelo sistema (01:53): usar só quando necessário.

## Aula 2 — montando o primeiro fluxo no Editor
- Os elementos ficam na **Toolbox**, que se recolhe ao soltar um elemento. Para inserir: clicar no elemento e depois no
  local do desenho (não arrastar do ícone, em algumas versões).
- Fluxo sai da atividade e chega ao finalizador: a seta vai do **sair** de uma atividade ao **entrar** da próxima.
  Erro comum de quem começa: inverter a direção da ligação (00:13).
- Responsável por **Relação de Pessoas e Filas**: adicionar a pessoa na coleção; verificar se foi adicionada antes de
  seguir (00:15–00:16).
- Grupos de trabalho: o grupo novo aparece em "Grupos de Trabalho" no cadastro; conferir se o grupo certo foi marcado
  antes de salvar (00:34–00:42).
- Papel de administrador consegue **ativar** a versão, mas não cria instâncias de processo (00:37).

## Aula 3 — salvar, validar e primeiros erros
- Salvar: como o editor grava no banco ao validar, em geral não é preciso salvar antes de validar (00:09).
- **Validar** a versão antes de ativar; a validação aponta pendências de cadastro (papel sem pessoa, campo sem
  associação, etc.).
- **Editar uma versão que já está ativa** pode dar comportamento estranho: criar uma nova versão para mudar (01:02).
- Nome de **associação** (Associação entre processos) deve ser único **dentro da associação** (01:23). Duas
  associações podem ter a mesma frase, mas não o mesmo nome.
- Para copiar cadastro de um processo a outro, a aula copia pelo combo de cadastro (01:53).
- **Quem abriu** a OS (solicitante) não é o cliente: informar o cliente errado troca o responsável pelo atendimento
  (00:39). Ver também `guias/contexto.md`.

## Aula 4 — aprovação, comunicados e ambientes
- Com dois aprovadores no mesmo papel, basta um aprovar para a tarefa avançar (00:11). O cenário "um aprova e outro
  reprova" foi deixado para estudo, não demonstrado. Não assumir o comportamento sem testar.
- Reserva de passagem e de hotel: se uma parte falha, o fluxo de cancelamento de todo o processo precisa existir (00:16).
- **Modelo de comunicado** é editado só pela Web, no caminho Processo > Processos > Modelo de comunicado (00:27, 00:46).
- **Ambientes são cópias uns dos outros**. Um link ou número pode apontar para o ambiente errado se o cadastro
  foi copiado de outro. Conferir o endereço antes de testar (00:32).
- No IronPython, manter o mesmo padrão de indentação em todo o script (espaços ou tabs). Mistura gera erro de sintaxe
  (00:41).

## Aula 5 — papéis, versões e visibilidade
- Papel criado é **visível para toda a base** (outros processos também veem). Nomes sugestivos ajudam, mas nada impede
  usar um papel "Aprovador" para o cliente. Nomear com cuidado (00:23).
- **Pode-se gerar muitas versões.** O que importa é a versão ativa funcionar e não atrapalhar o usuário final;
  criar nova versão é o caminho seguro para mudar um fluxo em uso (00:20).
- Atualizar um papel depois de criado: verificar a configuração da fila antes de cobrar o resultado (00:07, 00:19).
- Para mudar uma atividade de um processo em andamento, a aula gera uma nova versão e depois atualiza a atividade
  (00:19–00:20).

## Aula 6 — consultas, arquivos e modelagem
- Para testar uma consulta de pessoas, montar a consulta e rodar no ambiente de teste; ela devolve a lista de pessoas
  (00:09).
- Campo de **arquivo** tem limite de tamanho (a aula usou 10 MB). Arquivos grandes sobrecarregam o servidor: limitar
  o tamanho por campo (00:41).
- Um Artefato (arquivo) pode ser **reutilizado** entre processos; o que muda é a descrição. Cuidado com nome e tamanho
  (00:44–00:46).
- Documentação de cada processo deve seguir a mesma modelagem entre fluxos parecidos (00:31).
- Campos e papéis podem ser reutilizados entre processos; verificar a visibilidade antes (00:45).

## Pontos transversais
- Cada aula termina com o instrutor corrigindo erros de tela do participante; a maior parte dos problemas foi de
  **ambiente/perfil**, não de regra de negócio. Antes de mudar o fluxo, conferir perfil, grupo e versão.
- Os participantes erram sempre na mesma ordem: ligação invertida, papel sem pessoa, filtro esquecido, versão ativa
  editada. Usar isso como checklist de revisão de fluxo (ver `guias/desenho_fluxos.md`).
