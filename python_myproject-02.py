# project 2 Metro duraklar arası süre hesaplama

print('Lütfen sadece "kadıköy" veya "tavşantepe" seçeneklerinden birini giriniz..')
kadıköy_yönü = {"Kadıköy" : 1, "Ayrılık Çeşmesi" : 2, "Acıbadem" : 3, "Ünalan" : 4, "Uzunçayır" : 5, "Göztepe" : 6, 
           "Yenisahra" : 7, "Kozyatağı" : 8, "Bostancı" : 9, "Küçükyalı" : 10, "Maltepe" : 11, "Huzurevi" :12,
           "Gülsuyu" : 13, "Esenkent" : 14, "Hastane Adliye" : 15, "Soğanlık" : 16, "Kartal" : 17, 
           "Yakacık Adnan Kahveci" : 18, "Pendik" : 19, "Tavşantepe" : 20}
tavşantepe_yönü = {"Kadıköy" : 20, "Ayrılık Çeşmesi" : 19, "Acıbadem" : 18, "Ünalan" : 17, "Uzunçayır" : 16, "Göztepe" : 15, 
           "Yenisahra" : 14, "Kozyatağı" : 13, "Bostancı" : 12, "Küçükyalı" : 11, "Maltepe" : 10, "Huzurevi" :9,
           "Gülsuyu" : 8, "Esenkent" : 7, "Hastane Adliye" : 6, "Soğanlık" : 5, "Kartal" : 4, 
           "Yakacık Adnan Kahveci" : 3, "Pendik" : 2, "Tavşantepe" : 1}
ort_süre = 2

while True:
  yön = input("Hangi yöne gidiyorsunuz?").title()
  mevcut = input("Hangi duraktasınız? ").title()
  hedef = input("Hangi durağa gideceksiniz? ").title()
  if yön == "Kadıköy":
    durak_sayısı = (int(kadıköy_yönü[mevcut] - kadıköy_yönü[hedef]))
    sonuç = durak_sayısı * ort_süre
    print(f"Ortalama {sonuç} dakika sonra {hedef} durağına varacaksınız. İyi yolculuklar dileriz..")
    break
  elif yön == "Tavşantepe":
    durak_sayısı = (int(tavşantepe_yönü[mevcut] - tavşantepe_yönü[hedef]))
    sonuç = durak_sayısı * ort_süre
    print(f"Ortalama {sonuç} dakika sonra {hedef} durağına varacaksınız. İyi yolculuklar dileriz..")
    break
  else:
    print('Yanlış yön bilgisi girdiniz! Lütfen sadece "kadıköy" veya "tavşantepe" seçeneklerinden birini giriniz..')
