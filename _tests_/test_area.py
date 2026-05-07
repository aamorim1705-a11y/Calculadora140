# 1 - Bibliotecas, frameworks e referências externas
import pytest

# Funções 
from calculadora.area import area_quadrado, area_retangulo, area_triangulo
from utils.utils import ler_csv

# 2 - Testes
def test_area_quadrado():
     # Configura
    lado = 5
    resultado_esperado = 25

    # Executa
    resultado_obtido = area_quadrado(lado)

    # Valida
    assert resultado_esperado == resultado_obtido

def test_area_retangulo():
     # Configura
    base = 8
    altura = 3
    resultado_esperado = 24

    # Executa
    resultado_obtido = area_retangulo(base, altura)

    # Valida
    assert resultado_esperado == resultado_obtido

def test_area_triangulo():
     # Configura
    base = 8
    altura = 4
    resultado_esperado = 16

    # Executa
    resultado_obtido = area_triangulo(base, altura)

    # Valida
    assert resultado_esperado == resultado_obtido

# Massa de teste a partir de uma lista de valores
@pytest.mark.parametrize('lado, resultado_esperado',
                         [ 
                            (2, 4), 
                            (8, 64),
                            (5, 25),
                            (3, 9)
                         ]
                        )
def test_area_quadrado_lista(lado, resultado_esperado):
    # Executa
    resultado_obtido = area_quadrado(lado)

    # Valida
    assert resultado_esperado == resultado_obtido
    
# Massa de teste a partir de um arquivo csv   
@pytest.mark.parametrize('base, altura, resultado_esperado',
                           ler_csv('./fixtures/massa_area_retangulo.csv')
                         )

def test_area_retangulo_csv(base, altura, resultado_esperado):
   # Executa
    resultado_obtido = area_retangulo(float(base), float(altura))

   # Valida
    assert float(resultado_esperado) == resultado_obtido

    