from pytest import mark

from notas_musicais.acordes import acorde


@mark.parametrize(
    'nota,esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('C°', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#']),
        ('F#', ['F#', 'A#', 'C#']),
    ],
)
def test_acorde_deve_retornar_as_notas_correspondentes(nota, esperado):
    notas, _ = acorde(nota).values()

    assert esperado == notas


def test_acorde_deve_retornar_os_Graus_correspondentes():
    nota = 'C'
    esperado = ['I', 'III', 'V']
    _, graus = acorde(nota).values()
    assert graus == esperado
