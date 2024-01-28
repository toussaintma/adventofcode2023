#!/usr/bin/python3

from time import process_time

filename = 'input.txt'
hfile = open(filename).readlines()
print(f'Reading {filename}')

height = len(hfile)
width = len(hfile[0].strip())

pattern = [["" for i in range(width)] for j in range(height)]
for row in range(height):
  for col in range(width):
    pattern[row][col] = hfile[row][col]

# one slot is [index, length, count]
def get_total(slots):
  count = 0
  for i in range(len(slots)):
    for j in slots[i]:
      count += j[2]
  return count

def is_same(fs, rs):
  row = 0
  similar = True
  while row < height and similar:
    if fs[row] != rs[row]:
      similar = False
    row += 1
  return similar
  
def print_grid(slots, t):
  grid = get_grid(slots, t)
  print()
  print(f'Printing grid with {t} orientation: {len(slots)} slots with {get_total(slots)} blocks')
  for r in range(height):
    print(grid[r])
  return t

def get_grid(slots, t):
  grid = []
  for r in range(height):
    row = ['#' for c in range(width)]
    grid.append(row)
  
  if t == 'N' or t == 'S':  
    for c in range(width):
      slo = slots[c]
      for s in slo:
        for i in range(s[1]):
          result = '.'
          if t == 'N' and i < s[2]:
            result = 'O'
          if t == 'S' and i > s[1] - s[2] - 1:
            result = 'O'
          grid[s[0] + i][c] = result
  
  if t == 'W' or t == 'E':  
    for r in range(height):
      slo = slots[r]
      for s in slo:
        for i in range(s[1]):
          result = '.'
          if t == 'W' and i < s[2]:
            result = 'O'
          if t == 'E' and i > s[1] - s[2] - 1:
            result = 'O'
          grid[r][s[0] + i] = result  

  return grid

hori_slots = []
cell = ''
for row in range(height):
  new_line = []
  new_slot = []
  previous = ''
  for col in range(width):
    cell = pattern[row][col]
    if cell == '#' and previous != '#' and previous != '':
      new_line.append(new_slot)
      new_slot = []
    if cell != "#" and new_slot != []:
      new_slot[1] += 1
    if cell != "#" and new_slot == []:
      new_slot = [col, 1, 0]
    if cell == 'O':
      new_slot[2] += 1  
    previous = cell
    #print(f'Column {col}: {cell} with {new_slot} and {new_line}')
  if new_slot != []:
    new_line.append(new_slot)
  hori_slots.append(new_line)
  #print(f'Row {row}: found {new_line}')

#print(f'Horizontal slots: {len(hori_slots)} with {get_total(hori_slots)} blocks')
#for row in range(height):
#  print(f'{row}> {hori_slots[row]}')

vert_slots = []
cell = ''
for col in range(width):
  new_line = []
  new_slot = []
  previous = ''
  for row in range(height):
    cell = pattern[row][col]
    if cell == '#' and previous != '#' and previous != '':
      new_line.append(new_slot)
      new_slot = []
    if cell != "#" and new_slot != []:
      new_slot[1] += 1
    if cell != "#" and new_slot == []:
      new_slot = [row, 1, 0]
    if cell == 'O':
      new_slot[2] += 1  
    previous = cell
    #print(f'Row {row}: {cell} with {new_slot} and {new_line}')
  if new_slot != []:
    new_line.append(new_slot)
  vert_slots.append(new_line)
  #print(f'Column {col}: found {new_line}')

#print(f'Vertical slots: {len(vert_slots)} with {get_total(vert_slots)} blocks')
#for col in range(width):
#  print(f'{col}> {vert_slots[col]}')

def do_one_cycle(hori_slots, vert_slots):
  #tilt = "N" 
  #print_grid(vert_slots, tilt)

  tilt = "W" 
  for col in range(width):
    for s in vert_slots[col]:
      for c in range(s[2]):
        slots = hori_slots[s[0] + c]
        #print(f'col {col} pouring vert slots {s} into {slots}')
        out = False
        i = 0
        while not out and i < len(slots):
          if col >= slots[i][0] and col < slots[i][0] + slots[i][1]:
            slots[i][2] += 1
            out = True
            #print(f"col {col} +1 poured into {slots}")
            #if slots[i][2] > slots[i][1]:
            #  print(f'Fatal error! col {col} on ({row}, {col}) at slot {slots} found mode blocks than space left')
          i += 1
      s[2] = 0  
  #print_grid(hori_slots, tilt)
  #print(f'Done tilting to {tilt} total is {get_total(hori_slots)} blocks')

  tilt = "S" 
  for row in range(height):
    for s in hori_slots[row]:
      for c in range(s[2]):
        slots = vert_slots[s[0] + c]
        #print(f'row {row} pouring hori slots {s} into {slots}')
        out = False
        i = 0
        while not out and i < len(slots):
          if row >= slots[i][0] and row < slots[i][0] + slots[i][1]:
            slots[i][2] += 1
            out = True
            #print(f"row {row} +1 poured into {slots}")
            #if slots[i][2] > slots[i][1]:
            #  print(f'Fatal error! on ({row}, {col}) at slot {slots} found mode blocks than space left')
          i += 1
      s[2] = 0
  #print_grid(vert_slots, tilt)
  #print(f'Done tilting to {tilt} total is {get_total(vert_slots)} blocks')

  tilt = "E" 
  for col in range(width):
    for s in vert_slots[col]:
      for c in range(s[2]):
        slots = hori_slots[s[0] + s[1] - 1 - c]
        #print(f'col {col} pouring vert slots {s} into {slots}')
        out = False
        i = len(slots) - 1
        while not out  and i > -1 :
          if col >= slots[i][0] and col < slots[i][0] + slots[i][1]:
            slots[i][2] += 1
            out = True
            #print(f"col {col} +1 poured into {slots}")
            #if slots[i][2] > slots[i][1]:
            #  print(f'Fatal error! col {col} on ({row}, {col}) at slot {slots} found mode blocks than space left')
          i -= 1
      s[2] = 0
  #print_grid(hori_slots, tilt)
  #print(f'Done tilting to {tilt} total is {get_total(hori_slots)} blocks')

  tilt = "N"
  for row in range(height):
    for s in hori_slots[row]:
      for c in range(s[2]):
        slots = vert_slots[s[0] + s[1] - 1 - c]
        out = False
        #print(f'row {row} pouring hori slots {s} into {slots}')
        i = 0
        while not out and i < len(slots) :
          if row >= slots[i][0] and row < slots[i][0] + slots[i][1]:
            slots[i][2] += 1
            out = True
            #print(f"row {row} +1 poured into {slots} at block {i}")
            #if slots[i][2] > slots[i][1]:
            #  print(f'Fatal error! on ({row}, {col}) at slot {slots} found mode blocks than space left')
          i += 1   
      s[2] = 0
  #print_grid(vert_slots, tilt)
  #print(f'Done tilting to {tilt} total is {get_total(vert_slots)} blocks')
  return get_grid(vert_slots, tilt)

print()
print('-' * 50)
for row in range(height):
  for i in hori_slots[row]:
    i[2] = 0

# 112956
# 112959
# 112962
# cycle from 170 to 197 of length 27 next is 197+27=224
# 171 to 198 length 28
# 1000000000 - 171 = 999999829 % 27 = 19

cycle = 0
prior_runs = []
t1_start = process_time()
iterations = 1000000000
i = 0
is_cycle = False
cycle_length = 0
prior_runs.append(do_one_cycle(hori_slots, vert_slots))
#i += 1
while i < iterations and not is_cycle: #1000000000
  grid = do_one_cycle(hori_slots, vert_slots)
  is_cycle = False
  cycle_id = 0
  while cycle_id < len(prior_runs) and not is_cycle:
    if is_same(prior_runs[cycle_id], grid):
      is_cycle = True
      cycle_length = i - cycle_id
      print(f'Identified cycle of length {cycle_length} at {i} from {cycle_id}')
    cycle_id += 1
  prior_runs.append(grid)
  if i % 10000 == 0:
    print(f'Done {i} iterations ({i/1000000000:.2}%)')
  i += 1
print(f'Reached {i} iterations, found a cycle? {is_cycle} at {cycle_id}')
rest = (1000000000 - cycle_id) % cycle_length
print(f'{rest} needed at the end')
for i in range(rest):
  grid = do_one_cycle(hori_slots, vert_slots)
t1_stop = process_time()
print(f'Spent {t1_stop - t1_start:.2}s to do {i} iterations')
# with test1.txt
# old-run2.py: Spent 2.5s to do 10000 iterations
# old-run2.py: Spent 2.1s to do 10000 iterations (no copy)
# run2.py: Spent 8.8s to do 10000 iterations (by block)
# run2.py: Spent 0.56s to do 10000 iterations (no debug)
# run2.py: Spent 5.3s to do 100000 iterations (no change)
# run2.py: Spent 5.3e+01s to do 1000000 iterations (no change)

# with input.txt
# run2.py: Spent 1.2s to do 100 iterations
# run2.py: Spent 1.2e+02s to do 10000 iterations
# run2.py: Spent 1.1e+02s to do 10000 iterations (no intermed variables)
# run2.py: Spent 1.1e+02s to do 10000 iterations (no reset)
tilt = 'N'
print()
print(f'Final grid tilting {tilt}!')
grid = get_grid(vert_slots, tilt)        
load = 0
for row in range(height):
  many = grid[row].count("O")
  load += many * (height - row)
print()
print(f'The total load is {load}')
