nilai = int(input("inputkan nilai : "))
jenis_kelamin = input("inputkan jenis kelamin(Pria atau Wanita) : ")

if nilai >=90:
    grade = 'Predikat A'
    if jenis_kelamin=='Pria':
        print('Selamat mas ganteng mendapatkan grade : ', grade)
    elif jenis_kelamin=='Wanita':
        print('Selamat mba cantik mendapatkan grade : ', grade)
    else:
        print('Maaf jenis kelamin tidak dikenali, harap input Pria atau Wanita')
elif nilai >=85 and nilai <=89:
    grade = 'Predikat B+'
    if jenis_kelamin=='Pria':
        print('Selamat mas ganteng mendapatkan grade : ', grade)
    elif jenis_kelamin=='Wanita':
        print('Selamat mba cantik mendapatkan grade : ', grade)
    else:
        print('Maaf jenis kelamin tidak dikenali, harap input Pria atau Wanita')
elif nilai >=80 and nilai <=84:
    grade = 'Predikat B'
    if jenis_kelamin=='Pria':
        print('Selamat mas ganteng mendapatkan grade : ', grade)
    elif jenis_kelamin=='Wanita':
        print('Selamat mba cantik mendapatkan grade : ', grade)
    else:
        print('Maaf jenis kelamin tidak dikenali, harap input Pria atau Wanita')
elif nilai >=75 and nilai <=79:
    grade = 'Predikat C'
    if jenis_kelamin=='Pria':
        print('Selamat mas ganteng mendapatkan grade : ', grade)
    elif jenis_kelamin=='Wanita':
        print('Selamat mba cantik mendapatkan grade : ', grade)
    else:
        print('Maaf jenis kelamin tidak dikenali, harap input Pria atau Wanita')
elif nilai >=70 and nilai <=74:
    grade = 'Predikat D'
    if jenis_kelamin=='Pria':
        print('Selamat mas ganteng mendapatkan grade : ', grade)
    elif jenis_kelamin=='Wanita':
        print('Selamat mba cantik mendapatkan grade : ', grade)
    else:
        print('Maaf jenis kelamin tidak dikenali, harap input Pria atau Wanita')
else:
    grade = 'Predikat E'
    if jenis_kelamin=='Pria':
        print('Selamat mas ganteng mendapatkan grade : ', grade)
    elif jenis_kelamin=='Wanita':
        print('Selamat mba cantik mendapatkan grade : ', grade)
    else:
        print('Maaf jenis kelamin tidak dikenali, harap input Pria atau Wanita')