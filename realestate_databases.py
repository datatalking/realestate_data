# FILENAME realestate_database.py

import requests
import os
import json


# :TODO: rename this to realestate_database_api for these urls
url = "https://api.reonomy.com/v2/users/me"
headers = {"Authorization": "Basic YOUR_ACCESS_TOKEN"}
params = {}
response = requests.get(url, params=params, headers=headers).json()


def reonomy_realestate_api():
	"""

	:return:
	:TODO:
	"""
	# TODO use requests or other to access realestate_URL_list as the api name
	url_001 = 'https: // www.reonomy.com / signup'




def rapidapi_realestate_api():
	"""

	:return:
	:TODO:
	"""
	# TODO use requests or other to access realestate_URL_list as the api name
	url_001 = 'https://rapidapi.com/blog/best-real-estate-apis/'


def redfin_realestate_api():
	"""

	:return:
	:TODO:
	"""
	# TODO use requests or other to access realestate_URL_list as the api name
	url_001 = 'https://www.redfin.com/news/data-center/'
