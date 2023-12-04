lines = open("input.txt")

limits = {"red": 12, "green": 13, "blue": 14}

def is_out(obj, lim):
  result = False
  for k in lim.keys():
    if (obj[k] > lim[k]):
      result = True
    #print(">>" + str(obj[k]) + " " + str(lim[k]) + " " + str(result))
  return result

impossible = {}
for l in lines:
  l = l.strip()[5:]
  print(l)
  game = int(l.split(":")[0].strip())
  content = l.split(":")[1]
  c = content.split(";")
  impossible[game] = False
  for grab in c:
    g = grab.split(",")
    unit_obj = {"red": 0, "green": 0, "blue": 0}
    for unit in g:
      if (unit.find("green") != -1):
        unit_obj["green"] += int(unit.split(" green")[0])
      if (unit.find("red") != -1):
        unit_obj["red"] += int(unit.split(" red")[0])
      if (unit.find("blue") != -1):
        unit_obj["blue"] += int(unit.split(" blue")[0])
    if is_out(unit_obj, limits):
      impossible[game] = True
    print(f'{unit_obj} {impossible[game]}')
print(impossible)
result = 0
for i in impossible.keys():
  if not(impossible[i]):
    result += i
print(f'Sum of the IDs: {result}')  

