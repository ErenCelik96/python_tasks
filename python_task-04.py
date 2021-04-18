# assignment 008/1 (Password Reminder)
name = "Eren"
password = 12345
a = "Enter your name : "

while True:
  b = input(a).capitalize()

  if b != name:
    print(f"Hello {b}! See you later.")
  else:
    print(f"Hello, {b}! The password is : {password}")
    break
