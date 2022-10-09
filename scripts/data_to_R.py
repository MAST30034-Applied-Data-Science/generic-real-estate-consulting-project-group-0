import pandas as pd
df = pd.read_csv('../data/curated/full_listing.csv').iloc[:,1:]
remove = [ 'address', 'suburb', 'postcode', 'url', 'loc_address', 'lat', 'lon', 'list_date', 'list_history', 'list_count', 'SA2_NAME_2016', 'SA2', 'lgaregion', 'primary_school_name', 'secondary_school_name', 'pri_lat', 'pri_lon', 'sec_lat', 'sec_lon', 'closest_ed_name', 'ed_lat', 'ed_lon', 'train_stop', 'train_lat', 'train_lon']
df = df.drop(remove, axis=1)
df.to_csv('../data/curated/R_full_listing.csv')