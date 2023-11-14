## Installing on a LAMP Server
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
