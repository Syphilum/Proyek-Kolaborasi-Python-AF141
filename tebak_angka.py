# Tebak Angka - permainan sederhana
# Cara main: jalankan file ini dengan Python 3 (python tebak_angka.py)
# Ketik 'q' untuk keluar kapan saja saat menebak.

import random

MIN_ANGKA = 1
MAKS_ANGKA = 100

def play():
    secret = random.randint(MIN_ANGKA, MAKS_ANGKA)
    percobaan = 0
    print(f"Selamat datang di permainan Tebak Angka!")
    print(f"Saya sudah memilih angka antara {MIN_ANGKA} dan {MAKS_ANGKA}. Coba tebak!")
    print("Ketik 'q' lalu tekan Enter untuk keluar.\n")

    while True:
        jawaban = input(f"Masukkan tebakan ({MIN_ANGKA}-{MAKS_ANGKA}): ").strip()
        if jawaban.lower() == 'q':
            print("Keluar dari permainan. Sampai jumpa!")
            return

        try:
            tebakan = int(jawaban)
        except ValueError:
            print("Input tidak valid — masukkan angka bulat atau 'q' untuk keluar.")
            continue

        if tebakan < MIN_ANGKA or tebakan > MAKS_ANGKA:
            print(f"Silakan masukkan angka antara {MIN_ANGKA} dan {MAKS_ANGKA}.")
            continue

        percobaan += 1

        if tebakan < secret:
            print("Terlalu kecil! Coba lagi.\n")
        elif tebakan > secret:
            print("Terlalu besar! Coba lagi.\n")
        else:
            print(f"Selamat — benar! Angkanya {secret}.")
            print(f"Jumlah percobaan: {percobaan}\n")
            break

    # Tanyakan apakah mau main lagi
    while True:
        lagi = input("Mau main lagi? (y/n): ").strip().lower()
        if lagi == 'y':
            print()
            play()
            return
        elif lagi == 'n' or lagi == 'q' or lagi == '':
            print("Terima kasih sudah bermain!")
            return
        else:
            print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")

if __name__ == "__main__":
    play()