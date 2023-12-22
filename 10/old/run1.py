#!/usr/bin/python3

all_lines = open("input.txt")
lines = all_lines.readlines()

tiles = {
	"|": [0, 2],
	"-": [1, 3],
        "L": [0, 1],
        "J": [0, 3],
        "7": [2, 3],
        "F": [1, 2],
        "S": [0, 1, 2, 3],
}

def is_known(c):
  result = True
  if c in '|-LJ7FS':
    result = False
  else:
    result = True  
  return result

def is_walkable(c):
  result = False
  if c in '|-LJ7FS':
    result = True
  else:
    result = False
  return result

def is_connected(parent, child, direction):
  result = False
  p = diagram[parent[0]][parent[1]]
  c = diagram[child[0]][child[1]]
  print(f'Compatibility between {p} and {c} in direction {direction}', end = "")
  if p == 'S':
    result = True
  else:
    if direction < 2:
      opposite = direction + 2
      if (direction in tiles[p]) and (opposite in tiles[c]):
        result = True
    else:
      opposite = direction - 2
      if (direction in tiles[p]) and (opposite in tiles[c]):
        result = True
  print(f': {result}')
  return result

def get_children(diag, node):
  result = []
  tile = diag[node[0]][node[1]]
  children = []
  if is_walkable(tile):
    if (node[0] > 0): # direction 0
      child = [node[0] - 1, node[1], node[2] + 1]
      if is_walkable(diag[child[0]][child[1]]) and is_connected(node, child, 0):
        children.append(child)
    if (node[1] < len(diag) - 1): # direction 1
      child = [node[0], node[1] + 1, node[2] + 1]
      if is_walkable(diag[child[0]][child[1]]) and is_connected(node, child, 1):
        children.append(child)
    if (node[0] < len(diag) - 1): # direction 2
      child = [node[0] + 1, node[1], node[2] + 1]
      if is_walkable(diag[child[0]][child[1]]) and is_connected(node, child, 2):
        children.append(child)
    if (node[1] > 0): # direction 3
      child = [node[0], node[1] - 1, node[2] + 1]
      if is_walkable(diag[child[0]][child[1]]) and is_connected(node, child, 3):
        children.append(child)  
  return children  
  #children = tiles[tile] # Tile may not be compatible!!
  #for c in children:
  #  if is_walkable(tile):
  #    if (c == 0) and (node[0] > 0): # top
  #      result.append([node[0] - 1, node[1], node[2] + 1])
  #    if (c == 1) and (node[1] < len(diagram) - 1): # right
  #      result.append([node[0], node[1] + 1, node[2] + 1])
  #    if (c == 2) and (node[0] < len(diagram) - 1): # down
  #      result.append([node[0] + 1, node[1], node[2] + 1])
  #    if (c == 3) and (node[1] > 0): # left
  #      result.append([node[0], node[1] - 1, node[2] + 1])
  #return result

def print_diagram(d):
  w = 0
  print()
  for l in d:
    print(f'{w}>', end="")
    w += 1
    for c in l:
      print(c, end="")
    print()
 
start = []
diagram = []
raw = []
stats = {'width': 0, 'height': len(lines), 'useless': 0}

for line in range(len(lines)):
  lines[line] = lines[line].strip()
  if stats['width'] == 0:
    stats['width'] = len(lines[line])
  if lines[line].find('S') != -1:
    start = [line, lines[line].find('S')]
    print(f'Found start position: {start}')
  stats['useless'] += lines[line].count(".")
  raw.append([*lines[line]])

stats['usefull'] = stats['width'] * stats['height'] - stats['useless']
print_diagram(raw)
print(stats)
print()
print("Selecting")
diagram = raw
#diagram = [raw[i][:50] for i in range(0, 50)]
#start = [1, 1]
#diagram[start[0]][start[1]] = 'S'
print_diagram(diagram)
print()
start.append(0) # length
count = 0
queue = [start]
max_target = [-1, -1, -1]
print(f'Starting with queue: {queue}')
while len(queue) != 0:
  node = queue.pop()
  count += 1
  tile = diagram[node[0]][node[1]]
  print(f'Looking at {node}: {tile}, top of a queue of {len(queue)} items')
  children = get_children(diagram, node)
  diagram[node[0]][node[1]] = '?'
  if node[2] > max_target[2]:
    max_target = node
  print(f'Found {len(children)} children: {children}')
  for c in children:
    print(f'child {c} is {diagram[c[0]][c[1]]}')
    if not is_known(diagram[c[0]][c[1]]) and c not in queue:
      queue.insert(0, c)
      
  print(f'Queue is now: {queue} with max so far: {max_target}')
  print(f'Walked {count / stats["usefull"] * 100}% {count} / {stats["usefull"]}. {len(queue)} nodes in queue {queue}')

print_diagram(diagram)
print(f'The longest number of steps is {node[2]} at {node}')

   


