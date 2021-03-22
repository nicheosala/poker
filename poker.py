NUMERO_CARTE = 5


def check(mani):

    mani_concatenate = [item for sublist in mani for item in sublist]

    # Ogni carta ha due caratteri
    for carta in mani_concatenate:
        if len(carta) != 2:
            raise Exception("Carta non valida: " + carta + " COGLIONE")

    # Le carte devono essere NUMERO_CARTE
    for mano in mani:
        if len(mano) != NUMERO_CARTE:
            raise Exception(
                "Mano non valida: numero non corretto di carte COGLIONE")

    # Controllo semi
    for mano in mani:
        for carta in mano:
            if carta[1] not in ['1', '2', '3', '4']:
                raise Exception("Seme non valido. Carta: " +
                                carta + " COGLIONE")

    # Controllo valori
    for mano in mani:
        for carta in mano:
            if carta[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
                raise Exception("Valore non valido: " + carta + " COGLIONE")

    # Controllo doppioni
    for carta in mani_concatenate:
        if mani_concatenate.count(carta) > 1:
            raise Exception("Carta ripetuta: " + carta + " COGLIONE")


def is_colore(mano):
    return all(colore_carta == mano[0][1]
               for colore_carta in map(lambda x: x[1], mano))


VALORI = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', '1')
SEMI = ('1', '2', '3', '4')  # {1: picche, 2 : fiori, 3 : quadri, 4 : cuori}

# restituisce:
# - un numero negativo se c1 < c2
# - zero se le cart hanno lo stesso valore
# - un numero positivo se c1 > c2


def comparatore_valori(c1, c2):
    return VALORI.index(c1[0]) - VALORI.index(c2[0])


def ordina(mano):
    return sorted(mano, key=lambda x: VALORI.index(x[0]))


def is_scala(mano):
    mano_ordinata = ordina(mano)

    if list(map(lambda x: x[0], mano_ordinata)) == ['2', '3', '4', '5', '1']:
        return True

    for i in range(1, len(mano_ordinata)):
        if comparatore_valori(mano_ordinata[i], mano_ordinata[i - 1]) != 1:
            return False

    return True


def is_scala_reale(mano):
    return is_colore(mano) and is_scala(mano)


def semi(mano):
    return list(map(lambda x: x[1], mano))


def valori(mano):
    return list(map(lambda x: x[0], mano))


def is_poker(mano):
    vals = valori(mano)
    for valore in vals:
        if vals.count(valore) == 4:
            return True
    return False


def is_coppia(mano, valore):
    return valori(mano).count(valore) == 2


def is_tris(mano, valore):
    return valori(mano).count(valore) == 3

def is_doppia_coppia(mano):

    vals = valori(mano)
    coppia = 0

    for distinct_val in set(vals):
        if is_coppia(vals, distinct_val):
            coppia += 1

    return coppia == 2


def is_full(mano):

    vals = valori(mano)
    coppia = False
    tris = False

    for distinct_val in set(vals):
        if is_tris(vals, distinct_val):
            tris = True
        elif is_coppia(vals, distinct_val):
            coppia = True

    return coppia and tris


def valore_scala_reale(mano):
    mano_ordinata = ordina(mano)

    if list(map(lambda x: x[0], mano_ordinata)) == ['2', '3', '4', '5', '1']:
        return VALORI.index(mano_ordinata[3][0]) * 3 + SEMI.index(mano_ordinata[3][1])

    return VALORI.index(mano_ordinata[-1][0]) * 3 + SEMI.index(mano_ordinata[-1][1])


def valore_poker(mano):
    vals = valori(mano)
    for valore in vals:
        if vals.count(valore) == 4:
            return VALORI.index(valore)


def valore_full(mano):
    vals = valori(mano)
    for valore in vals:
        if vals.count(valore) == 3:
            return VALORI.index(valore)


def valore_colore(mano):
    mano_ordinata = ordina(mano)
    return VALORI.index(mano_ordinata[-1][0]) * 3 + SEMI.index(mano_ordinata[-1][1])


def valore_scala(mano):
    mano_ordinata = ordina(mano)

    if list(map(lambda x: x[0], mano_ordinata)) == ['2', '3', '4', '5', '1']:
        return VALORI.index(mano_ordinata[3][0]) * 3 + SEMI.index(mano_ordinata[3][1])

    return VALORI.index(mano_ordinata[-1][0]) * 3 + SEMI.index(mano_ordinata[-1][1])


def valore_tris(mano):
    vals = valori(mano)
    for valore in vals:
        if vals.count(valore) == 3:
            return VALORI.index(valore)


def valore_doppia_coppia(mano):
    mano_ordinata = ordina(mano)
    mosc = list(filter(lambda carta: valori(
        mano_ordinata).count(carta[0]) == 2, mano_ordinata))
    return VALORI.index(mosc[-1][0]) * 3 + VALORI.index(mosc[0][0]) + max(SEMI.index(mosc[-1][1]), SEMI.index(mosc[-2][1]))


def valore_coppia(mano):
    valutazione = 0
    coppia = list(filter(lambda carta : valori(mano).count(carta[0]) == 2, mano))
    for carta in mano:
        if carta not in coppia:
            valutazione += VALORI.index(carta[0]) / 2
        else:
            valutazione += VALORI.index(carta[0]) * 2
    valutazione += max(SEMI.index(coppia[0][1]), SEMI.index(coppia[1][1])) / 5
    return valutazione

def valore_carta_più_alta(mano):
    mano_ordinata = ordina(mano)
    return VALORI.index(mano_ordinata[-1][0]) * 3 + SEMI.index(mano_ordinata[-1][1])

# Punteggi:
# nullo             0
# coppia            100
# doppia coppia     200
# tris              300
# scala             400
# colore            500
# full              600
# poker             700
# scala reale       800


def valutazione(mano):

    if is_scala_reale(mano):
        return "scala reale", 8000 + valore_scala_reale(mano)
    elif is_poker(mano):
        return "poker", 7000 + valore_poker(mano)
    elif is_full(mano):
        return "full", 6000 + valore_full(mano)
    elif is_colore(mano):
        return "colore", 5000 + valore_colore(mano)
    elif is_scala(mano):
        return "scala", 4000 + valore_scala(mano)
    elif any(is_tris(mano, valore) for valore in valori(mano)):
        return "tris", 3000 + valore_tris(mano)
    elif is_doppia_coppia(mano):
        return "doppia coppia", 2000 + valore_doppia_coppia(mano)
    elif any(is_coppia(mano, valore) for valore in valori(mano)):
        return "coppia", 1000 + valore_coppia(mano)
    else:
        return "nullo", valore_carta_più_alta(mano)

# N = int(input())
# while N < 2 and N > 6:
#     N = int(input())

# mani = []
# for _ in range(N):
#     mano = input().split(", ")
#     mani.append(mano)

# check(mani)


mano = "K1 32 K2 T3 22".split(" ")

check([mano])
print(valutazione(mano))
