import pytest

from spotdl.providers.audio import YouTubeMusic
from spotdl.types.song import Song


@pytest.mark.vcr()
def test_ytm_search():
    provider = YouTubeMusic()

    assert provider.search(
        Song.from_dict(
            {
                "name": "Nobody Else",
                "artists": ["Abstrakt"],
                "artist": "Abstrakt",
                "album_name": "Nobody Else",
                "album_artist": "Abstrakt",
                "genres": [],
                "disc_number": 1,
                "disc_count": 1,
                "duration": 162.406,
                "year": 2022,
                "date": "2022-03-17",
                "track_number": 1,
                "tracks_count": 1,
                "isrc": "GB2LD2210007",
                "song_id": "0kx3ml8bdAYrQtcIwvkhp8",
                "cover_url": "https://i.scdn.co/image/ab67616d0000b27345f5ba253b9825efc88bc236",
                "explicit": False,
                "publisher": "NCS",
                "url": "https://open.spotify.com/track/0kx3ml8bdAYrQtcIwvkhp8",
                "copyright_text": "2022 NCS",
                "download_url": None,
                "song_list": None,
            }
        )
    ) in [
        "https://music.youtube.com/watch?v=nfyk-V5CoIE",
        "https://music.youtube.com/watch?v=bNXMlIogpXc",
    ]


@pytest.mark.vcr()
def test_ytm_get_results():
    provider = YouTubeMusic()

    results = provider.get_results("Lost Identities Moments")

    assert len(results) > 5
