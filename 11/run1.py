#!/usr/bin/python3

from copy import deepcopy

raw_lines = open("input.txt").readlines()

height = len(raw_lines)
width = len(raw_lines[0].strip())
raw_galaxies = []

for real_l in range(len(raw_lines)):
  raw_lines[real_l] = raw_lines[real_l].strip()
  for real_c in range(len(raw_lines[real_l])):
    if raw_lines[real_l][real_c] == '#':
      raw_galaxies.append([real_l, real_c])

print('Found the following galaxies:')
print(raw_galaxies)
print()

def get_lines_to_expand(sky):
  result = []
  for l in range(height):
    b = True
    for c in range(width):
      if sky[l][c] != '.':
        b = False  
    if b:
      result.append(l)
  return result

def get_columns_to_expand(sky):
  result = []
  for c in range(width):
    b = True
    for l in range(height):
      if sky[l][c] != '.':
        b = False  
    if b:
      result.append(c)
  return result
  
def get_shortest(index_from, index_to):
  #[6, 1] and [9, 5] 9-6+1 5-1+1 => 9
  #[7, 9] and [9, 5] 9-7+1 9-5+1 => 8
  hori = abs(index_from[0] - index_to[0]) 
  vert = abs(index_from[1] - index_to[1])
  return hori + vert
   
print('Now expanding')
expand_lines = get_lines_to_expand(raw_lines)
expand_columns = get_columns_to_expand(raw_lines) 
print(f'Found lines to expand: {expand_lines}')
print(f'Found columns to expand: {expand_columns}')
galaxies = deepcopy(raw_galaxies)
print('Expanding Lines first', end="")
for g in galaxies:
  applied = list(filter(lambda x: x < g[0], expand_lines))
  g[0] += len(applied)
print(', then columns')
for g in galaxies:
  applied = list(filter(lambda x: x < g[1], expand_columns))
  g[1] += len(applied)
print(f'Expanded galaxies are: {galaxies}')     
print()
n = int(len(galaxies) * (len(galaxies) - 1) / 2)
print(f'There are {n} pairs of galaxies')
shortest = []
for i in range(len(galaxies)):
  for j in range(i + 1, len(galaxies)):
    shortest.append(get_shortest(galaxies[i], galaxies[j]))
    #print(f'{i} -> {j}: From {galaxies[i]} to {galaxies[j]} is {get_shortest(galaxies[i], galaxies[j])}')
print(shortest)
print()
sum = 0
for s in shortest:
  sum += s
print(f'The sum of the shortest path is {sum}')



  
