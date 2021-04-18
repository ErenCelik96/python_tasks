# Beton sektörü için deneme projesi

print("Lütfen cevapları doğru ve yazım hatası olmadan doldurunuz..")

d = input("Adınız ve soyadınız? ").title()
e = int(input("Yaşınız? "))
f = input("Cinsiyetiniz? ").lower()
a = input("Çalıştığınız firma? ").title()
b = input("Çalıştığınız bölüm? ").lower()
c = input("Göreviniz? ").lower()
beyaz = ("muhasebe", "iş güvenliği", "insan kaynakları", "tesis şefliği", "it", "bölge müdürlüğü", "bakım onarım", "arge")
mavi = ("santral", "laboratuvar")
ofis = ("ofis elemanı", "uzman", "tekniker", "mühendis", "yönetici", "müdür")
saha = ("santral yağcısı", "mikser operatörü", "pompa operatörü", "santral operatörü", "meydancı", "formen")


cümle = f"{a} firmasında çalışan {e} yaşındaki {d}, {b} bölümünde {c} olarak çalışmaktadır. Cinsiyet : {f}."
print(cümle)

if e >= 18 :
  print("Statü: İşçi")
elif e >= 16 :
  print("Statü: Genç işçi")
else : 
  print("Statü: Çocuk işçi")

if f == "kadın" :
  print("Özel statü: kadın çalışan")
else :
  print("Özel statü yok")

if b in beyaz :
  print("Beyaz yaka")
elif b in mavi :
  print("Mavi yaka")
else :
  print("Hatalı giriş, lütfen çalıştığınız bölümü yazın.")

if c in ofis :
  c = "Temel İSG eğitimi"
elif c in saha :
  c = "Temel İSG eğitimi, Yüksekte çalışma eğitimi, Kapalı alanda çalışma eğitimi"
print(f"Alması gereken eğitimler: {c}.")
else: 
  print("Hatalı giriş, lütfen görevinizi yazın.")
