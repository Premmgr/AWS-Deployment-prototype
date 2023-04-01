## Requirements
``` mysql installed, root acccess to mysql ```

------------------------------------------------------------------------

## Usage

- check current userlist in mysql
```
root@server-k8s:~/mysql# ./mysql_user_lists.sh
+------------------+
| User             |
+------------------+
| debian-sys-maint |
| mysql.infoschema |
| mysql.session    |
| mysql.sys        |
| root             |
+------------------+
```

------------------------------------------------------------------------


- init database at first time

```
root@server-k8s:~/mysql# ./sample1db_init.py
Database [clients] was created.
```

------------------------------------------------------------------------


- sample query script 
```
root@server-k8s:~/mysql$ ./sample1_query_test1.py 
customers lists:
+-------------+------------+-----------+--------------+
| customer_id | first_name | last_name | phone_number |
+-------------+------------+-----------+--------------+
|           1 | John       | Doe       | 555-1234     |
|           2 | Jane       | Smith     | 555-5678     |
|           3 | Bob        | Johnson   | 555-9876     |
+-------------+------------+-----------+--------------+
products lists:
+------------+--------------+-------------+--------+
| product_id | product_name | category_id | price  |
+------------+--------------+-------------+--------+
|          1 | TV           |           1 | 799.99 |
|          2 | Shirt        |           2 |  29.99 |
|          3 | Couch        |           3 | 599.99 |
|          4 | Laptop       |           1 | 999.99 |
|          5 | Dress        |           2 |  49.99 |
|          6 | Chair        |           3 |  89.99 |
+------------+--------------+-------------+--------+
categories lists:
+-------------+---------------+
| category_id | category_name |
+-------------+---------------+
|           1 | Electronics   |
|           2 | Clothing      |
|           3 | Home Goods    |
+-------------+---------------+

```
------------------------------------------------------------------------


- configuration file for sipanx (exmaple db_user)

```
root@server-k8s:~/mysql/sample1_db# cat sample1_conf.json
{
    "user_name": "sipanx",
    "password": "EHVDUYG8YCEB",
    "db_name": "clients",
    "host": "localhost"
}
root@server-k8s:~/mysql/sample1_db#
```
