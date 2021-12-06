# Assignment-008/3 (Is it an Armstrong Number?)

print("Lütfen sadece pozitif bir sayı giriniz..")
sayı = "Bir sayı giriniz: "
while True:
  soru = (input(sayı))
  sayı_yeni = soru.isdigit()
  if sayı_yeni is False:
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
  else:
    break

uzunluk = len(soru)
liste = []

for i in soru:
  basamak = int(i) ** int(uzunluk)
  liste.append(basamak)
  sonuç = sum(liste)
if str(sonuç) == soru:
  print(f"{sonuç} is an Armstrong number")
else:
  print(f"{soru} is not an Armstrong number.")
