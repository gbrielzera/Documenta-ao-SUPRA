# MacroProcesso

Caminho: Customização > Modelo de objetos > Processo > MacroProcesso

Agrupamento de processos endereçados a uma área de negócio

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do MacroProcesso | String |
| **DescricaoCliente** | Descritivo apresentado para o cliente no passo de seleção de macro-processos da função de Abertura de Ordens de Serviço do Autoatendimento. Se não for informado então o sistema utilizará o próprio descritivo do macro-processo. | String |
| **GruposEnvolvidos** | Os Grupos de Trabalho envolvidos (incluindo seus sub-níveis) identificam todas as equipes que atuam Macroprocesso. A definição de Grupos envolvidos pode interferir na autorização para visualização de Ocorrências. A abertura de ocorrências de subprocessos contidos no Macroprocesso também está limitada a solucionadores lotados no grupo informado ou um dos seus sub-níveis. | [Lista de EnvolvimentoGrupo](objetos_envolvimentogrupo) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um MacroProcesso | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | MacroProcesso Carrega(int i); |
| **Novo** | Cria um novo registro do tipo MacroProcesso | MacroProcesso Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | MacroProcesso Carrega(string nomePropriedade, object valorPropriedade); |
