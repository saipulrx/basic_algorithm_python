pertemuan_hari_ini = {
  "judul": "Belajar Dictionary Pada Python 3",
  "tanggal": "01 Februari 2021",
  "kategori": [
    "Python", "Python Dasar"
  ],
  "page_views": 10,
  "published": True,
  "share_count": {
    "facebook": 0,
    "twitter": 2
  }
}

print('Judul' , pertemuan_hari_ini.get('judul'))
print('Tanggal ', pertemuan_hari_ini['tanggal'])
#print('Share count Instagram ', pertemuan_hari_ini['instagram'])
print('Share count Instagram ', pertemuan_hari_ini.get('instagram',0))

#mengubah data di key tanggal
pertemuan_hari_ini['tanggal'] = '20 Oktober 2021'
print(pertemuan_hari_ini.get('tanggal'))

#mengubah data di share_count.facebook
print(pertemuan_hari_ini.get('share_count').get('facebook'))
pertemuan_hari_ini['share_count']['facebook'] = 3
print(pertemuan_hari_ini.get('share_count').get('facebook'))