* Give me the triples of a particular resource
```
select ?p ?o WHERE { 
    <http://dragomans.digitalscholarship.utsc.utoronto.ca/node/5639?_format=jsonld> ?p ?o. 
}
```

* Get all resources of a type

```
prefix schema: <http://schema.org/>

SELECT ?subject
WHERE {
   ?subject rdf:type schema:DigitalDocument.
} 
```

* Count the number of entries of a type
```
prefix schema: <http://schema.org/>


SELECT (COUNT(?subject) AS ?no_subject)
WHERE {
  ?subject rdf:type schema:DigitalDocument.
}
```
