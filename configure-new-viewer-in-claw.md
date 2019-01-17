Currently four media types (audio, file, image, video) are supported in CLAW.  Additional viewers can be configured for these media types from the Drupal UI.  

* Install and make available the viewer for the media type. For instance, if you add a viewer for file, it should be available in `/admin/structure/media/manage/file/display`.

* Add a viwer term to the taxonomy: `/admin/structure/taxonomy/manage/islandora_display/overview`.  (Programmatically here: `https://github.com/Islandora-CLAW/islandora/blob/8.x-1.x/modules/islandora_demo_feature/migrate/tags.csv`)

* Add new content and media display modes for the viewer: `/admin/structure/display-modes`.  (ex: `core.entity_view_mode.media.pdfjs.yml` and `core.entity_view_mode.node.pdfjs.yml`)

* Go to media manage display `/admin/structure/media/manage/file/display` and configure the new mode (ex: `core.entity_view_display.media.file.pdfjs.yml`)

* We need to create a [EVA](https://www.drupal.org/project/eva) view to get the media displayed in the content.  Got to `/admin/structure/views` and copy an existing EVA such as `OpenSeadragon Media EVAs`, change the `title`, `Format/Show` and ` Machine Name`. (ex: `views.view.pdfjs_media_evas.yml`)

* Go to content manage display `/admin/structure/types/manage/islandora_object/display/` and configure the new mode. Specify the EVA you want to display to the user. (ex: `core.entity_view_display.node.islandora_object.pdfjs.yml`)

* Add a new context in `/admin/structure/context` with condition `Node has term` and reaction `Change view mode`, and select the content view mode that was added in the above step.  (ex: `context.context.pdfjs.yml`)


