# fin = open("input.txt")
# nr_stari = int(fin.readline())
# stari = [int(x) for x in fin.readline().split()]
# nr_tranzitii = int(fin.readline())
# tranzitii = []
#
# for i in range(nr_tranzitii):
#     tranzitii.append([])
#
# for i in range(nr_tranzitii):
#     a, b, c = (fin.readline().split())
#     a = int(a)
#     b = int(b)
#     tranzitii[a].append((b,c))
#
#
#
# stare_initiala = int(fin.readline())
# nr_stari_finale = int(fin.readline())
# stari_finale = [int(x) for x in fin.readline().split()]
# nr_cuv_verif = int(fin.readline())
# cuvinte = []
# for i in range(nr_cuv_verif):
#     cuvinte.append(fin.readline().strip("\n"))
# # #pana aici am realizat cititrea datelor din fisier
#
# def dfs (nod, index_curent):
#     global gasit
#     if gasit == 1:
#         return
#     if index_curent == len(cuvant) and nod in stari_finale:
#             gasit = 1
#
#     else:
#         for l in range(len(tranzitii[nod])):
#             try:
#                 if tranzitii[nod][l][1] == "ld":
#                     if vazut[tranzitii[nod][l][0]][index_curent] == 0:
#                         vazut[tranzitii[nod][l][0]][index_curent] = 1
#                         dfs(tranzitii[nod][l][0], index_curent)
#                 elif tranzitii[nod][l][1] == cuvant[index_curent]:
#                     if vazut[tranzitii[nod][l][0]][index_curent] == 0:
#                         vazut[tranzitii[nod][l][0]][index_curent] = 1
#                         dfs(tranzitii[nod][l][0], index_curent+1)
#
#             except IndexError:
#                 continue
#
#
# for cuvant in cuvinte:
#     gasit = 0
#     vazut=[]
#     for x in range(nr_stari+1):
#         vazut.append([0]*(len(cuvant)+1))
#     dfs(stare_initiala, 0)
#     if gasit == 0:
#         print(f"cuvantul {cuvant} nu este acceptat de NFA")
#     else:
#         print(f"cuvantul {cuvant} este acceptat de NFA")
#
#
# fin.close()


fin = open("input.txt")
nr_stari = int(fin.readline())
stari = [int(x) for x in fin.readline().split()]
nr_tranzitii = int(fin.readline())
tranzitii = []

for i in range(nr_tranzitii):
    tranzitii.append([])

for i in range(nr_tranzitii):
    a, b, c = (fin.readline().split())
    a = int(a)
    b = int(b)
    tranzitii[a].append((b,c))



stare_initiala = int(fin.readline())
nr_stari_finale = int(fin.readline())
stari_finale = [int(x) for x in fin.readline().split()]
nr_cuv_verif = int(fin.readline())
cuvinte = []
for i in range(nr_cuv_verif):
    cuvinte.append(fin.readline().strip("\n"))
# #pana aici am realizat cititrea datelor din fisier

def dfs (nod, index_curent):
    global gasit
    if gasit == 1:
        return
    if index_curent == len(cuvant) and nod in stari_finale:
        gasit = 1

    else:
        for l in range(len(tranzitii[nod])):
            try:
                if tranzitii[nod][l][1] == "ld":
                    if (tranzitii[nod][l][0],index_curent) not in vazut.keys():
                        vazut[(tranzitii[nod][l][0],index_curent)] = 1
                        dfs(tranzitii[nod][l][0], index_curent)
                elif tranzitii[nod][l][1] == cuvant[index_curent]:
                    if (tranzitii[nod][l][0],index_curent) not in vazut.keys():
                        vazut[(tranzitii[nod][l][0],index_curent)] = 1
                        dfs(tranzitii[nod][l][0], index_curent+1)

            except IndexError:
                continue


for cuvant in cuvinte:
    gasit = 0
    vazut=dict()

    dfs(stare_initiala, 0)
    if gasit == 0:
        print(f"cuvantul {cuvant} nu este acceptat de NFA")
    else:
        print(f"cuvantul {cuvant} este acceptat de NFA")


fin.close()