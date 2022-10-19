fin = open("input.txt")
fout = open("output.txt", "w")
nr_stari = int(fin.readline())
stari = [int(x) for x in fin.readline().split()]
nr_tranzitii = int(fin.readline())
tranzitii = dict()
stiva = ["$"]

for i in range(nr_tranzitii):
    a, b, c, d, e = (fin.readline().split())
    a = int(a)
    b = int(b)
    if a in tranzitii.keys():
        tranzitii[a].append((b, c, d, e))
    else:
        tranzitii[a] = [(b, c, d, e)]
stare_initiala = int(fin.readline())
nr_stari_finale = int(fin.readline())
stari_finale = [int(x) for x in fin.readline().split()]
nr_cuv_verif = int(fin.readline())
cuvinte = []
for i in range(nr_cuv_verif):
    cuvinte.append(fin.readline().strip("\n"))


#  pana aici am realizat citirea datelor din fisier

for cuv in cuvinte:
    nod_curent = stare_initiala
    for litera in cuv:
        if (litera, stiva[len(stiva)-1]) in [(x[1], x[2]) for x in tranzitii[nod_curent]]:
            # print(nod_curent, litera, stiva)
            if stiva != list():
                for tpl in tranzitii[nod_curent]:
                    if tpl[1] == litera and stiva[len(stiva)-1] == tpl[2]:
                        nod_curent = tpl[0]
                        stiva.pop(len(stiva)-1)
                        for lit in range(len(tpl[3])):
                            if tpl[3][len(tpl[3])-lit-1] != "&":
                                stiva.append(tpl[3][len(tpl[3])-lit-1])
                        break

        else:
            print(f"Cuvantul {cuv} nu este acceptat!")
            break
    else:
        print(f"cuvantul {cuv} este acceptat!")
# print(tranzitii)

fout.close()
fin.close()