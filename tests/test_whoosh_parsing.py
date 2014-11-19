import pytest
import os
import dj_haystack_url


def test_parser_for_whoosh_backend_with_relative_path():
    config = dj_haystack_url.parse('whoosh:relative/path/to/whoosh_index')
    expected = {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': 'relative/path/to/whoosh_index',
    }

    assert config == expected


def test_parser_for_whoosh_backend_with_absolute_path():
    config = dj_haystack_url.parse('whoosh:/absolute/path/to/whoosh_index')
    expected = {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': '/absolute/path/to/whoosh_index',
    }

    assert config == expected


def test_parser_for_whoosh_backend_with_user_home_in_path():
    config = dj_haystack_url.parse('whoosh:~/path/under/home/dir')
    home_dir = os.path.expanduser('~')
    expected = {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(home_dir, 'path/under/home/dir'),
    }

    assert config == expected


def test_parser_for_invalid_solr_url():
    with pytest.raises(ValueError) as err:
        dj_haystack_url.parse('whoosh:')

    assert str(err.value) == 'PATH value cannot be empty for the whoosh backend'
