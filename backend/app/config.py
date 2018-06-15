from os import environ


REDIS_URL = environ.get("REDIS_URL")
API_KEY = environ.get("API_KEY")
DEBUG = environ.get("DEBUG")
ACTIVE_ENVIRONMENTS = [
    "production",
    "puppystream",
    "doghouse",
    "puptownfunk",
    "dogsonscreek",
    "testminster",
    "barksandrec",
]
