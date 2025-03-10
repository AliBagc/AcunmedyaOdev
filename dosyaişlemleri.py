
with open("veriler.txt", "w") as dosya:
    for i in range(5):
        dosya.write(input(f"{i+1}. satır: ") + "\n")

with open("veriler.txt", "r") as dosya:
    print("\nDosya içeriği:")
    print(dosya.read())
