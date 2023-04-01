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

# sipanx.create_db()
# sipanx.login()
# sipanx.execute_sql(query_file="sample.sql")
# sipanx.db_dump(output_file="sipanx_db.sql")
# sipanx.db_del()
# sipanx.query()
# Database.list()
# sipanx.del_user()
# sipanx.db_del()
# sipanx.query()
# sipanx.execute_sql(sqlfile='sample_customer.sql')
print(f'customers lists:')
sipanx.query(query="SELECT * FROM customers;")

print(f'products lists:')
sipanx.query(query="SELECT * FROM products;")

print(f'categories lists:')
sipanx.query(query="SELECT * FROM categories;")
