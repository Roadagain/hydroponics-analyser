#!/usr/bin/env python3

import requests
import json

def fetch_dict(url):
    res = requests.get(url)
    return res.json()

def main():
    data = fetch_dict('http://localhost:5000/fetch/test')
    print(data)

if __name__ == '__main__':
    main()
