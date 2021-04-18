# alınan puana göre not verme (nested if loop)

x = int(input("Enter your note : "))
if x > 79 :
  if x >= 95:
    print("A+")
  elif x >= 90 :
    print("A")
  elif x >= 85 :
    print("B+")
  else : 
    print("B")
else :
  print("B-")
