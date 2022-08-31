# download and extract ABS SA2 District Boundaries files
import requests
import zipfile
import io
import os

if not os.path.exists('../data/raw/abs_SA2_District_Boundaries'):
    os.makedirs('../data/raw/abs_SA2_District_Boundaries')
    
url = 'https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('../data/raw/abs_SA2_District_Boundaries')

