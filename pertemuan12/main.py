import sqlite3
from sqlite3 import Error
import os
from create_table import create_connection


# create a database connection
database = r"/Users/muhammadsaipulrohman/Documents/IDB/source_code/python_algoritma/sqlite/books.db"
conn_db = create_connection(database)

def show_main_menu():
    print("++=============================================++")
    print("| MENU UTAMA APLIKASI MENGELOLA BUKU & PENERBIT |")
    print("++=============================================++")
    print("|| 1. || MENU BUKU ............................||")
    print("|| 2. || MENU PENERBIT ........................||")
    print("++============================================++")
    print("|| 0. || CLOSE PROGRAM........................||")
    print("++============================================++")
    main_menu = input("    Silahkan Pilih Menu -> ") 
  
    # clear screen 
    os.system("clear") 
  
    if main_menu == "1":
        show_buku_menu(conn_db)
    elif main_menu == "2":
        show_penerbit_menu(conn_db)
    elif main_menu == "0":
        exit()
    else:
        print("Menu salah!")            

def show_buku_menu(conn_db):
    print("++=====================================++")
    print("|| MENU UTAMA APLIKASI MENGELOLA BUKU  ||")
    print("++=====================================++")
    print("|| 1. || TAMPILKAN DATA BUKU ..........||")
    print("|| 2. || INSERT DATA BUKU .............||")
    print("|| 3. || UBAH DATA BUKU ...............||")
    print("|| 4. || HAPUS DATA BUKU ..............||")
    print("|| 5. || CARI DATA BUKU ...............||")
    print("++=====================================++")
    print("|| 9. || KEMBALI KE MENU UTAMA ........||")
    print("|| 0. || CLOSE PROGRAM ................||")
    print("++=====================================++")
    menu_buku = input("    Silahkan Pilih Menu -> ")

    # clear screen 
    os.system("clear")

    if menu_buku == "1":
        pass
        #show_data_buku(conn_db)
    elif menu_buku == "2":
        pass
        #insert_data_buku(conn_db)
    elif menu_buku == "3":
        pass
        #update_data_buku(conn_db)
    elif menu_buku == "4":
        pass
        #delete_data_buku(conn_db)
    elif menu_buku == "5":
        pass
        #search_data_buku(conn_db)
    elif menu_buku == "9":
        show_main_menu()
    elif menu_buku == "0":
        exit()
    else:
        print("Menu salah!")
        show_buku_menu(conn_db)

def show_penerbit_menu(conn_db):
    print("++======================================++")
    print("| MENU UTAMA APLIKASI MENGELOLA PENERBIT |")
    print("++======================================++")
    print("|| 1. || TAMPILKAN DATA PENERBIT .......||")
    print("|| 2. || INSERT DATA PENERBIT ..........||")
    print("|| 3. || UBAH DATA PENERBIT ............||")
    print("|| 4. || HAPUS DATA PENERBIT ...........||")
    print("|| 5. || CARI DATA PENERBIT ............||")
    print("++=====================================++")
    print("|| 9. || KEMBALI KE MENU UTAMA ........||")
    print("|| 0. || CLOSE PROGRAM ................||")
    print("++=====================================++")
    menu_penerbit = input("    Silahkan Pilih Menu -> ")

    # clear screen 
    os.system("clear")

    if menu_penerbit == "1":
        pass
        #show_data_task(conn_db)
    elif menu_penerbit == "2":
        pass
        #insert_data_task(conn_db)
    elif menu_penerbit == "3":
        pass
        #update_data_task(conn_db)
    elif menu_penerbit == "4":
        pass
        #delete_data_task(conn_db)
    elif menu_penerbit == "5":
        pass
        #search_data_task(conn_db)
    elif menu_penerbit == "9":
        show_main_menu()
    elif menu_penerbit == "0":
        exit()
    else:
        print("Menu salah!")
        show_penerbit_menu(conn_db)    

if __name__ == "__main__":
    while (True):
        show_main_menu()
