nilai = int(input("masukan nilai : "))
gender = input("masukan jenis kelamin (pria, wanita) : ")

if nilai >= 90 :
    if gender == "pria":
        print("selamat mas nya lulus dengan predikat A")
    elif gender == "wanita":
        print("selamat mba nya lulus dengan predikat A")
    else:
        print("maaf jenis kelamin tidak terdaftar")        
elif nilai >= 80 and nilai <=89:
    if gender == "pria":
        print("selamat mas nya lulus dengan predikat B")
    elif gender == "wanita":
        print("selamat mba nya lulus dengan predikat B")
    else:
        print("maaf jenis kelamin tidak terdaftar")  
elif nilai >=60 and nilai <=79:
    if gender == "pria":
        print("selamat mas nya lulus dengan predikat C")
    elif gender == "wanita":
        print("selamat mba nya lulus dengan predikat C")
    else:
        print("maaf jenis kelamin tidak terdaftar") 
elif nilai >= 40 and nilai <= 59:
    if gender == "pria":
        print("maaf mas nya tidak lulus dengan predikat D")
    elif gender == "wanita":
        print("maaf mba nya tidak lulus dengan predikat D")
    else:
        print("maaf jenis kelamin tidak terdaftar")       
else:
    print("maaf anda tidak lulus dengan predikat E")