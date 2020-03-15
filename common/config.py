import os

from dotenv import load_dotenv


load_dotenv()

GEODB_API_URL = "http://geodb-free-service.wirefreethought.com/v1/geo"
GEOCODING_API_URL = "https://nominatim.openstreetmap.org/search"
STREETVIEW_API_URL = "https://maps.googleapis.com/maps/api/streetview"
STREETVIEW_API_KEY = os.getenv("STREETVIEW_API_KEY")
MIN_CITY_POPULATION = 1000000  # focus on cities with at least 1 million people
IMAGE_SIZE = "640x480"  # {width}x{height} in pixels