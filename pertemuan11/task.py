
#fungsi menampilkan data
def show_data_task(db_conn):
    cur = db_conn.cursor()
    sql = "SELECT * FROM tasks" 
    cur.execute(sql)
    results = cur.fetchall()
    if len(results) <= 0: 
        print("\nTidak ada data\n")
    else: 
        for data in results:
            print(data)

#fungsi menambahkan data
def insert_data_task(db_conn):
    name = input("Masukan Nama Task : ")
    priority = int(input("Masukan priority berupa angka : (skala dari 1 sampai 5)"))
    status_id = 1
    project_id = int(input("Masukan projek id yang di dapat dari menu data projek : "))
    begin_date = input("Masukan tanggal mulai : (exp: 10 September 2020) ")
    end_date = input("Masukan tanggal selesai : (exp: 10 September 2020) ")
    val = (name, priority, status_id, project_id, begin_date, end_date) 
    cursor = db_conn.cursor() 
    sql = '''INSERT INTO tasks (name, priority, status_id, project_id, begin_date, end_date) VALUES (?, ?, ?, ?, ?, ?)'''
    #print(val)
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} data berhasil disimpan\n".format(cursor.rowcount))    

#fungsi mengubah data
def update_data_task(db_conn):
    cursor = db_conn.cursor()
    show_data_task(db_conn)
    id_task = int(input("\nKetik ID Task > "))
    name = input("Name   : ")
    priority = int(input("Priority : "))
    status_id = int(input("Status ID : "))
    project_id = int(input("Project ID : "))
    begin_date = input("Begin Date : (exp: 10 September 2020)")
    end_date = input("End Date : (exp: 10 September 2020) ")
  
    sql = "UPDATE tasks SET name=?, priority=?, status_id=?, project_id=?, begin_date=?, end_date=? WHERE id=?" 
    val = (name, priority, status_id, project_id, begin_date, end_date, id_task) 
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} Data berhasil diubah \n".format(cursor.rowcount))

#fungsi hapus data
def delete_data_task(db_conn):
    cursor = db_conn.cursor()
    show_data_task(db_conn) 
    id_task = int(input("\nKetik ID TASK > "))
    sql = "DELETE FROM tasks WHERE id = ? "
    val = (id_task,)
    cursor.execute(sql, val)
    db_conn.commit() 
    return print("\n{} Data berhasil dihapus \n".format(cursor.rowcount))

#fungsi cari data
def search_data_task(db_conn):
    cursor = db_conn.cursor()
    keyword = input("\nMasukkan Kata Kunci: ")
    sql = '''SELECT * FROM tasks 
    WHERE name LIKE '%%%s%%' 
    ''' % (keyword)
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) <= 0:
        print("\nTidak ada data\n") 
    else:
        for data in results:
            print(data)