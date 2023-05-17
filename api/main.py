from fastapi import BackgroundTasks, Response, status
from fastapi.encoders import jsonable_encoder
from tidal_dl import (
    TIDAL_API,
    Type,
    SETTINGS,
    downloadVideos,
    downloadCover,
    downloadTracks,
    downloadAlbumInfo,
    Settings,
)
from prometheus_client import Histogram, Counter
from pydantic import BaseModel
import aigpy
import logging
import tempfile


from . import api, getProfilePath

REQUEST_TIME = Histogram("request_processing_seconds", "Time spent processing request")
DOWNLOAD_TIME = Histogram("download_processing_seconds", "Time spent downloading")

ALBUMS_DOWNLOADED = Counter("albums_downloaded", "Number of albums downloaded")
TRACKS_DOWNLOADED = Counter("tracks_downloaded", "Number of tracks downloaded")


def do_download(artistID: str):
    logging.debug(f"Downloading {id}")
    SETTINGS.read(getProfilePath())

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
            for _ in tracks:
                TRACKS_DOWNLOADED.inc()
            ALBUMS_DOWNLOADED.inc()


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


@api.get("/settings")
def settings():
    SETTINGS.read(getProfilePath())
    data = aigpy.model.modelToDict(SETTINGS)
    data["audioQuality"] = SETTINGS.audioQuality.name
    data["videoQuality"] = SETTINGS.videoQuality.name
    return jsonable_encoder(data)


class SettingsModel(BaseModel):
    albumFolderFormat: str
    apiKeyIndex: int
    audioQuality: str
    checkExist: bool
    downloadDelay: bool
    downloadPath: str
    includeEP: bool
    language: int
    lyricFile: bool
    multiThread: bool
    playlistFolderFormat: str
    saveAlbumInfo: bool
    saveCovers: bool
    showProgress: bool
    showTrackInfo: bool
    trackFileFormat: str
    usePlaylistFolder: bool
    videoFileFormat: str
    videoQuality: str


@api.post("/settings")
def set_settings(settings: SettingsModel, response: Response):
    import json

    with tempfile.TemporaryFile("w") as fp:
        fp.write(f"{jsonable_encoder(settings)}")

        try:
            tempSettings = Settings()
            tempSettings.read(fp.name)
        except Exception as e:
            logging.error(e)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"success": False}

    with open(getProfilePath(), "w") as f:
        json.dump(jsonable_encoder(settings), f)
        SETTINGS.read(getProfilePath())
        SETTINGS.save()

    return {"success": True}
