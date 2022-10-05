__author__ = 'kamta'

import io
import requests

import pandas as pd


def get_dataframe(param_url=None):
    url = param_url if param_url else "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    s = requests.get(url).content
    c = pd.read_csv(io.StringIO(s.decode('utf-8')))
    return c
