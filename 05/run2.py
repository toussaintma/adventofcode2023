#!/usr/bin/python3

lines = open("input.txt")

l = lines.readline().strip()[6:]
raw_seeds = list(map(lambda x: int(x), filter(lambda x: len(x.strip()) != 0, l.split(' '))))
seeds = []
for i in range(0, len(raw_seeds), 2):
  seeds.append([raw_seeds[i], raw_seeds[i] + raw_seeds[i + 1]])
print(f'Initial seeds: {seeds}')

mappings = {"seed": [],
	"soil": [],
	"fertilizer": [],
	"water": [],
	"light": [],
	"temperature": [],
	"humidity": [],
	}

step = 'seed'
for l in lines:
  l = l.strip()
  if len(l) != 0:
    if l.find('map') != -1:
      step = l.split('-')[0]
      print(f'Now on {step}')
    else:
      m = list(map(lambda x: int(x), l.split(' ')))
      mappings[step].append([m[1], m[1] + m[2], m[0]])
      print(mappings[step][-1])

def one_trail(s):
  t = s[0]
  trail = [t]
  for m in mappings:
    done = False
    for r in mappings[m]:
      #print(f'Comparing {t} with {r[0]} {r[1]}')
      if t >= r[0] and t < r[1] and not done:
        t = r[2] + t - r[0]
        done = True
        #print(f'{t} changed from {trail[-1]}')
    trail.append(t)
  return t  
  #print(f'For seed {s} we land on {t} through {trail}')


def split_range(ranged, mapping):
  r = []
  msg = ""
  # range is below mapping or above entirely    [77, 88] against [64, 77, 68] 
  if (ranged[1] <= mapping[0]) or (ranged[0] >= mapping[1]):
    msg += "(out)"
    r.append(ranged)
  # range is overlapping from the top
  if (ranged[0] < mapping[0] and ranged[1] > mapping[0] and ranged[1] <= mapping[1]):
    msg += "(from the top)"
    r.append([ranged[0], mapping[0]])
    r.append([mapping[0], ranged[1]])
  # from the bottom
  if (ranged[0] > mapping[0] and ranged[0] < mapping[1] and ranged[1] > mapping[1]):
    msg += "(from the bottom)"
    r.append([ranged[0], mapping[1]])
    r.append([mapping[1], ranged[1]])
  # is overlapping the range
  if (mapping[0] <= ranged[0] and mapping[1] >= ranged[1]):
    msg += "(mapping overflow)"
    r.append([ranged[0], ranged[1]])
  # is overlapping the mapping
  if (ranged[0] < mapping[0] and ranged[1] >= mapping[1]):
    msg += "(range overflow)"
    r.append([ranged[0], mapping[0]])
    r.append([mapping[0], mapping[1]])
    r.append([mapping[1], ranged[1]])
  print(f'Ranges: {ranged} against {mapping} gives {r} {msg}')
  return r

def ranged_mapping(ranged, mapping):
  # split many ranges in many based on a mapping
  for m in mapping:
    a = []
    for l in ranged:
      a.extend(split_range(l, m))
    ranged = a
  print(ranged)
  # apply the mappings
  result = []
  for l in ranged:
    t = l[0]
    done = False
    for m in mapping:
      #print(f'Comparing {t} with {m[0]} {m[1]}')
      if t >= m[0] and t < m[1] and not done:
        t = m[2] + t - m[0]
        done = True
    print(f'Location is [{t}, {t + l[1] - l[0]}]')
    result.append([t, t + l[1] - l[0]])
  # return a list of destination ranges
  return result 

locations = []
#locations.append(one_trail(seeds[0]))
#locations.append(one_trail(seeds[1]))
#print(f'Locations found: {locations}')
#locations.sort()
#print(f'The lowest location number is {locations[0]}')
locations = seeds
for m in mappings:
  print(f'Starting on {locations} for mappings[{m}]')
  locations = ranged_mapping(locations, mappings[m])
for l in range(len(locations)):
  locations[l] = locations[l][0]  
locations.sort()
print(f'Lowest location is {locations[0]} from {locations}')
