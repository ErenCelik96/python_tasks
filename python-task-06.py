# while loop ile aklımdaki sayıyı bil oyunu

answer = 40
question = "Enter a number : "

print("Let's play game!")

while True :
  guess = int(input(question))

  if answer < answer:
    print("Little higher")
  elif answer > answer :
    print("Little lower")
  else :
    print("Are you mindreader?")
    break
