

<!-- INSTRUCTION_START

1. Analysis of Sampling Stratification and Sampling stratification and trash density tables
   * Objective: Ensure conclusions about the presence or absence of objects are based on a combined interpretation of sampling stratification and litter density data.
   * Data Validation: Confirm that any conclusions about trash density and land use are supported by the presence of samples in the sampling stratification table"
   * Interpretation Guidelines: Analyze how the distribution of land-use features influences the observed trash density. 
   * Draw conclusions only when both stratification and density data are aligned. Make sure to check all the values for a given land-use feature and proportion of buffer zone. Before making any conlusions"
   * A zero in the trash density table indicates that no objects were found for that land-use feature and proportion of buffer zone.

2. Reporting Geographic Information

   * Always provide the names of all the cities, cantons, and survey areas included in the report.
   * Always provide the names of all the lakes, rivers, and parks included in the report.

3. Definitions of Urban, Rural Areas, fail-rate

   * Urban Areas: The proportion of samples where building occupy 60% or more of the buffer is greater than 50%.

   * Rural Areas: The proportion of samples where forest occupy 60% or more of the buffer is greater than 50%.

   * Mixed Areas: Does not meet the criteria of urban or rural.

   * Fail Rate: The proportion of samples where at least one of the object categories was found.

   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**

1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column, if the table
reads 'no samples' that is equivalent to 0. 

2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column, if the table
reads 'no samples' that is equivalent to 0. 

3. Make the conclusion: If test one is greater than 50% then the classification is urban. If test two is greater than 50% then 
the classification is rural. If neither test one or test two is greater than 50% the the classification is mixed.

  

INSTRUCTION_END -->

# Bern canton 2020-01-01 2021-12-31
**Summary and analysis of observations of trash density**: objects related to recreation, personal items, unclassified, infrastructure, food and drink, packaging non food, plastic pieces, waste water, agriculture, tobaccoand micro plastics (< 5mm) found in lakes and rivers.


## Administrative boundaries Bern canton 2020-01-01 2021-12-31 : Cities, cantons, survey areas

The number and and names of the cities, cantons and survey areas included in this report



The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis.

Please provide a narrative of the contents of the following table. In your narrative be sure to include the list of cities and the names of the canton and survey areas.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

 |              |   count |
|:-------------|--------:|
| location     |      33 |
| city         |      21 |
| canton       |       1 |
| survey areas |       1 |

The following is the names of the cities, cantons, and survey areas.

city: Kallnach, Port, Bern, Köniz, Spiez, Walperswil, Vinelz, Brügg, Thun, Erlach, Gals, Bönigen, Ligerz, Lüscherz, Biel/Bienne, Nidau, Brienz (BE), Rubigen, Burgdorf, Beatenberg, Unterseen
canton: Bern
survey_area: aare


## Named features Bern canton 2020-01-01 2021-12-31 : The lakes, rivers and parks

The number and names of the lakes, rivers or parks included in this report



The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. Please provide a concise narrative of the contents of the following table. In your narrative be sure to the name of each park, lake or river

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
 INSTRUCTION_END ---> 

|       |   river |   lake |
|:------|--------:|-------:|
| count |       4 |      3 |

The following is the names of the lakes, rivers and parks included in the data.

river: aare, aarenidau-buren-kanal, schuss, emme
lake: thunersee, bielersee, brienzersee
park: 


## Summary statistics Bern canton 2020-01-01 2021-12-31: The descriptive statistics of the survey results

Bern: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.





This table summarizes the sample total in pcs/m for each survey. Each survey is defined by a sample_id. A survey total is the sum of all rows that have the same sample_id.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

|        |   total |   nsamples |   average |   5th |   25th |   50th |   75th |   95th |     std |   max | start      | end        |
|:-------|--------:|-----------:|----------:|------:|-------:|-------:|-------:|-------:|--------:|------:|:-----------|:-----------|
| result |    9028 |         89 |   2.75809 | 0.184 |   0.87 |   1.72 |   3.48 |  8.134 | 2.74195 |  14.8 | 2020-01-26 | 2021-04-23 |

## Material composition of objects Bern canton 2020-01-01 2021-12-31: estimated material composition

Bern: The proportion of each material type according to material category





The following table details the proportion that each material type represents to the total. 
Generate a narrative summary based on the following table. You need to include all the material types and their float values.
If there is more than one material entry in the table.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. Consider the example above

 INSTRUCTION_END ---> 

| material   | % of total   |
|:-----------|:-------------|
| chemicals  | 1%           |
| glass      | 5%           |
| metal      | 3%           |
| paper      | 2%           |
| plastic    | 85%          |
## Survey Totals for city


## Bern canton 2020-01-01 2021-12-31 city: The average pcs/m by city.

The average sample total for each city in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | city        |   quantity |    pcs/m |
|---:|:------------|-----------:|---------:|
|  0 | Beatenberg  |        104 | 2.425    |
|  1 | Bern        |        147 | 0.9825   |
|  2 | Biel/Bienne |       3307 | 5.07471  |
|  3 | Brienz (BE) |        696 | 4.48667  |
|  4 | Brügg       |         36 | 1.02     |
|  5 | Burgdorf    |         41 | 0.87     |
|  6 | Bönigen     |        277 | 3.175    |
|  7 | Erlach      |        101 | 1.83     |
|  8 | Gals        |         48 | 1.28     |
|  9 | Kallnach    |         82 | 1.315    |
| 10 | Köniz       |         12 | 0.16     |
| 11 | Ligerz      |        143 | 9.1      |
| 12 | Lüscherz    |        202 | 0.746    |
| 13 | Nidau       |         63 | 2.52     |
| 14 | Port        |        118 | 1.375    |
| 15 | Rubigen     |         57 | 3.2      |
| 16 | Spiez       |        530 | 0.722857 |
| 17 | Thun        |        276 | 1.4      |
| 18 | Unterseen   |       1879 | 1.88833  |
| 19 | Vinelz      |        895 | 4.495    |
| 20 | Walperswil  |         14 | 0.22     |


## Survey Totals for parent_boundary


## Bern canton 2020-01-01 2021-12-31 survey area: The average pcs/m by survey area.

The average sample total for each survey area in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | parent_boundary   |   quantity |   pcs/m |
|---:|:------------------|-----------:|--------:|
|  0 | aare              |       9028 | 2.75809 |



## Inventory items Bern canton 2020-01-01 2021-12-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |       pcs/m |   % of total |   sample_id |   fail rate | object                                                                                       |
|:-------|-----------:|------------:|-------------:|------------:|------------:|:---------------------------------------------------------------------------------------------|
| G27    |       1671 | 0.423708    |  0.185091    |          89 |   0.808989  | Cigarette filters                                                                            |
| Gfrags |       1323 | 0.45573     |  0.146544    |          89 |   0.88764   | Fragmented plastics                                                                          |
| G67    |        686 | 0.237753    |  0.0759858   |          89 |   0.775281  | Industrial sheeting                                                                          |
| G30    |        589 | 0.186292    |  0.0652415   |          89 |   0.797753  | Food wrappers; candy, snacks                                                                 |
| Gfoams |        474 | 0.12191     |  0.0525033   |          89 |   0.617978  | Expanded polystyrene                                                                         |
| G200   |        348 | 0.121685    |  0.0385467   |          89 |   0.651685  | Glass drink bottles, pieces                                                                  |
| G941   |        261 | 0.0869663   |  0.0289101   |          89 |   0.494382  | Packaging films nonfood or unknown                                                           |
| G74    |        240 | 0.0335714   |  0.026584    |          89 |   0.775281  | Foam packaging/insulation/polyurethane                                                       |
| Gcaps  |        227 | 0.0652809   |  0.025144    |          89 |   0.595506  | plastic caps, lid rings: G21, G22, G23, G24                                                  |
| G112   |        196 | 0.0538202   |  0.0217102   |          89 |   0.325843  | Industrial pellets (nurdles)                                                                 |
| G89    |        160 | 0.0566292   |  0.0177226   |          89 |   0.516854  | Plastic construction waste                                                                   |
| G98    |        140 | 0.0558427   |  0.0155073   |          89 |   0.235955  | Diapers - wipes                                                                              |
| G904   |        116 | 0.0420225   |  0.0128489   |          89 |   0.47191   | Fireworks; rocket caps, exploded parts & packaging                                           |
| G117   |        115 | 0.0296629   |  0.0127381   |          89 |   0.292135  | Styrofoam < 5mm                                                                              |
| G95    |        113 | 0.0348315   |  0.0125166   |          89 |   0.449438  | Cotton bud/swab sticks                                                                       |
| G25    |        111 | 0.0440449   |  0.0122951   |          89 |   0.449438  | Tobacco; plastic packaging, containers                                                       |
| G213   |        103 | 0.0293258   |  0.0114089   |          89 |   0.258427  | Paraffin wax                                                                                 |
| G940   |         97 | 0.0288764   |  0.0107444   |          89 |   0.157303  | Foamed EVA (flexible plastic) for crafts & watersports                                       |
| G177   |         97 | 0.0295506   |  0.0107444   |          89 |   0.460674  | Foil wrappers, aluminum foil                                                                 |
| G156   |         84 | 0.0203371   |  0.00930439  |          89 |   0.224719  | Paper fragments                                                                              |
| G106   |         82 | 0.0214607   |  0.00908285  |          89 |   0.314607  | Plastic fragments angular <5mm                                                               |
| G50    |         60 | 0.0194382   |  0.00664599  |          89 |   0.370787  | String < 1cm                                                                                 |
| G35    |         54 | 0.0169663   |  0.00598139  |          89 |   0.348315  | Straws and stirrers                                                                          |
| G31    |         54 | 0.0139326   |  0.00598139  |          89 |   0.314607  | Lollypop sticks                                                                              |
| G922   |         51 | 0.0195506   |  0.00564909  |          89 |   0.303371  | Labels, bar codes                                                                            |
| G178   |         51 | 0.0152809   |  0.00564909  |          89 |   0.348315  | Metal bottle caps, lids & pull tabs from cans                                                |
| G10    |         50 | 0.0164045   |  0.00553833  |          89 |   0.325843  | Food containers single use foamed or plastic                                                 |
| G73    |         48 | 0.0124719   |  0.00531679  |          89 |   0.213483  | Foamed items & pieces (non packaging/insulation) foamed sponge material                      |
| G211   |         46 | 0.0123596   |  0.00509526  |          89 |   0.325843  | Other medical (swabs, bandaging, adhesive plaster)                                           |
| G936   |         45 | 0.0122472   |  0.00498449  |          89 |   0.191011  | Sheeting ag. greenhouse film                                                                 |
| G33    |         43 | 0.0180899   |  0.00476296  |          89 |   0.280899  | Cups, lids, single use foamed and hard plastic                                               |
| G32    |         40 | 0.0133708   |  0.00443066  |          89 |   0.303371  | Toys and party favors                                                                        |
| G204   |         40 | 0.0132584   |  0.00443066  |          89 |   0.123596  | Construction material; bricks, pipes, cement                                                 |
| G153   |         38 | 0.0110112   |  0.00420913  |          89 |   0.157303  | Cups, food containers, wrappers (paper)                                                      |
| G944   |         34 | 0.0058427   |  0.00376606  |          89 |   0.0337079 | Pellet mass from injection molding                                                           |
| G66    |         33 | 0.00955056  |  0.00365529  |          89 |   0.292135  | Straps/bands;  hard, plastic package fastener                                                |
| G186   |         33 | 0.00730337  |  0.00365529  |          89 |   0.191011  | Industrial scrap                                                                             |
| G87    |         33 | 0.00876404  |  0.00365529  |          89 |   0.202247  | Tape, masking/duct/packing                                                                   |
| G908   |         33 | 0.0103371   |  0.00365529  |          89 |   0.235955  | Tape; electrical, insulating                                                                 |
| G91    |         28 | 0.00786517  |  0.00310146  |          89 |   0.224719  | Biomass holder                                                                               |
| G923   |         28 | 0.00898876  |  0.00310146  |          89 |   0.191011  | Tissue, toilet paper, napkins, paper towels                                                  |
| G125   |         27 | 0.00707865  |  0.0029907   |          89 |   0.157303  | Balloons and balloon sticks                                                                  |
| G152   |         26 | 0.00910112  |  0.00287993  |          89 |   0.123596  | Cigarette boxes, tobacco related paper/cardboard                                             |
| G927   |         26 | 0.00640449  |  0.00287993  |          89 |   0.123596  | String trimmer line, used to cut grass, weeds, and shrubbery                                 |
| G96    |         25 | 0.0108989   |  0.00276916  |          89 |   0.146067  | Sanitary pads /panty liners/tampons and applicators                                          |
| G70    |         24 | 0.0058427   |  0.0026584   |          89 |   0.191011  | Shotgun cartridges                                                                           |
| G3     |         24 | 0.0058427   |  0.0026584   |          89 |   0.157303  | Bags; plastic shopping/carrier/grocery and pieces                                            |
| G137   |         24 | 0.0106742   |  0.0026584   |          89 |   0.101124  | Clothing, towels & rags                                                                      |
| G191   |         23 | 0.00820225  |  0.00254763  |          89 |   0.168539  | Wire and mesh                                                                                |
| G905   |         23 | 0.0052809   |  0.00254763  |          89 |   0.191011  | Hair clip,  hair ties, personal accessories plastic                                          |
| G159   |         22 | 0.00539326  |  0.00243686  |          89 |   0.157303  | Corks                                                                                        |
| G201   |         21 | 0.00808989  |  0.0023261   |          89 |   0.0898876 | Jars, includes pieces                                                                        |
| G100   |         20 | 0.00707865  |  0.00221533  |          89 |   0.191011  | Medical; containers/tubes/ packaging                                                         |
| G175   |         20 | 0.00516854  |  0.00221533  |          89 |   0.11236   | Cans, beverage                                                                               |
| G942   |         20 | 0.00460674  |  0.00221533  |          89 |   0.11236   | Plastic shavings from lathes, CNC machining                                                  |
| G928   |         19 | 0.00955056  |  0.00210456  |          89 |   0.134831  | Ribbons and bows                                                                             |
| G208   |         19 | 0.00516854  |  0.00210456  |          89 |   0.0786517 | Glass or ceramic fragments > 2.5 cm                                                          |
| G93    |         18 | 0.00842697  |  0.0019938   |          89 |   0.134831  | Cable ties; steggel, zip, zap straps                                                         |
| G203   |         18 | 0.00550562  |  0.0019938   |          89 |   0.0898876 | Tableware ceramic or glass, cups, plates, pieces                                             |
| G144   |         17 | 0.00516854  |  0.00188303  |          89 |   0.011236  | Tampons                                                                                      |
| G198   |         17 | 0.00595506  |  0.00188303  |          89 |   0.168539  | Other metal pieces < 50cm                                                                    |
| G914   |         16 | 0.00348315  |  0.00177226  |          89 |   0.0898876 | Paperclips, clothespins, plastic utility items                                               |
| G131   |         15 | 0.00359551  |  0.0016615   |          89 |   0.11236   | Rubber bands                                                                                 |
| G165   |         15 | 0.00359551  |  0.0016615   |          89 |   0.134831  | Ice cream sticks, toothpicks, chopsticks                                                     |
| G48    |         15 | 0.00516854  |  0.0016615   |          89 |   0.134831  | Rope, synthetic                                                                              |
| G4     |         14 | 0.00449438  |  0.00155073  |          89 |   0.101124  | Small plastic bags; freezer, zip-lock etc.                                                   |
| G90    |         14 | 0.00247191  |  0.00155073  |          89 |   0.101124  | Plastic flower pots                                                                          |
| G943   |         14 | 0.00247191  |  0.00155073  |          89 |   0.0337079 | Fencing agriculture, plastic                                                                 |
| G210   |         14 | 0.00325843  |  0.00155073  |          89 |   0.0449438 | Other glass/ceramic                                                                          |
| G148   |         14 | 0.00325843  |  0.00155073  |          89 |   0.0786517 | Cardboard (boxes and fragments)                                                              |
| G34    |         14 | 0.00449438  |  0.00155073  |          89 |   0.134831  | Cutlery, plates and trays                                                                    |
| G149   |         13 | 0.0047191   |  0.00143996  |          89 |   0.0786517 | Paper packaging                                                                              |
| G170   |         13 | 0.00292135  |  0.00143996  |          89 |   0.11236   | Wood (processed)                                                                             |
| G26    |         11 | 0.00382022  |  0.00121843  |          89 |   0.11236   | Cigarette lighters                                                                           |
| G59    |         11 | 0.00348315  |  0.00121843  |          89 |   0.101124  | Fishing line monofilament (angling)                                                          |
| G161   |         11 | 0.00325843  |  0.00121843  |          89 |   0.0561798 | Processed timber                                                                             |
| G101   |         10 | 0.00325843  |  0.00110767  |          89 |   0.0786517 | Dog feces bag                                                                                |
| G7     |         10 | 0.00314607  |  0.00110767  |          89 |   0.0898876 | Drink bottles < = 0.5L                                                                       |
| G142   |         10 | 0.0047191   |  0.00110767  |          89 |   0.0449438 | Rope , string or nets                                                                        |
| G134   |          9 | 0.00258427  |  0.000996899 |          89 |   0.0674157 | Other rubber                                                                                 |
| G28    |          9 | 0.00382022  |  0.000996899 |          89 |   0.0898876 | Pens, lids, mechanical pencils etc.                                                          |
| G931   |          9 | 0.00303371  |  0.000996899 |          89 |   0.0449438 | Tape-caution for barrier, police, construction etc.                                          |
| G65    |          8 | 0.00134831  |  0.000886132 |          89 |   0.0337079 | Buckets                                                                                      |
| G115   |          8 | 0.00314607  |  0.000886132 |          89 |   0.0674157 | Foamed  plastic <5mm                                                                         |
| G917   |          8 | 0.00168539  |  0.000886132 |          89 |   0.0674157 | Terracotta balls                                                                             |
| G155   |          8 | 0.00157303  |  0.000886132 |          89 |   0.0898876 | Fireworks paper tubes and fragments                                                          |
| G158   |          7 | 0.00157303  |  0.000775366 |          89 |   0.0674157 | Other paper items                                                                            |
| G133   |          7 | 0.00179775  |  0.000775366 |          89 |   0.0674157 | Condoms incl. packaging                                                                      |
| G122   |          7 | 0.00651685  |  0.000775366 |          89 |   0.011236  | Plastic fragments ( >1mm)                                                                    |
| G939   |          7 | 0.00213483  |  0.000775366 |          89 |   0.0561798 | Flowers, plants plastic                                                                      |
| G933   |          7 | 0.00191011  |  0.000775366 |          89 |   0.0674157 | Bags, cases for accessories; glasses, electronics, incl. straps, pieces, plstc. nylon etc.   |
| G194   |          7 | 0.00303371  |  0.000775366 |          89 |   0.0674157 | Cables, metal wire(s) often inside rubber or plastic tubes                                   |
| G118   |          7 | 0.00235955  |  0.000775366 |          89 |   0.0337079 | Small industrial spheres <5mm                                                                |
| G901   |          6 | 0.00157303  |  0.000664599 |          89 |   0.0561798 | Mask medical, synthetic                                                                      |
| G124   |          6 | 0.00404494  |  0.000664599 |          89 |   0.0449438 | Other plastic or foam products                                                               |
| G2     |          6 | 0.00168539  |  0.000664599 |          89 |   0.0337079 | Bags                                                                                         |
| G176   |          6 | 0.00224719  |  0.000664599 |          89 |   0.0449438 | Cans, food                                                                                   |
| G49    |          6 | 0.00247191  |  0.000664599 |          89 |   0.0449438 | Rope > 1cm                                                                                   |
| G921   |          5 | 0.00101124  |  0.000553833 |          89 |   0.0561798 | Ceramic tile and pieces                                                                      |
| G68    |          5 | 0.00213483  |  0.000553833 |          89 |   0.0561798 | Fiberglass fragments                                                                         |
| G925   |          5 | 0.000674157 |  0.000553833 |          89 |   0.0337079 | Packets: desiccant/ moisture absorbers, plastic case filled with silica                      |
| G919   |          5 | 0.0011236   |  0.000553833 |          89 |   0.0337079 | Nails, screws, bolts etc.                                                                    |
| G141   |          5 | 0.00269663  |  0.000553833 |          89 |   0.0337079 | Carpet                                                                                       |
| G20    |          5 | 0.00157303  |  0.000553833 |          89 |   0.0561798 | Caps and lids                                                                                |
| G36    |          5 | 0.00202247  |  0.000553833 |          89 |   0.0449438 | Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc. |
| G116   |          4 | 0.00179775  |  0.000443066 |          89 |   0.011236  | Granules <5mm                                                                                |
| G913   |          4 | 0.000674157 |  0.000443066 |          89 |   0.0449438 | Pacifier                                                                                     |
| G918   |          4 | 0.00101124  |  0.000443066 |          89 |   0.0449438 | Safety pins, paper clips, small metal utility items                                          |
| G135   |          4 | 0.00146067  |  0.000443066 |          89 |   0.0449438 | Clothes, footware, headware, gloves                                                          |
| G37    |          4 | 0.000674157 |  0.000443066 |          89 |   0.0449438 | Mesh bags                                                                                    |
| G167   |          4 | 0.00101124  |  0.000443066 |          89 |   0.0224719 | Matches or fireworks                                                                         |
| G146   |          4 | 0.00101124  |  0.000443066 |          89 |   0.0224719 | Paper, cardboard                                                                             |
| G145   |          4 | 0.00123596  |  0.000443066 |          89 |   0.0337079 | Other textiles                                                                               |
| G103   |          4 | 0.000898876 |  0.000443066 |          89 |   0.0449438 | Plastic fragments rounded <5mm                                                               |
| G143   |          4 | 0.00134831  |  0.000443066 |          89 |   0.0449438 | Sails and canvas                                                                             |
| G64    |          4 | 0.00123596  |  0.000443066 |          89 |   0.0224719 | Fenders                                                                                      |
| G151   |          3 | 0.000786517 |  0.0003323   |          89 |   0.0224719 | Cartons, Tetrapacks                                                                          |
| G930   |          3 | 0.000674157 |  0.0003323   |          89 |   0.0337079 | Foam earplugs                                                                                |
| G182   |          3 | 0.00179775  |  0.0003323   |          89 |   0.0224719 | Fishing; hooks, weights, lures, sinkers etc.                                                 |
| G6     |          3 | 0.000561798 |  0.0003323   |          89 |   0.011236  | Bottles and containers, plastic non food/drink                                               |
| G38    |          3 | 0.00157303  |  0.0003323   |          89 |   0.0337079 | Coverings; plastic packaging, sheeting for protecting large cargo items                      |
| G119   |          3 | 0.00280899  |  0.0003323   |          89 |   0.011236  | Sheetlike user plastic (>1mm)                                                                |
| G12    |          3 | 0.000674157 |  0.0003323   |          89 |   0.0337079 | Cosmetics, non-beach use personal care containers                                            |
| G29    |          3 | 0.000674157 |  0.0003323   |          89 |   0.0224719 | Combs, brushes and sunglasses                                                                |
| G71    |          2 | 0.000337079 |  0.000221533 |          89 |   0.0224719 | Shoes sandals                                                                                |
| G43    |          2 | 0.000674157 |  0.000221533 |          89 |   0.0224719 | Tags fishing or industry (security tags, seals)                                              |
| G938   |          2 | 0.000561798 |  0.000221533 |          89 |   0.0224719 | Toothpicks, dental floss plastic                                                             |
| G157   |          2 | 0.00146067  |  0.000221533 |          89 |   0.0224719 | Paper                                                                                        |
| G202   |          2 | 0.00146067  |  0.000221533 |          89 |   0.0224719 | Light bulbs                                                                                  |
| G929   |          2 | 0.000561798 |  0.000221533 |          89 |   0.0224719 | Electronics and pieces; sensors, headsets etc.                                               |
| G174   |          2 | 0.000224719 |  0.000221533 |          89 |   0.0224719 | Aerosol spray cans                                                                           |
| G926   |          2 | 0.000337079 |  0.000221533 |          89 |   0.0224719 | Chewing gum, often contains plastics                                                         |
| G188   |          2 | 0.000561798 |  0.000221533 |          89 |   0.011236  | Other cans < 4 L                                                                             |
| G129   |          2 | 0.000561798 |  0.000221533 |          89 |   0.0224719 | Inner tubes and rubber sheets                                                                |
| G197   |          2 | 0.000449438 |  0.000221533 |          89 |   0.0224719 | Other metal                                                                                  |
| G179   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Disposable BBQs                                                                              |
| G114   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Films  <5mm                                                                                  |
| G53    |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Nets and pieces < 50cm                                                                       |
| G52    |          1 | 0.000674157 |  0.000110767 |          89 |   0.011236  | Nets and pieces                                                                              |
| G104   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Plastic fragments subrounded <5mm                                                            |
| G97    |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Toilet fresheners                                                                            |
| G11    |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Cosmetics for the beach, e.g. sunblock                                                       |
| G5     |          1 | 0.00101124  |  0.000110767 |          89 |   0.011236  | Generic plastic bags                                                                         |
| G150   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Milk cartons, tetrapack                                                                      |
| G111   |          1 | 0.00011236  |  0.000110767 |          89 |   0.011236  | Spheruloid pellets < 5mm                                                                     |
| G154   |          1 | 0.000337079 |  0.000110767 |          89 |   0.011236  | Newspapers or magazines                                                                      |
| G8     |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Drink bottles  > 0.5L                                                                        |
| G916   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Pencils and pieces                                                                           |
| G138   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Shoes and sandals                                                                            |
| G934   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Sandbag, plastic for flood, erosion control etc..                                            |
| G195   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Batteries - household                                                                        |
| G41    |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Glove industrial/professional                                                                |
| G128   |          1 | 0.000898876 |  0.000110767 |          89 |   0.011236  | Tires and belts                                                                              |
| G171   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Other wood < 50cm                                                                            |
| G190   |          1 | 0.00011236  |  0.000110767 |          89 |   0.011236  | Paint cans                                                                                   |
| G172   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Other wood > 50cm                                                                            |
| G61    |          1 | 0.000337079 |  0.000110767 |          89 |   0.011236  | Other fishing related                                                                        |
| G214   |          1 | 0.000449438 |  0.000110767 |          89 |   0.011236  | Oil/tar                                                                                      |

## Sampling stratification Bern canton 2020-01-01 2021-12-31: The environmental features surrounding the survey location.

Each survey location is surounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken according to the different conditions.



The sampling stratification table quantifies what proportion of the samples were collected according to the proportion of the buffer
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone.


<!--- INSTRUCTION_START

__How to interpret sampling stratification table:__

The sampling stratification table quantifies what proportion of the samples were conducted according to the proportion of the buffer
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone.


Therefore when you answer questions about sampling stratification you must qualify that with the corresponding value
in the sampling stratification and trash density table, in parentheses. For example, using the example tables
below, we would say 16% (0.53 pcs/m) of all samples were taken at locations where buildings occupied 80 - 100% of the buffer zone. 

__Example sampling stratification and trash density table:__


|   Proportion of buffer zone |   ('pcs/m', 'buildings') |  ('pcs/m', 'wetlands') |  ('pcs/m', 'forest')  |  ('pcs/m', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.37 |                    .46 |             .52  |                    0.31  |   
|                    20 - 40% |                0.45 |              no samples|             .33 |                    0.49       |
|                    40 - 60% |                0.57 |              no samples|       no samples       |                    no samples |
|                    60 - 80% |                0.5  |              no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.53  |              no samples|       no samples     |                   no samples    |

__Example sampling stratification table:__


|   Proportion of buffer zone |   ('Proportion of samples collected', 'buildings') |  ('Proportion of samples collected', 'wetlands') |  ('Proportion of samples collected', 'forest')  |  ('Proportion of samples collected', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                     0.13 |                       1|                 0.85  |                    0.95      |   
|                    20 - 40% |                     0.21 |              no samples|                   0.1 |                    0.05      |
|                    40 - 60% |                     0.22 |             no samples |             .05       |                    no samples|
|                    60 - 80% |                    0.18  |             no samples |            no samples |                 no samples   |
|                    80 - 100%|                    0.16  |              no samples|       no samples      |                   no samples  | 


__Example interpretation of the sampling stratification and trash density table__

The average objects per meter based on the sampling-stratification was as follows: 
where buildings occupied 0 - 20% of the buffer 13% of all samples, (0.37 pcs/m)

where buildings occupied 20 - 40% of the buffer 21% of all samples, (0.03 pcs/m)

where buildings occupied 40 - 60% of the buffer 22% of all samples, (0.01 pcs/m)

where buildings occupied 60 - 80% of the buffer 18% of all samples, (0.37 pcs/m)

where buildings occupied 80 - 100% of the buffer 16% of all samples, (0.49, pcs/m)



1. no samples indicates that no samples were collected at a location that fits this description.

2. Definitions of Urban, Rural or mixed

   * Urban Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column are greater than 50%.

   * Rural Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column are greater than 50%.

   * Mixed Areas: Does not meet the criteria of urban or rural.

   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**

1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column. In the example 
table above, the proportion of samples where buildings occupy 60-80% of the buffer is .18  and the proportion of samples 
where buildings occupy 80 - 100% of the buffer is .16 therefore the proportion of samples where buildings occupy more than 
50% of the buffer is .16 + .18 or 34%.


2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column. In the example 
table above, the proportion of samples where forest occupy 60-80% of the buffer is 0 (no samples)  and the proportion of 
samples where forest occupy 80 - 100% of the buffer is 0 (no samples) therefore the proportion of samples where forest occupy
more than 50% of the buffer is 0.


3. Make the conclusion: If the value of test one is greater than 50% then the area is urban. If the value of test two
is greater than 50% then the area is considered rural. If neither test one or test two is greater than 50% the classification is mixed.


 

INSTRUCTION_END -->
Generate a narrative summary based on the following table. Consider the example above

| proportion of buffer   | ('Proportion of samples collected', 'buildings')   | ('Proportion of samples collected', 'wetlands')   | ('Proportion of samples collected', 'forest')   | ('Proportion of samples collected', 'public-services')   | ('Proportion of samples collected', 'recreation')   | ('Proportion of samples collected', 'undefined')   | ('Proportion of samples collected', 'streets')   | ('Proportion of samples collected', 'vineyards')   | ('Proportion of samples collected', 'orchards')   |
|:-----------------------|:---------------------------------------------------|:--------------------------------------------------|:------------------------------------------------|:---------------------------------------------------------|:----------------------------------------------------|:---------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------|:--------------------------------------------------|
| 0-20%                  | 30.3%                                              | 100.0%                                            | 27.0%                                           | 98.9%                                                    | 100.0%                                              | 34.8%                                              | 44.9%                                            | 100.0%                                             | 100.0%                                            |
| 20-40%                 | 31.5%                                              | none                                              | 64.0%                                           | 1.1%                                                     | none                                                | 12.4%                                              | 36.0%                                            | none                                               | none                                              |
| 40-60%                 | 25.8%                                              | none                                              | 9.0%                                            | none                                                     | none                                                | 51.7%                                              | 11.2%                                            | none                                               | none                                              |
| 60-80%                 | 10.1%                                              | none                                              | none                                            | none                                                     | none                                                | 1.1%                                               | 5.6%                                             | none                                               | none                                              |
| 80-100%                | 2.2%                                               | none                                              | none                                            | none                                                     | none                                                | none                                               | 2.2%                                             | none                                               | none                                              |

## Sampling stratification and trash density Bern canton 2020-01-01 2021-12-31: The changes in the observed litter density and the changes in land use



The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the buffer 
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the 
buffer zone that is dedicated to a particular land use feature.


<!--- INSTRUCTION_START

__How to interpret sampling stratification and trash density table:__

The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the buffer 
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the 
buffer zone that is dedicated to a particular land use feature.


Therefore when you answer questions about sampling stratification and trash density you must qualify that with the corresponding value
in the sampling stratification table. For example, if you say that the trash density is 0.05 pcs/m in an area where buildings occupy 0-20% of the buffer zone,
you must also say that 6% of the samples were taken in an area where buildings occupy 0-20% of the buffer zone.


__Example sampling stratification and trash density table:__


|   Proportion of buffer zone |   ('pcs/m', 'buildings') |  ('pcs/m', 'wetlands') |  ('pcs/m', 'forest')  |  ('pcs/m', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.37 |                    .46 |             .52  |                    0.31  |   
|                    20 - 40% |                0.45 |              no samples|             .33 |                    0.49       |
|                    40 - 60% |                0.57 |              no samples|       no samples       |                    no samples |
|                    60 - 80% |                0.5  |              no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.53  |              no samples|       no samples     |                   no samples    |


__Example sampling stratification table:__


|   Proportion of buffer zone |   ('Proportion of samples collected', 'buildings') |  ('Proportion of samples collected', 'wetlands') |  ('Proportion of samples collected', 'forest')  |  ('Proportion of samples collected', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.13 |                   1|             0.85  |                    0.95  |   
|                    20 - 40% |                0.21 |          no samples|             0.1 |                    0.05       |
|                    40 - 60% |                0.22 |         no samples |       .05       |                    no samples |
|                    60 - 80% |                0.18  |        no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.16  |        no samples|       no samples     |                   no samples    | 



__Example interpretation of the sampling stratification and trash density table__

The average objects per meter based on the sampling-stratification was as follows: 
where buildings occupied 0 - 20% of the buffer (13% of all samples) the average objects per meter was 0.05

where buildings occupied 20 - 40% of the buffer (21% of all samples) the average objects per meter was 0.03

where buildings occupied 40 - 60% of the buffer (22% of all samples) the average objects per meter was 0.01

where buildings occupied 60 - 80% of the buffer (18% of all samples) the average objects per meter was 0.37

where buildings occupied 80 - 100% of the buffer (16% of all samples) the average objects per meter was 0.49


1. no samples indicates that no samples were takes at a location that fits this description.

2. Definitions of Urban, Rural or mixed

   * Urban Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column are greater than 50%.

   * Rural Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column are greater than 50%.

   * Mixed Areas: Does not meet the criteria of urban or rural.

   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**

1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column. In the example 
table above, the proportion of samples where buildings occupy 60-80% of the buffer is .18  and the proportion of samples 
where buildings occupy 80 - 100% of the buffer is .16 therefore the proportion of samples where buildings occupy more than 
50% of the buffer is .16 + .18 or 34%.


2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column. In the example 
table above, the proportion of samples where forest occupy 60-80% of the buffer is 0 (no samples)  and the proportion of 
samples where forest occupy 80 - 100% of the buffer is 0 (no samples) therefore the proportion of samples where forest occupy
more than 50% of the buffer is 0.


3. Make the conclusion: If the value of test one is greater than 50% then the area is urban. If the value of test two
is greater than 50% then the area is considered rural. If neither test one or test two is greater than 50% the classification is mixed.


INSTRUCTION_END -->


Generate a narrative summary based on the following table. Consider the example above 

| proportion of buffer   |   ('Pieces of trash per meter', 'buildings') | ('Pieces of trash per meter', 'wetlands')   | ('Pieces of trash per meter', 'forest')   | ('Pieces of trash per meter', 'public-services')   | ('Pieces of trash per meter', 'recreation')   | ('Pieces of trash per meter', 'undefined')   |   ('Pieces of trash per meter', 'streets') | ('Pieces of trash per meter', 'vineyards')   | ('Pieces of trash per meter', 'orchards')   |
|:-----------------------|---------------------------------------------:|:--------------------------------------------|:------------------------------------------|:---------------------------------------------------|:----------------------------------------------|:---------------------------------------------|-------------------------------------------:|:---------------------------------------------|:--------------------------------------------|
| 0-20%                  |                                      2.36778 | 2.7580898876404496                          | 3.02                                      | 2.7880681818181814                                 | 2.7580898876404496                            | 3.223548387096774                            |                                    1.64725 | 2.7580898876404496                           | 2.7580898876404496                          |
| 20-40%                 |                                      2.525   | none                                        | 2.8570175438596492                        | 0.12                                               | none                                          | 3.0963636363636367                           |                                    4.51094 | none                                         | none                                        |
| 40-60%                 |                                      4.08913 | none                                        | 1.2675                                    | none                                               | none                                          | 2.4186956521739136                           |                                    2.907   | none                                         | none                                        |
| 60-80%                 |                                      1.59    | none                                        | none                                      | none                                               | none                                          | 0.22                                         |                                    1.168   | none                                         | none                                        |
| 80-100%                |                                      1.24    | none                                        | none                                      | none                                               | none                                          | none                                         |                                    0.16    | none                                         | none                                        |

## Grid forecast Bern canton 2020-01-01 2021-12-31


### Grid Approximation method:

Grid approximation is a numerical technique used to approximate the distribution of a parameter. The technique employed here uses conditional probability to answer the question _What am I likely to observe given what was observed previously, under similar conditions ?_ The conditions are the land use features (reference sampling stratification table) and the proportion of the buffer zone dedicated to each land use feature. An inference table is constructed using observations from other locations that are similar to the survey location and the observed results. An inference table is a simple way to apply Bayes' theorem to estimate the posterior distribution of the parameter of interest. The data for the prior is randomly selected from the existing data with similar land use features, similarity is measured with cosine similarity or manhattan distance. The data for the prior does not include the data from the likelihood (ie the data defined by the report parameters).

In this report their maybe three priors that represent different possible interpretation of the survey results, each report is different.

 <!--- INSTRUCTION_START
The current report may not have all three priors, the priors are selected based on the similarity of the data. You must consult the users report and identify the priors that were used.  
You must locate the section that corresponds to the prior that was used and provide the results for that prior. 
INSTRUCTION_END -->

The grid approximation method is used to estimate the posterior distribution of the parameter of interest (e.g., the litter density) given the land use profile of the survey location. Therefore this method is an indicator of what the next survey will yield given the land use profile of the survey locations of interest. The steps of the grid approximation are the same for all three priors. The only difference is the data used for the prior (in-boundary, out-boundary, prior).

1. **Parameter Space Discretization**: Divide the continuous parameter space into a discrete grid of points. We use the 0 as the start of the grid and the 99th percentile of the observed values as the grid limit and we evaluate the function every 0.01.

2. **Evaluation of Function**: Evaluate the statistical function of interest (e.g., likelihood, posterior) at each grid point. This step gives a set of unnormalized values across the grid.

3. **Normalization**:
   - **Sum the Values**: Compute the sum of the evaluated function values over all grid points. This sum is used as the normalizing constant.
   - **Normalize**: Divide each evaluated function value by the normalizing constant to ensure that the sum (or integral, in the continuous case) over the grid points is 1. This is crucial when dealing with probability distributions, as it ensures the result is a valid probability distribution.

- **Probability Distributions**: In Bayesian inference, the posterior distribution needs to be properly normalized so that it integrates (or sums) to 1 over the parameter space.
- **Accuracy of Estimates**: Normalization ensures that derived quantities, like expectations or credible intervals, are accurate representations of the true statistical measures.

The normalization step is particularly crucial in Bayesian grid approximations because it transforms the unnormalized posterior into a proper probability distribution, enabling meaningful statistical inference.


### Combined prior grid approximation
These are random samples from all of the data (in different of geographic boundary) not including the likelihood and limited to the requested end date.  The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples This prior makes no difference between the locations inside or outside the boundary of interest. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations (indifferent of the geographic boundary) ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.6200000000000003
The expected posterior distribution is a grid approximation from 0 to 43.59 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   1.4428  |
| std   |   1.33903 |
| min   |   0       |
| 25%   |   0.5475  |
| 50%   |   1.115   |
| 75%   |   1.9025  |
| max   |   6.73    |

### In boundary grid approximation
This prior distribution is selected from random samples from within the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood feature variables  and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations in the geographic boundary ?'  There are fewer samples in the prior than the likelihood. All prior samples were used
The expected posterior distribution is a grid approximation from 0 to 11.02 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   1.0143  |
| std   |   1.14643 |
| min   |   0       |
| 25%   |   0.175   |
| 50%   |   0.67    |
| 75%   |   1.2725  |
| max   |   4.84    |

### Out boundary grid approximation
This prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations outside the geographic boundary ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.5800000000000003
The expected posterior distribution is a grid approximation from 0 to 43.17 every 0.01.

|       |    pcs/m |
|:------|---------:|
| count | 100      |
| mean  |   1.6717 |
| std   |   1.727  |
| min   |   0      |
| 25%   |   0.4675 |
| 50%   |   1.03   |
| 75%   |   2.2025 |
| max   |   8.53   |




### Cluster analysis Bern canton 2020-01-01 2021-12-31


Bern: Cluster compositionThe survey locations were labeled according to the type and magnitude of land use in a 1 500 m buffer zone aroundaround each survey location. A cluster analysis was performed using K-Means clustering, the optimal amount of clusters was determined using the elbow method. Each cluster represents a group of locations that have similar land use profiles, that is the locations are surrounded by similar quantities of buildings or forest or undefined land use.We consider the cluster composition and the proportion of each cluster dedicated to a particular land use. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location whose buffer zone was 45% dedicated to forest. 

The following are the summary results of a cluster analysis. The columns are the features that were used to make the clusters. The optimal number of clusters was
determined using the elbow method (you can check the docs for this: https://hammerdirt-analyst.github.io/feb_2024/titlepage.html). The table displays the average magnitude
of each feature in the cluster. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location that was
45% dedicated to forest.

Table has the following format:

1. the columns are the measured land use features
2. the index is the cluster number
3. the value is the proportion of the cluster that is attributed to that column. For example if buildings in cluster 1 = .17 it means that the average magnitude of
the buildings variable was 0.17 in cluster 1.

Convert the following table into a paragraph, reporting the values for each column along with their cluster number values without any comments or analysis:

|   cluster |   buildings |   wetlands |   forest |   public-services |   recreation |   undefined |   streets |   vineyards |   orchards |
|----------:|------------:|-----------:|---------:|------------------:|-------------:|------------:|----------:|------------:|-----------:|
|         0 |       0.035 |          0 |    0.212 |             0.002 |        0     |       0.753 | 0.0929149 |           0 |       0    |
|         1 |       0.167 |          0 |    0.559 |             0.038 |        0.002 |       0.133 | 0.0524869 |           0 |       0.14 |
|         2 |       0.463 |          0 |    0.33  |             0.05  |        0.006 |       0.206 | 0.607656  |           0 |       0    |





Bern: Average density per cluster
The following are the observed sample average per cluster. The units is objects per meter of beach. The columns are the use case of the objects: personal or professional. The index is
the cluster number.

Table has the following format:

1. the columns are the object use case
2. the index is the cluster number
3. the value is the objects found per meter of beach

Convert the following table into a paragraph, reporting the values for each column along with their respective cluster values without any comments or analysis:
The narrative needs to be in paragraph format.

|   cluster |   pcs/m |
|----------:|--------:|
|         0 | 2.381   |
|         1 | 0.746   |
|         2 | 3.60853 |



### Summary of regression methods Bern canton 2020-01-01 2021-12-31: 

In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. The feature variables are the land-use features identified in the land-use profile. From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model with the highest r² is then used in the BaggingRegressor and the VotingRegressor.





The following table details the results from different regression analysis of our data.

The table has the following format:

1. Model: the type of regression model used
2. R²: The coefficient of determination
3. MSE: the mean squared error

Generate a narrative summary based on the following table. You need to include all the models and the R² and MSE result.
The narrative needs to be in paragraph format.

|    | Model                            |         R² |      MSE |
|---:|:---------------------------------|-----------:|---------:|
|  0 | Linear Regression                | -1.14988   | 1.80444  |
|  1 | Random Forest Regression         |  0.254817  | 0.625448 |
|  2 | Gradient Boosting Regression     |  0.155916  | 0.708458 |
|  3 | Theil-Sen Regressor              | -0.139135  | 0.956101 |
|  4 | Bagging:Random Forest Regression |  0.251239  | 0.628451 |
|  5 | Voting                           | -0.0984127 | 0.921922 |



### Feature and permutation importance Bern canton 2020-01-01 2021-12-31



__Model feature importance__

Feature importance is a technique used in machine learning to identify and quantify the significance of different input variables (features) in predicting the target variable. In models like decision trees, random forests, and gradient boosting machines, feature importance is often calculated by measuring how much the model's accuracy or error changes when a particular feature is included versus when it is excluded. 
The following table details the model feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  7 | vineyards       |   0.304018   |
|  6 | streets         |   0.214139   |
|  2 | forest          |   0.165438   |
|  4 | recreation      |   0.127264   |
|  0 | buildings       |   0.0711197  |
|  3 | public-services |   0.0577698  |
|  5 | undefined       |   0.0555365  |
|  1 | wetlands        |   0.00471504 |



__Permutation feature importance__

Permutation importance is a model-agnostic method for assessing the importance of individual features in a predictive model. It is particularly useful because it can be applied to any type of model, whether it's a linear model, a decision tree, or a complex ensemble model. This method involves randomly shuffling the values of a feature in the dataset and observing the impact on the model's performance. A significant drop in performance indicates that the feature is important.
The following table details the permutation feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  6 | streets         |   0.266074   |
|  2 | forest          |   0.193992   |
|  4 | recreation      |   0.124154   |
|  5 | undefined       |   0.0681484  |
|  0 | buildings       |   0.0597527  |
|  1 | wetlands        |   0.00232975 |
|  7 | vineyards       |  -0.0163049  |
|  3 | public-services |  -0.0367921  |


## Inventory items Bern canton 2020-01-01 2021-12-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |       pcs/m |   % of total |   sample_id |   fail rate | object                                                                                       |
|:-------|-----------:|------------:|-------------:|------------:|------------:|:---------------------------------------------------------------------------------------------|
| G27    |       1671 | 0.423708    |  0.185091    |          89 |   0.808989  | Cigarette filters                                                                            |
| Gfrags |       1323 | 0.45573     |  0.146544    |          89 |   0.88764   | Fragmented plastics                                                                          |
| G67    |        686 | 0.237753    |  0.0759858   |          89 |   0.775281  | Industrial sheeting                                                                          |
| G30    |        589 | 0.186292    |  0.0652415   |          89 |   0.797753  | Food wrappers; candy, snacks                                                                 |
| Gfoams |        474 | 0.12191     |  0.0525033   |          89 |   0.617978  | Expanded polystyrene                                                                         |
| G200   |        348 | 0.121685    |  0.0385467   |          89 |   0.651685  | Glass drink bottles, pieces                                                                  |
| G941   |        261 | 0.0869663   |  0.0289101   |          89 |   0.494382  | Packaging films nonfood or unknown                                                           |
| G74    |        240 | 0.0335714   |  0.026584    |          89 |   0.775281  | Foam packaging/insulation/polyurethane                                                       |
| Gcaps  |        227 | 0.0652809   |  0.025144    |          89 |   0.595506  | plastic caps, lid rings: G21, G22, G23, G24                                                  |
| G112   |        196 | 0.0538202   |  0.0217102   |          89 |   0.325843  | Industrial pellets (nurdles)                                                                 |
| G89    |        160 | 0.0566292   |  0.0177226   |          89 |   0.516854  | Plastic construction waste                                                                   |
| G98    |        140 | 0.0558427   |  0.0155073   |          89 |   0.235955  | Diapers - wipes                                                                              |
| G904   |        116 | 0.0420225   |  0.0128489   |          89 |   0.47191   | Fireworks; rocket caps, exploded parts & packaging                                           |
| G117   |        115 | 0.0296629   |  0.0127381   |          89 |   0.292135  | Styrofoam < 5mm                                                                              |
| G95    |        113 | 0.0348315   |  0.0125166   |          89 |   0.449438  | Cotton bud/swab sticks                                                                       |
| G25    |        111 | 0.0440449   |  0.0122951   |          89 |   0.449438  | Tobacco; plastic packaging, containers                                                       |
| G213   |        103 | 0.0293258   |  0.0114089   |          89 |   0.258427  | Paraffin wax                                                                                 |
| G940   |         97 | 0.0288764   |  0.0107444   |          89 |   0.157303  | Foamed EVA (flexible plastic) for crafts & watersports                                       |
| G177   |         97 | 0.0295506   |  0.0107444   |          89 |   0.460674  | Foil wrappers, aluminum foil                                                                 |
| G156   |         84 | 0.0203371   |  0.00930439  |          89 |   0.224719  | Paper fragments                                                                              |
| G106   |         82 | 0.0214607   |  0.00908285  |          89 |   0.314607  | Plastic fragments angular <5mm                                                               |
| G50    |         60 | 0.0194382   |  0.00664599  |          89 |   0.370787  | String < 1cm                                                                                 |
| G35    |         54 | 0.0169663   |  0.00598139  |          89 |   0.348315  | Straws and stirrers                                                                          |
| G31    |         54 | 0.0139326   |  0.00598139  |          89 |   0.314607  | Lollypop sticks                                                                              |
| G922   |         51 | 0.0195506   |  0.00564909  |          89 |   0.303371  | Labels, bar codes                                                                            |
| G178   |         51 | 0.0152809   |  0.00564909  |          89 |   0.348315  | Metal bottle caps, lids & pull tabs from cans                                                |
| G10    |         50 | 0.0164045   |  0.00553833  |          89 |   0.325843  | Food containers single use foamed or plastic                                                 |
| G73    |         48 | 0.0124719   |  0.00531679  |          89 |   0.213483  | Foamed items & pieces (non packaging/insulation) foamed sponge material                      |
| G211   |         46 | 0.0123596   |  0.00509526  |          89 |   0.325843  | Other medical (swabs, bandaging, adhesive plaster)                                           |
| G936   |         45 | 0.0122472   |  0.00498449  |          89 |   0.191011  | Sheeting ag. greenhouse film                                                                 |
| G33    |         43 | 0.0180899   |  0.00476296  |          89 |   0.280899  | Cups, lids, single use foamed and hard plastic                                               |
| G32    |         40 | 0.0133708   |  0.00443066  |          89 |   0.303371  | Toys and party favors                                                                        |
| G204   |         40 | 0.0132584   |  0.00443066  |          89 |   0.123596  | Construction material; bricks, pipes, cement                                                 |
| G153   |         38 | 0.0110112   |  0.00420913  |          89 |   0.157303  | Cups, food containers, wrappers (paper)                                                      |
| G944   |         34 | 0.0058427   |  0.00376606  |          89 |   0.0337079 | Pellet mass from injection molding                                                           |
| G66    |         33 | 0.00955056  |  0.00365529  |          89 |   0.292135  | Straps/bands;  hard, plastic package fastener                                                |
| G186   |         33 | 0.00730337  |  0.00365529  |          89 |   0.191011  | Industrial scrap                                                                             |
| G87    |         33 | 0.00876404  |  0.00365529  |          89 |   0.202247  | Tape, masking/duct/packing                                                                   |
| G908   |         33 | 0.0103371   |  0.00365529  |          89 |   0.235955  | Tape; electrical, insulating                                                                 |
| G91    |         28 | 0.00786517  |  0.00310146  |          89 |   0.224719  | Biomass holder                                                                               |
| G923   |         28 | 0.00898876  |  0.00310146  |          89 |   0.191011  | Tissue, toilet paper, napkins, paper towels                                                  |
| G125   |         27 | 0.00707865  |  0.0029907   |          89 |   0.157303  | Balloons and balloon sticks                                                                  |
| G152   |         26 | 0.00910112  |  0.00287993  |          89 |   0.123596  | Cigarette boxes, tobacco related paper/cardboard                                             |
| G927   |         26 | 0.00640449  |  0.00287993  |          89 |   0.123596  | String trimmer line, used to cut grass, weeds, and shrubbery                                 |
| G96    |         25 | 0.0108989   |  0.00276916  |          89 |   0.146067  | Sanitary pads /panty liners/tampons and applicators                                          |
| G70    |         24 | 0.0058427   |  0.0026584   |          89 |   0.191011  | Shotgun cartridges                                                                           |
| G3     |         24 | 0.0058427   |  0.0026584   |          89 |   0.157303  | Bags; plastic shopping/carrier/grocery and pieces                                            |
| G137   |         24 | 0.0106742   |  0.0026584   |          89 |   0.101124  | Clothing, towels & rags                                                                      |
| G191   |         23 | 0.00820225  |  0.00254763  |          89 |   0.168539  | Wire and mesh                                                                                |
| G905   |         23 | 0.0052809   |  0.00254763  |          89 |   0.191011  | Hair clip,  hair ties, personal accessories plastic                                          |
| G159   |         22 | 0.00539326  |  0.00243686  |          89 |   0.157303  | Corks                                                                                        |
| G201   |         21 | 0.00808989  |  0.0023261   |          89 |   0.0898876 | Jars, includes pieces                                                                        |
| G100   |         20 | 0.00707865  |  0.00221533  |          89 |   0.191011  | Medical; containers/tubes/ packaging                                                         |
| G175   |         20 | 0.00516854  |  0.00221533  |          89 |   0.11236   | Cans, beverage                                                                               |
| G942   |         20 | 0.00460674  |  0.00221533  |          89 |   0.11236   | Plastic shavings from lathes, CNC machining                                                  |
| G928   |         19 | 0.00955056  |  0.00210456  |          89 |   0.134831  | Ribbons and bows                                                                             |
| G208   |         19 | 0.00516854  |  0.00210456  |          89 |   0.0786517 | Glass or ceramic fragments > 2.5 cm                                                          |
| G93    |         18 | 0.00842697  |  0.0019938   |          89 |   0.134831  | Cable ties; steggel, zip, zap straps                                                         |
| G203   |         18 | 0.00550562  |  0.0019938   |          89 |   0.0898876 | Tableware ceramic or glass, cups, plates, pieces                                             |
| G144   |         17 | 0.00516854  |  0.00188303  |          89 |   0.011236  | Tampons                                                                                      |
| G198   |         17 | 0.00595506  |  0.00188303  |          89 |   0.168539  | Other metal pieces < 50cm                                                                    |
| G914   |         16 | 0.00348315  |  0.00177226  |          89 |   0.0898876 | Paperclips, clothespins, plastic utility items                                               |
| G131   |         15 | 0.00359551  |  0.0016615   |          89 |   0.11236   | Rubber bands                                                                                 |
| G165   |         15 | 0.00359551  |  0.0016615   |          89 |   0.134831  | Ice cream sticks, toothpicks, chopsticks                                                     |
| G48    |         15 | 0.00516854  |  0.0016615   |          89 |   0.134831  | Rope, synthetic                                                                              |
| G4     |         14 | 0.00449438  |  0.00155073  |          89 |   0.101124  | Small plastic bags; freezer, zip-lock etc.                                                   |
| G90    |         14 | 0.00247191  |  0.00155073  |          89 |   0.101124  | Plastic flower pots                                                                          |
| G943   |         14 | 0.00247191  |  0.00155073  |          89 |   0.0337079 | Fencing agriculture, plastic                                                                 |
| G210   |         14 | 0.00325843  |  0.00155073  |          89 |   0.0449438 | Other glass/ceramic                                                                          |
| G148   |         14 | 0.00325843  |  0.00155073  |          89 |   0.0786517 | Cardboard (boxes and fragments)                                                              |
| G34    |         14 | 0.00449438  |  0.00155073  |          89 |   0.134831  | Cutlery, plates and trays                                                                    |
| G149   |         13 | 0.0047191   |  0.00143996  |          89 |   0.0786517 | Paper packaging                                                                              |
| G170   |         13 | 0.00292135  |  0.00143996  |          89 |   0.11236   | Wood (processed)                                                                             |
| G26    |         11 | 0.00382022  |  0.00121843  |          89 |   0.11236   | Cigarette lighters                                                                           |
| G59    |         11 | 0.00348315  |  0.00121843  |          89 |   0.101124  | Fishing line monofilament (angling)                                                          |
| G161   |         11 | 0.00325843  |  0.00121843  |          89 |   0.0561798 | Processed timber                                                                             |
| G101   |         10 | 0.00325843  |  0.00110767  |          89 |   0.0786517 | Dog feces bag                                                                                |
| G7     |         10 | 0.00314607  |  0.00110767  |          89 |   0.0898876 | Drink bottles < = 0.5L                                                                       |
| G142   |         10 | 0.0047191   |  0.00110767  |          89 |   0.0449438 | Rope , string or nets                                                                        |
| G134   |          9 | 0.00258427  |  0.000996899 |          89 |   0.0674157 | Other rubber                                                                                 |
| G28    |          9 | 0.00382022  |  0.000996899 |          89 |   0.0898876 | Pens, lids, mechanical pencils etc.                                                          |
| G931   |          9 | 0.00303371  |  0.000996899 |          89 |   0.0449438 | Tape-caution for barrier, police, construction etc.                                          |
| G65    |          8 | 0.00134831  |  0.000886132 |          89 |   0.0337079 | Buckets                                                                                      |
| G115   |          8 | 0.00314607  |  0.000886132 |          89 |   0.0674157 | Foamed  plastic <5mm                                                                         |
| G917   |          8 | 0.00168539  |  0.000886132 |          89 |   0.0674157 | Terracotta balls                                                                             |
| G155   |          8 | 0.00157303  |  0.000886132 |          89 |   0.0898876 | Fireworks paper tubes and fragments                                                          |
| G158   |          7 | 0.00157303  |  0.000775366 |          89 |   0.0674157 | Other paper items                                                                            |
| G133   |          7 | 0.00179775  |  0.000775366 |          89 |   0.0674157 | Condoms incl. packaging                                                                      |
| G122   |          7 | 0.00651685  |  0.000775366 |          89 |   0.011236  | Plastic fragments ( >1mm)                                                                    |
| G939   |          7 | 0.00213483  |  0.000775366 |          89 |   0.0561798 | Flowers, plants plastic                                                                      |
| G933   |          7 | 0.00191011  |  0.000775366 |          89 |   0.0674157 | Bags, cases for accessories; glasses, electronics, incl. straps, pieces, plstc. nylon etc.   |
| G194   |          7 | 0.00303371  |  0.000775366 |          89 |   0.0674157 | Cables, metal wire(s) often inside rubber or plastic tubes                                   |
| G118   |          7 | 0.00235955  |  0.000775366 |          89 |   0.0337079 | Small industrial spheres <5mm                                                                |
| G901   |          6 | 0.00157303  |  0.000664599 |          89 |   0.0561798 | Mask medical, synthetic                                                                      |
| G124   |          6 | 0.00404494  |  0.000664599 |          89 |   0.0449438 | Other plastic or foam products                                                               |
| G2     |          6 | 0.00168539  |  0.000664599 |          89 |   0.0337079 | Bags                                                                                         |
| G176   |          6 | 0.00224719  |  0.000664599 |          89 |   0.0449438 | Cans, food                                                                                   |
| G49    |          6 | 0.00247191  |  0.000664599 |          89 |   0.0449438 | Rope > 1cm                                                                                   |
| G921   |          5 | 0.00101124  |  0.000553833 |          89 |   0.0561798 | Ceramic tile and pieces                                                                      |
| G68    |          5 | 0.00213483  |  0.000553833 |          89 |   0.0561798 | Fiberglass fragments                                                                         |
| G925   |          5 | 0.000674157 |  0.000553833 |          89 |   0.0337079 | Packets: desiccant/ moisture absorbers, plastic case filled with silica                      |
| G919   |          5 | 0.0011236   |  0.000553833 |          89 |   0.0337079 | Nails, screws, bolts etc.                                                                    |
| G141   |          5 | 0.00269663  |  0.000553833 |          89 |   0.0337079 | Carpet                                                                                       |
| G20    |          5 | 0.00157303  |  0.000553833 |          89 |   0.0561798 | Caps and lids                                                                                |
| G36    |          5 | 0.00202247  |  0.000553833 |          89 |   0.0449438 | Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc. |
| G116   |          4 | 0.00179775  |  0.000443066 |          89 |   0.011236  | Granules <5mm                                                                                |
| G913   |          4 | 0.000674157 |  0.000443066 |          89 |   0.0449438 | Pacifier                                                                                     |
| G918   |          4 | 0.00101124  |  0.000443066 |          89 |   0.0449438 | Safety pins, paper clips, small metal utility items                                          |
| G135   |          4 | 0.00146067  |  0.000443066 |          89 |   0.0449438 | Clothes, footware, headware, gloves                                                          |
| G37    |          4 | 0.000674157 |  0.000443066 |          89 |   0.0449438 | Mesh bags                                                                                    |
| G167   |          4 | 0.00101124  |  0.000443066 |          89 |   0.0224719 | Matches or fireworks                                                                         |
| G146   |          4 | 0.00101124  |  0.000443066 |          89 |   0.0224719 | Paper, cardboard                                                                             |
| G145   |          4 | 0.00123596  |  0.000443066 |          89 |   0.0337079 | Other textiles                                                                               |
| G103   |          4 | 0.000898876 |  0.000443066 |          89 |   0.0449438 | Plastic fragments rounded <5mm                                                               |
| G143   |          4 | 0.00134831  |  0.000443066 |          89 |   0.0449438 | Sails and canvas                                                                             |
| G64    |          4 | 0.00123596  |  0.000443066 |          89 |   0.0224719 | Fenders                                                                                      |
| G151   |          3 | 0.000786517 |  0.0003323   |          89 |   0.0224719 | Cartons, Tetrapacks                                                                          |
| G930   |          3 | 0.000674157 |  0.0003323   |          89 |   0.0337079 | Foam earplugs                                                                                |
| G182   |          3 | 0.00179775  |  0.0003323   |          89 |   0.0224719 | Fishing; hooks, weights, lures, sinkers etc.                                                 |
| G6     |          3 | 0.000561798 |  0.0003323   |          89 |   0.011236  | Bottles and containers, plastic non food/drink                                               |
| G38    |          3 | 0.00157303  |  0.0003323   |          89 |   0.0337079 | Coverings; plastic packaging, sheeting for protecting large cargo items                      |
| G119   |          3 | 0.00280899  |  0.0003323   |          89 |   0.011236  | Sheetlike user plastic (>1mm)                                                                |
| G12    |          3 | 0.000674157 |  0.0003323   |          89 |   0.0337079 | Cosmetics, non-beach use personal care containers                                            |
| G29    |          3 | 0.000674157 |  0.0003323   |          89 |   0.0224719 | Combs, brushes and sunglasses                                                                |
| G71    |          2 | 0.000337079 |  0.000221533 |          89 |   0.0224719 | Shoes sandals                                                                                |
| G43    |          2 | 0.000674157 |  0.000221533 |          89 |   0.0224719 | Tags fishing or industry (security tags, seals)                                              |
| G938   |          2 | 0.000561798 |  0.000221533 |          89 |   0.0224719 | Toothpicks, dental floss plastic                                                             |
| G157   |          2 | 0.00146067  |  0.000221533 |          89 |   0.0224719 | Paper                                                                                        |
| G202   |          2 | 0.00146067  |  0.000221533 |          89 |   0.0224719 | Light bulbs                                                                                  |
| G929   |          2 | 0.000561798 |  0.000221533 |          89 |   0.0224719 | Electronics and pieces; sensors, headsets etc.                                               |
| G174   |          2 | 0.000224719 |  0.000221533 |          89 |   0.0224719 | Aerosol spray cans                                                                           |
| G926   |          2 | 0.000337079 |  0.000221533 |          89 |   0.0224719 | Chewing gum, often contains plastics                                                         |
| G188   |          2 | 0.000561798 |  0.000221533 |          89 |   0.011236  | Other cans < 4 L                                                                             |
| G129   |          2 | 0.000561798 |  0.000221533 |          89 |   0.0224719 | Inner tubes and rubber sheets                                                                |
| G197   |          2 | 0.000449438 |  0.000221533 |          89 |   0.0224719 | Other metal                                                                                  |
| G179   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Disposable BBQs                                                                              |
| G114   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Films  <5mm                                                                                  |
| G53    |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Nets and pieces < 50cm                                                                       |
| G52    |          1 | 0.000674157 |  0.000110767 |          89 |   0.011236  | Nets and pieces                                                                              |
| G104   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Plastic fragments subrounded <5mm                                                            |
| G97    |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Toilet fresheners                                                                            |
| G11    |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Cosmetics for the beach, e.g. sunblock                                                       |
| G5     |          1 | 0.00101124  |  0.000110767 |          89 |   0.011236  | Generic plastic bags                                                                         |
| G150   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Milk cartons, tetrapack                                                                      |
| G111   |          1 | 0.00011236  |  0.000110767 |          89 |   0.011236  | Spheruloid pellets < 5mm                                                                     |
| G154   |          1 | 0.000337079 |  0.000110767 |          89 |   0.011236  | Newspapers or magazines                                                                      |
| G8     |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Drink bottles  > 0.5L                                                                        |
| G916   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Pencils and pieces                                                                           |
| G138   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Shoes and sandals                                                                            |
| G934   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Sandbag, plastic for flood, erosion control etc..                                            |
| G195   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Batteries - household                                                                        |
| G41    |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Glove industrial/professional                                                                |
| G128   |          1 | 0.000898876 |  0.000110767 |          89 |   0.011236  | Tires and belts                                                                              |
| G171   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Other wood < 50cm                                                                            |
| G190   |          1 | 0.00011236  |  0.000110767 |          89 |   0.011236  | Paint cans                                                                                   |
| G172   |          1 | 0.000224719 |  0.000110767 |          89 |   0.011236  | Other wood > 50cm                                                                            |
| G61    |          1 | 0.000337079 |  0.000110767 |          89 |   0.011236  | Other fishing related                                                                        |
| G214   |          1 | 0.000449438 |  0.000110767 |          89 |   0.011236  | Oil/tar                                                                                      |
