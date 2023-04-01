#!/usr/bin/env python3
import os
import subprocess

"""Mysql database class"""
class Database:
    def __init__(self, user, password, db_name, host="localhost"):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host

    """Initialize db with usernam and password"""
    def db_init(self):
        try:
            os.system(f"mysql -e 'CREATE DATABASE {self.db_name};'")
            os.system(
                f"mysql -e \"CREATE USER '{self.user}'@'{self.host}' IDENTIFIED BY '{self.password}';\"")
            os.system(
                f"mysql -e 'GRANT ALL PRIVILEGES ON {self.db_name}.* TO {self.user}@{self.host};'")
            os.system(f"mysql -e 'FLUSH PRIVILEGES;'")
            print(f"Database [{self.db_name}] was created.")
        except SyntaxError as e:
            return e

    # login to database
    """Login to mysql with self.user and self.password"""
    def login(self):
        try:
            os.system(
                f'mysql -h {self.host} -u {self.user} -p{self.password} {self.db_name}')
        except SyntaxError as e:
            return e
    # execute sql file on database
    """Execute .sql file on db"""
    def execute_sql(self, sqlfile):
        try:
            os.system(
                f'mysql -h {self.host} -u {self.user} -p{self.password} {self.db_name} < {sqlfile}')
        except SystemError as e:
            print(f'error while executing {sqlfile} file, {e}')

    """Dump database data as output_file name"""    
    def db_dump(self, output_file="exported_db.sql"):
        try:
            os.system(
                f'mysqldump -u root -p  -h{self.host} {self.db_name} > {output_file}')
        except ConnectionError as e:
            print(f'error while dumping {self.db_name}, {e}')

    """Delete database with self user and self password"""
    def db_del(self):
        try:
            os.system(
                f'MYSQL_PWD={self.password} mysql -h {self.host} -u {self.user}  -e "DROP DATABASE {self.db_name};"')
        except:
            return
    """Query function"""
    def query(self, query):
        try:
            # prevent use of password in terminal
            os.system(
                f'MYSQL_PWD={self.password} mysql -h {self.host} -u {self.user} {self.db_name} -e "{query}"')
        except SyntaxError as e:
            return e
    """list of databases"""
    def list():
        try:
            os.system(f'mysql -e "SHOW DATABASES;"')
        except SyntaxError as e:
            return e
    """List all mysql users"""
    def list_users():
        os.system(f'mysql -e "SELECT User FROM mysql.user;"')
        
    """Delete mysql user with root permission"""
    def del_user(self):
        del_cmd = f"mysql -e \"DROP USER '{self.user}'@'{self.host}';\""
        try:
            subprocess.check_output(del_cmd, shell=True, stderr=subprocess.STDOUT)
            print(f"User {self.user} has been removed from MySQL.")
        except subprocess.CalledProcessError as e:
            print(f"Error removing user {self.user} from MySQL: {e.output.decode('utf-8').strip()}")


    """Restore the db with .sql file"""
    def db_restore(self, sqlfile):
        try:
            exit_code = os.system(
                f'MYSQL_PWD={self.password} mysql -h {self.host} -u {self.user} {self.db_name} < {sqlfile}')
            if exit_code == 0:
                print(f'successfully restored db from {sqlfile} file.')
            else:
                pass
        except SystemError as e:
            print(f'Error while executing {sqlfile} file: {e}')
    """Configuration Template"""

