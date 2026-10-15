"""Testes BDD que conectam os cenários Gherkin às regras do carrinho."""
from pathlib import Path

import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from carrinho import criar_carrinho, adicionar_produto


scenarios(str(Path(__file__).parent / "carrinho.feature"))


@given("que o carrinho está vazio", target_fixture="carrinho")
def carrinho_vazio():
    return criar_carrinho()


@when(
    parsers.parse(
        "adiciono {quantidade:d} unidades de um produto com estoque {estoque:d} e preço unitário {preco:f}"
    ),
    target_fixture="carrinho",
)
def adicionar_com_estoque(carrinho, quantidade, estoque, preco):
    try:
        adicionar_produto(carrinho, quantidade, estoque, preco)
    except ValueError as exc:
        carrinho["erro"] = str(exc)
    return carrinho


@when(
    parsers.parse(
        "tento adicionar {quantidade:d} unidades de um produto com estoque {estoque:d} e preço unitário {preco:f}"
    ),
    target_fixture="carrinho",
)
def tentar_adicionar_sem_garantia(carrinho, quantidade, estoque, preco):
    try:
        adicionar_produto(carrinho, quantidade, estoque, preco)
    except ValueError as exc:
        carrinho["erro"] = str(exc)
    return carrinho


@then(parsers.parse("o total do carrinho deve ser {total:f}"))
def validar_total_decimal(carrinho, total):
    assert carrinho["total"] == pytest.approx(total)


@then(parsers.parse("o total do carrinho deve ser {total:d}"))
def validar_total_inteiro(carrinho, total):
    assert carrinho["total"] == total


@then(parsers.parse("a quantidade de itens no carrinho deve ser {quantidade:d}"))
def validar_quantidade(carrinho, quantidade):
    assert carrinho["itens"] == quantidade


@then(parsers.parse('deve ocorrer o erro "{mensagem}"'))
def validar_erro(carrinho, mensagem):
    assert carrinho.get("erro") == mensagem
