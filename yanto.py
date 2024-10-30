class PersegiPanjang:
    def _init(self, panjang, lebar):  # Perbaiki nama constructor menjadi __init_
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def _str(self):  # Perbaiki nama metode __str_
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

if __name__== "_main":  # Perbaiki nama variable __name_ dan _main_
    try:
        # Input panjang dan lebar dari pengguna
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))
        
        # Memeriksa apakah panjang dan lebar adalah bilangan positif
        if panjang <= 0 or lebar <= 0:
            print("Error: Panjang dan lebar harus lebih besar dari 0.")
        else:
            persegi_panjang = PersegiPanjang(panjang, lebar)
            print(persegi_panjang)
            print("Keliling:", persegi_panjang.hitung_keliling(), "cm")
            print("Luas:", persegi_panjang.hitung_luas(), "cm^2")
    
    except ValueError:
        print("Error: Input harus berupa angka.")