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
            raise Exception("Mano non valida: numero non corretto di carte COGLIONE")

    # Controllo semi
    for mano in mani:
        for carta in mano:
            if carta[1] not in ['1', '2', '3', '4']:
                raise Exception("Seme non valido. Carta: " + carta + " COGLIONE")
    
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
    for colore_carta in map(lambda x : x[1], mano))

VALORI = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', '1')

# restituisce:
# - un numero negativo se c1 < c2
# - zero se le cart hanno lo stesso valore
# - un numero positivo se c1 > c2
def comparatore_valori(c1, c2):
    return VALORI.index(c1[0]) - VALORI.index(c2[0])

def is_scala(mano):
    mano_ordinata = sorted(mano, key = lambda x : VALORI.index(x[0]))
    
    if list(map(lambda x : x[0], mano_ordinata)) == ['2', '3', '4', '5', '1']:
        return True

    for i in range(1, len(mano_ordinata)):
        if comparatore_valori(mano_ordinata[i], mano_ordinata[i - 1]) != 1:
            return False

    return True

def is_scala_reale(mano):
    return is_colore(mano) and is_scala(mano)

def semi(mano):
    return list(map(lambda x : x[1], mano))

def valori(mano):
    return list(map(lambda x : x[0], mano))

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

# N = int(input())
# while N < 2 and N > 6:
#     N = int(input())

# mani = []
# for _ in range(N):
#     mano = input().split(", ")
#     mani.append(mano)

# check(mani)

mano = ['14', '13', 'K1', 'K3', '12']

check([mano])
print(is_full(mano))
