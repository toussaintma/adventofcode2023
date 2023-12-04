in_file = open("input.txt")


class Found():
  str_value = ""
  int_value = 0
  line = 0
  column = 0
  length = 0
  is_numeric = False
  
  def __init__(self, val, line, column, length):
    self.line = line
    self.column = column
    self.length = length
    self.str_value = val
    self.is_numeric = True
    for c in val:
      if not(c in "0123456789"):
        self.is_numeric = False
    if self.is_numeric:
      self.int_value = int(str_value)
   
  def __str__(self):
    return f'=Number {self.str_value} at position ({self.line}, {self.column})='
        
  def is_adjacent(self, line, column):
    result = True
    if abs(line - self.line) > 1:
      result = False
    if (column < self.column - 1) or (column > self.column + self.length):
      result = False
    return result

def is_symbol(s):
  result = False
  if (s != ".") and not(s in "0123456789"):
    result = True
  return result

space = []
count_line = 0
for line in in_file:
  line = line.strip()
  tab_line = []
  str_value = ""
  #print("New line " + line)
  for i in range(len(line)):
    #print(str(i) + str_value)
    if is_symbol(line[i]) and len(str_value) == 0:
      f = Found(line[i], count_line, i, 1)
      tab_line.append(f)
    if is_symbol(line[i]) and len(str_value) > 0:
      f = Found(str_value, count_line, i, 1)
      tab_line.append(f)
      str_value = ""
      f = Found(line[i], count_line, i, 1)
      tab_line.append(f)
    if line[i] in "0123456789":
      str_value += line[i]
      if i == len(line) - 1:
        f = Found(str_value, count_line, i - len(str_value) + 1, len(str_value))
        tab_line.append(f)
        str_value = ""
    if line[i] == ".":    
      if len(str_value) > 0:
        f = Found(str_value, count_line, i - len(str_value), len(str_value))
        tab_line.append(f)
        str_value = ""
 
  space.append(tab_line)
  count_line += 1  
print(f'Read {len(space)} lines')

def get_adj(node):
  result = []
  for i in range(node.line - 1, min(node.line + 2, len(space))):
    possible = space[i]
    for j in possible:
      if j.is_numeric and j.is_adjacent(node.line, node.column):
        result.append(j)
        print(f'adjacent identified: {j} to {node}')       
  return result
  
result = []
for i in range(len(space)):
  for j in range(len(space[i])):
    print(f'at {i},{j}: {space[i][j]}')
    if not(space[i][j].is_numeric):
      if space[i][j].str_value == "*":
        l = get_adj(space[i][j])
        print(f'there are {len(l)} adjacent to {space[i][j]}') 
        if len(l) == 2:
          result.append(l[0].int_value * l[1].int_value)

count = 0
for i in result:
  count += i

print(f'Sum of all part numbers id {count}')



    

