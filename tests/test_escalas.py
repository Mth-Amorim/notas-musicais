from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_escala_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # act
    result = escala(tonica, tonalidade)

    assert result


def test_deve_retornar_um_erro_quando_a_nota_nao_exist():
    # Arrumar
    tonica = 'z'
    tonalidade = 'maior'
    menssaem_esperada = f'Essa nota não existe, tente uma dessas {NOTAS}'

    # act
    result = escala(tonica, tonalidade)

    assert result == f'Essa nota não existe, tente uma dessas {NOTAS}'


def test_deve_retornar_um_erro_quando_a_escala_nao_exist():
    # Arrumar
    tonica = 'C'
    tonalidade = 'jujubinha'
    menssaem_esperada = f'Essa escala não existe, tente uma dessas {ESCALAS}'

    # act
    result = escala(tonica, tonalidade)

    assert result == f'Essa escala não existe, tente uma dessas {ESCALAS}'


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
