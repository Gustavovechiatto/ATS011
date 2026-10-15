# Exercício ATS11 — BDD em um carrinho de compras

## O que foi implementado

- `carrinho.feature`: dois cenários Gherkin em português — adição bem-sucedida com estoque suficiente e tentativa com estoque insuficiente.
- `carrinho.py`: funções `criar_carrinho()` e `adicionar_produto(...)`, com atualização do total e da quantidade de unidades e exceção `ValueError("Estoque insuficiente")`.
- `test_carrinho.py`: automação com `pytest-bdd`, usando `scenarios`, `given`, `when`, `then` e `parsers.parse`. O `try...except` guarda a mensagem da exceção em `carrinho["erro"]`, permitindo validar o cenário de falha.
- `requirements.txt`: dependências necessárias.

## Como executar

Recomendado: Python 3.10 ou superior.

### 1. Abra o terminal na pasta do projeto

Entre na pasta `Exercicio_ATS11_BDD_Carrinho`.

### 2. Crie e ative um ambiente virtual (opcional, recomendado)

Windows:
```bash
python -m venv .venv
.venv\\Scripts\\activate
```

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Execute os testes solicitados no enunciado

```bash
pytest test_carrinho.py -v
```

Os dois cenários devem passar. No primeiro, 2 unidades a R$ 10,00 resultam em total 20,00 e 2 itens. No segundo, a tentativa de adicionar 6 unidades quando o estoque é 3 registra e valida a mensagem `Estoque insuficiente`.

## Estrutura

```text
Exercicio_ATS11_BDD_Carrinho/
├── carrinho.feature
├── carrinho.py
├── test_carrinho.py
├── requirements.txt
└── README.md
```
