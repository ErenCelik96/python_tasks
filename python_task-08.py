# verilen sayı ile çarpım tablosu yapma (for loops)

n = int(input('enter a number between 1-10'))

for i in range(11):
    print('{}x{} = '.format(n, i), n*i)
