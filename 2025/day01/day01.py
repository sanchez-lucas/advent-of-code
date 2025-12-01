f = open("input.txt", "r")
rotations = [("RIGHT" if r == 'R' else 'LEFT', int("".join(n).strip())) for r, *n in f.readlines()]

t = 50
c = 0
for r in rotations:
  direction, steps = r
  print(t, direction, steps)
  t = (t + (steps if direction == "RIGHT" else -steps)) % 100
  if t == 0:
    c += 1

print(c)
