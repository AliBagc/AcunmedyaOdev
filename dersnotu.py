# Kullanıcıdan notunu al
not_sayisi = int(input("Notunuzu girin (0-100 arası): "))

# Harf notunu belirle
if 90 <= not_sayisi <= 100:
    print("Harf Notu: A")
elif 80 <= not_sayisi <= 89:
    print("Harf Notu: B")
elif 70 <= not_sayisi <= 79:
    print("Harf Notu: C")
elif 60 <= not_sayisi <= 69:
    print("Harf Notu: D")
elif 0 <= not_sayisi < 60:
    print("Harf Notu: F")
else:
    print("Geçersiz not girdiniz!")