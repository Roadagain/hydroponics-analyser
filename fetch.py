#!/usr/bin/env python3
"""This module's functions fetch data from the api server"""

import requests

def fetch_dict(url):
    """Fetches data and returns as a dict"""
    res = requests.get(url)
    return res.json()
