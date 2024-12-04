import numpy as np
from collections import Counter as c
n = 0
sim = []
dados1 = []
dados2 = []
dados = np.loadtxt("base1.txt",dtype=int)
for i in range(len(dados)):
  dados1.append(dados[i][0])
  dados2.append(dados[i][1])

dados1 = sorted(dados1)
dados2 = sorted(dados2)

print(sum(abs(dados1[i]-dados2[i])for i in range(len(dados))))

for i in range(len(dados)):
  n = 0
  for e in range(len(dados)):
    if dados1[i] == dados2[e]:
      n = n+1
  sim.append(dados1[i]*n)

print(sum(sim))