class kucing:
    var_judul = ""
    var_nama = ""
    var_usia = ""
    var_warna = ""

    #membuat contrukstor
    def __init__ (self, judul):
        self.var_judul = judul

    #fungsi untuk input data variabel
    def get_nama (self, nama):
        self.var_nama = nama

    #fungsi untuk input data variabel
    def get_usia (self, usia):
        self.var_usia = usia

    #fungsi untuk input data variabel
    def get_warna (self, warna):
        self.var_warna = warna

    #fungsi untuk menampilkan output
    def get_output(self):
        print("Judul : ",self.var_judul)
        print("Nama : ", self.var_nama)
        print("Usia : ", self.var_usia)
        print("Warna : ", self.var_warna)