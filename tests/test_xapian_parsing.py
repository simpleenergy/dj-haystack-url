import pytest
import os
import dj_haystack_url


def test_parser_for_xapian_backend_with_relative_path():
    config = dj_haystack_url.parse('xapian:relative/path/to/xapian_index')
    expected = {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': 'relative/path/to/xapian_index',
    }

    assert config == expected


def test_parser_for_xapian_backend_with_absolute_path():
    config = dj_haystack_url.parse('xapian:/absolute/path/to/xapian_index')
    expected = {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': '/absolute/path/to/xapian_index',
    }

    assert config == expected


def test_parser_for_xapian_backend_with_user_home_in_path():
    config = dj_haystack_url.parse('xapian:~/path/under/home/dir')
    home_dir = os.path.expanduser('~')
    expected = {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': os.path.join(home_dir, 'path/under/home/dir'),
    }

    assert config == expected


def test_parser_for_invalid_solr_url():
    with pytest.raises(ValueError) as err:
        dj_haystack_url.parse('xapian:')

    assert str(err.value) == 'PATH value cannot be empty for the xapian backend'
