sifreler = []
def sifre():
 
 while True:
  x=input("1.yeni kayit 2.giriş:")
  if x=="1":
   a=input("yeni kulanici adi:")
   b=input("yeni şifre:")
   sifreler.append((a,b))
   print("tebrikler kayit oldunuz!")
  elif x=="2":
   c=input("kulanici adi:")
   e=input("şifre:")
   if (c,e) in sifreler:
    print("giriş başarili!")
    break
   elif(c,e) not in sifreler:
    
    print("kullanici adi veya sifre yanlis.")



sifre()

   

  
  






     