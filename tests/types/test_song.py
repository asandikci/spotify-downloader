from spotdl.types.song import Song
from spotdl.types.album import Album
from spotdl.utils.spotify import SpotifyClient


import pytest


def test_setup(patch_dependencies):
    """
    Sets up the tests.
    """

    SpotifyClient.init(
        client_id="5f573c9620494bae87890c0f08a60293",
        client_secret="212476d9b0f3472eaa762d90b19b0ba8",
        user_auth=False,
        no_cache=True,
    )


def test_song_init():
    """
    Test if Song class is initialized correctly.
    """

    song = Song(
        name="test",
        artists=["test"],
        album_name="test",
        album_artist="test",
        genres=["test"],
        disc_number=1,
        duration=1,
        year=1,
        date="test",
        track_number=1,
        tracks_count=1,
        isrc="test",
        song_id="test",
        cover_url="test",
        explicit=True,
        download_url="test",
        artist="test",
        copyright_text="test",
        disc_count=1,
        publisher="test",
        url="test",
    )

    assert song.name == "test"
    assert song.artists == ["test"]
    assert song.album_name == "test"
    assert song.album_artist == "test"
    assert song.genres == ["test"]
    assert song.disc_number == 1
    assert song.duration == 1
    assert song.year == 1
    assert song.date == "test"
    assert song.track_number == 1
    assert song.tracks_count == 1
    assert song.isrc == "test"
    assert song.song_id == "test"
    assert song.cover_url == "test"
    assert song.explicit == True
    assert song.download_url == "test"


def test_song_wrong_init():
    """
    Tests if Song class raises exception when initialized with wrong parameters.
    """

    with pytest.raises(TypeError):
        Song(
            name="test",
            artists=["test"],
            album_name="test",
            album_artist=1,
            genres=["test"],
            disc_number=1,
            duration=1,
            year=1,
            date="test",
        )  # type: ignore


@pytest.mark.vcr()
def test_song_from_url():
    """
    Tests if Song.from_url() works correctly.
    """

    song = Song.from_url("https://open.spotify.com/track/1t2qKa8K72IBC8yQlhD9bU")

    assert song.name == "Ropes"
    assert song.artists == ["Dirty Palm", "Chandler Jewels"]
    assert song.album_name == "Ropes"
    assert song.album_artist == "Dirty Palm"
    assert song.genres == ["gaming edm", "melbourne bounce international"]
    assert song.disc_number == 1
    assert song.duration == 188
    assert song.year == 2021
    assert song.date == "2021-10-28"
    assert song.track_number == 1
    assert song.tracks_count == 1
    assert song.isrc == "GB2LD2110301"
    assert song.song_id == "1t2qKa8K72IBC8yQlhD9bU"
    assert (
        song.cover_url
        == "https://i.scdn.co/image/ab67616d0000b273fe2cb38e4d2412dbb0e54332"
    )
    assert song.explicit == False
    assert song.download_url == None


@pytest.mark.vcr()
def test_song_from_search_term():
    """
    Tests if Song.from_search_term() works correctly.
    """

    song = Song.from_search_term("Dirty Palm - Ropes")

    assert song.name == "Ropes"
    assert song.artists == ["Dirty Palm", "Chandler Jewels"]
    assert song.album_name == "Ropes"
    assert song.album_artist == "Dirty Palm"
    assert song.genres == ["gaming edm", "melbourne bounce international"]
    assert song.disc_number == 1
    assert song.duration == 188
    assert song.year == 2021
    assert song.date == "2021-10-28"
    assert song.track_number == 1
    assert song.tracks_count == 1
    assert song.isrc == "GB2LD2110301"
    assert song.song_id == "4SN9kQlguIcjPtMNQJwD30"
    assert song.explicit == False
    assert song.download_url == None


def test_song_from_data_dump():
    """
    Tests if Song.from_data_dump() works correctly.
    """

    # Loads from str
    song = Song.from_data_dump(
        """
        {
            "name": "Ropes",
            "artists": ["Dirty Palm", "Chandler Jewels"],
            "album_name": "Ropes",
            "album_artist": "Dirty Palm",
            "genres": ["gaming edm", "melbourne bounce international"],
            "disc_number": 1,
            "duration": 188,
            "year": 2021,
            "date": "2021-10-28",
            "track_number": 1,
            "tracks_count": 1,
            "isrc": "GB2LD2110301",
            "song_id": "1t2qKa8K72IBC8yQlhD9bU",
            "cover_url": "https://i.scdn.co/image/ab67616d0000b273fe2cb38e4d2412dbb0e54332",
            "explicit": false,
            "download_url": null,
            "artist" : "Dirty Palm",
            "disc_count": 1,
            "copyright_text": "",
            "publisher": "",
            "url": "https://open.spotify.com/track/1t2qKa8K72IBC8yQlhD9bU"
        }
        """
    )

    assert song.name == "Ropes"
    assert song.artists == ["Dirty Palm", "Chandler Jewels"]
    assert song.album_name == "Ropes"
    assert song.album_artist == "Dirty Palm"
    assert song.genres == ["gaming edm", "melbourne bounce international"]
    assert song.disc_number == 1
    assert song.duration == 188
    assert song.year == 2021
    assert song.date == "2021-10-28"
    assert song.track_number == 1
    assert song.tracks_count == 1
    assert song.isrc == "GB2LD2110301"
    assert song.song_id == "1t2qKa8K72IBC8yQlhD9bU"
    assert (
        song.cover_url
        == "https://i.scdn.co/image/ab67616d0000b273fe2cb38e4d2412dbb0e54332"
    )
    assert song.explicit == False
    assert song.download_url == None


def test_song_from_data_dump_wrong_type():
    """
    Tests if Song.from_data_dump() raises exception when wrong type is passed.
    """

    with pytest.raises(TypeError):
        Song.from_data_dump(1)  # type: ignore


def test_song_from_dict():
    """
    Tests if Song.from_dict() works correctly.
    """

    song = Song.from_dict(
        {
            "name": "Ropes",
            "artists": ["Dirty Palm", "Chandler Jewels"],
            "album_name": "Ropes",
            "album_artist": "Dirty Palm",
            "genres": ["gaming edm", "melbourne bounce international"],
            "disc_number": 1,
            "duration": 188,
            "year": 2021,
            "date": "2021-10-28",
            "track_number": 1,
            "tracks_count": 1,
            "isrc": "GB2LD2110301",
            "song_id": "1t2qKa8K72IBC8yQlhD9bU",
            "cover_url": "https://i.scdn.co/image/ab67616d0000b273fe2cb38e4d2412dbb0e54332",
            "explicit": False,
            "download_url": None,
            "artist": "Dirty Palm",
            "disc_count": 1,
            "copyright_text": "",
            "publisher": "",
            "url": "https://open.spotify.com/track/1t2qKa8K72IBC8yQlhD9bU",
            "song_list": {
                "name": "test",
                "url": "https://open.spotify.com/album/fakealbum",
                "urls": ["https://open.spotify.com/track/1t2qKa8K72IBC8yQlhD9bU"],
                "songs": [],
                "artist": {
                    "external_urls": {"spotify": ""},
                    "href": "",
                    "id": "",
                    "name": "",
                    "type": "",
                    "uri": "",
                },
            },
        }
    )

    assert song.song_list is not None
    assert isinstance(song.song_list, Album)
    assert song.name == "Ropes"
    assert song.artists == ["Dirty Palm", "Chandler Jewels"]
    assert song.album_name == "Ropes"
    assert song.album_artist == "Dirty Palm"
    assert song.genres == ["gaming edm", "melbourne bounce international"]
    assert song.disc_number == 1
    assert song.duration == 188
    assert song.year == 2021
    assert song.date == "2021-10-28"
    assert song.track_number == 1
    assert song.tracks_count == 1
    assert song.isrc == "GB2LD2110301"
    assert song.song_id == "1t2qKa8K72IBC8yQlhD9bU"
    assert (
        song.cover_url
        == "https://i.scdn.co/image/ab67616d0000b273fe2cb38e4d2412dbb0e54332"
    )
    assert song.explicit == False
