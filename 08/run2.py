#!/usr/bin/python3

file_in = open("input.txt")

lines = file_in.readlines()

instruct = lines[0].strip()
print('Instructions: ' + instruct)

mapping = {}

for line in lines[2:]:
  line = line.strip()
  ins = line[0:3]
  left = line[7:10]
  right = line[12:15]
  mapping[ins] = {"L": left, "R": right}

for m in mapping:
 print(f'{m} = {mapping[m]}')

starters = []
closers = []
for n in mapping:
  if n[-1] == "A":
    starters.append(n)
  if n[-1] == "Z":
    closers.append(n)
print(f'Starters: {starters}')
print(f'Closers: {closers}')

def reached_closers(l):
  result = True
  for n in l:
    if not(n in closers):
      result = False
  return result

def reached(l):
  result = True 
  for n in l:
    if n[-1] != "Z":
      result = False 
  return result

# 0 79 158 237 => starters[0] goes x * 79
# 0 71 142 213 => starters[1] goes x * 71
# 0 53 106 159 => starters[2] goes x * 53
# 0 67 134 201 => starters[3] goes x * 67
# 0 73 146 219 => starters[4] goes x * 73
# 0 47 94 141 => starters[5] goes x * 47
# 79 and 71 both primes, lowest multiple is 79 * 71 = 5609
# 79, 71, 53, 67, 73, 47 all primes, their lowest multiple is 68337144929
# always at position 262 after 263 steps
# 17972669000000
#
# 0 and 1 Execution done in 1475167 steps and 5609 cycles
# it means 263 * 5609 = 
# 0 and 1 and 2 should be 78183851 steps in 297277 cycles
# Yes! Execution done in 78183851 steps and 297277 cycles
# 68337144929 * 13 =  888382884077
#             * 50 = 3416857246450
#             * 50 = 3416857246450
#             * 50 = 3416857246450
#             * 50 = 3416857246450
#             * 50 = 3416857246450
# Total             17972669116327 

count = 0 
node = starters[0:3] 
current = 0
cycle = 0
while not reached(node):
  next_node = []
  ins = instruct[current]
  for n in node:
    next_node.append(mapping[n][ins])
  #print(f'Moving from {node} to {next_node} by executing {ins} at position {str(current)} in {cycle} cycles')
  if next_node[0][-1] == "Z" or next_node[1][-1] == "Z":
    print(f'Reached {next_node} by executing {ins} at position {str(current)} in {cycle} cycles')
  count += 1
  current += 1
  node = next_node
  if current == len(instruct):
    current = 0
    cycle += 1
    if cycle % 10000 == 0:
      print(f'Entering cycle {cycle}')
  #if cycle > 11:
    #exit()
print(f'Execution done in {count} steps and {cycle} cycles')
  


