class Segitiga:
    def __init__ (self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def get_luas(self):
        return 0.5 * self.alas * self.tinggi

segitiga1 = Segitiga(7,11)
segitiga2 = Segitiga(7,4)

print('luas segitiga1 adalah : ', segitiga1.get_luas())
print('luas segitiga2 adalah : ', segitiga2.get_luas())