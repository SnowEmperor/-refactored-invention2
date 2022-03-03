import requests
import argparse
import sqlite3
from a1 import path_dump

Session = requests.session()
datas = {"login_username": "def", "login_password": "def"}
login = input("enter you login: ")
password = input("password: ")
datas['login_username'] = login
datas['login_password'] = password
url = "http://127.0.0.1:8000/docs#/default/dump_file_items__item_id__post"
s = requests.Session()
loging = s.post(url, data=datas)

parser = argparse.ArgumentParser()
parser.add_argument('scan_file', type=str)
parser.add_argument('name_file', type=str)
args = parser.parse_args()

result = path_dump(args.scan_file, args.name_file)
file_path = list(result.items())


def insert_multi_path(records):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(

       name TEXT,
       path TEXT);
        """)
    cur.executemany("INSERT INTO users VALUES(?, ?);", records)
    print("Записи успешно вставлены в таблицу users")
    conn.commit()
    conn.close()


insert_multi_path(file_path)



