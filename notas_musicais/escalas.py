NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala partindo de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tônica da escala.
        tonalidade: Tonialidade da escala.

    Returns:
        um dicionario com as notas da escala e os graus.

    Raises:
        ValueErros: Caso a tônica não seja valida.
        KeyError: Caso a escala não exista ou não tenha sido implementada.

    Examples:
        >>> escala('C','maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a','maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        tonica_posicao = NOTAS.index(tonica)
        intervalos = ESCALAS[tonalidade]

    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas {NOTAS}')

    except KeyError:
        raise KeyError(
            f'Essa escala não existe ou não foi implementada, tente uma dessas {list(ESCALAS.keys())}'
        )

    temp = []

    for intervalo in intervalos:
        nota = (tonica_posicao + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
