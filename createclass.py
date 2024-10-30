class PersegiPanjang:
    def init(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)                                                                                                                                      

    def luas(self):
        return self.panjang * self.lebar

    def str(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    
def main():
    try:   
        panjang = int(input("Masukkan panjang persegi panjang (cm): "))
        lebar = int(input("Masukkan lebar persegi panjang (cm): "))

        if panjang <= 0 or lebar <= 0:
            print("Nilai panjang dan lebar harus lebih dari 0")
        else:

            persegi_panjang = PersegiPanjang(panjang, lebar)
            print(persegi_panjang)  
            print("Keliling:", persegi_panjang.keliling(), "cm")  
            print("Luas:", persegi_panjang.luas(), "cm²")
    except ValueError:
        print("Input harus berupa angka yang valid.")          



if __name__ == "main":
    main()