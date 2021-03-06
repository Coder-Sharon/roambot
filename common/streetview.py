import logging
from random import randint, uniform

import requests


class StreetviewClient():
	def __init__(self, config):
		self._base_url = config.STREETVIEW_API_URL
		self._metadata_url =  self._base_url + "/metadata"
		self._api_key = config.STREETVIEW_API_KEY
		self._image_size = config.IMAGE_SIZE
	
	def pick_image(self, bbox, attempts = 10):
		if not bbox:
			return None
		
		attempt = 0

		while attempt < attempts:  # give cities with less coverage a chance
			logging.info(f"streetview attempt: {attempt + 1}")
			coordinates = self.pick_coordinates(bbox)
			params = {"location": coordinates, "key": self._api_key}
			attributes = self.pick_attributes()
			params.update(attributes)
		
			if self.image_exists(params):
				r = requests.get(self._base_url, params=params)
				image = r.content
				return image
				
			attempt = attempt + 1
			
		return None

	def pick_coordinates(self, bbox):
		south, north, west, east = bbox
		latitude = uniform(south, north)
		longitude = uniform(west, east)
		coordinates = f"{latitude},{longitude}"
		return coordinates
		
	def pick_attributes(self):
		heading = randint(0, 360)  # compass heading of the camera
		fov = randint(90, 120)  # horizontal field of view; zoom
		pitch = randint(-25, 25)  # up or down angle of the camera
		radius = 250  #  radius in which to search (meters)
		
		attributes = {
			"size": self._image_size,
			"heading": heading,
			"fov": fov,
			"pitch": pitch,
			"radius": radius,
		}
		
		return attributes
		
	def image_exists(self, params):
		r = requests.get(self._metadata_url, params=params)
		data = r.json()
		
		if data["status"] == "OK":
			exists = True
		else:
			exists = False
			
		return exists