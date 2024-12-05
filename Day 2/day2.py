safe = 0
unSafe = 0
dado = []
dadoTxt= []
bruto = open('C:\\Users\\ArX\\Desktop\\Prog\\Estudos\\adventofcode\\Day 2\\base.txt','r')
for i in bruto.readlines():   
    a = list((int(e) for e in i.split()))
    dado.append(a)

for i in dado:
    n = 0
    for e in range(len(i)-1):
        if i[e] - i[e+1] > 3 or i[e] - i[e+1] < -3:
            print(i,'Unsafe')
            unSafe = unSafe + 1
            break
        if i != sorted(i) and i != sorted(i,reverse=True):
            print(i,'Unsafe')
            unSafe = unSafe + 1
            break
        if i[e] - i[e+1] == 0:
            print(i,'Unsafe')
            unSafe = unSafe + 1
            break
        n = n + 1
        if n == len(i)-1:
            safe = safe + 1
            print(i,'Safe')
print('Safe',safe,"unsafe",unSafe)


