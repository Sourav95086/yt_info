from fastapi import FastAPI
from yt_dlp import YoutubeDL

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Backend Running"
    }


@app.get("/video")
def get_video(url: str):

    ydl_opts = {

        # best playable mp4 stream
        "format": "best[ext=mp4]",

        # ignore playlists
        "noplaylist": True,

        # cleaner logs
        "quiet": True,

        # behave like android client
        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        },

        # fake browser headers
        "http_headers": {
            "User-Agent":
                "Mozilla/5.0"
        }
    }

    try:

        with YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )

            return {

                "success": True,

                "title":
                    info.get("title"),

                "description":
                    info.get("description"),

                "thumbnail":
                    info.get("thumbnail"),

                "views":
                    info.get("view_count"),

                "likes":
                    info.get("like_count"),

                "channel":
                    info.get("channel"),

                "channel_url":
                    info.get("channel_url"),

                "duration":
                    info.get("duration"),

                "upload_date":
                    info.get("upload_date"),

                "video_url":
                    info.get("url")
            }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)
        }