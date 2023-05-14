from fastapi import BackgroundTasks
from tidal_dl import (
    TIDAL_API,
    Type,
    SETTINGS,
    downloadVideos,
    downloadCover,
    downloadTracks,
    downloadAlbumInfo,
    Artist,
)
from prometheus_client import Histogram
import logging


from . import api

REQUEST_TIME = Histogram("request_processing_seconds", "Time spent processing request")
DOWNLOAD_TIME = Histogram("download_processing_seconds", "Time spent downloading")


def do_download(artistID: str):
    logging.debug(f"Downloading {id}")
    with DOWNLOAD_TIME.time():
        albums = TIDAL_API.getArtistAlbums(artistID, SETTINGS.includeEP)
        for album in albums:
            tracks, videos = TIDAL_API.getItems(album.id, Type.Album)
            if SETTINGS.saveAlbumInfo:
                downloadAlbumInfo(album, tracks)
            if SETTINGS.saveCovers and album.cover is not None:
                downloadCover(album)
            downloadTracks(tracks, album)
            downloadVideos(videos, album)


@api.get("/search/{item}")
def search(item: str):
    with REQUEST_TIME.time():
        logging.debug(f"Searching for {item}")
        response = TIDAL_API.search(item, Type.Null)
        return TIDAL_API.getSearchResultItems(response, Type.Artist)


@api.post("/download/{artistID}", response_model=dict[str, str])
def download(artistID: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(do_download, artistID)
    return {"message": "Added to download queue"}
