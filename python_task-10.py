# Assignment-008/9 (Letters Count) is due
word = input("Enter a word: ").lower()  # kullanıcıdan bir kelime istedik bu kelimenin tamamı küçük harf olacak
dic = {}  # boş bir dictionary yaratıp bunun içini dolduracağız
for i in word:  
  sayı = word.count(i)  # value
  dic.update({i:sayı})  # key ve value ları dict içine attık

print(dic)
