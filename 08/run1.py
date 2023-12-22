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


count = 0 
node = "AAA"
current = 0
while node != "ZZZ":
  next_node = mapping[node][instruct[current]]
  print(f'Moving from {node} to {next_node} by executing {instruct[current]} at position {str(current)}')
  count += 1
  current += 1
  node = next_node
  if current == len(instruct):
    current = 0
print(f'Execution done in {count} steps')
  


