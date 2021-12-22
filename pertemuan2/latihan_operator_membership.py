perusahaan = 'Microsoft'
list_pulau = ['Jawa', 'Sumatra', 'Sulawesi']

# ini adalah dictionary, insyaallah akan kita pelajari
# di pertemuan-pertemuan yang akan datang
mahasiswa = {
  'nama': 'Lendis Fabri',
  'asal': 'Lamongan'
}

print(
  "Apakah 'c' ada di variabel perusahaan?",
  'c' in perusahaan
)
print(
  "Apakah 'c' tidak ada di variabel perusahaan?",
  'c' not in perusahaan
)
print(
  "Apakah 'Madura' ada di variabel list_pulau?",
  'Madura' in list_pulau
)
print(
  "Apakah 'Madura' tidak ada di variabel list_pulau?",
  'Madura' not in list_pulau
)
print(
  "Apakah atribut 'nama' ada di variabel mahasiswa?",
  'nama' in mahasiswa
)