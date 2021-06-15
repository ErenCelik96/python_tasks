a = 0
b = 1
fibonacci = []
for i in range(11):
  c = a
  a = a + b
  b = c
  fibonacci.append(b)
print(fibonacci)
