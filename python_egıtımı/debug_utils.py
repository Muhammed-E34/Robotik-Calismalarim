import turtle
import math
import time

# --- AYARLAR ---
sevgili = "SENİ SEVİYORUM" # Burayı değiştir
arka_plan = "black"
kalp_rengi = "#E3170A" # Kan kırmızısı (Daha gerçekçi)

# --- EKRAN KURULUMU ---
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor(arka_plan)
wn.title("Senin İçin Atan Bir Kalp")
wn.tracer(0) # Animasyonu manuel kontrol edeceğiz (Titreşimi önler)

# --- KALEM KURULUMU ---
kalem = turtle.Turtle()
kalem.hideturtle()
kalem.speed(0)

# --- MATEMATİK MOTORU ---
def kalp_koordinat(t, boyut):
    # Kalbin x, y koordinatlarını hesaplar
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x * boyut, y * boyut

# --- ANİMASYON DÖNGÜSÜ (SONSUZ) ---
# Zaman sayacı (Kalbin atış ritmi için)
zaman = 0

try:
    while True:
        kalem.clear() # Eski kareyi sil
        
        # --- Kalbin Boyutunu Hesapla (Nefes Alma Efekti) ---
        # Sinüs dalgası kullanarak boyutu 12 ile 15 arasında gidip getiriyoruz
        boyut_katsayisi = 12 + 2 * math.sin(zaman * 0.15)
        
        # --- Kalbi Çiz ---
        kalem.color(kalp_rengi)
        kalem.begin_fill()
        
        # Kalbin çevresini oluşturan noktaları tek tek çiz
        # 0'dan 2*pi'ye kadar dönüyoruz
        nokta_sayisi = 100
        kalem.up() # Çizgi çekmeden git
        
        for i in range(nokta_sayisi + 1):
            t = i * (2 * math.pi / nokta_sayisi)
            x, y = kalp_koordinat(t, boyut_katsayisi)
            
            if i == 0:
                kalem.goto(x, y)
                kalem.down() # İlk noktada kalemi indir
            else:
                kalem.goto(x, y)
                
        kalem.end_fill()
        
        # --- Yazıyı Yaz (Sabit ve Ortada) ---
        kalem.up()
        # Yazı kalbin ortasında kalsın diye y koordinatını biraz aşağı çekiyoruz
        kalem.goto(0, -15) 
        kalem.color("white")
        # Font boyutu kalple orantılı büyüyüp küçülmesin, sabit kalsın
        kalem.write(sevgili, align="center", font=("Verdana", 15, "bold"))
        
        # --- Ekranı Güncelle ---
        wn.update()
        
        # Sayacı artır (Hızı değiştirmek istersen burayla oyna)
        zaman += 1
        
        # İşlemciyi yormamak için minik bir bekleme
        time.sleep(0.02)

except turtle.Terminator:
    # Pencere kapatılırsa hata vermeden çık
    print("Program kapatıldı.")