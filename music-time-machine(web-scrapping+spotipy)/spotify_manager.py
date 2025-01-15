import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyManager:

    def __init__(self):
        self.CLIENT_ID = ""
        self.SECRET_KEY = ""
        self.USER_ID = self.fetch()

    def fetch(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID,
                                                       client_secret=self.SECRET_KEY,
                                                       redirect_uri="http://example.com",
                                                       scope="user-library-read playlist-modify-private"))
        user_id = self.sp.current_user()["id"]
        # print(user_id)
        return user_id

    def fetch_song_urls(self, song_names):
        song_urls = []
        for song in song_names:
            # Search for the song
            result = self.sp.search(q=song, type="track", limit=1)
            if result['tracks']['items']:
                # Get the URL of the first search result
                track = result['tracks']['items'][0]
                song_urls.append(track['external_urls']['spotify'])
            else:
                # Handle case where no result is found
                pass
        print(song_urls)
        return song_urls

    def create_playlist(self, name, description=""):
        # Get the current user's ID
        # user_id = self.sp.me()["id"]
        user_id = self.sp.current_user()["id"]

        # Create a playlist
        playlist = self.sp.user_playlist_create(
            user=user_id,
            name=name,
            public=False,  # Private playlist
            description=description
        )
        playlist_url = playlist["external_urls"]["spotify"]
        print(f"Playlist URL: {playlist_url}")
        return playlist["id"]

    def add_songs_to_playlist(self, playlist_id, song_urls):
        # Add tracks to the playlist
        self.sp.playlist_add_items(playlist_id, song_urls)