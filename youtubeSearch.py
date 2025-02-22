# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

# To get Google's API Key from .env file
from dotenv import load_dotenv

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Loads .env variables (API Keys)
load_dotenv()
# Gets Youtube API key from .env
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

song_title = "Blackbird" + "Guitar Tutorial"

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        part="snippet",
        channelType="any",
        maxResults=1,
        q=song_title,
        order="relevance",
        safeSearch="moderate",
        type="video",
        videoCaption="any",
        videoDefinition="any",
        videoDimension="any",
        videoDuration="any",
        videoEmbeddable="true",
        videoLicense="any",
        videoPaidProductPlacement="any",
        videoSyndicated="any",
        videoType="any"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()