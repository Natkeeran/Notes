Though claw-playbook aims to be deployable to multiple machines out of the box, there is still work to be done to fully implement that. This guide describes a two machine deployment process of CLAW. 

* machine_1 - Drupal (Front End)
* machine_2 - Everything Else (Back End: Crayfish, Tomcat: Fedora, Blazegraph, Solr)


## Configuration
### Fedora Root URL
One possible way to separate the fedora entries for a site or collection is to configure a unique fedora root resource.  Create that resource under root in Fedora and configure the crayfish configuration to point to it.

https://github.com/Islandora-Devops/claw-playbook/blob/master/inventory/vagrant/group_vars/crayfish.yml

```
crayfish_gemini_fedora_base_url: http://localhost:8080/fcrepo/rest/dragomans
crayfish_houdini_fedora_base_url: http://localhost:8080/fcrepo/rest/dragomans
crayfish_hypercube_fedora_base_url: http://localhost:8080/fcrepo/rest/dragomans
crayfish_milliner_fedora_base_url: http://localhost:8080/fcrepo/rest/dragomans
```

### Triplestore namespace
You may also want to separate the triplestore entries by site or collection.  There does not exist a recommended way to do this now.  You would have to modify the https://github.com/Islandora-Devops/ansible-role-blazegraph role to do this.

The namespace gets defined here: https://github.com/Islandora-Devops/ansible-role-blazegraph/blob/master/files/blazegraph.properties#L6 and https://github.com/Islandora-Devops/ansible-role-blazegraph/blob/master/tasks/namespace.yml#L33

In addition, the karaf configuration need to be updated to point to this namespace:
```
---

alpaca_settings:
  - pid: ca.islandora.alpaca.connector.broadcast
    settings:
      input.stream: activemq:queue:islandora-connector-broadcast
  - pid: ca.islandora.alpaca.indexing.triplestore
    settings:
      error.maxRedeliveries: 10
      input.stream: activemq:queue:islandora-indexing-triplestore
      triplestore.baseUrl: http://localhost:8080/bigdata/namespace/dragomans/sparql
  - pid: ca.islandora.alpaca.indexing.fcrepo
    settings:
      error.maxRedeliveries: 10
      content.stream: activemq:queue:islandora-indexing-fcrepo-content
      file.stream: activemq:queue:islandora-indexing-fcrepo-file
      media.stream: activemq:queue:islandora-indexing-fcrepo-media
      delete.stream: activemq:queue:islandora-indexing-fcrepo-delete
      milliner.baseUrl: http://dragomans.dsu.utsc.utoronto.ca/milliner/

apix_config:
  - pid: org.fcrepo.apix.registry.http
    settings:
      timeout.socket.ms: 1000
  - pid: org.fcrepo.camel.indexing.triplestore
    settings:
      input.stream: activemq:topic:fedora
      triplestore.reindex.stream: activemq:queue:triplestore.reindex
      triplestore.baseUrl: http://localhost:8080/bigdata/namespace/dragomans/sparql
```


## Deployment 
* Deploy CLAW-PLaybook on machine_2
* Copy the `/var/www/html/drupal` to machine_1

* Create private/public key in `/opt/islandora/auth` in machine_1
* Replace the public key in machine_2 with the public key from machine_1 in the following places: crayfish, tomcat

* In machine_2, open the tcp connection port
* Update the activemq tcp connection



