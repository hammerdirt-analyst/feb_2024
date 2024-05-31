# Canton Bern

A report is the implementation of a `SurveyReport`, `LandUseReport` or a  `GridForecaster`. The `SurveyReport` is the basic 
element and does the initial aggregating and descriptive statistics for a query.

The land-use-report accepts `SurveyReport.sample_results` and assigns the land-use attributes to the record. The 
land-use-report provides the baseline assessment of litter density with reference to the surrounding environment. 
The assessment accepts as variables the proportion of available space that a topographical feature occupies in a 
circle of $\pi r² \text{ where r = 1 500 meters}$ and the center of that circle is the survey location. 
These proportions are compared to the `average pieces per meter` for an object or group of objects.

Each report and the inference method are documented: [SurveyReport](surveyreporter), [LandUseReport](landusereporter), [GridForecaster](gridforecaster)





o_report_r, o_land_use_r = gfcast.make_report_objects(o_prior_r)
this_report = reports.SurveyReport(dfc=df)
 # print('making prior')

 # generate the parameters for the landuse report
 target_df = this_report.sample_results
 features = geospatial.collect_topo_data(locations=target_df.location.unique())

 # make a landuse report
 this_land_use = geospatial.LandUseReport(target_df, features)