lines = open("input.txt")

limits = {"red": 12, "green": 13, "blue": 14}

def is_out(obj, lim):
  result = False
  for k in lim.keys():
    if (obj[k] > lim[k]):
      result = True
    #print(">>" + str(obj[k]) + " " + str(lim[k]) + " " + str(result))
  return result

powers = {}
for l in lines:
  l = l.strip()[5:]
  print(l)
  game = int(l.split(":")[0].strip())
  content = l.split(":")[1]
  c = content.split(";")
  max_obj = {"red": 0, "green": 0, "blue": 0}
  powers[game] = 0
  for grab in c:
    g = grab.split(",")
    for unit in g:
      if (unit.find("green") != -1):
        value = int(unit.split(" green")[0])
        if (value > max_obj["green"]):
          max_obj["green"] = value
      if (unit.find("red") != -1):
        value = int(unit.split(" red")[0])
        if (value > max_obj["red"]):
          max_obj["red"] = value
      if (unit.find("blue") != -1):
        value = int(unit.split(" blue")[0])
        if (value > max_obj["blue"]):
          max_obj["blue"] = value
  powers[game] = max_obj["red"] * max_obj["green"] * max_obj["blue"]
  print(f'{max_obj} {powers[game]}')
print(powers)
result = 0
for i in powers.keys():
  result += powers[i]
print(f'Sum of the powers: {result}')  

