
* In the README, the example solr instance url is given as  `http://10.0.2.2:9080/solr`.  What worked was pointing to the islandora core of the solr instance, example: `http://serverip:8080/solr/islandora`

* The particular source Islandora 7.x did not have the [datastream_info_to_solr.xslt](https://github.com/discoverygarden/islandora_transforms/blob/fdeac90196431504a83568869356c0bd46962600/datastream_info_to_solr.xslt#L9) enabled.  Needed to enable it and reindex the objects in solr to have the fedora_datastreams_ms solr fields required by migrate_7x_claw.

* There can be security or authorization issues connecting from target CLAW machine to source Islandora 7.x machine.  One way to test this is to go to the CLAW machine and run a curl call as below:
```
 curl -I http://fedoraAdmin:fedoraPwd@fedoraServer:8080/fedora/objects/objectPid/objectXML
 ```
 If you get a 201 response, you should be good. Else, resolve the security or authorization issue first.  

* migrate_7x_claw depends on jonathangee's tuque 2.0.  Thus, it needs to be added via composer.  To do that, clone/copy the migrate_7x_claw into another location in the vagrant box.  From `/var/www/html/drupal`, run

```
composer config repositories.local path "/path/to/migrate_7x_claw"
composer require islandora/migrate_7x_claw
```

* If your target collection is not already available, it may not be imported into the field!
