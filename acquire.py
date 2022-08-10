import pandas as pd
import requests

#Using the code from the lesson as a guide and the REST API from 
# https://python.zgulde.net/api/v1/items as we did in the lesson, 
# create a dataframe named items that has all of the data for items.

response = requests.get('https://python.zgulde.net/api/v1/items ')
response