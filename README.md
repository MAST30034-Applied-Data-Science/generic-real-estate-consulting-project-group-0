# Generic Real Estate Consulting Project
## Group 0 (authors)
- Anthony He; 1133985; anthony.he@student.unimelb.edu.au
- Junbo Hu; 1038361; junboh@student.unimelb.edu.au
- Stefan Solagratio Simanjuntak; 1039092; ssimanjuntak@student.unimelb.edu.au

## Instructions
1.  `scripts/external\_dataset.py` would download all external datasets that are needed
2.  In `notebooks/`
    1. `scrape01\_seedlinks.ipynb`, `scrape01\_suburb.ipynb`, `scrape03\_all\_link.ipynb` and `scrape04\_data.ipynb` scrapes necessary data from oldlistings.com.au
    2. `geocoder.ipynb` gets the geo-coordinates of all records where feasible
    3. `pre-processing\_pastlisting.ipynb` perform preliminary pre-processing on the dataset that is scraped 
    4. `feature\_engineering.ipynb` generates features from the pre-processed data and also embed all external datasets used in this project
    5.  `proximity.ipynb` determines the directions from the properties to points of interest
3. In `models/`, 
    1. `Mini\_Presentation\_original.pdf` is the file that was presented as a check point during the tutorial
    2. The following files are deliverables. Assumptions and limitations are mentioned in these notebooks along the way.
        - `random\_forest.ipynb` fit a model to predict the rental price and determines the importance of each feature. This also gives in depth view of important external and internal features.
        - `top_growing.ipynb` predicts the rental price in 5 years.
        - `top_suburbs.ipynb` shows the top growing suburbs using a scoring system. 
        

## Requirements
Here is a full list of packages that are used in this project.

* `from ast import literal_eval`
* `from bs4 import BeautifulSoup`
* `from decimal import Decimal`
* `from matplotlib import pyplot as plt`
* `from random import randrange`
* `from random import sample`
* `from random import uniform`
* `from requests_ip_rotator import ApiGateway, EXTRA_REGIONS`
* `from scipy.spatial.distance import cdist`
* `from sklearn import metrics`
* `from sklearn.datasets import load_boston`
* `from sklearn.ensemble import RandomForestRegressor`
* `from sklearn.inspection import permutation_importance`
* `from sklearn.model_selection import train_test_split`
* `from tqdm import tqdm`
* `import collections`
* `import csv`
* `import geopandas as gpd`
* `import geopy`
* `import html`
* `import json`
* `import matplotlib.pyplot as plt`
* `import numpy as np`
* `import os`
* `import pandas as pd`
* `import random`
* `import re`
* `import requests`
* `import seaborn as sns`
* `import statistics`
* `import time`
* `import urllib.request `

## Note
Meeting minutes are stored in `meetings/`