#!/usr/bin/python3

file_in = open("input.txt")
ranking = {"high": "1", "one": "2", "two": "3", "three": "4", "full": "5", "four": "6", "five": "7"}
strength = {"J": "00", "2": "01", "3": "02", "4": "03", "5": "04", "6": "05", "7": "06", "8": "07", "9": "08", "T": "09", "Q": "10", "K": "11", "A": "12"}

def get_score(hand):
  return hand.rank
  
def get_ranking(s):
  return int(ranking[s])

class Hand():
  hand = ""
  bid = 0
  rank = 0
  joker = 0
  status = ""
    
  def __init__(self, cards, bid):
    self.bid = bid
    self.hand = cards
    self.status = self.get_joker_status(self.hand) 
    self.rank = self.get_rank()
    
  def __str__(self):
    return 'Hand ' + self.hand + ' (' + str(self.bid) + ') with ' + str(self.joker) + ' jokers, scores ' + str(self.rank) + ' in group ' + self.status
  
  def get_rank(self):
    rank = ranking[self.status]
    for c in self.hand:
      rank = rank + strength[c]
    return int(rank)
  
  def get_joker_status(self, cards):
    min_cards = "".join(cards.split("J"))
    print(min_cards)
    j = 5 - len(min_cards)
    self.joker = j
    result = 0
    if j == 0:
      result = self.get_status(cards, 0)
    else:
      result = self.get_status(min_cards, j)
      
    return result
  
  def get_status(self, cards, jokers):
    stats = {}
    for i in cards:
      if i in stats:
        stats[i] += 1
      else:
        stats[i] = 1
    vol = [stats[s] for s in stats]
    vol.sort()
    
    print(f'Before: {vol}', end="")
    if jokers != 5:
      vol[len(vol) - 1] += jokers
    else:
      vol.append(5)
    print(f' after: {vol}')
    
    result = ""
    if len(vol) == 1:  
      result = "five"
    elif len(vol) == 2 and vol[0] == 1:
      result = "four"
    elif len(vol) == 2 and vol[0] == 2:
      result = "full"
    elif len(vol) == 3 and vol[2] == 3:
      result = "three"
    elif len(vol) == 3 and vol[2] == 2:
      result = "two"
    elif len(vol) == 4:
      result = "one"
    elif len(vol) == 5:
      result = "high"
    else:
      result = "error"
    return result
 

hands = {}
for line in file_in:
  line = line.strip()
  tokens = line.split(" ")
  h = Hand(tokens[0].strip(), int(tokens[1]))
  if h.status in hands:
    hands[h.status].append(h)
  else:
    hands[h.status] = [h]

print('Hands by type:')
winnings = 0
count = 1
ranked = list(hands.keys())
ranked.sort(key=get_ranking)
print('Searching through ', end="")
print(ranked)
for s in ranked:
  print('  Type ' + s)
  l = hands[s]
  l.sort(key=get_score)
  for h in l:
    winnings += count * h.bid
    print(str(count) + "> " + str(winnings) + " > ", end="")
    print(h)
    count += 1
    
print(f'total winnings are {winnings} over {count-1} hands')
  
