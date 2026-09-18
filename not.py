def not_defteri():
    öğrenciler=[]
    
    while True:
        x=input("1.öğrenci ekle 2.öğrencileri listele 3.sinif ortalamsi 4.cikis")
        if x=="1":
         a=input("öğrenci adi giriniz:")
         b=int(input("öğrenci notu giriniz"))
         if a<0:
           print("hata!")
         else:
           öğrenciler.append((a,b))
           print("Öğrenci eklendi!!")


        
        elif x=="2":
          
         if not öğrenciler:
          print("kayitli öğrenci yok!")
         else:
           
        
        
        elif x=="3":
         
        print(a+b)/list

        elif x=="4":
         print("cikis yapliyor...")
         break
         





        not_defteri()
