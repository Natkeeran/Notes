* CLAW Playbook currently expects an `ubuntu` user with sudo privileges.  Thought this need not be the ansible user.

```
#adduser ubuntu
(follow the prompts to create the user)
#usermod -aG sudo ubuntu
(add ubuntu to sudo
```
