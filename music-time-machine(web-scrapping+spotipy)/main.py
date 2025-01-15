from billboard_manager import BillboardManager
from spotify_manager import SpotifyManager

time_point = input("Which year you would like to travel to in YYY-MM-DD: ")
print(time_point)

billboard_manager = BillboardManager()
songs_list = billboard_manager.fetch_100_list(time_point)
spotify_manager = SpotifyManager()
songs_urls = spotify_manager.fetch_song_urls(songs_list)
playlist_id = spotify_manager.create_playlist(time_point, f"The best songs of {time_point}")
spotify_manager.add_songs_to_playlist(playlist_id, songs_urls)