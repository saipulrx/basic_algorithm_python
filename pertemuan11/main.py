import sqlite3
from sqlite3 import Error
import os
from create_table import create_connection
from project import *
from task import *

# create a database connection
database = r"/Users/muhammadsaipulrohman/Documents/IDB/source_code/python_algoritma/sqlite/testing.db"
conn_db = create_connection(database)

def show_main_menu():
    print("++============================================++")
    print("| MENU UTAMA APLIKASI MENGELOLA PROJECT & TASK |")
    print("++============================================++")
    print("|| 1. || MENU PROJEK .........................||")
    print("|| 2. || MENU TASK ...........................||")
    print("++============================================++")
    print("|| 0. || CLOSE PROGRAM........................||")
    print("++============================================++")
    main_menu = input("    Silahkan Pilih Menu -> ") 
  
    # clear screen 
    os.system("clear") 
  
    if main_menu == "1":
        show_project_menu(conn_db)
    elif main_menu == "2":
        show_task_menu(conn_db)
    elif main_menu == "0":
        exit()
    else:
        print("Menu salah!")            

def show_project_menu(conn_db):
    print("++=====================================++")
    print("| MENU UTAMA APLIKASI MENGELOLA PROJECT |")
    print("++=====================================++")
    print("|| 1. || TAMPILKAN DATA PROJEK ........||")
    print("|| 2. || INSERT DATA PROJEK ...........||")
    print("|| 3. || UBAH DATA PROJEK .............||")
    print("|| 4. || HAPUS DATA PROJEK ............||")
    print("|| 5. || CARI DATA PROJEK .............||")
    print("++=====================================++")
    print("|| 9. || KEMBALI KE MENU UTAMA ........||")
    print("|| 0. || CLOSE PROGRAM ................||")
    print("++=====================================++")
    menu_project = input("    Silahkan Pilih Menu -> ")

    # clear screen 
    os.system("clear")

    if menu_project == "1":
        show_data_project(conn_db)
    elif menu_project == "2":
        insert_data_project(conn_db)
    elif menu_project == "3":
        update_data_project(conn_db)
    elif menu_project == "4":
        delete_data_project(conn_db)
    elif menu_project == "5":
        search_data_project(conn_db)
    elif menu_project == "9":
        show_main_menu()
    elif menu_project == "0":
        exit()
    else:
        print("Menu salah!")
        show_project_menu(conn_db)

def show_task_menu(conn_db):
    print("++=====================================++")
    print("|| MENU UTAMA APLIKASI MENGELOLA TASK  ||")
    print("++=====================================++")
    print("|| 1. || TAMPILKAN DATA TASK ..........||")
    print("|| 2. || INSERT DATA TASK .............||")
    print("|| 3. || UBAH DATA TASK ...............||")
    print("|| 4. || HAPUS DATA TASK ..............||")
    print("|| 5. || CARI DATA TASK ...............||")
    print("++=====================================++")
    print("|| 9. || KEMBALI KE MENU UTAMA ........||")
    print("|| 0. || CLOSE PROGRAM ................||")
    print("++=====================================++")
    menu_task = input("    Silahkan Pilih Menu -> ")

    # clear screen 
    os.system("clear")

    if menu_task == "1":
        show_data_task(conn_db)
    elif menu_task == "2":
        insert_data_task(conn_db)
    elif menu_task == "3":
        update_data_task(conn_db)
    elif menu_task == "4":
        delete_data_task(conn_db)
    elif menu_task == "5":
        search_data_task(conn_db)
    elif menu_task == "9":
        show_main_menu()
    elif menu_task == "0":
        exit()
    else:
        print("Menu salah!")
        show_project_menu(conn_db)    

if __name__ == "__main__":
    while (True):
        show_main_menu()
