#fungsi insert data 
def insert_data_penerbit(db_conn):
    nama_penerbit = input("Masukan Nama Penerbit : ")
    alamat = input("Masukan alamat penerbit : ")
    no_kontak = input("Masukan no kontak penerbit : ")
    val = (nama_penerbit, alamat, no_kontak) 
    cursor = db_conn.cursor() 
    sql = '''INSERT INTO penerbit (nama_penerbit, alamat, no_kontak) VALUES (?, ?, ?)'''
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} data berhasil disimpan\n".format(cursor.rowcount))

#fungsi menampilkan data
def show_data_penerbit(db_conn):
    cur = db_conn.cursor()
    sql = "SELECT * FROM penerbit" 
    cur.execute(sql)
    results = cur.fetchall()
    if len(results) <= 0: 
        print("\nTidak ada data\n")
    else: 
        for data in results:
            print(data) 

#fungsi update data
def update_data_penerbit(db_conn):
    cursor = db_conn.cursor()
    show_data_penerbit(db_conn)
    id = int(input("\nKetik ID penerbit > "))
    nama_penerbit = input("Nama Penerbit   : ")
    alamat = input("Alamat : ")
    no_kontak = input("no kontak penerbit : ")
  
    sql = "UPDATE penerbit SET nama_penerbit=?, alamat=?, no_kontak=? WHERE id=?" 
    val = (nama_penerbit, alamat, no_kontak, id) 
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} Data berhasil diubah \n".format(cursor.rowcount))

#hapus data
def delete_data_penerbit(db_conn):
    cursor = db_conn.cursor()
    show_data_penerbit(db_conn) 
    id = int(input("\nKetik ID Penerbit > "))
    sql = "DELETE FROM penerbit WHERE id = ? "
    val = (id,)
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} Data berhasil dihapus \n".format(cursor.rowcount))

#fungsi cari data
def search_data_penerbit(db_conn):
    cursor = db_conn.cursor()
    keyword = input("\nMasukkan Kata Kunci: ")
    sql = '''SELECT * FROM penerbit 
    WHERE nama_penerbit LIKE '%%%s%%' 
    ''' % (keyword)
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) <= 0:
        print("\nTidak ada data\n") 
    else:
        for data in results:
            print(data)