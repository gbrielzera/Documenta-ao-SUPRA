# Cadastro de Serviços

Caminho: Guia para Administradores > Roteiro de implantação > Cadastro de Serviços

Um Serviço é um recurso cujo objetivo é satisfazer uma ou mais necessidades de um cliente e suportar os objetivos estratégicos do negócio do cliente. Um Serviço seria, por exemplo: um sistema, um equipamento, um recurso de rede, um serviço administrativo, um produto, etc.

Para realizar o cadastro de um serviço, primeiro é necessário cadastrar um **Tipo de Serviço**. O cadastro deste pode ser feito através do caminho **Processo | Serviços | Tipos de Serviço**:

Para inserir um novo registro, basta clicar em **Novo **na tela de listagem. Logo, será aberta uma nova tela com os devidos campos a serem preenchidos:

Cadastro de Tipo de Serviço

Em caso de dúvidas no preenchimento dos campos, consulte o tópico sobre [Tipos de Serviço](classeservico_sub).

**Importante**: Há uma hierarquia **Classes de Serviço -> Grupos de Serviço -> Tipos de Serviço -> Serviço**. Porém, estas duas primeiras são opcionais, para auxiliar apenas caso hajam muitas subdivisões.

Realizado o cadastro do Tipo de Serviço, poderão ser cadastrados seus respectivos Serviços, através do caminho **Processo | Serviços | Serviços**:

Clicando em **Novo **na tela de listagem, será aberta uma tela de cadastro:

Cadastro de Serviço

Em caso de dúvidas no preenchimento dos campos, consulte o tópico sobre [Serviço](servico_sub).

Após realizar o cadastro dos Serviços que serão disponibilizados no Supravizio, o usuário também pode esclarecer mais informações sobre cada serviço acessando a aba "Catálogo Serviços" do cadastro de um Serviço:

Através deste cadastro é possível incluir mais informações e descritivos mais claros para um cliente. Estes são:

- Pré-requisitos/Dependências
- Benefícios
- Disponibilidade
- Programação manutenção
- Solicitação Serviços

Além de exibir mais informações ao cliente, o Supravizio também disponibiliza um campo na aba Catalogo Serviços um campo **Descritivo cliente**. Este campo é utilizado para casos em que um descritivo de um serviço seja muito técnico para um cliente, por exemplo um cliente de TI. Caso este descritivo de cliente esteja preenchido, este que será exibido na terceira etapa de uma abertura de Ordem de Serviço no Portal. Vamos exemplificar. Suponhamos que tenhamos um sistema de folha de pagamento chamado XPTO como Serviço cadastrado no Supravizio:

Porém, para um usuário comum, possivelmente este descritivo XPTO não é amigável, não existe clareza no nome deste serviço para um cliente comum, que não tenha conhecimentos técnicos suficiente para identificar este serviço. Poderíamos então criar um outro descritivo de cliente chamado Folha de Pagamento:

No Portal de Processos então será exibido (se existir) o Descritivo cliente, ao invés do Descritivo do Serviço:

Caso não exista um Descritivo cliente preenchido, o sistema exibe automaticamente o Descritivo do Serviço.
