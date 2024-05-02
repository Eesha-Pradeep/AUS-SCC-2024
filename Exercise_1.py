#getting temperature input
t = eval(input("enter temperature: "))
while True:
  if type(t)==int and (t<121 and t>-31):
    break

  print("Invalid input. Try again.")
  t = eval(input("enter temperature: "))

#table
s = " "*9
ss = " "*7
sss = " "*8
print(f"-30{ss}0{s}30{sss}60{sss}90{sss}120")

#output
star_no = int(round(abs(t)/3, 0))
if t<0:
  print((10-star_no)*" "+star_no*"*"+"|")
else:
  print(" "*10+"|"+star_no*"*")