#!/usr/bin/python3

raw_lines = open("input.txt").readlines()

records = []
info = []
for l in raw_lines:
  l = l.strip()
  raw = l.split()
  records.append(raw[0])
  info.append(list(map(lambda x: int(x), raw[1].split(','))))
print(f'Found {len(records)} records {records}')
print(f'With duplicate info: {info}')

def get_possible(s):
  m = s.count('?')
  n = 2 ** m
  variation = [[] for i in range(n)]
  for i in range(n):
    variation[i] = list(map(lambda x: '#' if x == '1' else '.', bin(i)[2:].zfill(m)))
  result = []
  for v in variation:
    line = ['' for i in range(len(s))]
    for i in range(len(s)):
      if s[i] == '?':
        line[i] = v.pop()
      else:
        line[i] = s[i]
    result.append("".join(line))
  return result

def check_arrangement(arr, infor):
  result = True
  s = list(filter(lambda x: len(x) != 0, arr.split('.')))
  if len(s) != len(infor):
    result = False
  else:
    for g in range(len(s)):
      if len(s[g]) != infor[g]:
        result = False
  return result

results = []
for r in range(len(records)):
  p = get_possible(records[r])
  real_p = []
  for i in range(len(p)):
    if check_arrangement(p[i], info[r]):
      real_p.append(p[i])
  #print(real_p)
  print('&', end="")
  results.append(len(real_p))

print()
sum = 0
for r in results:
  sum += r
print(f'The sum of all different arrangements is {sum}')

