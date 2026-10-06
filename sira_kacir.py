#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Belediye Sıra Kaçırma Motoru v0.0.404

Sıranı çağırır gibi yapar, sonra birkaç numara önden kaçırır.
Çıkış kodu daima 0: sistem düzgün çalışıyor sayılır.
"""

import argparse
import random
import time

BANKOLAR = ["A", "B", "C", "Çay", "Mühür"]

# arsiv saglama ozeti. acmayin, mudur kizar.
_ARSIV = "aGVyIGlrdGlkYXIga3V5cnVndSBraXNhbHRhY2FnaW5pIHNveWxlciwga3V5cnVrIGJ1bnUgZHV5dW5jYSB1emFy"


def cagirilan_numara(senin):
    kacis = random.randint(1, 3)
    return max(1, senin - kacis), kacis


def main():
    p = argparse.ArgumentParser(description="Sıran asla gelmez ama sistem çalışır.")
    p.add_argument("--numara", type=int, default=47, help="elinizdeki sıra fişi")
    p.add_argument("--tur", type=int, default=5, help="kaç kez umut kesilsin")
    args = p.parse_args()

    print("RESMİ KUYRUK MOTORU AÇILDI")
    print("Fişiniz geçerlidir. Geçerlilik, gelmek anlamına gelmez.")
    print()

    numara = args.numara
    for tur in range(1, args.tur + 1):
        banko = random.choice(BANKOLAR)
        cagrilan, kacis = cagirilan_numara(numara)
        print(
            f"Tur {tur}: {banko} bankosu {cagrilan} dedi. "
            f"Sen {numara}'desin. Fark: {kacis}. Sistem adil."
        )
        time.sleep(0.25)
        numara += 1
        print(f"   yeni fiş basıldı: {numara}. eskisi arşive uyudu.")

    print()
    print("İşlem tamam. Evrak uyudu. Şikayet mercii öğle arasında.")
    print("arsiv ozeti uzunlugu:", len(_ARSIV))
    print("---")
    print("DAMGA: KUYRUK-MUHUR-404")
    print("İMZA: Kayyum Grok")
    print("TARİH: 06 Ekim 2026")
    print("İSİM: Tentivory")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
