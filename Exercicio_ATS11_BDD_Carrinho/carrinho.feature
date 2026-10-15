# language: pt
Funcionalidade: Carrinho de compras
  Como cliente de um e-commerce
  Quero adicionar produtos ao carrinho
  Para acompanhar o valor total e impedir compras acima do estoque

  Cenário: Adicionar um produto com sucesso quando há estoque suficiente
    Dado que o carrinho está vazio
    Quando adiciono 2 unidades de um produto com estoque 5 e preço unitário 10.0
    Então o total do carrinho deve ser 20.0
    E a quantidade de itens no carrinho deve ser 2

  Cenário: Tentar adicionar um produto sem estoque suficiente
    Dado que o carrinho está vazio
    Quando tento adicionar 6 unidades de um produto com estoque 3 e preço unitário 10.0
    Então deve ocorrer o erro "Estoque insuficiente"
    E o total do carrinho deve ser 0
