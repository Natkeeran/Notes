* ![alt text](CLAW_Data_Flow.jpeg)

CLAW derivative data flow is similar to the the data flow for creating and indexing a repository item.  

When user creates a media, if a derivative action is configured via context, Drupal will fire an event and put a message in the ActiveMQ.  

Alpaca connectors will pick that message and call the micro services.  

Micro services will process the request and create Drupal objects, which in turn can fire off events to index media metadata into Fedora and Triplestore.


## How to add a derivative service
* Create a micro service
* Create a connector in Alpaca
* Create the action and context needed to trigger the derivative workflow
