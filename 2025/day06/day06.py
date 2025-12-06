f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]
numbers = list(zip(*[list(map(int, [n for n in line.split(" ") if n != ""])) for line in lines[:-1]]))
operators = [op for op in lines[-1].split(" ") if op != ""]

res = 0
for i in range(len(operators)):
  op = operators[i]
  col = numbers[i]
  if op == "+":
    res += sum(col)
  elif op == "*":
    prod = 1
    for n in col:
      prod *= n
    res += prod

print(res)
