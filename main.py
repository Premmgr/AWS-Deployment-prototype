#!/usr/bin/env python3
from modules import color, check_os
import os
import sys
import logging

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

state_files = {'.terraform.lock.hcl',
               'terraform.tfstate', 'terraform.tfstate.backup'}
state_dir = {'.terraform'}
logger = logging.getLogger(__name__)

# terraform option section


class TeraOption:
    def __init__(self, option_name, path):
        self.option_name = option_name
        self.path = path
    # pefrom section

    def perfom(self, action=None):
        os.chdir(f'{terraform_path}/{self.path}')
        if action == None:
            print(f'{color.red}No action provided for {self.option_name}{color.ec}')
            return sys.exit(1)
        elif self.option_name == None:
            print(f'{color.red}No option_name provided{color.ec}')
            return sys.exit(1)

        elif action == "init":
            print(f"{color.yellow}{self.option_name}_{action}{color.ec}", lines)
            exit_code = os.system(f'terraform {action} -var-file={var_tf}')
            if not exit_code == 0:
                print(f'{color.red}{self.option_name} {action} eror {color.ec}')

        elif action == "clean":
            no_file_found = f'{color.yellow}no static files and directory are found, so not removed {self.option_name}{color.ec}'
            print(f'\nclearing statefiles for {self.option_name}')
            for file in state_files:
                try:
                    os.remove(file)
                    logger.info(f'removed {file} form {self.option_name}')
                except FileNotFoundError:
                    logger.warning(
                        f'{color.green}{file} not present, so not deleted{color.ec}')
            for dir in state_dir:
                try:
                    os.system(f'rm -rf {dir}')
                except FileNotFoundError:
                    logger.warning(f'{dir} not found')

        else:
            print(f"{color.yellow}{self.option_name}_{action}{color.ec}", lines)
            exit_code = os.system(
                f'terraform {action} -var-file={var_tf} {auto_approve}')
            if not exit_code == 0:
                print(f'{color.red}{self.option_name} {action} eror {color.ec}')
        # reset path
        os.chdir(current_path)


network = TeraOption(option_name="network", path=network_path)
security = TeraOption(option_name="security_group", path=secgrp_path)
appserver = TeraOption(option_name="appserver", path=appserver_path)

# end of terraform option

# ansible section
# hostfile required if ansible apply options is used (uses hotfile to connect and execute all playbooks)


class Ansible:
    def apply():
        os.chdir(f'{terraform_path}/{ansible_path}')
        network.perfom(action="init")
        print(f'{color.magenta}running provisioner..{color.ec}')
        os.system(
            f'ansible-playbook -i {appserver_ansible_host_file} --private-key ../{appserver_ssh_key} -u {appserver_ssh_user} provisioner_apply.yml')
        # ansible-playbook -i hosts  --private-key ../server-key.pem  -u ubuntu provisioner_apply.yml
        # prvosion app server with ansible playbooks

    def revert():
        # reverst every process done by ansible playbooks
        pass


def server_ip(self, filename="hosts"):
    # for ip address uses hosts file to extract ip
    os.chdir(f'{terraform_path}/{ansible_path}')
    with open(f"{filename}, 'r'") as f:
        return f.read


class SSH:
    def __init__(self, user_name, ip):
        self.user_name = user_name
        self.ip = ip

    def exec(self):
        cmd = input("exec command or script: ")
        print(f'\n{color.green}executing..{color.ec}')
        os.system(
            f'ssh -i ../{appserver_ssh_key} {self.user_name}@{server_ip()} "{cmd}"')

    def login():
        # for ip address uses hosts file to extract ip
        print(f'\n{color.green}connecting..{color.ec}')
        os.system(f'ssh -i ../{appserver_ssh_key} ubuntu@{server_ip()}')

    def pipeline_exec(cmmand=None):
        print(f'\n{color.green}executing..{color.ec}')
        os.system(
            f'ssh -i ../{appserver_ssh_key} ubuntu@{server_ip()} "{cmmand}"')

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
--ansible-revert    : {color.red}reverts{color.ec} all action applied by --apply option ({color.yellow}NOT READY{color.ec})

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
        network.perfom(action="init")
        security.perfom(action="init")
        appserver.perfom(action="init")

    if arg1 == "--deploy-network":
        network.perfom(action="apply")

    if arg1 == "--deploy-secgrp":
        security.perfom(action="apply")

    if arg1 == "--deploy-appserver":
        # deployments
        network.perfom(action="apply")
        security.perfom(action="apply")
        appserver.perfom(action="apply")
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
        network.perfom(action="plan")

    # destroy args --------------------------------
    if arg1 == "--destroy-appserver":
        appserver.perfom(action="destroy")

    if arg1 == "--destroy-network":
        network.perfom(action="destroy")

    if arg1 == "--destroy-secgrp":
        security.perfom(action="destroy")

    if arg1 == "--destroy-all":
        appserver.perfom(action="destroy")
        network.perfom(action="destroy")
        security.perfom(action="destroy")

    # clear statefiles
    if arg1 == "--clear-statefiles":
        network.perfom(action="clean")
        security.perfom(action="clean")
        appserver.perfom(action="clean")

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
