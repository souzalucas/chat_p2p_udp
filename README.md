
# Chat P2P UDP - Python 3

Implementação em Python 3 de um chat P2P usando o protocolo UDP que possibilita dois clientes trocarem mensagens entre si.

## Compilar/executar

#### Para iniciar o primeiro cliente
```
> python cliente.py 0 
```
#### Para iniciar o segundo cliente
``` 
> python cliente.py 1 
```

## Bibliotecas
  - socket:     Este módulo fornece acesso à interface de socket BSD.

  - threading:  Este módulo constrói interfaces de threading de alto-nível no topo do módulo _thread de baixo-nível. 

## Exemplo de uso: Enviar mensagem de de um cliente para o outro

#### Inicie o primeiro cliente em um console e digite seu apelido
  ```
> python cliente.py 0
> Joao
```

#### Inicie o segundo cliente em outro console e digite seu apelido
```
> python cliente.py 1
> Maria
```

####  Agora, em cada console você pode digitar sua mensagem e pressionar enter para enviá-la.
