# Generic Real Estate Consulting Project
## Group 0 (authors)
- Anthony He; 1133985; anthony.he@student.unimelb.edu.au
- Junbo Hu; 1038361; junboh@student.unimelb.edu.au
- Stefan Solagratio Simanjuntak; 1039092; ssimanjuntak@student.unimelb.edu.au

## Instructions
1.  ‘scripts/external_dataset.py’ would download all external datasets that are needed
2.  In ‘notebooks/‘
    1. ‘scrape01_seedlinks.ipynb’, ‘scrape01_suburb.ipynb’, ‘scrape03_all_link.ipynb’ and ’scrape04_data.ipynb’ scrapes necessary data from oldlistings.com.au
    2. ‘geocoder.ipynb’ gets the geo-coordinates of all records where feasible
    3. ‘pre-processing_pastlisting.ipynb’ perform preliminary pre-processing on the dataset that is scraped 
    4. ‘feature_engineering.ipynb’ generates features from the pre-processed data and also embed all external datasets used in this project
    5.  ‘proximity.ipynb’ determines the directions from the properties to points of interest
3. In ‘models/‘
    1. ‘random_forest.ipynb’ fit a model to predict the rental price and determines the importance of each feature
    2. ‘grow.ipynb’ predicts the rental price in 5 years

## Requirements

## Note
Meeting minutes are stored in 'meetings/'