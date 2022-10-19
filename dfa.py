fin = open("input.txt")
fout = open("output.txt", "w")
nr_stari = int(fin.readline())
stari = [int(x) for x in fin.readline().split()]
nr_tranzitii = int(fin.readline())
tranzitii = dict()

for i in range(nr_tranzitii):
    a, b, c = (fin.readline().split())
    a = int(a)
    b = int(b)
    if c in tranzitii.keys():
        if a in tranzitii[c].keys():
            tranzitii[c][a].append(b)
        else:
            tranzitii[c][a] = b
    else:
        tranzitii[c] = {a:b}
print(tranzitii)
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
        if nod_curent in tranzitii[litera].keys():
            nod_curent = tranzitii[litera][nod_curent];
        else:
            break
    else:
        if(nod_curent not in stari_finale):
            fout.write("NU\n")
            continue
        else:
            fout.write("DA\n")
            continue
    fout.write("NU\n")


fout.close()
fin.close()