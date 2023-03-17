This repository contains a set of templates and configuration files for webapplication deployment using teraform and anisble.

Usage:

*deploy appserver on aws* `$ main.py --deploy-appserver`   
*destroy all resources on aws* `$ main.py --destroy-all`   
*execute pipeline script on aws server* `$ main.py --ssh-exec`  

This python script can do: 
* deploy network resource on aws 
* deploy security group resource on aws
* deploy appserver resource on aws 
* execute any command on aws server 
* initialize terraform for all resource with one command `./main.py --init-all`
* run external bash script with SSH class fucntion `./main.py --ssh-exec`
* automatic login using extracted public ip (terraform/ansible/hosts) `./main.py --login`

for the help `$ main.py --help`
