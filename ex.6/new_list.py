firstlist = [2, 4, 9, 16, 25]
listfor = []
listmap = []
listgen = []

for element in firstlist:
    listfor.append(element**2)
print(listfor)

listmap = list(map(lambda x: pow(x, 2), firstlist))
print(listmap)

listgen = [x**2 for x in firstlist]
print(listgen)
