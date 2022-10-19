fin = open("input.txt")
fout = open("output.txt", "w")
nr_stari = int(fin.readline())
stari = sorted([int(x) for x in fin.readline().split()])
dictionar = dict()
for i in range(1, len(stari)+1):
    dictionar[stari[i-1]] = i

stari = sorted(dictionar.values())

nr_tranzitii = int(fin.readline())
tranzitii = []
for i in range(100001):
    tranzitii.append([])

for i in range(nr_tranzitii):
    a, b, c = (fin.readline().split())
    a = int(a)
    b = int(b)
    tranzitii[dictionar[a]].append((dictionar[b],c))


stare_initiala = int(fin.readline())
nr_stari_finale = int(fin.readline())
stari_finale = [dictionar[int(x)] for x in fin.readline().split()]
nr_cuv_verif = int(fin.readline())
cuvinte = []
for i in range(nr_cuv_verif):
    cuvinte.append(fin.readline().strip("\n"))

# #pana aici am realizat cititrea datelor din fisier

def dfs (nod, index_curent):
    if index_curent == len(cuvant):
        if stop[nod] == 1:
            global gasit
            gasit = 1

    else:
        for l in range(len(tranzitii[nod])):
            if tranzitii[nod][l][1] == cuvant[index_curent]:
                if vazut[tranzitii[nod][l][0]][index_curent] == 0:
                    vazut[tranzitii[nod][l][0]][index_curent] = 1
                    dfs(tranzitii[nod][l][0], index_curent+1)


stop = []
for i in range(1001):
    stop.append(0)
for i in stari_finale:
    stop[i]=1


for cuvant in cuvinte:
    gasit = 0
    vazut=[]
    for x in range(nr_stari+1):
        vazut.append([0]*(len(cuvant)+1))
    dfs(stare_initiala, 0)
    if gasit == 0:
        fout.write("NU\n")
    else:
        fout.write("DA\n")



fout.close()
fin.close()