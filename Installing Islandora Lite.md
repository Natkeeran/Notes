## ISLE-DC (Docker)
### Fresh Build
```
git clone --branch 1.0.0-beta2 https://github.com/digitalutsc/isle-dc.git isle-dc-lite
cd isle-dc-lite
make lite_dev
```

### To Rebuild
```
make clean
composer clear-cache 
make lite_dev
```

### For Windows Users:

__Environment Setup:__

1. Install WSL2 and Ubuntu. Instructions for doing so can be found on the [Ubuntu Website](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview) and the [Microsoft Website](https://learn.microsoft.com/en-us/windows/wsl/install)

1. Download and install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/). In Docker Desktop, navigate to Settings (gear icon in the menu bar) > Resources > WSL Integration and check "Enable integration with my default WSL distro". Also, under "Enable integration with additional distros," turn on the Ubuntu distribution you are using. If WSL2 is currently running, close it by running `wsl --shutdown` in an elevated Powershell window. 
    
    **NOTE:** You should not ever have to run Docker Desktop with elevated privileges (as administrator). If a message appears stating that the current user does not have privilleges, run this command in an elevated Command Prompt window: 
    ```
    net localgroup docker-users "your-user-id" /ADD
    ```

    **NOTE:** If a message appears stating that you should convert from WSL1 to WSL2, run the following in a normal (non-elevated) *Windows* Command Prompt
    ```
    wsl --set-version Ubuntu-<VERSION NUMBER> 2
    wsl --list --verbose    # the version number next to the Ubuntu distribution should be 2
    ```

1. Install GNU make.
    ```bash
    sudo apt install make
    ```

1. Open WSL2 (Start > Ubuntu Version) and run the build commands found [above](#isle-dc-docker). Make sure to clone the isle-dc repository within the WSL2 filesystem (do not clone in /mnt or any of its subdirectories). 

1. Check if everything works. There should be a Drupal website present at https://islandora.traefik.me/

## Installing on a LAMP Server (Manual Installation)
### Prepare the LAMP Server
* Install necessary components such as linux, apache, mysql, php, composer, git,  curl, and imagemagick
* Ensure that you have necessary php extensions, including php-curl php-json php-mbstring php-mysql php-tokenizer php-xml php-zip php-imagick php-gd 
* Please see [How To Install Linux, Apache, MySQL, PHP (LAMP) Stack on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-22-04) for detail guidence

### Installing Drupal

* Clone the project
```
git clone https://github.com/digitalutsc/islandora-sandbox
```

* [Create mysql user and grant privilages](https://www.drupal.org/docs/getting-started/installing-drupal/create-a-database)
```
CREATE USER username@localhost IDENTIFIED BY 'password';
```
```
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'demo_islandora'@'localhost' WITH GRANT OPTION;
```
 
* Append the database into assets/patches/default_settings.txt

```
  $databases['default']['default'] = array (
  'database' => 'db_name',
  'username' => 'db_user',
  'password' => 'Db_password1#',
  'prefix' => '',
  'host' => 'localhost',
  'port' => '3306',
  'namespace' => 'Drupal\\mysql\\Driver\\Database\\mysql',
  'driver' => 'mysql',
  'autoload' => 'core/modules/mysql/src/Driver/Database/mysql/',
);

$settings['trusted_host_patterns'] = [
  '^localhost$',
 ];

```

Note that you would need to add the ip `^##\.##\.##\.##$` or the domain `^mydomain\.com$` to the trusted host patterns.

* Install the site
```
sudo ./vendor/drush/drush/drush si -y --existing-config minimal --account-pass password
```

* Set folder ownership for `web/sites/default/files` and `web/sites/default/private` to be www-data. For example:
```
chown -R www-data:www-data private
```

### Setting up Apache and Virtual Host

* Ensure that apache rewrite is enabled
```
sudo a2enmod rewrite
```

* Modify the apache2 virtual host to point to the web folder, and add the rewrite rules.  For example:

```
<VirtualHost *:80>
  <Directory /var/www/islandora-sandbox/web>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
  </Directory>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/islandora-sandbox/web

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>

```

* Restart apache
```
systemctl restart apache2
```

### Islandora Lite Configurations

* Import required taxonomy
```
sudo ./vendor/drush/drush/drush migrate:import islandora_tags
```

### Configuring Solr
* [Install Solr](https://tecadmin.net/how-to-install-apache-solr-on-ubuntu-22-04/)
* Create a Solr core for indexing islandora lite content
```
sudo su - solr -c "/opt/solr/bin/solr create -c ISLANDORA -n data_driven_schema_configs"
```
* Configure the solr server: `/admin/config/search/search-api/server/default_solr_server/edit`
* Download the config.zip and replace the solr core conifgs

```
root@demo_server:/var/solr/data/ISLANDORA/conf# ls /opt/solr_9_x_config/
accents_en.txt   protwords_en.txt   schema_extra_fields.xml  solrconfig_extra.xml  solrconfig_requestdispatcher.xml  stopwords_und.txt
accents_und.txt  protwords_und.txt  schema_extra_types.xml   solrconfig_index.xml  solrcore.properties               synonyms_en.txt
elevate.xml      schema.xml         solrconfig.xml           solrconfig_query.xml  stopwords_en.txt                  synonyms_und.txt
root@demo_server:/var/solr/data/ISLANDORA/conf# cp /opt/solr_9_x_config/*.* ./
root@demo_server:/var/solr/data/ISLANDORA/conf# sudo systemctl restart solr
```
* Reindex the solr index `/admin/config/search/search-api/index/default_solr_index_islandora_lite`

### Other considerations
* Max upload size `upload_max_filesize` and `post_max_size`
```
sudo pico /etc/php/8.2/apache2/php.ini
systemctl restart apache2
```
