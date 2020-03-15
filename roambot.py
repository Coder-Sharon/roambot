from random import uniform

import requests

import common.config as config
from common.geodb import GeoDBClient
from common.geocoding import GeocodingClient
from common.streetview import StreetviewClient


class Roambot:
	def __init__(self):
		self._geodb = GeoDBClient(config)
		self._geocoding = GeocodingClient(config)
		self._streetview = StreetviewClient(config)
		
	def tweet(self):
		image = None
		attempt = 0

		while not image and attempt < 10:
			place = self._geodb.pick_place()
			coordinates = self.pick_coordinates(place)
			image = coordinates
			#image = self._streetview.pick_image(coordinates)
			attempt = attempt + 1
			
		print(coordinates)
		print(attempt)
			
		
	def pick_coordinates(self, place):
			geocode = self._geocoding.geocode(place.get("city"), place.get("country"))
	
			try:
				bbox = geocode["boundingbox"]
				bboxf = [float(v) for v in bbox]
				south, north, west, east = bboxf
				latitude = uniform(south, north)
				longitude = uniform(west, east)
				coordinates = f"{latitude},{longitude}"
			except KeyError:
				coordinates = ""
				
			return coordinates	


if __name__ == "__main__":
	Roambot().tweet()