import requests


class GeocodingClient:
	def __init__(self, config):
		self._base_url = config.GEOCODING_API_URL
		
	def geocode(self, city, country):
		if not city and not country:
			return {}
	
		query = f"{city},{country}"
		params = {"q": query, "limit": 1, "format": "json"}
		params["accept-language"] = "en-US"  # important for encoding; solves most issues!
		r = requests.get(self._base_url, params=params)

		try:
			geocode = r.json()[0]  # sometimes fields are still not UTF-8 encoded; be wary
		except KeyError:
			geocode = {}
			
		return geocode