f = open("input.txt", "r")
ranges = [tuple(map(int,r.split("-"))) for r in f.read().split(",")]

res = 0
for r in ranges:
  for i in range(r[0], r[1]+1):
    s = str(i)
    for j in range(1, len(s) // 2 + 1):
      parts = []
      for k in range(0, len(s), j):
        parts.append(s[k:k+j])
      if all(part == parts[0] for part in parts):
        res += i
        break

print(res)
