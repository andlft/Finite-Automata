fin = open("input.txt")
nr_stari = int(fin.readline())
stari = [int(x) for x in fin.readline().split()]
nr_tranzitii = int(fin.readline())
tranzitii = dict()
litere = dict()

for i in range(nr_tranzitii):
    a, b, c = (fin.readline().split())
    a = int(a)
    b = int(b)
    tranzitii[(a, c)]=b
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

# print(stari)
# print(tranzitii)

nod_extra = max(stari)+1
for stare in stari:
    for litera in litere:
        if (stare, litera) not in tranzitii.keys():
            tranzitii[(stare, litera)] = nod_extra
            f = 1
# print(stari)
#
# print(stari_finale)

partitii = []
partitii.append(list(set(stari)-set(stari_finale)))
partitii.append(stari_finale)

# print(partitii)
while(True):
    partitii_refacute = []
    for partitie in partitii:
        dictionar = dict()
        for stare in partitie:
            lista_multimi = []
            for litera in litere:
                aux = tranzitii[(stare, litera)]
                for multime in partitii:
                    if aux in multime:
                        lista_multimi.append(tuple(multime))
                        break
            try:
                dictionar[tuple(lista_multimi)].append(stare)
            except:
                dictionar[tuple(lista_multimi)] = [stare]
        # print(dictionar)
        for value in dictionar.values():
            partitii_refacute.append(value)
    if sorted(partitii_refacute) == sorted(partitii):
        break
    partitii = partitii_refacute

# print(partitii)
print("stari dfa minimal:")

for i in range(len(partitii)):
    print(i, end='')
    if(partitii[i][0] in stari_finale):
        print("->finala", end='')
    print(' ')
print("tranzitii:")

for i in range(len(partitii)):
    trz = []
    for j in range(len(partitii[i])):
        for litera in litere:
            aux = tranzitii[(partitii[i][j], litera)]
            for k in range(len(partitii)):
                if aux in partitii[k]:
                    trz.append((k,litera))
    print(f"de la starea {i} la:")
    print(*set(trz))



fin.close()