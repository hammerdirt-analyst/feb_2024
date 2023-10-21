# utility methods used when comaparing different sets of the same data


import pandas as pd

def collect_vitals(data):
    total = data.quantity.sum()
    median = data.pcs_m.median()
    samples = data.loc_date.nunique()
    ncodes = data.code.nunique()
    nlocations = data.slug.nunique()
    nbodies = data.feature_name.nunique()
    ncities = data.city.nunique()
    min_date = data["date"].min()
    max_date = data["date"].max()
    
    return total, median, samples, ncodes, nlocations, nbodies, ncities, min_date, max_date

def find_missing(more_than, less_than):
    return np.setdiff1d(more_than, less_than)
def find_missing_loc_dates(done, dtwo):
    locs_one = done.loc_date.unique()
    locs_two = dtwo.loc_date.unique()
    return find_missing(locs_one, locs_two)

def use_gfrags_gfoams_gcaps(data, codes,columns=["Gfoams", "Gfrags", "Gcaps"]):
    for col in columns:
        change = codes.loc[codes.parent_code == col].index
        data.loc[data.code.isin(change), "code"] = col
        
    return data

def make_a_summary(vitals, add_summary_name=False):

    a_summary = f"""
    Number of objects: {vitals[0]}
    
    Median pieces/meter: {vitals[1]}
    
    Number of samples: {vitals[2]}
    
    Number of unique codes: {vitals[3]}
    
    Number of sample locations: {vitals[4]}
    
    Number of features: {vitals[5]}
    
    Number of cities: {vitals[6]}
    
    Start date: {vitals[7]}
    
    End date: {vitals[8]}
    
    """

    if add_summary_name:
        a_summary = f"""
        Summary name = {add_summary_name}

        {a_summary}
        """
        
    return a_summary
    
def combine_survey_files(list_of_files):

    files = []
    for afile in list_of_files:
        files.append(pd.read_csv(afile))
    return pd.concat(files)