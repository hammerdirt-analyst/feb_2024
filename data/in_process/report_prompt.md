# Finding objects on the beach



These are the instructions and data for completing a survey report. The instructions are marked with an asterix \*.

\* directly check and summarize the provided links, keeping the responses concise and within a 90-word limit. 

The data is a collection of sources that was first summarized in the Swiss national survey of beach litter density, IQAASL: https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/

This is a survey report of field observations of citizen scientists. The soure of this data and how 
to generate similar reports can be found the repo where the federal reports were designed. The link is here: https://hammerdirt-analyst.github.io/feb_2024/titlepage.html




## Description

The dataset records the counts of objects found on the beach, this metric is given as pieces per meter of shore line or `pcs/m`. The area of concern is the
on the shores of lakes in the Canton of Bern, Switzerland.  The dataset includes various topographical features within a 1,500-meter buffer zone around the lakes, 
such as the proportion of land occupied by buildings, streets, public services, orchards, vineyards, forests, and undefined areas.

\* Explain citizen-science and beach-litter in one paragraph: consider this source https://hammerdirt-analyst.github.io/feb_2024/titlepage.html
and consider this source: https://mcc.jrc.ec.europa.eu/main/dev.py?N=41&O=466

\* Explain the origins of the data and how users can access it. Give a descriptive name for each link

\* Summarize the description 




## Objectives

What we must do is identify areas for investment and be specific about what a proposed action will reduce and where does the reduction actually take
place, in reference to the chain of events that turns an object into beach litter. Therefore we want to identify areas that would most benefit or at least have 
the greatest need. The greatest need is defined by the greatest value of the target variable which is pcs/m. 

\* State the objectives. Find at least three references that indicate this may be a good path to follow analytically.



We have also considered the data in three different ways: 1. the combined data, 2. only objects of direct personal consumption, 3. only objects of profesional use. The members of each group are defined as __recreation__ (rec):

['Cigarette filters' 'Food wrappers; candy, snacks' 'Straws and stirrers']


And __profesional__ (pro):

['Plastic construction waste' 'Industrial sheeting'
 'Industrial pellets (nurdles)' 'Cable ties; steggel, zip, zap straps'
 'Straps/bands;  hard, plastic package fastener'
 'Foam packaging/insulation/polyurethane' 'Traffic cones'
 'Tape, masking/duct/packing' 'Buckets' 'Helmets or hardhats'
 'Fiberglass fragments' 'Tags fishing or industry (security tags, seals)'
 'Glove industrial/professional'
 'Coverings; plastic packaging, sheeting for protecting large cargo items'
 'Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc.'
 'Car parts' 'Injection gun cartridge' 'Fragmented plastics']




## Observed survey totals

### Combined survey totals
Summarize the following table. Note the start and end dates, the number of samples and the average. Round all float values to 2 in the table. Reply in paragraph form. Reproduct tables after paragraph.

|          | result             |
|:---------|:-------------------|
| total    | 9889               |
| nsamples | 98                 |
| average  | 2.8136734693877545 |
| 5th      | 0.3685             |
| 25th     | 0.88               |
| 50th     | 1.835              |
| 75th     | 3.6900000000000004 |
| 95th     | 8.048499999999999  |
| std      | 2.6318385704151193 |
| max      | 14.8               |
| start    | 2017-04-16         |
| end      | 2021-04-08         |

### Object groups

The following table has the survey totals of the two different object groups (rec and pro). Explain what the object groups are, give a list of for the members of each group. Compare the results with the combined survey totals. Note where the maximum and minimum values are.

| use   |   count |    mean |     std |   min |    25% |   50% |   75% |   max |
|:------|--------:|--------:|--------:|------:|-------:|------:|------:|------:|
| pers  |      74 | 2.04635 | 1.9413  |  0.14 | 0.7125 |  1.31 | 2.585 |  9.55 |
| pro   |      74 | 1.04311 | 1.13764 |  0    | 0.28   |  0.64 | 1.49  |  5.32 |






## Features

The feature variables have a definite relationship for example forest, undefined, vineyards, orchards and buildings do not overlap. 
that is if you sum them up you get close to 1. however public services and streets are in addition to the other feature variables. 
i mean that you can have streets and public services in forest, buildings, orhards, vineyards and undefined areas but not the other way around.

\* Explain the difference between land use and land cover. Explain why the feature variables may be important: one - two paragraphs



### Land use - land cover - features

Land use refers to the measurable topographic features within a cirlce of r = 1 500 m and area = pi(r)²
with the survey location in the middle (the buffer). The features, measured in meters squared, are given as a ratio

. Thus a location with high percentage of buildings will have a rating or value between 60% and 100%. The pcs/m rating is the average of all locations with a land-use profile of the same rating.

The land use is further divided in to two groups: cover and use. Cover refers to those topographical features that do not overlap. That is cover features are mutually exclusive, a given area of the buffer is either one or the other of the cover features. The cover features are:

    Buildings, orchards, forest, undefined, vineyards

Use refers to the activities or features that are present in one of the cover features. For example public services can be located within buildings (hospitals, schools) or in a forest (parks, nature areas). The use features are:

    Pubilc services, streets

#### Streets

The streets are measured as the length of the road network in the cirlce with r= 1 500 m and area
²
and the survey location in the middle. The lengths for each location are normalized from 0 - 1. Thus in the table below, the locations that have the shortest road net work will be in category 1, the those with a more dense network will be higher.


The following tables are summaries of the survey results according to the topographical features the first table is the average 
objects permeter observed for the given feature (columns) at the speicified magnitude (1 - 5), the index. The second table is 
the proportions of surveys for the specified feature (column) and magnitude (index). The values were derived from the vector layers available at 
Swiss topo: https://www.swisstopo.admin.ch/de/landschaftsmodell-swisstlmregio 

\* In two paragraphs Explain what land use is. And how it is calculated.

\* Tell where the source datas is and give provided link.

\* Explain the results in the two tables, identify areas of concern and areas where pcs/m is lowest.

\* explain how a high number in the second table is an indicator of the confidence for the values in the first table. 

\* Reply in paragraph form. Reproduce tables after paragraph. 

\* Make a label for each table or a subheader when you reproduce the tables


\* Summarize the observed sample results and the landuse profile. Do this in two paragraphs.



### Objects per meter of shoreline by magnitude of feature
|    |   buildings |   wetlands |   forest |   public-services |   recreation |   undefined |   streets |   vineyards |   orchards |
|---:|------------:|-----------:|---------:|------------------:|-------------:|------------:|----------:|------------:|-----------:|
|  1 |     2.51652 |    3.08946 |  3.51444 |           3.08946 |      3.08946 |     3.74692 |         0 |     3.08946 |    3.08946 |
|  2 |     2.525   |    0       |  3.19959 |           0       |      0       |     4.9     |         0 |     0       |    0       |
|  3 |     5.3525  |    0       |  1.22571 |           0       |      0       |     2.42381 |         0 |     0       |    0       |
|  4 |     2.384   |    0       |  0       |           0       |      0       |     0       |         0 |     0       |    0       |
|  5 |     1.24    |    0       |  0       |           0       |      0       |     0       |         0 |     0       |    0       |


### Objects per meter of shoreline by magnitude of feature
|    |   buildings |   wetlands |    forest |   public-services |   recreation |   undefined |   streets |   vineyards |   orchards |
|---:|------------:|-----------:|----------:|------------------:|-------------:|------------:|----------:|------------:|-----------:|
|  2 |   0.378378  |          0 | 0.662162  |                 0 |            0 |   0.0810811 |         0 |           0 |          0 |
|  1 |   0.310811  |          1 | 0.243243  |                 1 |            1 |   0.351351  |         0 |           1 |          1 |
|  3 |   0.216216  |          0 | 0.0945946 |                 0 |            0 |   0.567568  |         0 |           0 |          0 |
|  4 |   0.0675676 |          0 | 0         |                 0 |            0 |   0         |         0 |           0 |          0 |
|  5 |   0.027027  |          0 | 0         |                 0 |            0 |   0         |         0 |           0 |          0 |

