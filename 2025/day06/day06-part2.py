f = open("input.txt", "r")
lines = [line for line in f.readlines()]
cols = list(zip(*lines))

operations = []
op_cols = []
op = ""
for idx, col in enumerate(cols):
  col_str = "".join(col)
  if col_str.strip() == "" or idx == len(cols) - 1:
    if idx == len(cols) - 1:
      op_cols.append(int(col_str[:-1].strip()))
    operations.append((op_cols, op))
    op_cols = []
    op = ""
  else:
    if col_str[-1] in "+*":
      op = col_str[-1]
    op_cols.append(int(col_str[:-1].strip()))

res = 0
for col, op in operations:
  if op == "+":
    res += sum(col)
  elif op == "*":
    prod = 1
    for n in col:
      prod *= n
    res += prod

print(res)
