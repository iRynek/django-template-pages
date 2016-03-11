django-template-pages
=====================

Flat pages based on template directory structure for [django](http://djangoproject.com).


Installation
---

* via [virtualenv](http://www.virtualenv.org/en/latest/#what-it-does) - yup we highly recommend it!

```bash
pip install django-template-pages
```

Usage
=====================

* [Install](https://github.com/iRynek/django-template-pages#installation) ``template_pages``
* In your main template directory create ``template_pages`` folder, it will be your root template_pages directory
* Connect ``urls.py``, 

```python
urlpatterns = [
    url(ur'any-other', YourFancyClass.as_view()),
    # all others urls above - template_pages.urls last one to try!
    url(ur'', include('template_pages.urls')),
]
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


Adding context
---
* define ``TEMPLATE_PAGES_CONTEXT_MODULE`` eg.

```python
TEMPLATE_PAGES_CONTEXT_MODULE = 'apps.core.template_pages_context'
```
* create functions returning context named tweaked template path in ``TEMPLATE_PAGES_CONTEXT_MODULE``:

```python
    # context for http://localhost/ vel  template_pages/index.html
    def index(request)
        return {'foo' : 'bar'}

    # context for http://localhost/nice-huh/ vel  template_pages/nice-huh.html
    def nicehuh(request)
        return {'foo' : 'bar'}

    # context for http://localhost/nice/huh/ vel  template_pages/nice/huh.html
    def nice_huh(request)
        return {'foo' : 'bar'}

    # context for http://localhost/nice/ vel  template_pages/nice/index.html
    def nice(request)
        return {'foo' : 'bar'}
```
So context function name is created by changing relative path to template and applying:
* all ``-`` are stripped
* all ``/`` became ``_``


Tips And Tricks
---
* use different than ``*.html`` extension (eg. ``*.htm``) to keep base files in ``template_pages/`` structure and avoid unwanted base'ed named pages eg. ``/base/``
* to run test just ``cd tests/test_project`` and run

```bash
./manage.py tests
```

Known Issues/Limitations
---
* fill them in [here](https://github.com/iRynek/django-template-pages/issues)

Changelog
---
1.0.2
* support for django 1.9+
1.0.1
* do not supress ``TemplateDoesNotExists`` errors while on ``DEBUG = True``
* do not supress ``TemplateDoesNotExists`` errors if they are raised by other stuff (eg. {% include %} template tag)
