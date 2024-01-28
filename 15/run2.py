#!/usr/bin/python3

infilename = 'input.txt'
infile = open(infilename)
print(f'Reading {infilename}')
steps = infile.readline().strip().split(',')
print(steps)

def get_hash(current_value, input_string):
  for c in input_string:
    ascii_code = ord(c)
    current_value += ascii_code
    current_value *= 17
    current_value %= 256
  return current_value

print(f'Hash value for the string HASH is: {get_hash(0, "HASH")}')
print()

boxes = [[] for i in range(256)]
focals = {}

def print_boxes(boxes):
  print()
  print('Printing all the boxes:')
  for i in range(len(boxes)):
    b = boxes[i]
    if len(b) > 0:
      print(f'Box {i}: ', end="")
      for l in b:
        print(f'[{l} {focals[l]}] ', end="") 
      print()

for s in steps:
  if "=" in s:
    command = s.split('=')
    comm = "="
    lens = command[0]
    box = get_hash(0, command[0])
    focal = int(command[1])
    print(f'For step {s} we read command {comm} on box {box} with lens {lens} of focal {focal}')
    if lens in boxes[box]:
      focals[lens] = focal
    else:
      boxes[box].append(lens)
      focals[lens] = focal
    print(f'Changed box {box} to {boxes[box]} with lens {lens} of focal {focal}') 
  else:
    command = s.split('-')
    comm = "-"
    lens = command[0]
    box = get_hash(0, command[0])
    print(f'For step {s} we read command {comm} on box {box} with lens {lens}') 
    if lens in boxes[box]:
      boxes[box].remove(lens)
      focals.pop(lens)
    print(f'Changed box {box} to {boxes[box]} with lens {lens} (in focals: {lens in focals})') 
  
print_boxes(boxes)

print()
results = []
for i in range(len(boxes)):
  b = boxes[i]
  if len(b) > 0:
    for j in range(len(b)):
      l = b[j]
      temp_result = (1 + i) * (1 + j) * focals[l]
      results.append(temp_result)
      print(f'Box {i} in position {j}: [{l} {focals[l]}] has {temp_result}') 


  
print(f'Focusing power is: {sum(results)}') 
  
infile.close()
