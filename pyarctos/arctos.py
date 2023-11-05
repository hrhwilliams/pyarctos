import json

import requests
import pyarctos


_API_KEY = None
_ARCTOS_URL = "https://arctos.database.museum/component/api/v2"


def set_api_key(key: str):
    '''Set the API key to use to access Arctos through'''
    global _API_KEY
    _API_KEY = key


def catalog(query: str):
    if _API_KEY is None:
        raise 'no api key'
    params = { 'api_key': _API_KEY, 'method': 'getCatalogData', 'scientific_name': query }
    headers = {'user-agent': 'PyArctos/0.0.1'}
    r = requests.get(f'{_ARCTOS_URL}/catalog.cfg', params=params)
    if not r.status_code == requests.codes.ok:
        r.raise_for_status()
    return r

