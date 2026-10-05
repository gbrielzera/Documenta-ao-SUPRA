# MemoriaOCS

Caminho: Customização > Modelo de objetos > Ativos > Hardware > MemoriaOCS

Tamanho da memória detectada pelo OCS NG em megabytes

**Exemplo 1: modificação da propriedade MemoriaOCS**

```
# carrega objeto Hardware de identificador 1
hardware = Hardware.Carrega(1)
# modifica a propriedade MemoriaOCS
hardware.MemoriaOCS = 1;
# salva modificação da propriedade MemoriaOCS
Hardware.Salva(hardware)
```
