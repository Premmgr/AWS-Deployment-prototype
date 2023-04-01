import json

"""generate the conf template for db conf"""
def conf_template(user="example_user",password="example_password",db_name="example_db",host="localhost"):
    data = {
        "user_name": f"{user}",
        "password": f"{password}",
        "db_name": f"{db_name}",
        "host": f"{host}"
    }
    """save conf as conf.json file in current path"""
    with open('example_conf.json', 'w') as f:
        json.dump(data, f, indent='\t')

