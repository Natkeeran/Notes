## Get all books

```
select ?s from <#ri> where {
?s <fedora-rels-ext:isMemberOfCollection> <info:fedora/islandora:bookCollection>
}
```


## Get all pages in a book
```
select ?object from <#ri> where {
?object <http://islandora.ca/ontology/relsext#isPageOf> <info:fedora/islandora:18> 
}
```
