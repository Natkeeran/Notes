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

* Install the site
```
 sudo ./vendor/drush/drush/drush si -y --existing-config minimal --account-pass password
```
## Setting up Apache and Virtual Host

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
