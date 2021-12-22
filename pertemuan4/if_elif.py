nilai = input("inputkan nilai : ")
nilai_akhir = int(nilai)
if nilai_akhir >=90:
    grade = 'Predikat A'
    print('grade adalah : ', grade)
elif nilai_akhir >=85 and nilai_akhir <=89:
    grade = 'Predikat B+'
    print('grade adalah : ', grade)
elif nilai_akhir >=80 and nilai_akhir <=84:
    grade = 'Predikat B'
    print('grade adalah : ', grade)
elif nilai_akhir >=75 and nilai_akhir <=79:
    grade = 'Predikat C'
    print('grade adalah : ', grade)
elif nilai_akhir >=70 and nilai <=74:
    grade = 'Predikat D'
    print('grade adalah : ', grade)
else:
    grade = 'Predikat E' 
    print('grade adalah : ', grade)               