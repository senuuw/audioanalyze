import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_credentials():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

        with open("token.json", "w") as token:
            token.write(creds.to_json())
        return creds

    flow = InstalledAppFlow.from_client_secrets_file("client_secret_1.json", scopes)
    creds = flow.run_local_server(port=0)

    # Save token.json so future runs don't need the browser
    with open("token.json", "w") as token:
        token.write(creds.to_json())

    return creds

def check_latest_video():

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_1.json"

    # Get credentials and create an API client
    credentials = get_credentials()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    playlist_id_request = youtube.channels().list(
        part="contentDetails",
        id="UCiFOL6V9KbvxfXvzdFSsqCw"
    )
    response = playlist_id_request.execute()
    playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    latest_vid_request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=1,
        playlistId=playlist_id
    )

    latest_vid_request = latest_vid_request.execute()
    video_id = latest_vid_request['items'][0]['contentDetails']['videoId']


if __name__ == "__main__":
    check_latest_video()