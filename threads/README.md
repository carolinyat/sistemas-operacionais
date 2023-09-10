Programa que simula o processamento de pedidos em um restaurante.
Neste exemplo, criamos uma função processar_pedido que simula o processamento de um pedido com um tempo de processamento aleatório entre 1 e 5 segundos. 
Em seguida, criamos uma lista de threads, onde cada thread representa o processamento de um pedido. 
As threads são iniciadas e depois aguardamos que todas elas terminem usando o método join.

Isso simula a situação da vida real em que vários pedidos estão sendo processados em paralelo, o que pode melhorar significativamente o desempenho em comparação com o processamento sequencial.