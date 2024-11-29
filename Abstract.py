from abc import ABC, abstractmethod

# Kelas Abstrak
class AlatElektronik(ABC):
    @abstractmethod
    def fungsi(self):
        pass

    @abstractmethod
    def sumber_energi(self):
        pass

# Kelas Anak 1
class Televisi(AlatElektronik):
    def fungsi(self):
        return "Menampilkan gambar dan suara"

    def sumber_energi(self):
        return "Listrik"

# Kelas Anak 2
class Laptop(AlatElektronik):
    def fungsi(self):
        return "Mengolah data dan menjalankan program"

    def sumber_energi(self):
        return "Listrik atau baterai"

# Pemanggilan
def main():
    alat1 = Televisi()
    alat2 = Laptop()

    print("Televisi:")
    print(f"  Fungsi: {alat1.fungsi()}")
    print(f"  Sumber energi: {alat1.sumber_energi()}")

    print("\nLaptop:")
    print(f"  Fungsi: {alat2.fungsi()}")
    print(f"  Sumber energi: {alat2.sumber_energi()}")

if __name__ == "__main__":
    main()
