import os
import logging

from dotenv import load_dotenv


load_dotenv()
logging.basicConfig(level=logging.INFO)

GEODB_API_URL = "http://geodb-free-service.wirefreethought.com/v1/geo"
GEOCODING_API_URL = "https://nominatim.openstreetmap.org/search"
STREETVIEW_API_URL = "https://maps.googleapis.com/maps/api/streetview"
STREETVIEW_API_KEY = os.getenv("STREETVIEW_API_KEY")

TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN_KEY = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

MIN_CITY_POPULATION = 1000000  # focus on cities with at least 1 million people
IMAGE_SIZE = "640x480"  # {width}x{height} in pixels