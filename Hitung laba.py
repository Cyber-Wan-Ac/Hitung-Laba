import pyfiglet  

teks = "Hitung Laba"
ascii_art = pyfiglet.figlet_format(teks, font="big")
print(ascii_art)


def hitung_harga_per_porsi(total_pengeluaran, persen_laba, total_porsi):
    laba = total_pengeluaran * (persen_laba / 100)
    total_dengan_laba = total_pengeluaran + laba
    harga_per_porsi = total_dengan_laba / total_porsi
    return round(harga_per_porsi, 2)

# Input dari user
try:
    total_pengeluaran = float(input("Masukkan total pengeluaran (Rp): "))
    persen_laba = float(input("Masukkan persentase laba (%): "))
    total_porsi = int(input("Masukkan total porsi: "))

    harga = hitung_harga_per_porsi(total_pengeluaran, persen_laba, total_porsi)
    print(f"\nHarga per porsi (laba {persen_laba}%): Rp{harga:,.2f}")

except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")
