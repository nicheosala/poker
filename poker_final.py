from time import sleep
from poker import valutazione, check

print("\n\nPoker legge una mano di poker e stabilisce il vincitore\n\n")
print("input:")

n = input()
mani = []

for _ in range (int(n)):
    mano = input().split()
    mani.append(mano)

if check(mani):
    mani_con_valutazione = []
    for mano in mani:
        mani_con_valutazione.append(valutazione(mano))

    posto = 1

    print("\n\n\t\t*** Classifica finale ***")
    print("\n")
    
    for i in sorted(mani_con_valutazione, key = lambda x:x[1], reverse = True):
        print(str(posto)+".", i[2], i[0], sep = "\t")
        posto += 1

    sleep(1.5)
    print("\n\nproduct by jst_greg and nicheosala\n")
