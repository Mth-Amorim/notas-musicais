import re

from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_escala_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # act
    result = escala(tonica, tonalidade)

    assert result


def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError, match=re.escape(mensagem_de_erro)):
        escala(tonica, tonalidade)


def test_deve_retornar_um_erro_dizendo_que_a_escala_não_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_de_erro = f'Essa escala não existe ou não foi implementada. Tente uma dessas {list(ESCALAS.keys())}'

    with raises(KeyError, match=re.escape(mensagem_de_erro)):
        escala(tonica, tonalidade)


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado


def test_deve_garantir_os_graus_funcionam():
    assert escala('c', 'maior')['graus'] == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
