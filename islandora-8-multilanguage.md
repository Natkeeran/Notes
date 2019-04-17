Drupal 8 has good support for developing multilingual sites. In this guide, we will describe the steps needed to setup a basic multilingual Islandora 8 site.  The site 

Drupal 8 comes with several [multilingual modules](https://www.drupal.org/docs/8/multilingual/choosing-and-installing-multilingual-modules) in the core. Islandora 8 enables Language and Content Translation modules by default.

## Adding Languages
From the top menu, go to Configuration >> Regional and language >> Languages (`http://localhost:8000/admin/config/regional/language`). Add a language. You can place the default language selector block to switch between languages.To create the language switcher block go to Structure >> Block layout. Click Place block in a region of your choice.  Search for `Language switcher` block and click `Place block`.

## Adding Multilingual Menu
From the top menu, go to Configuration >> Regional and language >> Content language and translation. Check `Custom menu link` under `Custom language settings`. Scroll down to `Custom menu link` section and check all the relevant fields and Save the configurations. Clear the cache.  

From the top menu, go to Structure >> Menu. Edit "Main navigation" menu. Default home menu item cannot be translated due to [this issue](https://www.drupal.org/project/drupal/issues/2838106). Disable that menu item. Click `Add link` to create a new menu item. Provide a menu title (i.e Home) and input `<front>` for the link field. Save. Right click on the Operations beside the new menu link and click the Translate button. Translate the menu link title for the language added above and save.

Go back to home.  The language switcher will enable you to switch the language/content of the menu and content.

## Adding a Multilingual Repository Item

