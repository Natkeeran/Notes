* CLAW Playbook currently expects an `ubuntu` user with sudo privileges.  Thought this need not be the ansible user.

```
#adduser ubuntu
(follow the prompts to create the user)
#usermod -aG sudo ubuntu
(add ubuntu to sudo
```

* Change the [hosts](https://github.com/Islandora-Devops/claw-playbook/blob/master/inventory/vagrant/hosts) file to point to the server ip and provide the ansible ssh user and port.  
