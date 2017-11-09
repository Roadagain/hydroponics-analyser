#!/usr/bin/env python3

import fetch
from datetime import datetime as dt
import json

def main():
    data = fetch.fetch_dict('http://localhost:5000/fetch/test')
    del data['result']
    filename = dt.today().strftime('%Y%m%d%H%M%S') + '.json'
    f = open(filename, 'w')
    f.write(json.dumps(data))

if __name__ == '__main__':
    main()
