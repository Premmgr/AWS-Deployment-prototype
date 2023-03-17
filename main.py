#!/usr/bin/env python3
from modules import color, check_os
import os, sys

# global variables
terraform_path = "terraform"
network_path = "network"
secgrp_path = "security-groups"
appserver_path = "app-server"
ansible_path = "ansible"
current_path = os.getcwd()
auto_approve = "-auto-approve"
appserver_ssh_key = "server-key.pem"
appserver_ansible_host_file = "hosts"
appserver_ssh_user = "ubuntu"

var_tf = "../terraform.tfvars"
lines = '-'*100

# prints platform
check_os.check_host_os()


# terraform actions
def apply(option):
    print(f"{color.yellow}{option}_apply{color.ec}", lines)
    apply_exit = os.system(
        f'terraform apply -var-file={var_tf} {auto_approve}')
    if not apply_exit == 0:
        init("network")
        retry_exit = os.system(
            f'terraform apply -var-file={var_tf} {auto_approve}')
        if not retry_exit == 0:
            print(
                f'{color.red}terraform {option} apply error, check {option} configuration section{color.ec}')
            # prints erro when terraform apply fails
            return apply_exit
        
def init(option):
    print(f"{color.yellow}{option}_init{color.ec}", lines)
    init_exit = os.system(f'terraform init -var-file={var_tf}')
    if not init_exit == 0:
        # prints erro when terraform init fails
        print(
            f'{color.red}terraform {option} init error, check {option} configuration section{color.ec}')
        return init_exit

def plan(option):
    print(f"{color.yellow}{option}_plan{color.ec}", lines)
    plan_exit = os.system(f'terraform plan -var-file={var_tf}')
    if not plan_exit == 0:
        # prints erro when terraform init fails
        print(
            f'{color.red}terraform {option} plan error, check {option} configuration section{color.ec}')
        return plan_exit

def destroy(option):
    print(f"{color.yellow}{option}_destroy{color.ec}", lines)
    destroy_exit = os.system(
        f'terraform destroy -var-file={var_tf} {auto_approve}')
    if not destroy_exit == 0:
        # prints erro when terraform init fails
        print(
            f'{color.red}terraform {option} plan error, check {option} configuration section{color.ec}')
        return destroy_exit
    
def delete_state(option):
    pass
    print(f'{color.red}removed statefiles {option}{color.ec}')
    state_files = ['.terraform.lock.hcl','terraform.tfstate', 'terraform.tfstate.backup', '.terraform/']
    linux_statefiles = " ".join(state_files)
    os.system(f'rm -rf {linux_statefiles}')


# terraform resources deployements
class Tera:
    def _init_all():
        # initiate all configuration
        # network init
        os.chdir(f'{terraform_path}/{network_path}')
        init("network")
        # secgrp init
        os.chdir(f'../{secgrp_path}')
        init("sec-grp")
        os.chdir(f'../{appserver_path}')
        init("appserver")
        print(os.getcwd())
        print(f'{color.green}init process completed{color.ec}')

    # applied from network path any modification will take effect on next apply or update option
    def _network_apply():
        os.chdir(f'{current_path}/{terraform_path}/{network_path}')
        plan(option="network")
        apply(option="network")
    # destroys network resources (all configuration will be reverted related to networks)
    def _network_destroy():
        os.chdir(f'{current_path}/{terraform_path}/{network_path}')
        destroy(option="network")
    # remove security group from 
    def _secgrp_apply():
        os.chdir(f'{current_path}/{terraform_path}/{secgrp_path}')
        plan(option="sec-grp")
        apply(option="sec-grp")

    def _secgrp_destroy():
        os.chdir(f'{current_path}/{terraform_path}/{secgrp_path}')
        destroy(option="seg-grp")

    def _appserver_apply():
        os.chdir(f'{current_path}/{terraform_path}/{appserver_path}')
        plan(option="appserver")
        apply(option="appserver")

    def _appserver_destroy():
        os.chdir(f'{current_path}/{terraform_path}/{appserver_path}')
        destroy(option="appserver")

    def _delete_all_statefile():

        # clear appserver statefiles
        os.chdir(f'{current_path}/{terraform_path}/{appserver_path}')
        delete_state(option="app-server")

        # clear ansible statefiles
        os.chdir(f'{current_path}/{terraform_path}/{ansible_path}')
        delete_state(option="ansible")

        # clear secgrp stagefiles
        os.chdir(f'{current_path}/{terraform_path}/{secgrp_path}')
        delete_state(option="sec-grp")
        
        # clear network statefiles
        os.chdir(f'{current_path}/{terraform_path}/{network_path}')
        delete_state(option="network")
        
# ansible section
# hostfile required if ansible apply options is used (uses hotfile to connect and execute all playbooks)

class Ansible:
    def apply():
        os.chdir(f'{terraform_path}/{ansible_path}')
        init("ansible-resource")
        apply("ansible-host-extract")
        print(f'{color.magenta}running provisioner..{color.ec}')
        os.system(f'ansible-playbook -i {appserver_ansible_host_file} --private-key ../{appserver_ssh_key} -u {appserver_ssh_user} provisioner_apply.yml')
        # ansible-playbook -i hosts  --private-key ../server-key.pem  -u ubuntu provisioner_apply.yml
        # prvosion app server with ansible playbooks

    def revert():
        # reverst every process done by ansible playbooks
        pass


class SSH:
    def exec():
        # for ip address uses hosts file to extract ip
        os.chdir(f'{terraform_path}/{ansible_path}')
        with open('hosts', 'r') as f:
            server_ip = f.read()
        cmd = input("exec command or script: ")
        print(f'\n{color.green}executing..{color.ec}')
        os.system(f'ssh -i ../{appserver_ssh_key} ubuntu@{server_ip} "{cmd}"')

    def login():
        # for ip address uses hosts file to extract ip
        os.chdir(f'{terraform_path}/{ansible_path}')
        with open('hosts', 'r') as f:
            server_ip = f.read()
        print(f'\n{color.green}connecting..{color.ec}')
        os.system(f'ssh -i ../{appserver_ssh_key} ubuntu@{server_ip}')
    
    def pipeline_exec(cmmand=None):
        os.chdir(f'{current_path}/{terraform_path}/{ansible_path}')
        with open('hosts', 'r') as f:
            server_ip = f.read()
        print(f'\n{color.green}executing..{color.ec}')
        os.system(f'ssh -i ../{appserver_ssh_key} ubuntu@{server_ip} "{cmmand}"')
# help sections 


class Help:
    def general():
        print(f'requires terraform installed')
        print(f"""--help              : prints this help
{lines}
{color.yellow}deploy options{color.ec}:
--update            : reapply all config on aws
--deploy-network    : deploy network resources on aws
--deploy-secgrp     : deploy security group resources on aws
--deploy-appserver  : deploy appserver resources on aws (executes{color.magenta} ansible playbooks{color.ec})
{lines}
{color.yellow}destroy options{color.ec}:
--clear-statefiles  : clear all the statefiles ({color.red}works only on linux host{color.ec})
--destroy-network   : destroy network resources on aws
--destroy-secgrp    : destroy security group resources on aws
--destroy-appserver : destroy appserver resources on aws
--destroy-all       : {color.red}destroys all{color.ec} resources on aws (related{color.red} networks security-group {color.ec}etc)
{lines}
{color.yellow}ssh_options{color.ec}:
--ssh-exec          : {color.green}executes{color.ec} provided command on appserver (input command required)
--login             : login to {color.green}appserver{color.ec} (with default ssh key)
{lines}
{color.yellow}ansible_options{color.ec}:
--ansible-apply     : applies playbook to aws instance ({color.green}executes on host file only{color.ec})
--ansible-revert    : {color.red}reverts{color.ec} all action applied by --apply option ({color.yellow}limitation on revert function{color.ec})

""")

# argument section --------------------------------


def custom_agrs():
    if len(sys.argv) < 2:
        print(f'{color.red}no option provided{color.ec}')
        Help.general()
        sys.exit(1)

    print(f"{color.green}passed command{color.ec}: {color.magenta}{sys.argv}{color.ec}")

    # args section
    arg1 = sys.argv[1]
    # help args -----------------------------------
    if arg1 == "--help":
        Help.general()

    # deploy args ---------------------------------

    if arg1 == "--init-all":
        Tera._init_all()

    if arg1 == "--deploy-network":
        Tera._network_apply()

    if arg1 == "--deploy-secgrp":
        Tera._secgrp_apply

    if arg1 == "--deploy-appserver":
        # deployments
        Tera._network_apply()
        Tera._secgrp_apply()
        Tera._appserver_apply()
        os.chdir('../../')

        # ansible provisioner
        Ansible.apply()

        # execute ssh command to build and start application
        print(f'{color.green}building application image{color.ec}')
        build_cmd = "cd application && docker build -t webserver:latest ."
        SSH.pipeline_exec(cmmand=build_cmd)
        print(f'{color.green}starting application{color.ec}')
        start_cmd = "cd application && docker-compose up -d"
        SSH.pipeline_exec(cmmand=start_cmd)
        print(f'{color.green}Application deployed on aws{color.ec}')
    
    if arg1 == "--update":
        Tera._network_apply()
        Tera._secgrp_apply()
        Tera._appserver_apply()

    # destroy args --------------------------------
    if arg1 == "--destroy-appserver":
        Tera._appserver_destroy()

    if arg1 == "--destroy-network":
        Tera._network_destroy()

    if arg1 == "--destroy-secgrp":
        Tera._secgrp_destroy()

    if arg1 == "--destroy-all":
        Tera._appserver_destroy()
        Tera._secgrp_destroy()
        Tera._network_destroy()

    # clear statefiles
    if arg1 == "--clear-statefiles":
        Tera._delete_all_statefile()

    # ssh args ------------------------------------
    if arg1 == "--login":
        SSH.login()
    if arg1 == "--ssh-exec":
        SSH.exec()

    # ansible args --------------------------------
    if arg1 == "--ansible-apply":
        Ansible.apply()

    if arg1 == "--ansible-revert":
        Ansible.revert()

# entrypoint --------------------------------------
if __name__ == "__main__":
    custom_agrs()
