* Give me the triples of a particular resource
```
select ?p ?o WHERE { 
    <http://dragomans.digitalscholarship.utsc.utoronto.ca/node/5639?_format=jsonld> ?p ?o. 
}
```

* Get all resources of a particular type

```
prefix schema: <http://schema.org/>

SELECT ?subject
WHERE {
   ?subject rdf:type schema:DigitalDocument.
} 
```
