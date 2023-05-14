from tidal_dl import (
    TIDAL_API,
    SETTINGS,
    TOKEN,
    apiKey,
    loginByConfig,
    loginByWeb,
)
from prometheus_client import make_asgi_app
import os
import sys
import logging

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:\t%(message)s")

profilePath = os.environ.get("PROFILE_PATH")
tokenPath = os.environ.get("TOKEN_PATH")

if None in (profilePath, tokenPath):
    print("Must set 'PROFILE_PATH' and 'TOKEN_PATH'")
    sys.exit(1)


SETTINGS.read(profilePath + "/.tidal-dl.json")
TOKEN.read(tokenPath + "/.tidal-dl.token.json")

api = FastAPI()

metrics_app = make_asgi_app()
api.mount("/metrics", metrics_app)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.info("Logging in ...")

if not apiKey.isItemValid(SETTINGS.apiKeyIndex):
    SETTINGS.apiKeyIndex = 4
    SETTINGS.save()
    TIDAL_API.apiKey = apiKey.getItem(SETTINGS.apiKeyIndex)
    loginByWeb()
elif not loginByConfig():
    loginByWeb()

logging.info("Successfully logged in!")
