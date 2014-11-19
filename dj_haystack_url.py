import os


SUPPORTED_ENGINES = (
    'simple',
    'whoosh',
    'xapian',
    'elasticsearch',
    'solr',
)

BACKEND_MAPPING = {
    'simple': 'haystack.backends.simple_backend.SimpleEngine',
    'whoosh': 'haystack.backends.whoosh_backend.WhooshEngine',
    'elasticsearch': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    'solr': 'haystack.backends.solr_backend.SolrEngine',
    'xapian': 'xapian_backend.XapianEngine',
}


def parse(connection_uri, **extra_config):
    engine_name, _, right = connection_uri.partition(':')
    if engine_name not in SUPPORTED_ENGINES:
        raise ValueError(
            "Unsupported Haystack Backend `{0}`.  Must be one of {1}".format(
                engine_name, SUPPORTED_ENGINES,
            ),
        )

    conf = {'ENGINE': BACKEND_MAPPING[engine_name]}

    if engine_name in ('whoosh', 'xapian'):
        path = os.path.expanduser(right)
        if not path:
            raise ValueError(
                'PATH value cannot be empty for the {0} backend'.format(engine_name)
            )
        conf['PATH'] = os.path.expanduser(right)
    elif engine_name == 'solr':
        if not right:
            raise ValueError(
                'URL value cannot be empty for the the solr backend'
            )
        conf['URL'] = right
    elif engine_name == 'elasticsearch':
        url, _, index_name = right.rpartition('/')
        if not url or not index_name:
            raise ValueError(
                'URL and INDEX_NAME are required for the elasticsearch backend'
            )
        conf['URL'] = url
        conf['INDEX_NAME'] = index_name
    elif engine_name == 'simple':
        pass
    else:
        assert False, "This should be impossible"

    conf.update(extra_config)
    return conf


DEFAULT_ENV = 'HAYSTACK_CONNECTION_URL'


def config(env=DEFAULT_ENV, default=None):
    if env not in os.environ:
        raise KeyError('Missing environment variable {0}'.format(env))

    connection_url = os.environ[env]
    return parse(connection_url)
