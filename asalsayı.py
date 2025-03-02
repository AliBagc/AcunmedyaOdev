#Asal sayı olup olmadığını söyleyen program 

sayi=int(input("Sayı Giriniz"))
adet = 0
for i in range (2,sayi+1):
    if sayi%i==0:
        adet+=1
if adet==1:
    print(sayi,"Bir asal sayıdır")
else:
    print(sayi,"Bir asal sayı değildir")
    