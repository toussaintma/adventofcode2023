input_lines = open("input.txt")

tot = 0
for l in input_lines:
  digits = []
  for c in l:
    if c in "0123456789":
      digits.append(c)
  value_string = digits[0] + digits[-1]
  value = int(value_string)
  tot += value
  print(f'{value} for line {l}')
print(tot)
    
