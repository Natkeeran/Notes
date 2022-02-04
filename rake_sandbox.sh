  GNU nano 4.8                                                            rake_sandbox.sh                                                                      
#!/bin/bash

PATH=$PATH:/usr/local/bin

cd /opt/isle-dc
#docker-compose down -v
yes | make clean
make local-install-profile
docker-compose exec drupal with-contenv bash -lc 'composer -n update -W'
docker-compose exec drupal with-contenv bash -lc 'drush -y updb'
cd /opt/islandora_workbench
./workbench --config create_repo_demo_objects.yml




