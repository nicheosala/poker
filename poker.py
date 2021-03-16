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

N = int(input())
while N < 2 and N > 6:
    N = int(input())

mani = []
for _ in range(N):
    mano = input().split(", ")
    mani.append(mano)

check(mani)

