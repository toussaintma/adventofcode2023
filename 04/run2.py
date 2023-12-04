lines = open("input.txt")

matching = []
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
      points += 1
  matching.append(points)
      #print(f'Number {i} is a winner')
  print(f'Card {card}: {points} points for {winning.strip()} and {h}')
print("Now processing")
cards = [1 for i in range(len(matching))]
for c in range(len(matching)):
  for i in range(matching[c]):
    cards[c + i + 1] += cards[c]
    print(f'Card {c + 1} adding {cards[c]} cards to {c + i + 2}')  
 
#print(matching)
#print(cards)
total = 0
for c in cards:
  total += c
print(f'There are {total} scratchcards')
  
