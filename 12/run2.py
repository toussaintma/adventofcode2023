#!/usr/bin/python3

import time
import itertools
from functools import reduce 

raw_lines = open("test1.txt").readlines()

records = []
info = []
for l in raw_lines:
  l = l.strip()
  raw = l.split()
  records.append(raw[0])
  info.append(list(map(lambda x: int(x), raw[1].split(','))))
print(f'Found {len(records)} records {records}')
print(f'With duplicate info: {info}')

# 1,1,3 parmi 7 déjà 3# et 1. 3libres emplacements pour 1. => 3 possibilités
# 1,1,3 parmi 14 déjà 2# 7. 5libres pour 2. => 10 possibilités
# 1,3,1,6 parmi 15 déjà 7# 0. 8l pour 4. => 70 possibilités
#len(list(itertools.combinations(range(8), 4)))
# 1,6,5 parmi 19 déjà 11# 4. 4l pour 3. => 
# 3,2,1 parmi 12 déjà 3# 0. 9l pour 6. =>  

#2 sur 7 '.' manquant or il y en a déjà 1 => 3 possibilités
# 3 groupes 1,1,3 parmi 14: 7 sur 9 '.' manquant => on place 2. 2 parmi 5  

# 1 1 3    1*1*1*1*1=1        >> 21 pattern
# ???.###? ???.###? ???.###? ???.###? ???.### no 9
# ???.### ????.### ????.### ????.### ????.### 5

# #.#.### .#.#.###
# .#.#.### #.#.###
# 4 4 8    4*8*8*8*8=16384    >> 13 pattern
# .??..??...?##. ?.??..??...?##. ?.??..??...?##. ?.??..??...?##. ?.??..??...?##. 19
# .??..??...?##.? .??..??...?##.? .??..??...?##.? .??..??...?##.? .??..??...?##. no 19
# 1 1 1    1*1*1*1*1=1        
# 1 2 4    2*2*2*2*1=16 forcément 16 car 1 ne combine pas      >> 21 pattern
# ????.#...#...?  ????.#...#...
# ????.#...#... ?????.#...#...

# 4 4 5    4*5*5*5*5=2500     >> 13 pattern
# ????.######..#####.? ????.######..#####.? ????.######..#####.? ????.######..#####.? ????.######..#####.  no 9
# ????.######..#####. ?????.######..#####. ?????.######..#####. ?????.######..#####. ?????.######..#####. 5
# 10 15 10 15*15*15*15*10=506250 >> 21 pattern
# ?###???????? ?###????????? 4
# ?###???????? ??###???????? no 4

def get_variation(free, dot):
  comb = []
  #print(f'Computing variations for {dot} dots out of {free} slots', end="")
  for c in itertools.combinations(range(free), dot):
    item = ['#' for f in range(free)]
    for i in c:
      item[i] = '.'
    comb.append(item)
  #print(f' {len(comb)} combinations found')
  return comb

def get_possible(s, inf):
  free = s.count('?')
  broken = reduce(lambda x, y: x + y, inf)
  dot = len(s) - broken - s.count('.')
  result = []
  variat = get_variation(free, dot)
  for v in variat:
    line = ['' for i in range(len(s))]
    for i in range(len(s)):
      if s[i] == '?':
        line[i] = v.pop()
      else:
        line[i] = s[i]
    result.append("".join(line))
  #print(f'For pattern {s} with {broken}/{len(s)}, {dot} dots out of {free} we find: {result}')
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

# unfold
#for r in range(len(records)):
#  before = records[r]
#  records[r] = ((records[r] + '?') * 5)[:-1]
  #print(f'Unfolded records from {before} to {records[r]}')
#  before = info[r]
#  info[r] = info[r] * 5 
  #print(f'Unfolded info from {before} to {info[r]}')

def compute_pattern(rec, info):
  #print(f'Computing with: {rec} {info}')
  e0_time = time.time()
  p = get_possible(rec, info)
  e1_time = time.time()
  #print(f'1> Generate {len(p)} variations {(e1_time - e0_time):.2}s')
  real_p = []
  e2_time = time.time()
  for i in range(len(p)):
    if check_arrangement(p[i], info):
      real_p.append(p[i])
  #print(real_p)
  e3_time = time.time()
  #print(f'2> Check arrangements {e3_time - e1_time:.2}s')
  #print('&', end="")
  #print(f'At the end {len(real_p)} combinations')
  return len(real_p)

results = []
for r in range(len(records)):
  #print(f'Target is record {r}: {records[r]}')
  a = compute_pattern(records[r], info[r])
  b = compute_pattern(records[r] + '?', info[r])
  c = compute_pattern('?' + records[r], info[r])
  print(f'Unfolding record {r} found: {b*b*b*b*a} and {a*c*c*c*c}')
  results.append(a)

print()
sum = 0
for r in results:
  sum += r
print(f'The sum of all different arrangements is {sum}')

