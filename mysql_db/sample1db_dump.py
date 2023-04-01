#!/usr/bin/env python3
from modules.db import Database
import json
import os

root_path = "sample1_db"
os.chdir(root_path)

sapinx_conf = "sample1_conf.json"
with open(sapinx_conf, 'r') as f:
    data = json.load(f)

db_user_name = data['user_name']
db_password = data['password']
db_name = data['db_name']
db_host = data['host']


# sample1_db = Database(user=db_user_name, password=db_password, db_name=db_name, host=db_host)
# sample1_db.create_db()

# # sample1_db.del_user()

sipanx = Database(user=db_user_name, password=db_password, db_name=db_name)

sipanx.db_dump(output_file='exported_sipanxdb.sql')
