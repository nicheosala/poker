# Giocatore
# - username
# - denaro iniziale
# - mano (5 carte)

# 1. G1 può definire un invito, ovvero una quantità di soldi minima che gli altri giocatori devono puntare per partecipare alla partita
# 2. Distribuzione delle carte: cinque a testa
# 3. G1 guarda la propria mano e decide se puntare oppure no.
#   - se G1 decide di non puntare, tocca al giocatore successivo decidere se puntare.
#       - se tutti passano, la partita va monte
from random import shuffle


def pesca(mazzo, num_carte):

    if len(mazzo) < num_carte:
        raise Exception()

    ret = []
    for _ in range(num_carte):
        ret.append(mazzo.pop())

    return ret


def usernames(giocatori):
    return list(map(lambda g: g['username'], giocatori))


mazzo = [
    '11', '21', '31', '41', '51', '61', '71', '81', '91', 'T1', 'J1', 'Q1', 'K1',
    '12', '22', '32', '42', '52', '62', '72', '82', '92', 'T2', 'J2', 'Q2', 'K2',
    '13', '23', '33', '43', '53', '63', '73', '83', '93', 'T3', 'J3', 'Q3', 'K3',
    '14', '24', '34', '44', '54', '64', '74', '84', '94', 'T4', 'J4', 'Q4', 'K4'
]

giocatore = {
    'username': '',
    'denaro': 0,
    'mano': []
}

# Costanti
MAX_GIOCATORI = 5
NUM_GIOCATORI = 4
DENARO_INIZIALE = 1000

assert NUM_GIOCATORI <= MAX_GIOCATORI

# Fase 0
print('*** POKER STARS . GREG ***')
NUM_GIOCATORI = int(input("Benvenuti! Quanti giocatori siete? "))
while NUM_GIOCATORI <= 0 or NUM_GIOCATORI > MAX_GIOCATORI:
    NUM_GIOCATORI = int(
        input("Numero di giocatori non valido. Quanti giocatori siete? "))

shuffle(mazzo)

giocatori = []
for _ in range(NUM_GIOCATORI):
    nuovo_giocatore = giocatore.copy()
    username = input("Username: ")
    if username in usernames(giocatori):
        username = input("Username già in uso. Username: ")
    nuovo_giocatore['username'] = username
    nuovo_giocatore['denaro'] = DENARO_INIZIALE
    nuovo_giocatore['mano'] = pesca(mazzo, 5)
    giocatori.append(nuovo_giocatore)

# Fase 1: invito