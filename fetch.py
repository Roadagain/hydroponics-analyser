#!/usr/bin/env python3

import requests

def fetch_dict(url):
    res = requests.get(url)
    return res.json()
