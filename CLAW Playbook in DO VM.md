## Introduction
Ansible is an configuration and deployment automation tool.  Ansible executes instructions in the target host machines by conntecting to them via ssh.  The instructions are organized into units called Roles.  Roles are grouped into playbooks.

Currently CLAW-playbook specifies a default target host machine.  However, it is divided into [six groups](https://github.com/Islandora-Devops/claw-playbook/blob/master/inventory/vagrant/hosts), each group can potentially target different host machines.  


## Installation
* Ensure that your VM has SSH public key.  

* CLAW Playbook currently expects an `ubuntu`.  Thought this need not be the ansible user.

```
#adduser ubuntu
(follow the prompts to create the user)
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

* Change the trusted host settings in Drupal settings.php by going to `/var/www/html/drupal/web/sites/default/settings.php` and changing the `$settings['trusted_host_patterns']` to include `'.*'`

* In this file /var/www/html/Crayfish/Milliner/src/Converter/DrupalEntityConverter.php, replace the convertJsonld function with the following function.  This is a bug in synching drupal content to fedora.
```
    public function convertJsonld($path, Request $request)
    {
        $path = substr($path, 4);
        // Return the response from Drupal.
        $options = $this->preprocess($this->cleanPath($path), $request);
        return $this->client->get($this->cleanPath($path) . '?_format=jsonld', $options);
    }

```

## Possible Issues
Rerunning ansible seem to fix these issues!

```
TASK [karaf : Install wrapper] ***************************************************************************************************************************************
Thursday 09 November 2017  11:53:49 -0500 (0:00:06.102)       0:21:34.718 ***** 
fatal: [default]: FAILED! => {"changed": true, "cmd": ["./client", "wrapper:install"], "delta": "0:00:01.542893", "end": "2017-11-09 16:53:51.088577", "failed": true, "rc": 1, "start": "2017-11-09 16:53:49.545684", "stderr": "Failed to get the session.", "stderr_lines": ["Failed to get the session."], "stdout": "client: JAVA_HOME not set; results may vary", "stdout_lines": ["client: JAVA_HOME not set; results may vary"]}
```
