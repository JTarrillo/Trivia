import random

faciles = {
    1: [
        "¿Cuándo se libró la Batalla de Boyacá?",
        "7 de agosto de 1819",
        "Sabías que…",
    ],
    2: [
        "¿Cuál fue la primer ciudad del país en liberarse de la Corona Española?",
        "Cali", "Sabías que…"
    ],
    3: [
        "¿A qué suceso histórico del país hace referencia Gabriel García Márquez en su obra 'Cien años de soledad'?",
        "Masacre de las Bananeras", "Sabías que…"
    ],
    4: ["¿En qué año se separó Panamá de Colombia?", "1903", "Sabías que…"]
}
a = int(random.randrange(1, 4) in faciles)


def Formato(Cadena):
    for Vocal1, Vocal2 in [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"),
                           ("ú", "u")]:
        Cadena = Cadena.replace(Vocal1, Vocal2)
    return Cadena.upper()


def Respuesta(mayuscula):
    for D, C in faciles.items():
        if Formato(D) == Formato(mayuscula):
            return C


def elemento(mayuscula):
    for C in faciles.items:
        if mayuscula(C) == faciles.get([a][1]):
            return C


sabias = faciles.get([a][2])
print(("Sabías que... ", sabias), "Respuesta: ", Respuesta(input()))
