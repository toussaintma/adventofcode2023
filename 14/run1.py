#!/usr/bin/python3

filename = 'input.txt'
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
  result = [["." for i in range(width)] for j in range(height)]
  for row in range(height):
    for col in range(width):
      result[row][col] = pattern[row][col]
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

result = tilt_north(pattern)
load = 0
for row in range(height):
  many = result[row].count("O")
  load += many * (height - row)
  print(result[row])
print()
print(f'The total load is {load}')
