//bot que diga que musica se esta reproduciendo en spotify o youtube

import requests
import json
# Create a new Twitch client.
client = requests.Session()
# Set the client's user agent.
client.headers["User-Agent"] = "Twitch Bot"
# Get the Twitch API base URL.
base_url = "https://api.twitch.tv/kraken/"
# Get the current song that is playing on Spotify.
spotify_response = client.get(
    "https://api.spotify.com/v1/me/player/currently-playing"
)
spotify_data = spotify_response.json()
# Get the current song that is playing on YouTube.
youtube_response = client.get(
    "https://www.googleapis.com/youtube/v3/search?part=snippet&q=now+playing&type=video&maxResults=1"
)
youtube_data = youtube_response.json()
# Get the title of the current song.
if spotify_data["is_playing"]:
    song_title = spotify_data["item"]["name"]
else:
    song_title = youtube_data["items"][0]["snippet"]["title"]
# Send a message to the chat with the current song title.
client.post(
    base_url + "chat/channel/{}/messages".format(CHANNEL_ID),
    data={
        "message": song_title,
    },
)