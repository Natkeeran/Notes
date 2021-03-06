Islandora CLAW installs the Apache Solr server (localhost:8983/solr) and the needed search related Drupal modules ([Search API](https://www.drupal.org/project/search_api), [Solr Search](https://www.drupal.org/project/search_api_solr), [Facets](https://www.drupal.org/project/facets).  The server setting can be found here: `/admin/config/search/search-api/server/default_solr_server/edit`

## Adding fields to the Solr index
Islandora CLAW also creates a default search index: `/admin/config/search/search-api/index/default_solr_index`  You can configure the fields that need to be indexed here: `/admin/config/search/search-api/index/default_solr_index/fields`.  For example, the following steps can be followed to add Subject taxonomy term to the index.

1. Go to `/admin/config/search/search-api/index/default_solr_index/fields`
2. Click Add fields.  A popup with fields will be shown.  Locate the Subject under Content.  Expand the Subject taxonomy fields by clicking on the + button.  Then click Add button besides the `Name (field_subject:entity:name)` field to add Subject taxonomy name field to the index.
3. Reindex by going to `/admin/config/search/search-api/index/default_solr_index`

## Creating and showing facets
To show and create the above created field as a facet, see the following steps:

1. Go to `/admin/config/search/facets`
2. Click the button Add facet. `admin/config/search/facets/add-facet`
3. Select the default solr index as facet source.  And the subject field added above for field.  You can modify the name to just Subject.  Click to Save.  It will take you to facet configuration page.  Example: `/admin/config/search/facets/subject/edit`
4. Select the appropriate settings.  For example check "Show the amount of results", "Sort by count"
5. Go to the blocks layout `/admin/structure/block`.  Search for the Subject facet block.  Place in a position you need.  
6. Go to the search view or page `/solr-search/content`.  Click Search.  You can will see the facet appear.  

## Additional references
* [Faceted Search in Drupal 8: Using Search API Solr and Facets](https://dev.acquia.com/blog/search-strategies-in-drupal-8/faceted-search-in-drupal-8-using-search-api-solr-and-facets/06/05/2016/10406)
* [Common Pitfalls](https://www.drupal.org/docs/7/modules/search-api/getting-started/common-pitfalls)
* [The state of Search API in Drupal8](https://drupalcamp.be/sites/default/files/slides/state%20of%20search%20%7C%20drupalcamp%20ghent.pdf)
* [Indexing content from Drupal 8 using Elasticsearch](https://www.lullabot.com/articles/indexing-content-from-drupal-8-to-elasticsearch)







