## Get all books

```
select ?s from <#ri> where {
?s <fedora-rels-ext:isMemberOfCollection> <info:fedora/islandora:bookCollection>
}
```
