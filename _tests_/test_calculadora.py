# 1 - bibliotecas, frameworks e referências externas
import pytest # framework de teste de unidade

# funções que serão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# 2 - Testes
def test_somar_dois_numeros():

    # Padrão / Standard AAA (Triple A / 3A) IEEE = Arrange, Act, Assert

    # Arrange / Prepara / Configura
    # Dados de entrada e saída
    num1 = 5
    num2 = 7
    resultado_esperado = 12

   # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

   # Assert / Valida
    assert resultado_esperado == resultado_obtido