#fungsi insert data 
def insert_data_buku(db_conn):
    judul = input("Masukan Judul Buku : ")
    total_halaman = int(input("Masukan total halaman berupa angka : "))
    harga = int(input("Masukan harga berupa angka : "))
    stock = int(input("Masukan stock berupa angka : "))
    val = (judul, total_halaman, harga, stock) 
    cursor = db_conn.cursor() 
    sql = '''INSERT INTO buku (judul, total_halaman, harga, stock) VALUES (?, ?, ?, ?)'''
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} data berhasil disimpan\n".format(cursor.rowcount))

#fungsi menampilkan data
def show_data_buku(db_conn):
    cur = db_conn.cursor()
    sql = "SELECT * FROM buku" 
    cur.execute(sql)
    results = cur.fetchall()
    if len(results) <= 0: 
        print("\nTidak ada data\n")
    else: 
        for data in results:
            print(data) 

#fungsi update data
def update_data_buku(db_conn):
    cursor = db_conn.cursor()
    show_data_buku(db_conn)
    id = int(input("\nKetik ID Buku > "))
    judul = input("Judul Buku   : ")
    total_halaman = int(input("total halaman berupa angka : "))
    harga = int(input("harga berupa angka : "))
    stock = int(input("stock berupa angka : "))
  
    sql = "UPDATE buku SET judul=?, total_halaman=?, harga=?, stock=? WHERE id=?" 
    val = (judul, total_halaman, harga, stock, id) 
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} Data berhasil diubah \n".format(cursor.rowcount))

#fungsi hapus data
def delete_data_buku(db_conn):
    cursor = db_conn.cursor()
    show_data_buku(db_conn) 
    id = int(input("\nKetik ID Buku > "))
    sql = "DELETE FROM buku WHERE id = ? "
    val = (id,)
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} Data berhasil dihapus \n".format(cursor.rowcount))

#fungsi cari data
def search_data_buku(db_conn):
    cursor = db_conn.cursor()
    keyword = input("\nMasukkan Kata Kunci: ")
    sql = '''SELECT * FROM buku 
    WHERE judul LIKE '%%%s%%' 
    ''' % (keyword)
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) <= 0:
        print("\nTidak ada data\n") 
    else:
        for data in results:
            print(data)