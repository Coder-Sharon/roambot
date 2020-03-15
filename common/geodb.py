from random import randint

import requests


class GeoDBClient:
	def __init__(self, config):
		self._base_url = config.GEODB_API_URL
		self._countries_url = self._base_url + "/countries"
		self._cities_url = self._base_url + "/cities"
		self._min_population = config.MIN_CITY_POPULATION
		
	def pick_place(self):
		country = self.pick_country()  # pick country first to balance small vs. large countries
		country_id = country["code"]
		city = self.pick_city(country_id)
		return city
		
	def pick_country(self):
		r = requests.get(self._countries_url)
		country_count = r.json()["metadata"]["totalCount"]
		country_choice = randint(0, country_count - 1)	
		
		params = {"limit": 1, "offset": country_choice}
		r = requests.get(self._countries_url, params=params)
		country = r.json()["data"][0]
		
		return country
		
	def pick_city(self, country_id):
		params = {"countryIds": [country_id], "minPopulation": self._min_population, "types": ["CITY"]}
		r = requests.get(self._cities_url, params=params)		
		city_count = r.json()["metadata"]["totalCount"]
		
		if city_count:
			city_choice = randint(0, city_count - 1)
			params.update({"limit": 1, "offset": city_choice})
			r = requests.get(self._cities_url, params=params)
			city = r.json()["data"][0]
		else:
			city = {}
			
		return city