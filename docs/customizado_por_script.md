# Customizado por script

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Papéis e responsabilidades > Tipos de Papéis > Customizado por script

Um papel pode ser definido através de scripts na tela de cadastros de papéis. Esta opção de configuração é a que oferece maior flexibilidade possível para definição do papel.

### Selecionar Script Seleção Atores

Para a definição de papel por script utiliza-se a sintaxe Iron Python, adicionando as pessoas na lista Atores. Veja o exemplo abaixo onde indicamos como atores do papel o gestor do favorecido em uma Ordem de Serviço. Repare que o segundo parâmetro é um texto explicativo exibido como explicação na aba de pessoas envolvidas da tela de Ordem de Serviço:

### Configuração do Script

Na configuração por scripts podemos utilizar campos do tipo [Pessoa](objetos_pessoa) existentes na Ordem de Serviço ou cadastros associados. Veja na sequência abaixo algumas dessas possibilidades:

```
# solucionador responsável configurado no Serviço
Atores.Adiciona(OrdemServico.Servico.ResponsavelTecnico, "Solucionador responsável pelo Serviço")
# pessoa configurada no Serviço como responsável na área de negócio
Atores.Adiciona(OrdemServico.Servico.ResponsavelArea, "Responsável pelo serviço na área de negócio");
# responsável pelo tipo de subprocesso da Ordem de Serviço
Atores.Adiciona(OrdemServico.ClasseSubProcesso.Responsavel, "Responsável pelo subprocesso")
# Cliente da OS
Atores.Adiciona(OrdemServico.Cliente, "Cliente informado na Ordem de Serviço");
# Cliente da OS
Atores.Adiciona(OrdemServico.Cliente.Orgao.Gestor, "Gestor do cliente informado na Ordem de Serviço");
# Responsável pela OS
Atores.Adiciona(OrdemServico.Responsavel, "Responsável pela Ordem de Serviço");
```

Repare que em cada comando utilizamos a função Adiciona do objeto Atores, fornecendo como primeiro parâmetro um objeto do tipo [Pessoa](pessoa_sub) e um comentário. O resultado final desta configuração pode ser confirmado na aba de pessoas envolvidas da Ordem de Serviço da figura abaixo:

Papéis definidos por scripts

Além desses critérios, é possível definir o critério de Seleção final, para saber mais verifique o tópico sobre [Critério de Seleção Final](tipos_papeis).
