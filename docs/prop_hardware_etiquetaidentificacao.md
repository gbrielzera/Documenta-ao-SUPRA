# EtiquetaIdentificacao

Caminho: Customização > Modelo de objetos > Ativos > Hardware > EtiquetaIdentificacao

Número da Etiqueta de Identificação do Equipamento pela equipe de suporte. Este número pode ser utilizado pelo Solucionador durante o atendimento de um chamado.

**Exemplo 1: modificação da propriedade EtiquetaIdentificacao**

```
# carrega objeto Hardware de identificador 1
hardware = Hardware.Carrega(1)
# modifica a propriedade EtiquetaIdentificacao
hardware.EtiquetaIdentificacao = "Etiqueta identificação";
# salva modificação da propriedade EtiquetaIdentificacao
Hardware.Salva(hardware)
```
