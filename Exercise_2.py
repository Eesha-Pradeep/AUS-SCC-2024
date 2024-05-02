#Part 1

# a)
with open("tick.txt","r") as f:
  lines = f.readlines()

for i in lines:
  print(i)

print()

# b)
for i in lines:
  if lines.index(i)==0:
    continue
  for j in i:
    if j=="1":
      print("#",end="")
    else:
      print(" ",end="")
  print()


#Part 2

with open("tick.txt","r") as f:
  lines = f.readlines()

rows = len(lines)
cols = len(lines[0])-1

print("Original Image")
for i in lines:
  for j in i:
    if j=="1":
      print("#",end="")
    else:
      print(" ",end="")
  print()

print()
chars = []

for i in range(rows):
  row_chars = []
  for j in range(0,cols-1,2):
    row_chars.append(int(lines[i][j]) or int(lines[i][j+1]))
  chars.append(row_chars)

op = []
for i in range(0,rows,2):
  op_rows = []
  for j in range(len(chars[i])):
    op_rows.append(chars[i][j] and chars[i+1][j])
  op.append(op_rows)

print("Scaled Image")
for i in op:
  for j in i:
    if j==1:
      print("#", end="")
    else:
      print(" ", end="")
  print()