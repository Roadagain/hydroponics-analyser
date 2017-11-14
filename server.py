#!/usr/bin/env python3
"""The main program of hydroponics-analyser"""

from datetime import datetime as dt
import json
import fetch

API_URL = 'http://localhost:5000/fetch'
DATA_DIR = './data/'

def main():
    """Main function"""
    data = fetch.fetch_dict(API_URL)
    del data['result']
    filename = DATA_DIR + dt.today().strftime('%Y%m%d%H%M%S') + '.json'
    datafile = open(filename, 'w')
    datafile.write(json.dumps(data))

if __name__ == '__main__':
    main()
