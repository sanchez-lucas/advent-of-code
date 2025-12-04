f = open("input.txt", "r")
banks = [list(map(int,list(l.strip()))) for l in f.readlines()]

total_jolt = 0

def get_highest_jolt(bank: list[int], jolt_size: int) -> int:
  if jolt_size == 0 or len(bank) == 0:
    return 0
  if jolt_size == 1:
    return max(bank)
  highest_number = max(bank[:-(jolt_size - 1)])
  highest_number_index = bank.index(highest_number)
  return highest_number * (10 ** (jolt_size - 1)) + get_highest_jolt(bank[highest_number_index + 1:], jolt_size - 1)

for bank in banks:
  total_jolt += get_highest_jolt(bank, 12)

print(total_jolt)
