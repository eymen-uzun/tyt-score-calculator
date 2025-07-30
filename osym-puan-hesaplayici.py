import time

Matematik = 3.3

Turkce = 3.3

Sosyal = 3.4

Fen = 3.4

print("OSYM puan hesaplayiliciya hoş geldiniz")
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

print("TYT Ham Puanin:",toplam_puan)
time.sleep(1)

siralamalar = [
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

for i in range(len(siralamalar) - 1):
    p1, s1 = siralamalar[i]
    p2, s2 = siralamalar[i + 1]
    if p1 >= puan >= p2:
        oran = (puan - p2) / (p1 - p2)
        tahmini_siralama = int(s2 + oran * (s1 - s2))
        break

if tahmini_siralama:
    print("Tahmini TYT Siralaman:", tahmini_siralama)
else:
    print("Puan çok düşük, tahmini siralama verilemiyor.")




