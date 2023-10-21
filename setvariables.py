# aconfig file for summarizing the data from surveys

# period dates
period_dates = {
    "mcbp":["2015-11-15", "2017-03-31"],
    "slr": ["2017-04-01", "2020-02-28"],
    "iqaasl": ["2020-03-01", "2021-05-31"],
    "2022": ["2021-06-01", "2022-12-01"]
}

survey_data = [
    "data/end_process/after_may_2021.csv",
    "data/end_process/iqaasl.csv",
    "data/end_process/mcbp.csv",
    "data/end_process/slr.csv",
]

source_data = "data/end_process/new_allx.csv"

code_data =  "data/end_process/codes.csv"
beach_data = "data/end_process/beaches.csv"
land_cover_data = "data/end_process/land_cover.csv"
land_use_data = "data/end_process/land_use.csv"
street_data = "data/end_process/streets.csv"
intersection_attributes = "data/end_process/river_intersect_lakes.csv"

code_result_columns = [
    'loc_date', 
    'date',
    'parent_boundary',
    'feature_name',
    'city',
    'slug',
    'length',
    'code']

agg_groups = {
    "quantity":"sum",
    "pcs_m": "median"
}



group_by_columns = [
    'loc_date', 
    'date',
    'parent_boundary',
    'feature_name',
    'city',
    'slug',
    'length',
    'groupname',
    'code', 
]
unit_agg = {
    "quantity":"sum",
    "pcs_m": "sum"
}
