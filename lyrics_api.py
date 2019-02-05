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
    """ The API might pull from different sources: sometimes I received a site
        attribution in the lyrics. Checking for a snippet of the lyrics as
        opposed to whole equality is better in this case. For example, see the
        difference in the responses between 'curl_examples.png' and
        'curl_problematic.png'.

    """

    artist = "Lisa Loeb"
    title = "I Do"
    assert "when i'm done with thinking" in get_lyrics(artist, title).lower()


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

