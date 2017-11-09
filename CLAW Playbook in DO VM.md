## Installation
* Ensure that your VM has ssh key via public key

* CLAW Playbook currently expects an `ubuntu` user with sudo privileges.  Thought this need not be the ansible user.

```
#adduser ubuntu
(follow the prompts to create the user)
#usermod -aG sudo ubuntu
(add ubuntu to sudo
```

* Change the [hosts](https://github.com/Islandora-Devops/claw-playbook/blob/master/inventory/vagrant/hosts) file to point to the server ip and provide the ansible ssh user and port.  

* Install dependencies
```
ansible-galaxy install -r requirements.yml
```
* Execute Ansible
```
ansible-playbook -i inventory/vagrant/hosts playbook.yml
```

## Possible Issues
Rerunning ansible seem to fix these issues!

```
TASK [karaf : Install wrapper] ***************************************************************************************************************************************
Thursday 09 November 2017  11:53:49 -0500 (0:00:06.102)       0:21:34.718 ***** 
fatal: [default]: FAILED! => {"changed": true, "cmd": ["./client", "wrapper:install"], "delta": "0:00:01.542893", "end": "2017-11-09 16:53:51.088577", "failed": true, "rc": 1, "start": "2017-11-09 16:53:49.545684", "stderr": "Failed to get the session.", "stderr_lines": ["Failed to get the session."], "stdout": "client: JAVA_HOME not set; results may vary", "stdout_lines": ["client: JAVA_HOME not set; results may vary"]}
```
