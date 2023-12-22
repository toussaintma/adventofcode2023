#!/usr/bin/python3

lines = open("input.txt")

series = []
for line in lines:
  line = line.strip()
  series.append(list(map(lambda x: int(x), filter(lambda x: len(x.strip()) != 0, line.split(" ")))))
for s in series:
  print(s)
print("-" * 10)

deriv_all = [[] for i in range(len(series))]
for s in range(len(series)):
  deriv = [series[s]]
  
  ref = series[s]
  d = []
  done = False
  while not done:
    d = []
    done = True
    for i in range(1, len(ref)):
      diff = ref[i] - ref[i - 1]
      d.append(diff)
      if diff != 0:
        done = False
    deriv.append(d)
    ref = d
  print(f'For {s} found: {deriv}')
  deriv_all[s] = deriv

for ref in range(len(series)):
  d = deriv_all[ref]
  for s in range(len(d)):
    for j in range(len(d[s])):
      print(f'{" " * s}{d[s][j]:3}', end="")
    print()
  print()
print("-" * 10)

result = []
for ref in range(len(series)):
  deriv = deriv_all[ref]
  poss = [0]
  print(f'Targetting: {deriv}')
  for i in range(len(deriv) - 2, -1, -1):
    val = deriv[i][-1] + poss[-1]
    print(f'For {ref}: with {i} we got {deriv[i][-1]} + {poss[-1]} = {val}')
    poss.append(val)
  result.append(poss[-1])
  print(f'For {ref}: new deriv are {poss}')
total = 0
for i in result:
  total += i
print(f'{total} is the sum of the extrapolated values {result}')


