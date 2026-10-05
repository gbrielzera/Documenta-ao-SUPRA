# Item de Configuração opcional

Caminho: Guia para Administradores > Configurando Processos > Tópicos Avançados > Formulários Dinâmicos > Exemplos de criação de formulários > Item de Configuração opcional

Caso um Item de Configuração não seja obrigatório na Ordem de Serviço, é possível torná-lo invisível, se o usuário não precisar anexá-lo.

Fluxo utilizado no Processo

Nesta exemplo, nomeamos o Item de Configuração como "EVIDENCIA" e o campo customizado, "POSSUI_EVIDENCIA" do tipo Checkbox.

Após, inserimos o código em **Script Modificado **do campo:

**Local: Script Modificado**

**Campo: Possui Evidência?**

```
if Controle.Valor == True:
    Formulario["EVIDENCIA"].Visivel = True
else:
    Formulario["EVIDENCIA"].Visivel = False
```

E em **Script Formulário carregado**, o seguinte código:

**Local: Script Formulário carregado**

**Campo: Descrever Falha**

```
Formulario["EVIDENCIA"].Visivel = False
```

Ao abrir uma Ordem de Serviço, caso seja marcada a opção "Possui Evidência", o campo para anexar o Item de Configuração se tornará visível.

Caso esteja desmarcada, o Item de Configuração não estará visível.

Tela de edição da Ordem de Serviço
