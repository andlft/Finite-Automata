fin = open("input.txt")
nr_stari = int(fin.readline())
stari = [int(x) for x in fin.readline().split()]
nr_tranzitii = int(fin.readline())
tranzitii = []
litere = dict()
tabel1 = dict()
tabel2 = dict()

for i in range(nr_stari):
    tranzitii.append([])

for i in range(nr_tranzitii):
    a, b, c = (fin.readline().split())
    a = int(a)
    b = int(b)
    tranzitii[a].append((b,c))
    if c not in litere.keys():
        litere[c] = 1

stare_initiala = int(fin.readline())
nr_stari_finale = int(fin.readline())
stari_finale = [int(x) for x in fin.readline().split()]
# nr_cuv_verif = int(fin.readline())
# cuvinte = []
# for i in range(nr_cuv_verif):
#     cuvinte.append(fin.readline().strip("\n"))
#pana aici am realizat cititrea datelor din fisier

# tabel_nfa = []

for stare in stari:
    for litera in litere.keys():
        multime = []
        try:
            for tranzitie in tranzitii[stare]:
                if tranzitie[1] == litera:
                    multime.append(tranzitie[0])
            tabel1[(stare, litera)] = multime
        except:
            pass


stari_dfa = [[stare_initiala]]


index = 0

while(index < len(stari_dfa)):
    for litera in litere.keys():
        stare_noua = []
        for nr in stari_dfa[index]:
            stare_noua += tabel1[(nr, litera)]

        tabel2[tuple(stari_dfa[index]), litera] = stare_noua
        stare_noua = set(stare_noua)
        stare_noua = list(stare_noua)

        if stare_noua not in stari_dfa:
            stari_dfa.insert(index + 1, stare_noua)

    index += 1


print("stari DFA: ")
for stare in sorted(stari_dfa):
    if stare != []:
        print(*stare,sep='_', end='')
    else:
        continue
    if set(stare).intersection(stari_finale) != set():
        print("--> finala", end='')
    print(" ")
print(f"stare intiala DFA: {stare_initiala}")

print("tranzitii:")
for tranzitie in tabel2.keys():
    if tranzitie[0] != []:
        if tabel2[tranzitie] != []:
            print(*tranzitie[0], sep='_', end='')
            print("-->", end = '' )
            print(*set(tabel2[tranzitie]), sep = '_', end = '')
            print(f": {tranzitie[1]}")


fin.close()