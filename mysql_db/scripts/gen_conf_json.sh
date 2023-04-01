#!/bin/bash
# Check arguments count
if [ "{$#}" -lt 4 ]; then
    echo "Usage: $0 <user> <password> <db_name> <host>"
    exit 1
fi
# input arguments to variables
user="$1"
password="$2"
db_name="$3"
host="$4"

# json format
data=$(cat <<EOF
{
    "user_name": "${user}",
    "password": "${password}",
    "db_name": "${db_name}",
    "host": "${host}"
}
EOF
)

# output conf file
echo "${data}" > example_conf.json
