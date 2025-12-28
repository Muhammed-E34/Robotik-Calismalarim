kullanici_sayisi = int(input("Faktöriyelini istediğin sayı: "))
çarpim = 1

for sayi in range(1, kullanici_sayisi + 1):
    
    çarpim = çarpim * sayi
    # Burası döngü içi (Sessizce topla)

# Burası döngü dışı (Bittiği zaman konuş)
print(f"faktöriyeli: {çarpim}")