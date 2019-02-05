# Py3
# requires pytest -- pip install -U pytest
# requires requests -- pip install -U requests

import requests

def get_lyrics(artist, title):
    """ Returns lyrics string for specified artist-title pair. """

    artist, title = str(artist), str(title)

    url = "https://api.lyrics.ovh/v1"
    route = "/"

    response = requests.get(f"{url}{route}{artist}/{title}").json()

    if is_err(response):
        print(response['error'])
        return None

    return response['lyrics']


def is_err(response):
    err = response.get("error")
    return True if err else False


def test_should_return_lyrics_for_known_good():
    artist = "Lisa Loeb"
    title = "I Do"
    assert "When I'm done with" in get_lyrics(artist, title)


def test_should_return_error_for_known_bad():
    artist = "noartist"
    title = "notitle"
    assert get_lyrics(artist, title) == None


def test_should_return_none_for_bad_input():
    """ get_lyrics doesn't know what is a valid artist or title, so it should
        stringify the user input just in case and send it to the API.

    """

    artist = [3,2,5]
    title = "I Do"
    assert get_lyrics(artist, title) == None

