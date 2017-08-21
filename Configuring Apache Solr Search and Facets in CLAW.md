(Note that these instructions are outdated as some of the modules have been enabled in CLAW by default.)


# Configuring Apache Solr Search and Facets in CLAW
## Required Modules
* [Search API](https://www.drupal.org/project/search_api)  (comes pre installed in CLAW vagrant as of July 14, 2016)
* [Solr Search](https://www.drupal.org/project/search_api_solr) 
* [Facets](https://www.drupal.org/project/facets)

## Steps
### Step 1 - Install Apache Solr Search module
* Go to `ubuntu@claw:/var/www/html/drupal$ `
* Download search_api_solr module
* Issue the following command `composer require drupal/search_api_solr` to install the required dependencies
* Enable search_api_solr module
* Optionally, also enable Solr Search Defaults submodule to make the configuration process easier

### Step 2 - Configuring Apache Solr Core on the server
The default core that comes with the current vagrant does not have the configuration expected by Drupal, thus for now we will create a new Apache core and copy the expected configurations.  
* Verify that solr is available here: `http://localhost:8983/solr/`
* Go to Cores Admin `http://localhost:8983/solr/#/~cores`
* Add a core called CLAW2.  It will produce an error with message similar to the following message, you can ignore that message for now: `Error CREATEing SolrCore 'CLAW2': Unable to create core [new_core] Caused by: Can't find resource 'solrconfig.xml' in classpath or '/opt/solr-6.2.1/server/solr/CLAW2'`
* Go to `cd /opt/solr-6.2.1/server/solr/`
* Create a directory with the same name as the new core `mkdir CLAW2`
* Inside CLAW2, create a `config` directory and a `data` directory 
* Go into the config directory and copy solr 6.x configuration from the module: `cp -R /var/www/html/drupal/web/modules/contrib/search_api_solr/solr-conf/6.x/* ./`
* Go to the bin directory: `/opt/solr-6.2.1/bin` and restart the server by issuing the following commands:
```
./solr stop -p 8983 
./solr start -p 8983 
```

### Step 3 - Configure the Apache Solr server in Drupal
* Go to search api configuration page: http://localhost:8000/admin/config/search/search-api
* Click the `Add server` button
* Provide a name, select solr back end
* Under the field set titled "Configure Solr backend", check `Standard` option for Solr Connection
* Verify the values in the standard connection fields, ensure to set the Solr core name with the value of the newly created/configured core
* Save.  If the configuration is working as expected, you should see a checkmark status for server.

### Step 4 - Configure the Apache Solr index in Drupal
* Go to search api configuration page: http://localhost:8000/admin/config/search/search-api
* CLAW vagrant does come with a default index called "Default Solr content index"
* Edit the default solr content index
* Chose the required data sources that need to be index
* Ensure to select the above configured Apache Server as the server.
* Also chose to `Index items immediately`
* Save.  If the configuration is working as expected, you should see a checkmark for status for index.
* Once you save it, it will immediately index the current content.

### Step 5 - Searching
* Go to `http://localhost:8000/search/node` to search the index content

### Step 6 - Setting up Faceted search
* To get faceted search, enable the [facets](https://www.drupal.org/project/facets ) module
* Follow the steps [here](https://www.jeffgeerling.com/blog/2017/setting-faceted-apache-solr-search-drupal-8) under the section of "Make a Faceted Solr Search View" to configure a Facet

## References
* [Drupal 8 and Solr: Google-fast search on your own website | Why and how](https://blog.openlucius.com/en/blog/drupal-8-and-solr-google-fast-search-your-own-website-why-and-how)
* [Setting up Faceted Apache Solr search in Drupal 8](https://www.jeffgeerling.com/blog/2017/setting-faceted-apache-solr-search-drupal-8)
