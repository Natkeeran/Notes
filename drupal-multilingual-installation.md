
## Enable the following modules:
* Language
* Content Translation 
* Configuration Translation (If fields need to be translated)
* Interface Translation 

## Adding Languages
* Go to 'config/regional/language'
* Add Language
* You can place the default language selector block or use the [lang_dropdown](https://www.drupal.org/project/lang_dropdown) module

## Translating Content
* Go to `/admin/config/regional/content-language`
* Enable the content type and fields that can be translated

## Translating Menus
* Go to `/admin/config/regional/content-language`
* Enable `Custom menu link`
* Go to `/admin/structure/menu/manage/main`
* Add Translation to the menu
* Go to a translation of a page and provide the url and title of the translated menu

## Translating Fields

## References
* https://www.slideshare.net/AcquiaInc/multilingual-improvements-for-drupal-8
* https://www.drupal.org/docs/8/multilingual/choosing-and-installing-multilingual-modules
* https://www.drupal.org/project/drupal/issues/2599228
