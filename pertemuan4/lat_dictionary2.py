pertemuan_hari_ini = {
    "judul" : "Belajar Dictionary pada Python 3",
    "tanggal" : "18 Oktober 2021",
    "kategori" : 
    ["Python","Python Dasar"],
    "page_view" : 10,
    "published" : True,
    "share_count" : {
        "facebook" : 0,
        "twitter" : 1
    }
}

print('Judul:', pertemuan_hari_ini.get('judul'))
print('Tanggal sebelum di ubah:', pertemuan_hari_ini['tanggal'])

pertemuan_hari_ini['tanggal'] = "18 Oktober 2021 jam 20.03 WIB"

print('Tanggal setelah di ubah:', pertemuan_hari_ini.get('tanggal'))

print('Facebook share:', pertemuan_hari_ini.get('share_count').get('facebook'))
print('Twitter share:', pertemuan_hari_ini['share_count']['twitter'])
pertemuan_hari_ini['share_count']['facebook'] = 5
pertemuan_hari_ini['share_count']['twitter'] = 3

print('Facebook share setelah di ubah : ', pertemuan_hari_ini['share_count']\
    ['facebook'])
print('Twitter share setelah di ubah : ', \
    pertemuan_hari_ini.get('share_count').get('twitter'))

#tambah data mata kuliah
pertemuan_hari_ini['mata_kuliah'] = 'Algoritma'

print('mata kuliah pertemuan ini : ', pertemuan_hari_ini['mata_kuliah'])

del pertemuan_hari_ini['mata_kuliah']
pertemuan_hari_ini.pop('published')

print('mata kuliah setelah di hapus : ', pertemuan_hari_ini.get('mata_kuliah'))
