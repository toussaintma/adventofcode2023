#!/usr/bin/python3

lines = open("input.txt")

seeds = []
l = lines.readline().strip()[6:]
seeds = list(map(lambda x: int(x), filter(lambda x: len(x.strip()) != 0, l.split(' '))))
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

locations = []
for s in seeds:
  t = s
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
    
  #print(f'For seed {s} we land on {t} through {trail}')
  locations.append(t)
print(f'Locations found: {locations}')
locations.sort()
print(f'The lowest location number is {locations[0]}')
