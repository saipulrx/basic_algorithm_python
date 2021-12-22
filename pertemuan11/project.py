
#fungsi menampilkan data
def show_data_project(db_conn):
    cur = db_conn.cursor()
    sql = "SELECT * FROM projects" 
    cur.execute(sql)
    results = cur.fetchall()
    if len(results) <= 0: 
        print("\nTidak ada data\n")
    else: 
        for data in results:
            print(data) 
    
#fungsi insert data 
def insert_data_project(db_conn):
    name = input("Masukan Nama Projek : ")
    begin_date = input("Masukan tanggal mulai : (exp: 10 September 2020) ")
    end_date = input("Masukan tanggal selesai : (exp: 10 September 2020) ")
    val = (name, begin_date, end_date) 
    cursor = db_conn.cursor() 
    sql = '''INSERT INTO projects (name, begin_date, end_date) VALUES (?, ?, ?)'''
    #print(val)
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} data berhasil disimpan\n".format(cursor.rowcount))
    
#fungsi update data
def update_data_project(db_conn):
    cursor = db_conn.cursor()
    show_data_project(db_conn)
    id_project = int(input("\nKetik ID Project > "))
    name = input("Name   : ")
    begin_date = input("Begin Date : (exp: 10 September 2020)")
    end_date = input("End Date : (exp: 10 September 2020) ")
  
    sql = "UPDATE projects SET name=?, begin_date=?, end_date=? WHERE id=?" 
    val = (name, begin_date, end_date, id_project) 
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} Data berhasil diubah \n".format(cursor.rowcount))

#fungsi hapus data
def delete_data_project(db_conn):
    cursor = db_conn.cursor()
    show_data_project(db_conn) 
    id_project = int(input("\nKetik ID PROJECT > "))
    sql = "DELETE FROM projects WHERE id = ? "
    val = (id_project,)
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} Data berhasil dihapus \n".format(cursor.rowcount))

#fungsi cari data
def search_data_project(db_conn):
    cursor = db_conn.cursor()
    keyword = input("\nMasukkan Kata Kunci: ")
    sql = '''SELECT * FROM projects 
    WHERE name LIKE '%%%s%%' 
    ''' % (keyword)
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) <= 0:
        print("\nTidak ada data\n") 
    else:
        for data in results:
            print(data)
    #return show_project_menu(db_conn)