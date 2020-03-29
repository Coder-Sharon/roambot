import logging
from tempfile import TemporaryFile 

import twitter

import common.config as config
from common.geodb import GeoDBClient
from common.geocoding import GeocodingClient
from common.streetview import StreetviewClient


class Roambot:
	def __init__(self):
		self._geodb = GeoDBClient(config)
		self._geocoding = GeocodingClient(config)
		self._streetview = StreetviewClient(config)
		
		self._twitter =  twitter.Api(
			config.TWITTER_CONSUMER_KEY,
			config.TWITTER_CONSUMER_SECRET,
			config.TWITTER_ACCESS_TOKEN_KEY,
			config.TWITTER_ACCESS_TOKEN_SECRET,
		)
		
	def tweet(self, attempts = 10):
		attempt = 0

		while attempt < attempts:  # try to tweet before giving up
			logging.info(f"tweet attempt: {attempt + 1}")
			place = self._geodb.pick_place()
			address = self.format_address(place)
			bbox = self.get_bounding_box(address)
			image = self._streetview.pick_image(bbox)

			if image:
				with TemporaryFile() as imagef:
					imagef.write(image)
					self._twitter.PostUpdate(status=address, media=imagef)
					logging.info(f"yay: tweeted {address}")
				return

			attempt = attempt + 1

		logging.warning("whoops: no tweet this time")

	def get_bounding_box(self, address):
		geocode = self._geocoding.geocode(address)

		try:
			bbox = geocode["boundingbox"]
			bbox = [float(v) for v in bbox]
		except KeyError:
			bbox = []
			
		return bbox
		
	def format_address(self, place):
		city = place.get("city", "")
		region = place.get("region", "")
		country = place.get("country", "")
		parts = [city, region, country]
		parts = list(dict.fromkeys(parts))  # remove duplication
		address = ", ".join(parts)
		
		return address


if __name__ == "__main__":
	Roambot().tweet()