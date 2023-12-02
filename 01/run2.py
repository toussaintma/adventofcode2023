lines = open("input.txt")

dig = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
possible = []
possible.extend(dig.keys())
possible.extend(dig.values())

def get_lowest(s):
  lower_index = len(s)
  lower_digit = ""
  
  for w in possible:
    found = s.find(w)
    if (found != -1) and (found <= lower_index):
      lower_index = found
      lower_digit = w
  return lower_index, lower_digit

def get_highest(s):
  higher_index = 0
  higher_digit = ""
 
  for w in possible:
    found = s.rfind(w)
    if (found != -1) and (found >= higher_index):
      higher_index = found
      higher_digit = w
  return higher_index, higher_digit

total = 0
for line in lines:
  l = line.strip()
  
  lower_index, lower_digit = get_lowest(l)
  if len(lower_digit) > 1:
    lower_digit = dig[lower_digit]
  #print(f'For {l} lowest is at {lower_index}: {lower_digit}')
  
  higher_index, higher_digit = get_highest(l)
  if len(higher_digit) > 1:
    higher_digit = dig[higher_digit]
  #print(f'For {l} highest is at {higher_index}: {higher_digit}')
  
   
  value = int(lower_digit + higher_digit)
  total += value
  print(f'{l} => {value} summing to {total}')
  
print(f'Final sum is {total}')

