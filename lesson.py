#küçük hesap makinesi
def hesap_makinesi():
 while True:

     x= input ("1.topla 2.cikar 3.carp 4 .bol 5.cikis işlemlerinden birini seçiniz:") 
     if x=="1":
          a=int (input("birinci sayiyi giriniz:"))
          b=int (input("ikinci sayiyi giriniz:"))
          print("Sonuç:",a+b)
          
     elif x=="2":
          a=int (input("birinci sayiyi giriniz:"))
          b=int (input("ikinci sayiyi giriniz:"))
          print("Sonuç:",a-b)
          
     elif x=="3":
          a=int (input("birinci sayiyi giriniz:"))
          b=int (input("ikinci sayiyi giriniz:"))
          print("Sonuç:",a*b)
   
     elif x=="4": 
          a=int (input("birinci sayiyi giriniz:"))
          b=int (input("ikinci sayiyi giriniz:"))

          if b==0:
           print("Hata! Bir sayi 0 ile bölünmez")
          else:
           print("Sonuç:",a/b)
            

     if b==0:
              print("Hata! Bir sayi 0 ile bölünmez")
     else:
          print("Sonuç:",a/b)
      
     elif x=="5":
     print("cikis yapiliyor...")
     break
 
 else: print("hatali sayi girdiniz")
  
hesap_makinesi()

     
     
          
