import pytest

import dj_haystack_url


def test_config_function(monkeypatch):
    monkeypatch.setenv('HAYSTACK_CONNECTION_URL', 'simple')

    actual = dj_haystack_url.config()
    expected = {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    }

    assert actual == expected


def test_config_function_for_missing_environment_variable(monkeypatch):
    monkeypatch.delenv('HAYSTACK_CONNECTION_URL', raising=False)

    with pytest.raises(KeyError) as err:
        dj_haystack_url.config()

    expected = 'Missing environment variable HAYSTACK_CONNECTION_URL'
    actual = str(err.value)
    assert expected in actual
