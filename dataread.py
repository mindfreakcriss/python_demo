import csv
import json
from pprint import pprint
import numpy as np


def csv_read(file):
    with open(file) as f:
        data = csv.reader(f)

        for line in data:
            print(line)
    return


def csv_numpy(file):
    data = np.genfromtxt(file,skip_header=1,dtype=None,delimiter=",")
    print(data)


def json_read(file):
    with open(file) as f:
        data = json.loads(f.read())
        pprint(data)


file = "./data/gas_data/daily_json.json"

## csv_read(file)
## csv_numpy(file)
json_read(file)