var = []

for i in range(10):
    num = int(input("digite um  numero:"))
    var.append(num)

rep = []

for i in range(len(var)):
    for j in range(u + 1, len(var)):
        if var[i] == var[j] and var[i] not in rep:
            rep.append(var[i])
            print("rep ", i)

for r in rep:
    pos = []
for u in range(len(var)):
    if var[u] == r:
        pos.append(i)
        print("a pos do numero ", r, " no vetor posição", pos)