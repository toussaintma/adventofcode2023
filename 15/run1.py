#!/usr/bin/python3

infilename = "input.txt"
infile = open(infilename)
print(f"Reading {infilename}")
steps = infile.readline().strip().split(",")
print(steps)


def get_hash(current_value, input_string):
    for c in input_string:
        ascii_code = ord(c)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value


print(f'Hash value for the string HASH is: {get_hash(0, "HASH")}')
print()

results = []
current_value = 0
for s in steps:
    temp_result = get_hash(0, s)
    results.append(temp_result)
    print(f"Step {s} has hash value {temp_result}")

print(f"Results summed up: {sum(results)}")

infile.close()
