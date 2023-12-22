#!/usr/bin/python3
file_in = open("input.txt")

race_time = 0
race_distance = 0

for line in file_in:
  line = line.strip()
  tokens = int("".join(line[10:].split(" ")))
  #print(tokens)
  if line[0] == "T":
    race_time = tokens 
  else:
    race_distance = tokens
print(f'Race today: {race_time}ms with {race_distance}mm to beat.')

def bin_split(low, high, time, tobeat):
  i = low + (high - low) // 2
  dist = (time - i) * i
  print(f'Searching to beat {tobeat}: holding {i}')
  if dist > tobeat:
    result = i
  else:
    r = bin_split(i, high, time, tobeat)
    if r != -1:
      result = r
    r = bin_split(low, i, time, tobeat)
    if r != -1:
      result = r  
  return result

ways = 0
time = race_time
tobeat = race_distance

def bin_boundary_low(low, high, time, tobeat):
  i = low + (high - low) // 2
  dist = (time - i) * i
  print(f'Searching boundary down {low}-{high}: holding {i}', end="")
  if (high - low) <= 2:
    if dist > tobeat:
      result = i
      print(f' success with {result}!')
    else:
      result = high
      print(f' success with boundary {result}!')
  else:
    if dist > tobeat:
      print(f' {dist} vs {tobeat} looking down')
      result = bin_boundary_low(low, i, time, tobeat)
    else:
      print(f' {dist} vs {tobeat} looking up')
      result = bin_boundary_low(i, high, time, tobeat)
  return result

def bin_boundary_high(low, high, time, tobeat):
  i = low + (high - low) // 2
  dist = (time - i) * i
  print(f'Searching boundary up {low}-{high}: holding {i}', end="")
  if (high - low) <= 2:
    if dist > tobeat:
      result = i
      print(f' success with {result}!')
    else:
      result = low
      print(f' success with boundary {result}!')
  else:
    if dist > tobeat:
      print(f' {dist} vs {tobeat} looking up')
      result = bin_boundary_high(i, high, time, tobeat)
    else:
      print(f' {dist} vs {tobeat} looking down')
      result = bin_boundary_high(low, i, time, tobeat)
  return result
# 62588

first = bin_split(0, time, time, tobeat)
print(f'Found race winning at {first}')
# go down
result = [bin_boundary_low(0, first, time, tobeat)]
# go up
result.append(bin_boundary_high(first, time, time, tobeat))
ways = result[1] - result[0] + 1
print(f'Number of ways is {ways} with range {result}')

print(f'Numbers of ways gives {ways}')  

