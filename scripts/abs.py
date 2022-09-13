# download and extract ABS SA2 District Boundaries files
import requests
import zipfile
import io
import os
from urllib.request import urlretrieve

# files (raw data) stored in ../data/raw
output_relative_dir = '../data/raw/'
# in this particular script, all files are from ABS 
# hence they are stored in the following directory
if not os.path.exists(output_relative_dir + 'abs'):
    os.makedirs(output_relative_dir + 'abs')
output_relative_dir = output_relative_dir + 'abs/'

# download SA2 district boundaries information
if not os.path.exists(output_relative_dir + 'abs_SA2_District_Boundaries'):
    os.makedirs(output_relative_dir + 'abs_SA2_District_Boundaries')
url = 'https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(output_relative_dir + 'abs_SA2_District_Boundaries')

# download income statistics from ABS
urlretrieve('https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/personal-income-australia/2014-15-2018-19/6524055002_DO002.xlsx', f"{output_relative_dir}/income_distribution.xlsx")

# doanload population statistics from ABS
urlretrieve('https://www.abs.gov.au/statistics/people/population/regional-population-age-and-sex/2021/32350DS0001_2021.xlsx', f"{output_relative_dir}/population.xlsx")

# doanload school locations
urlretrieve('https://www.education.vic.gov.au/Documents/about/research/datavic/dv331_schoollocations2022.csv', f"{output_relative_dir}/schools.csv")

# download postcode data
# see https://github.com/matthewproctor/australianpostcodes/blob/master/README.md 
# for documentations
urlretrieve('https://raw.githubusercontent.com/matthewproctor/australianpostcodes/master/australian_postcodes.csv', f"{output_relative_dir}/australian_postcodes.csv")
