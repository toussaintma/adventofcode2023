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

#for p in range(len(patterns)):
#  print(f'Pattern {p}:')  
#  for r in range(len(patterns[p])):
#    print(f'{r}> {patterns[p][r]}')
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

#print(f'Comparing rows 1 and 2: {row_compare(1, 2, patterns[0])}')
#print(f'Comparing rows 2 and 3: {row_compare(2, 3, patterns[0])}')
#print(f'Comparing cols 1 and 2: {col_compare(1, 2, patterns[0])}')
#print(f'Comparing cols 4 and 5: {col_compare(4, 5, patterns[0])}')
print()

def get_href(tab):
  ref = []
  for r in range(len(tab) - 1):
    min_dist = min(r + 1, len(tab) - r - 1)
    #print(f'At row {r} we have a min of {min_dist}')
    is_ref = []
    for j in range(min_dist):
      is_ref.append(row_compare(r - j, r + j + 1, tab))
      #print(f'Comparing {r - j} and {r + j + 1}: {is_ref}')
    i = 0
    while i < len(is_ref) and is_ref[i]:
     i += 1       
    if i == 0:
      pass
      #print(f'No reflection found after row {r}')
    elif i == min_dist:
      #print(f'Found horizontal reflection of length {i} over {min_dist} after row {r}. Adding {r + 1}.')
      ref.append(['h', r, i, r + 1]) 
    else:
      pass
      #print(f'No reflection found after row {r}')
  return ref

def get_vref(tab):
  ref = []
  width = len(tab[0])
  for c in range(width - 1):
    min_dist = min(c + 1, width - c - 1)
    #print(f'At col {c} we have a min of {min_dist}')
    is_ref = []
    for j in range(min_dist):
      is_ref.append(col_compare(c - j, c + j + 1, tab))
      #print(f'Comparing {c - j} and {c + j + 1}: {is_ref}')
    i = 0
    while i < len(is_ref) and is_ref[i]:
     i += 1       
    if i == 0:
      pass
      #print(f'No reflection found after col {c}')
    elif i == min_dist:
      #print(f'Found vertical reflection of length {i} over {min_dist} after col {c}. Adding {c + 1}.')
      ref.append(['v', c, i, c + 1])
    else:
      pass
      #print(f'No reflection found after col {c}')
  return ref

def get_reflection(tab, legacy=None):
  ref = get_href(tab)
  ref.extend(get_vref(tab))
  l = list(filter(lambda x: len(x) != 0, ref))
  if legacy:
    l = list(filter(lambda x: x != legacy, l))
  #print(f'Found reflections: {l}')
  if len(l) == 0:
    result = l
  else:
    result = l[0]
  return result

result = {}

# Finding reflections
for p in range(len(patterns)):
  #print(f'Checking pattern {p}')
  result[p] = get_reflection(patterns[p])

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
print()
# part 1: Overall we find a summary number of 42974 from 427 rows above and 274 columns left of reflections


# for each pattern
# for each position we switch and check if different

optim = {}
for p in range(len(patterns)):
  print(f'Checking pattern {p}')
  height = len(patterns[p])
  width = len(patterns[p][0])
  h = 0
  w = 0
  out = False
  while h < height and not out:
    w = 0 
    while w < width and not out:
      old_val = patterns[p][h][w]
      if old_val == '.':
        patterns[p][h][w] = '#'
      else:
        patterns[p][h][w] = '.'
      ref = get_reflection(patterns[p], result[p])
      similarity = ((ref == result[p]) or (len(ref) == 0))      
      print(f'Position ({h},{w}) found: {ref} instead of {result[p]} similarity {similarity}')
      patterns[p][h][w] = old_val
      # if ref diff store and exit
      if not similarity:
        optim[p] = ref
        print(f'Found replacement, leaving loop: {optim}')
        out = True;
      w += 1
    h += 1
  #if p not in optim:
  #  optim[p] = result[p]      
  # test example where the alg fails to find a different reflection
    
rows_above = 0
cols_left = 0  
for i in optim:
  if optim[i][0] == 'h':
    rows_above += optim[i][3]
  else:
    cols_left += optim[i][3]

total = 100 * rows_above + cols_left
print()
print(f'Overall we find a summary number of {total} from {rows_above} rows above and {cols_left} columns left of reflections')


