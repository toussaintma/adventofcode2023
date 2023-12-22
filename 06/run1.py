#!/usr/bin/python3
file_in = open("input.txt")

raw_times = []
raw_distance = []

for line in file_in:
  line = line.strip()
  tokens = list(map(lambda x: int(x), filter(lambda x: len(x.strip()) != 0, line[10:].split(" "))))
  #print(tokens)
  if line[0] == "T":
    raw_times = tokens 
  else:
    raw_distance = tokens

races = [[0, 0] for i in range(len(raw_times))]
for i in range(len(raw_times)):
  races[i] = [raw_times[i], raw_distance[i]]
print(f'Races today: {races}')

def bin_split(low, high, time, tobeat):
  i = low + (high - low) // 2
  dist = (time - i) * i
  print(f'Searching to beat {tobeat}: holding {i} runs {dist}')
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

ways = []
for ra in races:
  time = ra[0]
  tobeat = ra[1]

  first = bin_split(0, time, time, tobeat)
  print(f'Found race winning at {first}')
  # go down
  i = first - 1
  dist = (time - i) * i
  print(f'Checking {i} to beat {tobeat} runs {dist}')
  while (dist > tobeat) and (i > 0):
    i -= 1
    dist = (time - i) * i
    print(f'Checking {i} to beat {tobeat} runs {dist}')
  result = [i + 1]
  # go up
  i = first + 1
  dist = (time - i) * i
  print(f'Checking {i} to beat {tobeat} runs {dist}')
  while (dist > tobeat) and (i < time):
    i += 1
    dist = (time - i) * i
    print(f'Checking {i} to beat {tobeat} runs {dist}')
  result.append(i - 1)
  ways.append(result[1] - result[0] + 1)
  print(f'Race {ra}: number of ways is {ways} with range {result}')

result = 1
for i in ways:
  result *= i 
print(f'Multiplication of numbers of ways gives {result}')  

