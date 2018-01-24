Though claw-playbook aims to be deployable to multiple machines, there is still work to be done to fully implement that. This guide describes a two machine deployment process of CLAW. 

* machine_1 - Drupal (Front End)
* machine_2 - Everything Else (Back End: Crayfish, Tomcat: Fedora, Blazegraph, Solr)


## Configuration
* Fedora root url
* Triplestore namespace

## Deployment 
* Deploy CLAW-PLaybook on machine_2
* Copy the `/var/www/html/drupal` to machine_1

* Create private/public key in `/opt/islandora/auth` in machine_1
* Replace the public key in machine_2 with the public key from machine_1 in the following places: crayfish, tomcat

* In machine_2, open the tcp connection port
* Update the activemq tcp connection



