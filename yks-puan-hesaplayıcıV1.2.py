import time

Matematik = 3.3
Turkce = 3.3
Sosyal = 3.4
Fen = 3.4

print("YKS puan hesaplayiciya hos geldiniz")
time.sleep(1)
print("Kaynak: OSYM Resmi Raporlari ve MEB & YOK YKS Analizleri")
time.sleep(1)

print("Matematik Neti:")
mat_net = float(input())
print("Turkce Neti:")
turkce_net = float(input())
print("Sosyal Neti:")
sosyal_net = float(input())
print("Fen Neti:")
fen_net = float(input())

toplam_puan = (mat_net * Matematik) + (turkce_net * Turkce) + (sosyal_net * Sosyal) + (fen_net * Fen) + 100
print("TYT Ham Puanin:", toplam_puan)
time.sleep(1)

siralamalar_tyt = [
    (500, 5000),
    (495, 8000),
    (490, 12000),
    (485, 17000),
    (480, 23000),
    (475, 30000),
    (470, 38000),
    (465, 47000),
    (460, 57000),
    (455, 68000),
    (450, 80000),
    (445, 93000),
    (440, 107000),
    (435, 122000),
    (430, 138000),
    (425, 160000),
    (420, 180000),
    (415, 200000),
    (410, 220000),
    (405, 240000),
    (400, 270000),
    (395, 300000),
    (390, 330000),
    (385, 360000),
    (380, 390000),
    (375, 500000),
    (370, 570000),
    (365, 640000),
    (360, 710000),
    (355, 780000),
    (350, 850000),
    (345, 920000),
    (340, 990000),
    (335, 1060000),
    (330, 1130000),
    (325, 1000000),
    (320, 1030000),
    (315, 1060000),
    (310, 1090000),
    (305, 1120000),
    (300, 1300000),
    (295, 1340000),
    (290, 1380000),
    (285, 1420000),
    (280, 1460000),
    (275, 1600000),
    (270, 1660000),
    (265, 1720000),
    (260, 1780000),
    (255, 1840000),
    (250, 1900000),
    (245, 1960000),
    (240, 2020000),
    (235, 2060000),
    (230, 2080000),
    (225, 2100000),
    (220, 2150000),
    (215, 2180000),
    (210, 2210000),
    (205, 2240000),
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
    print("Puan cok dusuk, tahmini siralama verilemiyor.")

AYTMatematik = 3.0
AYTFen = 2.85
AYTTDE = 3.0
AYTSosyal = 2.8
AYTDil = 3.0

print("AYT puaninizi hesaplamak icin Bolum secimi yapiniz")
time.sleep(2)
print("Sayisal icin: 1 | Esit Agirlik icin: 2 | Sozel icin: 3 | Dil icin: 4")
bolum = int(input("Seciminiz: "))

AYT_puan = 0
if bolum == 1:
    print("AYT Matematik Netiniz:")
    AYTmatnet = float(input())
    print("AYT Fen Netiniz:")
    AYTfennet = float(input())
    AYT_puan = (AYTmatnet * AYTMatematik) + (AYTfennet * AYTFen)
elif bolum == 2:
    print("AYT Matematik Netiniz:")
    AYTmatnet = float(input())
    print("AYT Turk Dili ve Edebiyati + Sosyal-1 Netiniz:")
    AYTTDE_net = float(input())
    AYT_puan = (AYTmatnet * AYTMatematik) + (AYTTDE_net * AYTTDE)
elif bolum == 3:
    print("AYT Turk Dili ve Edebiyati + Sosyal-1 Netiniz:")
    AYTTDE_net = float(input())
    print("AYT Sosyal-2 Netiniz:")
    AYTSosyal_net = float(input())
    AYT_puan = (AYTTDE_net * AYTTDE) + (AYTSosyal_net * AYTSosyal)
elif bolum == 4:
    print("AYT Yabanci Dil Netiniz:")
    AYTDil_net = float(input())
    AYT_puan = (AYTDil_net * AYTDil)
else:
    print("Gecersiz secim yaptiniz.")

obp = float(input("Ortaogretim Basari Puaninizi (OBP) giriniz: "))
toplam_genel = toplam_puan + AYT_puan + obp
print(f"Toplam Puaniniz: {toplam_genel}")

siralamalar_yer = [
    (550, 1000),
    (545, 3000),
    (540, 5000),
    (535, 8000),
    (530, 12000),
    (525, 18000),
    (520, 25000),
    (515, 35000),
    (510, 45000),
    (505, 60000),
    (500, 80000),
    (495, 100000),
    (490, 125000),
    (485, 150000),
    (480, 180000),
    (475, 210000),
    (470, 240000),
    (465, 270000),
    (460, 300000),
    (455, 340000),
    (450, 380000),
    (445, 420000),
    (440, 460000),
    (435, 500000),
    (430, 550000),
    (425, 600000),
    (420, 650000),
    (415, 700000),
    (410, 760000),
    (405, 820000),
    (400, 880000),
    (395, 940000),
    (390, 1000000),
    (385, 1070000),
    (380, 1140000),
    (375, 1210000),
    (370, 1280000),
    (365, 1350000),
    (360, 1420000),
    (355, 1500000),
    (350, 1580000),
    (345, 1660000),
    (340, 1740000),
    (335, 1820000),
    (330, 1900000),
    (325, 1980000),
    (320, 2060000),
    (315, 2140000),
    (310, 2220000),
    (305, 2260000),
    (300, 2300000),
    (295, 2320000),
    (290, 2340000),
    (285, 2360000),
    (280, 2380000),
    (275, 2400000),
    (270, 2420000),
    (265, 2440000),
    (260, 2460000),
    (255, 2480000),
    (250, 2500000),
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
    print("Tahmini Yerlestirme Siralaman:", tahmini_siralama_yer)
else:
    print("Puan cok dusuk, tahmini yerlestirme siralama verilemiyor.")




