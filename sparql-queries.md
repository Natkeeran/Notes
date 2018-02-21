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

* Get subject by title
```
prefix dcterms: <http://purl.org/dc/terms/>

SELECT ?s
WHERE {
  ?s dcterms:title  "Test123".
}
```

* Get all the honorifics
```
prefix dbpedia: <http://dbpedia.org/ontology/>
prefix dragomans: <https://github.com/digitalutsc/dragomans_ontology/>

SELECT ?s ?o
WHERE {
  ?s dragomans:honorificPrefix  ?o
}
```
