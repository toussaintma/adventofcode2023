#!/usr/bin/python3

from time import process_time

filename = 'test1.txt'
hfile = open(filename).readlines()
print(f'Reading {filename}')

height = len(hfile)
width = len(hfile[0].strip())

pattern = [["" for i in range(width)] for j in range(height)]
for row in range(height):
  for col in range(width):
    pattern[row][col] = hfile[row][col]

def swap(tab, src, tgt):
  #print(f'Swapping {src} and {tgt}')
  temp = tab[src[0]][src[1]]
  tab[src[0]][src[1]] = tab[tgt[0]][tgt[1]]
  tab[tgt[0]][tgt[1]] = temp
  return
  
def tilt_north(tab):
  result = tab
  for col in range(width):
    #print(f'Doing column {col}')
    ptop = 0
    pbottom = 0
    for ptop in range(height):
      i = result[ptop][col]
      if i == '#':
        pass
      if i == 'O':
        pass
      if i == '.':
        #print(f'Found a . at {ptop}')
        # cherche un O pour swap
        pbottom = ptop
        out = False
        while pbottom < height and result[pbottom][col] != "#" and not out:
          j = result[pbottom][col]
          #print(f'At {pbottom} there is {j}')
          if j == 'O':
            swap(result, [pbottom, col], [ptop, col])
            out = True
          pbottom += 1
  return result

def tilt_south(tab):
  result = tab
  for col in range(width):
    #print(f'Doing column {col}')
    ptop = 0
    pbottom = 0
    for ptop in range(height - 1, -1, -1):
      i = result[ptop][col]
      if i == '#':
        pass
      if i == 'O':
        pass
      if i == '.':
        #print(f'Found a . at {ptop}')
        # cherche un O pour swap
        pbottom = ptop
        out = False
        while pbottom > -1 and result[pbottom][col] != "#" and not out:
          j = result[pbottom][col]
          #print(f'At {pbottom} there is {j}')
          if j == 'O':
            swap(result, [pbottom, col], [ptop, col])
            out = True
          
          pbottom += -1
  return result

def tilt_east(tab):
  result = tab
  for row in range(height):
    #print(f'Doing row {row}')
    pleft = 0
    pright = 0
    for pleft in range(width - 1, -1, -1):
      i = result[row][pleft]
      if i == '#':
        pass
      if i == 'O':
        pass
      if i == '.':
        #print(f'Found a . at {pleft}')
        pright = pleft
        out = False
        while pright > -1 and result[row][pright] != "#" and not out:
          j = result[row][pright]
          #print(f'At {pright} there is {j}')
          if j == 'O':
            swap(result, [row, pright], [row, pleft])
            out = True
          
          pright += -1
  return result

def tilt_west(tab):
  result = tab
  for row in range(height):
    #print(f'Doing row {row}')
    pleft = 0
    pright = 0
    for pleft in range(width):
      i = result[row][pleft]
      if i == '#':
        pass
      if i == 'O':
        pass
      if i == '.':
        #print(f'Found a . at {pleft}')
        pright = pleft
        out = False
        while pright < width and result[row][pright] != "#" and not out:
          j = result[row][pright]
          #print(f'At {pright} there is {j}')
          if j == 'O':
            swap(result, [row, pright], [row, pleft])
            out = True
          
          pright += 1
  return result

cycle = 0
result = pattern
t1_start = process_time()
iterations = 10000
for i in range(iterations): #1000000000
  result = tilt_east(tilt_south(tilt_west(tilt_north(result))))
t1_stop = process_time()
print(f'Spent {t1_stop - t1_start:.2}s to do {iterations} iterations')
# Spent 2.5s to do 10000 iterations
# Spent 2.1s to do 10000 iterations: no copy
#

load = 0
for row in range(height):
  many = result[row].count("O")
  load += many * (height - row)
  print(result[row])
print()
print(f'The total load is {load}')
