f = open("input.txt", "r")
ranges, ids = [section.split("\n") for section in f.read().split("\n\n")]
ranges = [tuple(map(int, r.split("-"))) for r in ranges]
ids = list(map(int, ids))

res = 0
for id in ids:
  for low_r, high_r in ranges:
    if low_r <= id <= high_r:
      res += 1
      break

print(res)
