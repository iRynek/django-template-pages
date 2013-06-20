django-template-pages
=====================


Flat pages based on template directory structure for [django](http://djangoproject.com).


Basic usage
-----------

* In your main template directory create ``template_pages`` folder, it will be your root template_pages directory
* Connect ``urls.py``

```python
urlpatterns = patterns('',
    # all others urls, template_pages.urls is last one to try!
    url(ur'', include('template_pages.urls')),
)
```

* Create pages adding properly named files and folders in your ``template_pages`` template direcory, eg:

```bash
- template_pages/       #  available at:
-- index.html           #  http://localhost/
-- nice-huh.html        #  http://localhost/nice-huh/
-- nice/
--- huh.html            #  http://localhost/nice/huh/
--- index.html          #  http://localhost/nice/
```


Installation
-----------
to do

Tricks
-----------
* use different than *.html extension (eg. *.htm) to keep base files in template_pages structure and avoid unwanted base pages

Known Issues/Limitations
-----------
* there is no DRY way of defining language specific URL to the same page:

```bash
http://example.com/im-a-genious/       # English
http://example.com/jestem-geniuszem/   # Polish
```

