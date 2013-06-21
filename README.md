django-template-pages
=====================


Flat pages based on template directory structure for [django](http://djangoproject.com).


Usage
=====================

* [Install](https://github.com/iRynek/django-template-pages#installation) ``template_pages``
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


Adding context
---
* define ``TEMPLATE_PAGES_CONTEXT_MODULE`` eg.

```python
TEMPLATE_PAGES_CONTEXT_MODULE = 'apps.core.template_pages_context'
```
* create functions returing context named by Your template path:

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

So contenxt function name is created by changing relative path to template and applying:
* all ``-`` are stripped
* all ``/`` becaming ``_``


Tips And Tricks
---
* use different than ``*.html`` extension (eg. ``*.htm``) to keep base files in ``template_pages/`` structure and avoid unwanted base'ed named pages eg. ``/base/``
* to run test just add ``template_pages`` to Your ``INSTALLED_APPS`` settings and run
``` python
python manage.py tests template_pages
```


Known Issues/Limitations
---
* fill them in [here](https://github.com/iRynek/django-template-pages/issues)


Installation
---

* **pip install django-template-pages** (yup we highly recommend [virtualenv](http://www.virtualenv.org/en/latest/#what-it-does))
* or [download v1.0 package](https://github.com/iRynek/django-template-pages/archive/v1.0.zip), unzip and run:

```bash
python setup.py install
```

* or [download v1.0 package](https://github.com/iRynek/django-template-pages/archive/v1.0.zip), unzip and copy ``template_pages`` directory to Your **PYTHONPATH**
