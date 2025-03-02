while True:
    Birincisayi = int(input("Birinci sayıyı Giriniz: "))
    İkincisayi = int(input("İkinci sayıyı Giriniz: "))
    islem = input("Hangi işlemin yapılmasını istersin? (+, -, *, /): ")

    if (islem == "+"):
        sonuc = (Birincisayi + İkincisayi)
        print(sonuc)
    elif (islem == "-"):
        sonuc = (Birincisayi - İkincisayi)
        print(sonuc)
    elif (islem == "*"):
        sonuc = (Birincisayi * İkincisayi)
        print(sonuc)
    elif (islem == "/"):
        if (İkincisayi == 0):
            print("Hata: Bölmede ikinci sayı 0 olamaz!")
        else:
            sonuc = (Birincisayi / İkincisayi)
            print(sonuc)
    else:
        print("Geçersiz işlem türü")
