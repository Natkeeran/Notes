* User creates a node in Drupal.

* Drupal Rules get executed (`islandora/src/Plugin/RulesAction/Broadcaster.php`) and a create event message gets posted to to the `islandora-indexing-fcrepo-create queue` in the ActiveMQ.  Sample Message:
```
IslandoraBroadcastRecipients:activemq\cqueue\cislandora-indexing-fcrepo-create,activemq\cqueue\cislandora-indexing-triplestore Authorization:Bearer Authorization Token @"@context":"https:\/\/www.w3.org\/ns\/activitystreams","type":"Create","actor":{"type":"Person","id":"http:\/\/dsu-beta.utsc.utoronto.ca:8000\/user\/1","object":"http:\/\/dsu-beta.utsc.utoronto.ca:8000\/node\/49"}
```

* Alpaca is a subscriber to this queue.  Islandora-indexing-fcrepo-create queue is mapped to create.rdf.input.stream queue in Alpaca.  In FcrepoIndexer.java, Alpaca preforms some processing and 
