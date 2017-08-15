Ansible is used for deployment automation/provisioning, configuration management and documentation.

## Resources
* http://docs.ansible.com/ansible/intro_getting_started.html
* https://serversforhackers.com/an-ansible-tutorial 
* https://www.linode.com/docs/applications/ansible/getting-started-with-ansible
* http://atpras.blogspot.ca/2014/02/ansible-hello-world.html’
* https://sysadmincasts.com/episodes/43-19-minutes-with-ansible-part-1-4

## Create a target vagrant ubuntu machine for this exercise
```
vagrant init aspyatkin/ubuntu-16.04-server-amd64; vagrant up --provider virtualbox
```

## Install Python on the Master Machine and on the Slave machine
(If apt-get-repository command not found)
```
sudo apt-get install software-properties-common python-software-properties
```
```
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python2.7

python --version
```

## Installing Ansible
```
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```

### Ensure you have your SSH Public Key set on the target server
http://sshkeychain.sourceforge.net/mirrors/SSH-with-Keys-HOWTO/SSH-with-Keys-HOWTO-4.html

“When speaking with remote machines, Ansible by default assumes you are using SSH keys. SSH keys are encouraged but password authentication can also be used where needed by supplying the option --ask-pass. If using sudo features and when sudo requires a password, also supply --ask-become-pass (previously --ask-sudo-pass which has been deprecated).”

### Edit your hosts file and add the target machine
sudo pico /etc/ansible/hosts

```
[ubuntu1]
127.0.0.1 ansible_port=2222 ansible_user=vagrant
```

### Run a simple ansible command against the target machine
The command for ansible is of the following format:

ansible server_or_group -m module_name -a arguments

```
ansible ubuntu1 -m ping
```

### Create a hello world playbook
hello.yml

```yml
---
- name: Hello World
  hosts: ubuntu1
  user: vagrant
  sudo: yes

  tasks:
    - name: Hello World
        shell: date >> now.txt
```        

### Run the playbook
```
ansible-playbook hello.yml
```

Ansible will create a now.txt file in the home directory of the target machine: /home/vagrant.  It will output the date each time the playbook is run.
