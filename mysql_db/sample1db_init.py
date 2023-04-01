#!/usr/bin/env python3
from modules.db import Database
import json
import os

""""Root path of current database user"""
root_path = "sample1_db"
os.chdir(root_path)

"""Read user conf from conf file"""
sapinx_conf = "sample1_conf.json"
with open(sapinx_conf, 'r') as f:
    data = json.load(f)

"""Db username from conf .json file"""
db_user_name = data['user_name']

"""Db password form conf .json file"""
db_password = data['password']

"""Db name from conf .json file"""
db_name = data['db_name']

"""Db host from conf .json file"""
db_host = data['host']

""""""
sipanx = Database(user=db_user_name, password=db_password, db_name=db_name)

sipanx.db_init()
# sipanx.login()
# sipanx.execute_sql(query_file="sample.sql")
# sipanx.db_dump(output_file="sipanx_dump.sql")
# sipanx.db_del()
# sipanx.query()
# Database.list()
# sipanx.del_user()
# sipanx.db_del()
# sipanx.query()
sipanx.execute_sql(sqlfile='sample_customer.sql')
