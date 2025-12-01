f = open("input.txt", "r")
rotations = [("RIGHT" if r == 'R' else 'LEFT', int("".join(n).strip())) for r, *n in f.readlines()]

t = 50
c = 0
for r in rotations:
  direction, steps = r
  for i in range(steps):
    t += 1 if direction == "RIGHT" else -1
    t = t % 100
    if t == 0:
      c += 1

print(c)
