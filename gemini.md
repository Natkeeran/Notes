## How to look up a Gemini entry for a node?
To locate a particular Gemini entry for a node, you need to know the uuid of the node. You can get the uuid for the node by looking at the devel tab in Drupal or you can get it from json representation: `http://localhost:8000/node/2?_format=json`.  You can look it up via Gemini service via curl or using REST client such as POSTman. 

```
curl -H "Authorization:Bearer islandora" http://localhost:8000/gemini/1dab4f15-cad6-45f5-a47e-49ddf26b3279
```

Note that you can look up media and files in Drupal using the above method as well.

## How to look up a file in Fedora?
