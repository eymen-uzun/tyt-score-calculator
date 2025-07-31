import time

Matematik = 3.3
Turkce = 3.3
Sosyal = 3.4
Fen = 3.4

print("YKS puan hesaplayiliciya hoş geldiniz")
time.sleep(1)
print("Kaynak: ÖSYM Resmî Raporları ve MEB & YÖK YKS Analizleri")
time.sleep(1)

print("Matematik Neti:")
mat_net = float(input())

print("Türkçe Neti:")
türkce_net = float(input())

print("Sosyal Neti:")
sosyal_net = float(input())

print("Fen Neti:")
fen_net = float(input())

toplam_puan = (mat_net * Matematik) + (türkce_net * Turkce) + (sosyal_net * Sosyal) + (fen_net * Fen) + 100

print("TYT Ham Puanin:", toplam_puan)
time.sleep(1)

siralamalar_tyt = [
    (500, 5000),
    (475, 30000),
    (450, 80000),
    (425, 160000),
    (400, 300000),
    (375, 500000),
    (350, 700000),
    (325, 1000000),
    (300, 1300000),
    (275, 1600000),
    (250, 1900000),
    (225, 2100000),
    (200, 2300000),
]

puan = toplam_puan
tahmini_siralama_tyt = None
for i in range(len(siralamalar_tyt) - 1):
    p1, s1 = siralamalar_tyt[i]
    p2, s2 = siralamalar_tyt[i + 1]
    if p1 >= puan >= p2:
        oran = (puan - p2) / (p1 - p2)
        tahmini_siralama_tyt = int(s2 + oran * (s1 - s2))
        break

if tahmini_siralama_tyt:
    print("Tahmini TYT Siralaman:", tahmini_siralama_tyt)
else:
    print("Puan çok düşük, tahmini siralama verilemiyor.")

AYTMatematik = 3.0
AYTFen = 2.85
AYTTDE = 3.0
AYTSosyal = 2.8
AYTDil = 3.0

print("AYT puaninizi hesaplamak için Bölüm seçimi yapiniz")
time.sleep(2)
print("Sayisal için: 1 | Eşit Ağirlik için: 2 | Sözel için: 3 | Dil için: 4")

bölüm = int(input("Seçiminiz: "))

AYT_puan = 0

if bölüm == 1:
    print("AYT Matematik Netiniz:")
    AYTmatnet = float(input())
    print("AYT Fen Netiniz:")
    AYTfennet = float(input())
    AYT_puan = (AYTmatnet * AYTMatematik) + (AYTfennet * AYTFen)
elif bölüm == 2:
    print("AYT Matematik Netiniz:")
    AYTmatnet = float(input())
    print("AYT Türk Dili ve Edebiyati + Sosyal-1 Netiniz:")
    AYTTDE_net = float(input())
    AYT_puan = (AYTmatnet * AYTMatematik) + (AYTTDE_net * AYTTDE)
elif bölüm == 3:
    print("AYT Türk Dili ve Edebiyati + Sosyal-1 Netiniz:")
    AYTTDE_net = float(input())
    print("AYT Sosyal-2 Netiniz:")
    AYTSosyal_net = float(input())
    AYT_puan = (AYTTDE_net * AYTTDE) + (AYTSosyal_net * AYTSosyal)
elif bölüm == 4:
    print("AYT Yabanci Dil Netiniz:")
    AYTDil_net = float(input())
    AYT_puan = (AYTDil_net * AYTDil)
else:
    print("Geçersiz seçim yaptiniz.")

obp = float(input("Ortaöğretim Başari Puaninizi (OBP) giriniz: "))

toplam_genel = toplam_puan + AYT_puan + obp
print(f"Toplam Puaniniz: {toplam_genel}")

siralamalar_yer = [
    (550, 1000),
    (525, 5000),
    (500, 20000),
    (475, 60000),
    (450, 120000),
    (425, 250000),
    (400, 450000),
    (375, 700000),
    (350, 1000000),
    (325, 1400000),
    (300, 1800000),
    (275, 2100000),
    (250, 2300000),
]

tahmini_siralama_yer = None
for i in range(len(siralamalar_yer) - 1):
    p1, s1 = siralamalar_yer[i]
    p2, s2 = siralamalar_yer[i + 1]
    if p1 >= toplam_genel >= p2:
        oran = (toplam_genel - p2) / (p1 - p2)
        tahmini_siralama_yer = int(s2 + oran * (s1 - s2))
        break

if tahmini_siralama_yer:
    print("Tahmini Yerleştirme Siralaman:", tahmini_siralama_yer)
else:
    print("Puan çok düşük, tahmini yerleştirme siralama verilemiyor.")




