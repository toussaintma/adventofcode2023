#!/usr/bin/python3

filename = 'input.txt'
hfile = open(filename).readlines()
print(f'Reading {filename}')

patterns = []
tab = []
for row in range(len(hfile)):
  line = list(hfile[row].strip())
  if len(line) == 0:
    patterns.append(tab)
    tab = []
  else:
    tab.append(line)
if len(tab) != 0:
  patterns.append(tab)

for p in range(len(patterns)):
  print(f'Pattern {p}:')  
  for r in range(len(patterns[p])):
    print(f'{r}> {patterns[p][r]}')
print(f'We have a series of {len(patterns)} patterns')

def row_compare(f, s, tab):
  return tab[f] == tab[s]

def col_compare(f, s, tab):
  fcol = []
  scol = []
  for r in range(len(tab)):
    fcol.append(tab[r][f])
    scol.append(tab[r][s])
  #print(f'Checking {fcol} and {scol}')
  return fcol == scol

print(f'Comparing rows 1 and 2: {row_compare(1, 2, patterns[0])}')
print(f'Comparing rows 2 and 3: {row_compare(2, 3, patterns[0])}')
print(f'Comparing cols 1 and 2: {col_compare(1, 2, patterns[0])}')
print(f'Comparing cols 4 and 5: {col_compare(4, 5, patterns[0])}')
print()

reflections = {}

# Finding horizontal reflections
for p in range(len(patterns)):
  print()
  reflections[p] = []
  #print(f'Checking pattern {p}')
  for r in range(len(patterns[p]) - 1):
    min_dist = min(r + 1, len(patterns[p]) - r - 1)
    #print(f'At row {r} we have a min of {min_dist}')
    is_ref = []
    for j in range(min_dist):
      is_ref.append(row_compare(r - j, r + j + 1, patterns[p]))
      #print(f'Comparing {r - j} and {r + j + 1}: {is_ref}')
    i = 0
    while i < len(is_ref) and is_ref[i]:
     i += 1       
    if i == 0:
      pass
      #print(f'No reflection found after row {r} in pattern {p}')
    elif i == min_dist:
      print(f'Found horizontal reflection of length {i} over {min_dist} after row {r} in pattern {p}. Adding {r + 1}.')
      reflections[p].append(['h', r, i, r + 1]) 
    else:
      pass
      #print(f'No reflection found after row {r} in pattern {p}')

# Finding vertical reflections
for p in range(len(patterns)):
  print()
  #print(f'Checking pattern {p}')
  width = len(patterns[p][0])
  for c in range(width - 1):
    min_dist = min(c + 1, width - c - 1)
    #print(f'At col {c} we have a min of {min_dist}')
    is_ref = []
    for j in range(min_dist):
      is_ref.append(col_compare(c - j, c + j + 1, patterns[p]))
      #print(f'Comparing {c - j} and {c + j + 1}: {is_ref}')
    i = 0
    while i < len(is_ref) and is_ref[i]:
     i += 1       
    if i == 0:
      pass
      #print(f'No reflection found after col {c} in pattern {p}')
    elif i == min_dist:
      print(f'Found vertical reflection of length {i} over {min_dist} after col {c} in pattern {p}. Adding {c + 1}.')
      reflections[p].append(['v', c, i, c + 1])
    else:
      pass
      #print(f'No reflection found after col {c} in pattern {p}')

result = {}
for i in reflections:
  max_ref = 0
  max_val = []
  for l in reflections[i]:
    if l[2] > max_ref:
      max_ref = l[2]
      max_val = l
  result[i] = max_val
print()
print(f'All reflections found: {result}')
rows_above = 0
cols_left = 0  
for i in result:
  if result[i][0] == 'h':
    rows_above += result[i][3]
  else:
    cols_left += result[i][3]

total = 100 * rows_above + cols_left
print()
print(f'Overall we find a summary number of {total} from {rows_above} rows above and {cols_left} columns left of reflections')

