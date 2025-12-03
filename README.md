# Proyek Kolaborasi Python AF141

Selamat datang di **Proyek Kolaborasi Python AF141**. Repo ini merupakan hasil kerja sama dan pembelajaran kelompok kami dalam mata kuliah Python.

## Anggota Kolaborasi

- **Muh. Hidayat** ([Syphilum](https://github.com/Syphilum))
- **Indra Satya Nicolaus Pamilangan** ([Yoikss](https://github.com/Yoikss))
- **Jimmy Ponto Wohon** ([jiwopes-pixel](https://github.com/jiwopes-pixel))
- **Ferel Timothy Kimbal** ([ferelkimbal026](https://github.com/ferelkimbal026))

## Deskripsi Proyek

Proyek kolaborasi berupa game **TETRIS**

## Requirements
- [python](https://www.python.org/downloads/release/python-3140/)
- PyQt5
  ```bash
  pip install pyqt5
  ```
- NumPy
  ```bash
  pip install numpy
  ```

## Cara Penggunaan

1. Clone repo:
   ```bash
   git clone https://github.com/Syphilum/Proyek-Kolaborasi-Python-AF141.git
   ```
2. Masuk ke direktori:
   ```bash
   cd Proyek-Kolaborasi-Python-AF141
   ```
3. jalankan permainan
   ```bash
   python tetris_game.py
   ```

## Flowchart
```mermaid
    flowchart TD
    Start --> GUI
    GUI --> InisTetris
    InisTetris --> Setup
    Setup --> BeginGame
    BeginGame --> GameLoop
    GameLoop --> Input
    Input --> MoveDown
    Input --> Restart
    Restart --> BeginGame
    MoveDown --> AI
    AI --> MoveDown
    AI --> Score
    Score --> IsGameOver
    IsGameOver -- Tidak --> GameLoop
    IsGameOver -- Ya --> EndGame
    EndGame --> Input
```

## Kontributor

The gang members:

| Nama Kontributor        | Persentase Kontribusi | Jumlah Kontribusi | Profil GitHub                              | Avatar                                        |
|------------------------|----------------------|-------------------|--------------------------------------------|-----------------------------------------------|
| Hidayat               | 73%                  | 24                | [Syphilum](https://github.com/Syphilum)            | ![Syphilum](https://avatars.githubusercontent.com/u/193500420?v=4)     |
| Indra                 | 12%                  | 4                 | [Yoikss](https://github.com/Yoikss)                | ![Yoikss](https://avatars.githubusercontent.com/u/246048604?v=4)       |
| Ferel         | 6%                   | 2                 | [ferelkimbal026](https://github.com/ferelkimbal026) | ![ferelkimbal026](https://avatars.githubusercontent.com/u/242188861?v=4)|
| Jimmy          | 9%                  | 3                 | [jiwopes-pixel](https://github.com/jiwopes-pixel)  | ![jiwopes-pixel](https://avatars.githubusercontent.com/u/242097269?v=4) |

> Persentase kontribusi otomatis dihitung dari jumlah kontribusi (commits/PR/issue) berdasarkan data halaman [Insights Contributors](https://github.com/Syphilum/Proyek-Kolaborasi-Python-AF141/graphs/contributors).

Terima kasih atas kontribusi semua rekan-rekan!

## Lisensi

Repo ini dibuat khusus untuk keperluan pembelajaran dan tidak dimaksudkan untuk penggunaan komersial.

---

Terima kasih telah mampir! Untuk pertanyaan atau diskusi bisa menghubungi salah satu anggota atau menggunakan fitur _Issues_ pada repository.
