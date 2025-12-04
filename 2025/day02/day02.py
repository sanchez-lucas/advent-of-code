f = open("input.txt", "r")
ranges = [tuple(map(int,r.split("-"))) for r in f.read().split(",")]

res = 0
for r in ranges:
  for i in range(r[0], r[1]+1):
    s = str(i)
    if len(s) % 2 != 0:
      continue
    mid = len(s) // 2
    if s[:mid] == s[mid:]:
      res += i

print(res)
