f = open("input.txt", "r")
banks = [list(map(int,list(l.strip()))) for l in f.readlines()]

total_jolt = 0

for bank in banks:
  highest_number = max(bank[:-1])
  highest_number_index = bank.index(highest_number)
  second_highest_number_from_index = max(bank[highest_number_index+1:])
  total_jolt += highest_number * 10 + second_highest_number_from_index

print(total_jolt)
