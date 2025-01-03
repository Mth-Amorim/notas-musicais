NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': [0, 2, 4, 5, 7, 9, 11]}


def escalas(tonica, tonalidade):
    """
    Gera uma escala musical baseada na tônica e tonalidade fornecidas.
    
    Args:
        tonica (str): A nota inicial da escala (ex: 'C', 'A', 'G#').
        tonalidade (str): A tonalidade da escala (ex: 'maior', 'menor').
    
    Returns:
        dict: Um dicionário contendo as notas da escala e seus respectivos graus.
            - 'notas': Lista de notas na escala.
            - 'graus': Lista de graus da escala.
    
    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """

    intervalos = ESCALAS[tonalidade]
    tonica_POS = NOTAS.index(tonica.capitalize())
    temp = []

    for intervalo in intervalos:
        nota = (tonica_POS + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    ...
