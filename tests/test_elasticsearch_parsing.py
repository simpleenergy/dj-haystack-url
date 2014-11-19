import pytest

import dj_haystack_url


def test_parser_for_elasticsearch_backend():
    config = dj_haystack_url.parse('elasticsearch:http://127.0.0.1:9200/haystack')
    expected = {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200',
        'INDEX_NAME': 'haystack',
    }

    assert config == expected


def test_parser_for_invalid_elasticsearch_url():
    with pytest.raises(ValueError) as err:
        dj_haystack_url.parse('elasticsearch:')

    assert str(err.value) == 'URL and INDEX_NAME are required for the elasticsearch backend'
