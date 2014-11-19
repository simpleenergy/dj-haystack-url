import pytest

import dj_haystack_url


def test_parser_for_solr_backend():
    config = dj_haystack_url.parse('solr:http://127.0.0.1:8983/solr')
    expected = {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
    }

    assert config == expected


def test_parser_for_solr_backend_with_specified_index():
    config = dj_haystack_url.parse('solr:http://127.0.0.1:8983/solr/foo')
    expected = {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/foo',
    }

    assert config == expected


def test_parser_for_invalid_solr_url():
    with pytest.raises(ValueError) as err:
        dj_haystack_url.parse('solr:')

    assert str(err.value) == 'URL value cannot be empty for the the solr backend'
