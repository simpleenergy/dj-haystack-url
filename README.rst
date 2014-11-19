===============================
Django Haystack URL
===============================

.. image:: https://badge.fury.io/py/dj-haystack-url.png
    :target: http://badge.fury.io/py/dj-haystack-url

.. image:: https://travis-ci.org/simpleenergy/dj-haystack-url.png?branch=master
        :target: https://travis-ci.org/simpleenergy/dj-haystack-url

.. image:: https://pypip.in/d/dj-haystack-url/badge.png
        :target: https://pypi.python.org/pypi/dj-haystack-url


Haystack configuration from environment variable

* Free software: MIT license

Supported Backends
------------------

Support currently exists for Simple, Whoosh, Elasticsearch, Solr, and Xapian
backends.

Installation
------------

Installation is simple::

    $ pip install dj-haystack-url

Usage
-----

Configure your Haystack connections in ``settings.py`` from
``HAYSTACK_CONNECTIONS`` (``default`` is optional)::

    HAYSTACK_CONNECTIONS = {'default': dj_haystack_url.config(default='simple')}

Parse an arbitrary Haystack connection URL::

    HAYSTACK_CONNECTIONS = {'default': dj_haystack_url.parse('simple')}

URL schema
----------

+---------------+-----------------------------------------------------------------------+----------------------------------+
| Engine        | Haystack Backend                                                      | URL                              |
+===============+=======================================================================+==================================+
| Simple        | ``haystack.backends.simple_backend.SimpleEngine``                     | ``simple``                       |
+---------------+-----------------------------------------------------------------------+----------------------------------+
| Whoosh        | ``haystack.backends.whoosh_backend.WhooshEngine``                     | ``whoosh:PATH`` [1]_             |
+---------------+-----------------------------------------------------------------------+----------------------------------+
| Elasticsearch | ``haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine`` | ``elasticsearch:URL/INDEX_NAME`` |
+---------------+-----------------------------------------------------------------------+----------------------------------+
| Solr          | ``haystack.backends.solr_backend.SolrEngine``                         | ``solr:URL``                     |
+---------------+-----------------------------------------------------------------------+----------------------------------+
| Xapian        | ``xapian_backend.XapianEngine``                                       | ``xapian:PATH`` [1]_             |
+---------------+-----------------------------------------------------------------------+----------------------------------+

.. [1] Whoosh and Xapian connect to an index on the file system. The same URL
       format is used, omitting the hostname, and using the "file" portion as the file
       path to the index.
