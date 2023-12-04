lines = open("input.txt")

total = 0
for line in lines:
  line = line[4:].strip()
  line = line.split(":")
  card = int(line[0])
  line = line[1].split("|")
  winning = line[0]
  have = line[1]
  h = list(map(lambda x: int(x.strip()), filter(lambda x: len(x) != 0, have.split(" "))))
    
  points = 0
  for i in h:
    s = str(i)
    if i < 10:
      s = " " + str(i) + " " 
    if s in winning:
      if points == 0:
        points = 1
      else:
        points *= 2
      
      print(f'Number {i} is a winner')
  total += points
  print(f'Card {card}: {points} points for {winning.strip()} and {h}')
print(f'There are {total} points')
  
  
  
  
