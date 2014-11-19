import dj_haystack_url


def test_parser_for_simple_backend():
    config = dj_haystack_url.parse('simple')
    expected = {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    }

    assert config == expected
