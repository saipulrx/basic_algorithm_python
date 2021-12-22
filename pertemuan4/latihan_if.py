nilai = int(input("masukan nilai : "))

if nilai >= 90 :
    print("selamat anda lulus dengan predikat A")
elif nilai >= 80 and nilai <=89:
    print("selamat anda lulus dengan predikat B") 
elif nilai >=60 and nilai <=79:
    print("selamat anda lulus dengan predikat C")
elif nilai >= 40 and nilai <= 59:
    print("maaf anda tidak lulus dengan predikat D")       
else:
    print("maaf anda tidak lulus dengan predikat E")