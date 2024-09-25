

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


# lac leman

**Summary and analysis of observations of trash density**: objects related to recreation, personal items, unclassified, infrastructure, food and drink, packaging non food, plastic pieces, waste water, agriculture, tobacco and micro plastics (< 5mm) found in lakes and rivers. <i>Report number: lac leman 2020-01-01 2021-05-31</i>



## Administrative boundaries lac leman 2020-01-01 2021-05-31 : Cities, cantons, survey areas

The number and and names of the cities, cantons and survey areas included in this report



The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis.

Please provide a narrative of the contents of the following table. In your narrative be sure to include the list of cities and the names of the canton and survey areas.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

 |              |   count |
|:-------------|--------:|
| location     |      24 |
| city         |      13 |
| canton       |       3 |
| survey areas |       1 |

The following is the names of the cities, cantons, and survey areas.

city: La Tour-de-Peilz, Genève, Montreux, Tolochenaz, Bourg-en-Lavaux, Saint-Gingolph, Allaman, Gland, Saint-Sulpice (VD), Préverenges, Vevey, Versoix, Lausanne
canton: Vaud, Genève, Valais
survey_area: rhone


## Named features lac leman 2020-01-01 2021-05-31 : The lakes, rivers and parks

The number and names of the lakes, rivers or parks included in this report



The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. Please provide a concise narrative of the contents of the following table. In your narrative be sure to the name of each park, lake or river

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
 INSTRUCTION_END ---> 

|       |   lake |
|:------|-------:|
| count |      1 |

The following is the names of the lakes, rivers and parks included in the data.

river: 
lake: lac-leman
park: 


## Summary statistics lac leman 2020-01-01 2021-05-31: The descriptive statistics of the survey results

lac leman: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.





This table summarizes the sample total in pcs/m for each survey. Each survey is defined by a sample_id. A survey total is the sum of all rows that have the same sample_id.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

|        |   total |   nsamples |   average |   5th |   25th |   50th |   75th |   95th |     std |   max | start      | end        |
|:-------|--------:|-----------:|----------:|------:|-------:|-------:|-------:|-------:|--------:|------:|:-----------|:-----------|
| result |   27447 |         98 |   8.66245 | 0.914 |  2.305 |  4.505 | 9.6825 | 26.959 | 11.6118 | 66.17 | 2020-04-28 | 2021-05-12 |

## Material composition of objects lac leman 2020-01-01 2021-05-31: estimated material composition

lac leman: The proportion of each material type according to material category





The following table details the proportion that each material type represents to the total. 
Generate a narrative summary based on the following table. You need to include all the material types and their float values.
If there is more than one material entry in the table.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. Consider the example above

 INSTRUCTION_END ---> 

| material   | % of total   |
|:-----------|:-------------|
| glass      | 3%           |
| metal      | 2%           |
| paper      | 1%           |
| plastic    | 90%          |
## Survey Totals for city


## lac leman 2020-01-01 2021-05-31 city: The average pcs/m by city.

The average sample total for each city in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | city               |   quantity |    pcs/m |
|---:|:-------------------|-----------:|---------:|
|  0 | Allaman            |        631 |  7.22667 |
|  1 | Bourg-en-Lavaux    |        121 |  5.015   |
|  2 | Genève             |       4059 |  3.3     |
|  3 | Gland              |        134 |  1.43    |
|  4 | La Tour-de-Peilz   |       2936 |  4.326   |
|  5 | Lausanne           |        997 | 19.4114  |
|  6 | Montreux           |        738 |  4.21    |
|  7 | Préverenges        |       3744 |  6.61615 |
|  8 | Saint-Gingolph     |       7560 | 23.6418  |
|  9 | Saint-Sulpice (VD) |       2507 | 18.426   |
| 10 | Tolochenaz         |        274 |  3.555   |
| 11 | Versoix            |        583 |  3.11    |
| 12 | Vevey              |       3163 |  6.38917 |


## Survey Totals for canton


## lac leman 2020-01-01 2021-05-31 canton: The average pcs/m by canton.

The average sample total for each canton in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | canton   |   quantity |    pcs/m |
|---:|:---------|-----------:|---------:|
|  0 | Genève   |       4642 |  3.27    |
|  1 | Valais   |       7560 | 23.6418  |
|  2 | Vaud     |      15245 |  7.74603 |


## Survey Totals for parent_boundary


## lac leman 2020-01-01 2021-05-31 survey area: The average pcs/m by survey area.

The average sample total for each survey area in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | parent_boundary   |   quantity |   pcs/m |
|---:|:------------------|-----------:|--------:|
|  0 | rhone             |      27447 | 8.66245 |



## Inventory items lac leman 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |       pcs/m |   % of total |   sample_id |   fail rate | object                                                                                       |
|:-------|-----------:|------------:|-------------:|------------:|------------:|:---------------------------------------------------------------------------------------------|
| Gfrags |       4212 | 1.50582     |  0.153459    |          98 |   0.969388  | Fragmented plastics                                                                          |
| Gfoams |       3586 | 1.28816     |  0.130652    |          98 |   0.836735  | Expanded polystyrene                                                                         |
| G27    |       3116 | 0.810918    |  0.113528    |          98 |   0.94898   | Cigarette filters                                                                            |
| G30    |       1679 | 0.50551     |  0.0611724   |          98 |   0.959184  | Food wrappers; candy, snacks                                                                 |
| G112   |       1387 | 0.403367    |  0.0505338   |          98 |   0.469388  | Industrial pellets (nurdles)                                                                 |
| Gcaps  |       1212 | 0.382959    |  0.0441578   |          98 |   0.887755  | plastic caps, lid rings: G21, G22, G23, G24                                                  |
| G95    |       1112 | 0.353673    |  0.0405144   |          98 |   0.816327  | Cotton bud/swab sticks                                                                       |
| G74    |       1097 | 0.169628    |  0.0399679   |          98 |   1.29592   | Foam packaging/insulation/polyurethane                                                       |
| G67    |       1058 | 0.367653    |  0.038547    |          98 |   0.77551   | Industrial sheeting                                                                          |
| G117   |        689 | 0.227347    |  0.0251029   |          98 |   0.295918  | Styrofoam < 5mm                                                                              |
| G89    |        584 | 0.174388    |  0.0212774   |          98 |   0.663265  | Plastic construction waste                                                                   |
| G200   |        510 | 0.148878    |  0.0185813   |          98 |   0.581633  | Glass drink bottles, pieces                                                                  |
| G106   |        427 | 0.109082    |  0.0155573   |          98 |   0.244898  | Plastic fragments angular <5mm                                                               |
| G70    |        345 | 0.105714    |  0.0125697   |          98 |   0.520408  | Shotgun cartridges                                                                           |
| G178   |        308 | 0.0663265   |  0.0112216   |          98 |   0.714286  | Metal bottle caps, lids & pull tabs from cans                                                |
| G25    |        295 | 0.0988776   |  0.010748    |          98 |   0.55102   | Tobacco; plastic packaging, containers                                                       |
| G10    |        288 | 0.0917347   |  0.010493    |          98 |   0.510204  | Food containers single use foamed or plastic                                                 |
| G35    |        278 | 0.0843878   |  0.0101286   |          98 |   0.734694  | Straws and stirrers                                                                          |
| G31    |        237 | 0.0766327   |  0.00863482  |          98 |   0.663265  | Lollypop sticks                                                                              |
| G103   |        229 | 0.062551    |  0.00834335  |          98 |   0.0612245 | Plastic fragments rounded <5mm                                                               |
| G33    |        196 | 0.0580612   |  0.00714104  |          98 |   0.571429  | Cups, lids, single use foamed and hard plastic                                               |
| G32    |        192 | 0.062449    |  0.0069953   |          98 |   0.632653  | Toys and party favors                                                                        |
| G177   |        177 | 0.0462245   |  0.00644879  |          98 |   0.561224  | Foil wrappers, aluminum foil                                                                 |
| G100   |        176 | 0.0687755   |  0.00641236  |          98 |   0.612245  | Medical; containers/tubes/ packaging                                                         |
| G921   |        175 | 0.0466327   |  0.00637592  |          98 |   0.244898  | Ceramic tile and pieces                                                                      |
| G73    |        162 | 0.0539796   |  0.00590228  |          98 |   0.397959  | Foamed items & pieces (non packaging/insulation) foamed sponge material                      |
| G3     |        156 | 0.049898    |  0.00568368  |          98 |   0.22449   | Bags; plastic shopping/carrier/grocery and pieces                                            |
| G38    |        151 | 0.0441837   |  0.00550151  |          98 |   0.112245  | Coverings; plastic packaging, sheeting for protecting large cargo items                      |
| G66    |        130 | 0.0481633   |  0.0047364   |          98 |   0.418367  | Straps/bands;  hard, plastic package fastener                                                |
| G98    |        113 | 0.0344898   |  0.00411703  |          98 |   0.336735  | Diapers - wipes                                                                              |
| G211   |        102 | 0.0222449   |  0.00371625  |          98 |   0.438776  | Other medical (swabs, bandaging, adhesive plaster)                                           |
| G156   |        101 | 0.0221429   |  0.00367982  |          98 |   0.27551   | Paper fragments                                                                              |
| G922   |         95 | 0.0314286   |  0.00346122  |          98 |   0.326531  | Labels, bar codes                                                                            |
| G91    |         95 | 0.0287755   |  0.00346122  |          98 |   0.367347  | Biomass holder                                                                               |
| G159   |         90 | 0.0247959   |  0.00327905  |          98 |   0.418367  | Corks                                                                                        |
| G208   |         87 | 0.0166327   |  0.00316975  |          98 |   0.153061  | Glass or ceramic fragments > 2.5 cm                                                          |
| G904   |         85 | 0.0230612   |  0.00309688  |          98 |   0.255102  | Fireworks; rocket caps, exploded parts & packaging                                           |
| G941   |         85 | 0.0196939   |  0.00309688  |          98 |   0.163265  | Packaging films nonfood or unknown                                                           |
| G90    |         79 | 0.0257143   |  0.00287827  |          98 |   0.265306  | Plastic flower pots                                                                          |
| G125   |         78 | 0.027449    |  0.00284184  |          98 |   0.27551   | Balloons and balloon sticks                                                                  |
| G124   |         68 | 0.0178571   |  0.0024775   |          98 |   0.173469  | Other plastic or foam products                                                               |
| G165   |         68 | 0.0162245   |  0.0024775   |          98 |   0.244898  | Ice cream sticks, toothpicks, chopsticks                                                     |
| G96    |         67 | 0.0211224   |  0.00244107  |          98 |   0.306122  | Sanitary pads /panty liners/tampons and applicators                                          |
| G914   |         64 | 0.0210204   |  0.00233177  |          98 |   0.255102  | Paperclips, clothespins, plastic utility items                                               |
| G153   |         62 | 0.0168367   |  0.0022589   |          98 |   0.193878  | Cups, food containers, wrappers (paper)                                                      |
| G50    |         61 | 0.0133673   |  0.00222247  |          98 |   0.306122  | String < 1cm                                                                                 |
| G105   |         59 | 0.0368367   |  0.0021496   |          98 |   0.0816327 | Plastic fragments subangular <5mm                                                            |
| G34    |         58 | 0.0152041   |  0.00211316  |          98 |   0.265306  | Cutlery, plates and trays                                                                    |
| G908   |         58 | 0.0155102   |  0.00211316  |          98 |   0.214286  | Tape; electrical, insulating                                                                 |
| G28    |         55 | 0.0167347   |  0.00200386  |          98 |   0.295918  | Pens, lids, mechanical pencils etc.                                                          |
| G923   |         51 | 0.0235714   |  0.00185813  |          98 |   0.204082  | Tissue, toilet paper, napkins, paper towels                                                  |
| G93    |         47 | 0.0119388   |  0.00171239  |          98 |   0.255102  | Cable ties; steggel, zip, zap straps                                                         |
| G26    |         45 | 0.0144898   |  0.00163952  |          98 |   0.244898  | Cigarette lighters                                                                           |
| G905   |         45 | 0.00989796  |  0.00163952  |          98 |   0.306122  | Hair clip,  hair ties, personal accessories plastic                                          |
| G155   |         44 | 0.00540816  |  0.00160309  |          98 |   0.0306122 | Fireworks paper tubes and fragments                                                          |
| G115   |         43 | 0.0113265   |  0.00156666  |          98 |   0.0408163 | Foamed  plastic <5mm                                                                         |
| G131   |         43 | 0.0126531   |  0.00156666  |          98 |   0.285714  | Rubber bands                                                                                 |
| G198   |         43 | 0.010102    |  0.00156666  |          98 |   0.244898  | Other metal pieces < 50cm                                                                    |
| G146   |         40 | 0.0130612   |  0.00145735  |          98 |   0.102041  | Paper, cardboard                                                                             |
| G152   |         39 | 0.0120408   |  0.00142092  |          98 |   0.142857  | Cigarette boxes, tobacco related paper/cardboard                                             |
| G149   |         39 | 0.0106122   |  0.00142092  |          98 |   0.122449  | Paper packaging                                                                              |
| G937   |         38 | 0.0120408   |  0.00138449  |          98 |   0.183673  | Pheromone baits for vineyards                                                                |
| G157   |         35 | 0.0108163   |  0.00127518  |          98 |   0.112245  | Paper                                                                                        |
| G939   |         33 | 0.00693878  |  0.00120232  |          98 |   0.142857  | Flowers, plants plastic                                                                      |
| G7     |         32 | 0.0110204   |  0.00116588  |          98 |   0.132653  | Drink bottles < = 0.5L                                                                       |
| G204   |         32 | 0.00959184  |  0.00116588  |          98 |   0.153061  | Construction material; bricks, pipes, cement                                                 |
| G4     |         32 | 0.0128571   |  0.00116588  |          98 |   0.132653  | Small plastic bags; freezer, zip-lock etc.                                                   |
| G20    |         31 | 0.00795918  |  0.00112945  |          98 |   0.132653  | Caps and lids                                                                                |
| G207   |         30 | 0.0109184   |  0.00109302  |          98 |   0.0102041 | Octopus pots                                                                                 |
| G137   |         28 | 0.00857143  |  0.00102015  |          98 |   0.163265  | Clothing, towels & rags                                                                      |
| G213   |         28 | 0.010102    |  0.00102015  |          98 |   0.193878  | Paraffin wax                                                                                 |
| G142   |         27 | 0.00663265  |  0.000983714 |          98 |   0.142857  | Rope , string or nets                                                                        |
| G65    |         26 | 0.0094898   |  0.00094728  |          98 |   0.132653  | Buckets                                                                                      |
| G12    |         25 | 0.00693878  |  0.000910846 |          98 |   0.142857  | Cosmetics, non-beach use personal care containers                                            |
| G148   |         23 | 0.00346939  |  0.000837979 |          98 |   0.0714286 | Cardboard (boxes and fragments)                                                              |
| G191   |         23 | 0.00612245  |  0.000837979 |          98 |   0.132653  | Wire and mesh                                                                                |
| G99    |         21 | 0.00785714  |  0.000765111 |          98 |   0.173469  | Syringes - needles                                                                           |
| G135   |         20 | 0.00459184  |  0.000728677 |          98 |   0.132653  | Clothes, footware, headware, gloves                                                          |
| G48    |         18 | 0.00602041  |  0.000655809 |          98 |   0.122449  | Rope, synthetic                                                                              |
| G943   |         18 | 0.00479592  |  0.000655809 |          98 |   0.0816327 | Fencing agriculture, plastic                                                                 |
| G114   |         18 | 0.00183673  |  0.000655809 |          98 |   0.0204082 | Films  <5mm                                                                                  |
| G6     |         18 | 0.00489796  |  0.000655809 |          98 |   0.0612245 | Bottles and containers, plastic non food/drink                                               |
| G134   |         17 | 0.00367347  |  0.000619376 |          98 |   0.132653  | Other rubber                                                                                 |
| G126   |         17 | 0.00571429  |  0.000619376 |          98 |   0.112245  | Balls                                                                                        |
| G123   |         17 | 0.00173469  |  0.000619376 |          98 |   0.0102041 | Polyurethane granules < 5mm                                                                  |
| G2     |         16 | 0.0044898   |  0.000582942 |          98 |   0.0816327 | Bags                                                                                         |
| G87    |         16 | 0.0022449   |  0.000582942 |          98 |   0.0816327 | Tape, masking/duct/packing                                                                   |
| G936   |         16 | 0.00479592  |  0.000582942 |          98 |   0.102041  | Sheeting ag. greenhouse film                                                                 |
| G194   |         16 | 0.00397959  |  0.000582942 |          98 |   0.153061  | Cables, metal wire(s) often inside rubber or plastic tubes                                   |
| G918   |         15 | 0.00744898  |  0.000546508 |          98 |   0.0816327 | Safety pins, paper clips, small metal utility items                                          |
| G43    |         15 | 0.00255102  |  0.000546508 |          98 |   0.0612245 | Tags fishing or industry (security tags, seals)                                              |
| G927   |         14 | 0.00428571  |  0.000510074 |          98 |   0.0816327 | String trimmer line, used to cut grass, weeds, and shrubbery                                 |
| G175   |         14 | 0.00377551  |  0.000510074 |          98 |   0.102041  | Cans, beverage                                                                               |
| G113   |         14 | 0.00142857  |  0.000510074 |          98 |   0.0408163 | Filaments  <5mm                                                                              |
| G182   |         14 | 0.00479592  |  0.000510074 |          98 |   0.0714286 | Fishing; hooks, weights, lures, sinkers etc.                                                 |
| G144   |         13 | 0.00826531  |  0.00047364  |          98 |   0.0816327 | Tampons                                                                                      |
| G145   |         13 | 0.00306122  |  0.00047364  |          98 |   0.0918367 | Other textiles                                                                               |
| G201   |         13 | 0.00397959  |  0.00047364  |          98 |   0.0612245 | Jars, includes pieces                                                                        |
| G203   |         13 | 0.00377551  |  0.00047364  |          98 |   0.0510204 | Tableware ceramic or glass, cups, plates, pieces                                             |
| G186   |         12 | 0.00377551  |  0.000437206 |          98 |   0.0408163 | Industrial scrap                                                                             |
| G930   |         12 | 0.00306122  |  0.000437206 |          98 |   0.102041  | Foam earplugs                                                                                |
| G59    |         11 | 0.00367347  |  0.000400772 |          98 |   0.0714286 | Fishing line monofilament (angling)                                                          |
| G928   |         11 | 0.00306122  |  0.000400772 |          98 |   0.0510204 | Ribbons and bows                                                                             |
| G170   |         11 | 0.00285714  |  0.000400772 |          98 |   0.0714286 | Wood (processed)                                                                             |
| G940   |         10 | 0.00326531  |  0.000364339 |          98 |   0.0408163 | Foamed EVA (flexible plastic) for crafts & watersports                                       |
| G942   |         10 | 0.00612245  |  0.000364339 |          98 |   0.0816327 | Plastic shavings from lathes, CNC machining                                                  |
| G901   |         10 | 0.00295918  |  0.000364339 |          98 |   0.0816327 | Mask medical, synthetic                                                                      |
| G210   |         10 | 0.00204082  |  0.000364339 |          98 |   0.0408163 | Other glass/ceramic                                                                          |
| G11    |         10 | 0.00367347  |  0.000364339 |          98 |   0.0816327 | Cosmetics for the beach, e.g. sunblock                                                       |
| G158   |         10 | 0.00306122  |  0.000364339 |          98 |   0.0306122 | Other paper items                                                                            |
| G938   |          9 | 0.00234694  |  0.000327905 |          98 |   0.0816327 | Toothpicks, dental floss plastic                                                             |
| G8     |          9 | 0.00316327  |  0.000327905 |          98 |   0.0714286 | Drink bottles  > 0.5L                                                                        |
| G128   |          8 | 0.00193878  |  0.000291471 |          98 |   0.0612245 | Tires and belts                                                                              |
| G926   |          8 | 0.00234694  |  0.000291471 |          98 |   0.0612245 | Chewing gum, often contains plastics                                                         |
| G133   |          8 | 0.0027551   |  0.000291471 |          98 |   0.0714286 | Condoms incl. packaging                                                                      |
| G119   |          8 | 0.00214286  |  0.000291471 |          98 |   0.0102041 | Sheetlike user plastic (>1mm)                                                                |
| G118   |          8 | 0.00183673  |  0.000291471 |          98 |   0.0408163 | Small industrial spheres <5mm                                                                |
| G68    |          7 | 0.00132653  |  0.000255037 |          98 |   0.0612245 | Fiberglass fragments                                                                         |
| G916   |          7 | 0.00102041  |  0.000255037 |          98 |   0.0612245 | Pencils and pieces                                                                           |
| G900   |          7 | 0.0022449   |  0.000255037 |          98 |   0.0612245 | Gloves latex  personal protective equipment                                                  |
| G929   |          7 | 0.00112245  |  0.000255037 |          98 |   0.0612245 | Electronics and pieces; sensors, headsets etc.                                               |
| G61    |          7 | 0.00377551  |  0.000255037 |          98 |   0.0612245 | Other fishing related                                                                        |
| G176   |          6 | 0.00183673  |  0.000218603 |          98 |   0.0306122 | Cans, food                                                                                   |
| G933   |          6 | 0.00244898  |  0.000218603 |          98 |   0.0204082 | Bags, cases for accessories; glasses, electronics, incl. straps, pieces, plstc. nylon etc.   |
| G101   |          5 | 0.00142857  |  0.000182169 |          98 |   0.0510204 | Dog feces bag                                                                                |
| G167   |          5 | 0.00122449  |  0.000182169 |          98 |   0.0306122 | Matches or fireworks                                                                         |
| G17    |          5 | 0.00183673  |  0.000182169 |          98 |   0.0204082 | Injection gun cartridge                                                                      |
| G195   |          5 | 0.00142857  |  0.000182169 |          98 |   0.0510204 | Batteries - household                                                                        |
| G147   |          5 | 0.00102041  |  0.000182169 |          98 |   0.0510204 | Paper bags                                                                                   |
| G97    |          5 | 0.00163265  |  0.000182169 |          98 |   0.0510204 | Toilet fresheners                                                                            |
| G919   |          5 | 0.00397959  |  0.000182169 |          98 |   0.0408163 | Nails, screws, bolts etc.                                                                    |
| G917   |          5 | 0.00183673  |  0.000182169 |          98 |   0.0306122 | Terracotta balls                                                                             |
| G136   |          4 | 0.00132653  |  0.000145735 |          98 |   0.0306122 | Shoes                                                                                        |
| G931   |          4 | 0.00153061  |  0.000145735 |          98 |   0.0204082 | Tape-caution for barrier, police, construction etc.                                          |
| G181   |          4 | 0.00122449  |  0.000145735 |          98 |   0.0408163 | Tableware metal;  cups, cutlery etc.                                                         |
| G29    |          4 | 0.00132653  |  0.000145735 |          98 |   0.0408163 | Combs, brushes and sunglasses                                                                |
| G915   |          3 | 0.00204082  |  0.000109302 |          98 |   0.0306122 | Reflectors, plastic mobility items                                                           |
| G906   |          3 | 0.000816327 |  0.000109302 |          98 |   0.0306122 | coffee capsules aluminum                                                                     |
| G913   |          3 | 0.000816327 |  0.000109302 |          98 |   0.0306122 | Pacifier                                                                                     |
| G92    |          3 | 0.000612245 |  0.000109302 |          98 |   0.0306122 | Bait containers                                                                              |
| G116   |          3 | 0.00173469  |  0.000109302 |          98 |   0.0102041 | Granules <5mm                                                                                |
| G19    |          3 | 0.000816327 |  0.000109302 |          98 |   0.0204082 | Car parts                                                                                    |
| G108   |          3 | 0.000918367 |  0.000109302 |          98 |   0.0204082 | disk pellets  <5mm                                                                           |
| G63    |          3 | 0.000816327 |  0.000109302 |          98 |   0.0204082 | Buoys                                                                                        |
| G62    |          3 | 0.00112245  |  0.000109302 |          98 |   0.0204082 | Floats for nets                                                                              |
| G161   |          3 | 0.000612245 |  0.000109302 |          98 |   0.0204082 | Processed timber                                                                             |
| G104   |          3 | 0.000306122 |  0.000109302 |          98 |   0.0204082 | Plastic fragments subrounded <5mm                                                            |
| G37    |          3 | 0.00102041  |  0.000109302 |          98 |   0.0204082 | Mesh bags                                                                                    |
| G197   |          3 | 0.000918367 |  0.000109302 |          98 |   0.0306122 | Other metal                                                                                  |
| G199   |          2 | 0.000510204 |  7.28677e-05 |          98 |   0.0204082 | Other metal pieces > 50cm                                                                    |
| G13    |          2 | 0.000408163 |  7.28677e-05 |          98 |   0.0102041 | Bottles, containers, drums to transport, store material                                      |
| G139   |          2 | 0.000510204 |  7.28677e-05 |          98 |   0.0102041 | Backpacks                                                                                    |
| G140   |          2 | 0.000204082 |  7.28677e-05 |          98 |   0.0102041 | Bags, burlap, hessian, jute or hemp                                                          |
| G150   |          2 | 0.000306122 |  7.28677e-05 |          98 |   0.0204082 | Milk cartons, tetrapack                                                                      |
| G151   |          2 | 0.000612245 |  7.28677e-05 |          98 |   0.0204082 | Cartons, Tetrapacks                                                                          |
| G932   |          2 | 0.000714286 |  7.28677e-05 |          98 |   0.0102041 | Bio-beads, micro plastic for wastewater treatment, irregular shape, ridged sides < 5mm       |
| G907   |          2 | 0.000408163 |  7.28677e-05 |          98 |   0.0204082 | coffee capsules plastic                                                                      |
| G109   |          2 | 0.000204082 |  7.28677e-05 |          98 |   0.0102041 | Flat pellets  <5mm                                                                           |
| G925   |          2 | 0.000816327 |  7.28677e-05 |          98 |   0.0204082 | Packets: desiccant/ moisture absorbers, plastic case filled with silica                      |
| G107   |          2 | 0.000306122 |  7.28677e-05 |          98 |   0.0102041 | Cylindrical pellets < 5mm                                                                    |
| G55    |          2 | 0.000408163 |  7.28677e-05 |          98 |   0.0204082 | Fishing line (entangled)                                                                     |
| G5     |          2 | 0.000408163 |  7.28677e-05 |          98 |   0.0204082 | Generic plastic bags                                                                         |
| G36    |          2 | 0.000306122 |  7.28677e-05 |          98 |   0.0102041 | Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc. |
| G49    |          2 | 0.000510204 |  7.28677e-05 |          98 |   0.0204082 | Rope > 1cm                                                                                   |
| G154   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Newspapers or magazines                                                                      |
| G129   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Inner tubes and rubber sheets                                                                |
| G102   |          1 | 0.000306122 |  3.64339e-05 |          98 |   0.0102041 | Flip-flops                                                                                   |
| G138   |          1 | 0.000408163 |  3.64339e-05 |          98 |   0.0102041 | Shoes and sandals                                                                            |
| G64    |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Fenders                                                                                      |
| G14    |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Engine oil bottles                                                                           |
| G51    |          1 | 0.000102041 |  3.64339e-05 |          98 |   0.0102041 | Fishing net                                                                                  |
| G202   |          1 | 0.000408163 |  3.64339e-05 |          98 |   0.0102041 | Light bulbs                                                                                  |
| G171   |          1 | 0.000102041 |  3.64339e-05 |          98 |   0.0102041 | Other wood < 50cm                                                                            |
| G172   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Other wood > 50cm                                                                            |
| G173   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Other                                                                                        |
| G935   |          1 | 0.000408163 |  3.64339e-05 |          98 |   0.0102041 | Walking stick pads and pieces, often elastomeric material                                    |
| G179   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Disposable BBQs                                                                              |
| G40    |          1 | 0.000510204 |  3.64339e-05 |          98 |   0.0102041 | Gloves household/gardening                                                                   |
| G183   |          1 | 0.00122449  |  3.64339e-05 |          98 |   0.0102041 | Fish hook remains                                                                            |
| G39    |          1 | 0.000102041 |  3.64339e-05 |          98 |   0.0102041 | Gloves                                                                                       |
| G193   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | car parts and batteries                                                                      |
| G166   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Paint brushes                                                                                |

## Sampling stratification lac leman 2020-01-01 2021-05-31: The environmental features surrounding the survey location.

Each survey location is surrounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken according to the different conditions.



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
| 0-20%                  | 5.1%                                               | 100.0%                                            | 86.7%                                           | 80.6%                                                    | 100.0%                                              | 79.6%                                              | 19.4%                                            | 98.0%                                              | 100.0%                                            |
| 20-40%                 | 14.3%                                              | none                                              | 2.0%                                            | 17.3%                                                    | none                                                | 15.3%                                              | 19.4%                                            | none                                               | none                                              |
| 40-60%                 | 1.0%                                               | none                                              | 11.2%                                           | 2.0%                                                     | none                                                | 5.1%                                               | 36.7%                                            | 2.0%                                               | none                                              |
| 60-80%                 | 19.4%                                              | none                                              | none                                            | none                                                     | none                                                | none                                               | 10.2%                                            | none                                               | none                                              |
| 80-100%                | 60.2%                                              | none                                              | none                                            | none                                                     | none                                                | none                                               | 14.3%                                            | none                                               | none                                              |

## Sampling stratification and trash density lac leman 2020-01-01 2021-05-31: The changes in the observed litter density and the changes in land use



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
| 0-20%                  |                                      4.908   | 8.662448979591836                           | 6.894117647058822                         | 7.2497468354430366                                 | 8.662448979591836                             | 7.015128205128206                            |                                   15.8905  | 8.738437500000002                            | 8.662448979591836                           |
| 20-40%                 |                                     19.4179  | none                                        | 1.4300000000000002                        | 15.656470588235296                                 | none                                          | 18.480000000000004                           |                                    3.78263 | none                                         | none                                        |
| 40-60%                 |                                      5.35    | none                                        | 23.64181818181818                         | 5.015                                              | none                                          | 4.9079999999999995                           |                                    6.35333 | 5.015                                        | none                                        |
| 60-80%                 |                                      5.93684 | none                                        | none                                      | none                                               | none                                          | none                                         |                                   21.008   | none                                         | none                                        |
| 80-100%                |                                      7.36237 | none                                        | none                                      | none                                               | none                                          | none                                         |                                    2.595   | none                                         | none                                        |

## Grid forecast lac leman 2020-01-01 2021-05-31


### Grid Approximation method:

Grid approximation is a numerical technique used to approximate the distribution of a parameter. The parameter of interest is the likelihood of observing a certain litter density given the land use profile of the survey location. The values are defined on the grid between 0 and the and the 99th percentile of the likelihood, every 0.01, or for every 1 meter of beach. The likelihood is defined using the binomial probability  that a survey exceeded a given value on the grid. This can be easily represented in an inference table, where each row represents a point on the  grid. The inference table has four columns, the first column is the prior, the second is the likelihood, the third is the prior * the likelihood  and the fourth column is the normalized version of column three, that is the sum of column 4 is 1.
The fourth column is the posterior distribution that an inventory will exceed a point on the grid given the observations/likelihood, and the data from similar locations both regionally and nationally - the prior. Similarity between locations is defined by the manhattan distance between the land-use or sampling stratification of each location. This is an application of conditional probability and Bayes theorem to approximate beach litter density based on observations from various data sources.In this report every forecast is conditioned on results from similary locations, either in the same region or nationaly or mixed. The exact number and  where the sample conditions come from is defined by the land use of the likelihood.The whole process can be generalized to a multinomial distribution. The grid is being used in a simple form here to ensure that the same calculation is executed at each scale and to maximize the use of the prior data at each scale
These are the steps fore creating the inference table 

1. **grid index parameter space discretization**: Divide the continuous parameter space into a discrete grid of points. We use the 0 as the start of the grid and the 99th percentile
 2. **column one prior** using the prior data, evaluate the number of times that each samle exceeded each point. divde that by the number of samples.
 3. **column two likelihood** using the current data do the same thing as the prior for each point on the grid or row in the table
4. **column three likelihood times prior**: the product of column one and two
5. **column four posterior distribution**: the sum of column three is the normalizing constant. divide each value in column three by the normalizing constant

An inference table is created for each forecast, allowing the end user to determine whether conditions outside of the region of interest are influencing the forecast. <!--- INSTRUCTION_START
All conclusions should be in reference to the likelihood. For example, if the posterior distribution is lower than the likelihood then the prediction is a decrease, however this also means that with respect to the prior conditions the likelihood was higher. In the same way that if an increase is predicted the prior was very close to of maybe even greater than the likelihood. Always state the conclusions with respect to which prior was used. 
You must locate the section that corresponds to the prior that was used and provide the results for that prior, a precise definition is given. 
INSTRUCTION_END -->



### Combined prior grid approximation
This prior distribution is selected from random samples from inside and outside the requested administrative boundary (if a boundary was selected) and if their are enough samples with similar land use. The prior does not include samples from the likelihood. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the manhattan distance between the likelihood samples and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations (indifferent of the geographic boundary) ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7800000000000005
The expected posterior distribution is a grid approximation from 0 to 53.160000000000004 every 0.01.

|       |    pcs/m |
|:------|---------:|
| count | 100      |
| mean  |   3.2843 |
| std   |   5.2543 |
| min   |   0      |
| 25%   |   0.88   |
| 50%   |   2.025  |
| 75%   |   3.8875 |
| max   |  48.42   |

### In boundary grid approximation
This prior distribution is selected from random samples from within the requested administrative boundary (if a boundary was selected) and if their are enough samples with similar land use. The prior does not include samples from the likelihood. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the manhattan distance between the likelihood feature variables  and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations in the geographic boundary ?'  There are fewer samples in the prior than the likelihood. All prior samples were used
The expected posterior distribution is a grid approximation from 0 to 53.160000000000004 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   3.5403  |
| std   |   4.20632 |
| min   |   0       |
| 25%   |   0.5875  |
| 50%   |   2.335   |
| 75%   |   3.8925  |
| max   |  19.21    |

### Out boundary grid approximation
This prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected) and if their are enough samples with similar land use. The prior does not include samples from the likelihood. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations outside the geographic boundary ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7700000000000005
The expected posterior distribution is a grid approximation from 0 to 53.160000000000004 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   3.1857  |
| std   |   3.58429 |
| min   |   0.02    |
| 25%   |   0.7925  |
| 50%   |   2.005   |
| 75%   |   3.925   |
| max   |  16.18    |




### Cluster analysis lac leman 2020-01-01 2021-05-31


lac leman: Cluster compositionThe survey locations were labeled according to the type and magnitude of land use in a 1 500 m buffer zone aroundaround each survey location. A cluster analysis was performed using K-Means clustering, the optimal amount of clusters was determined using the elbow method. Each cluster represents a group of locations that have similar land use profiles, that is the locations are surrounded by similar quantities of buildings or forest or undefined land use.We consider the cluster composition and the proportion of each cluster dedicated to a particular land use. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location whose buffer zone was 45% dedicated to forest. 

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

|   cluster |   buildings |   public-services |   streets |   undefined |   recreation |   forest |
|----------:|------------:|------------------:|----------:|------------:|-------------:|---------:|
|         0 |       0.362 |             0.126 |  0.184287 |       0.393 | -3.46945e-18 |    0.044 |
|         1 |       1     |             0.079 |  0        |       0     |  0.02        |    0     |
|         2 |       0.876 |             0.171 |  1        |       0.017 |  0.041       |    0     |





lac leman: Average density per cluster
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
|         0 | 15.087  |
|         1 |  5.3274 |
|         2 | 10.0289 |



### Summary of regression methods lac leman 2020-01-01 2021-05-31: 

In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. The feature variables are the land-use features identified in the land-use profile. From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model with the highest r² is then used in the BaggingRegressor and the VotingRegressor.





The following table details the results from different regression analysis of our data.

The table has the following format:

1. Model: the type of regression model used
2. R²: The coefficient of determination
3. MSE: the mean squared error

Generate a narrative summary based on the following table. You need to include all the models and the R² and MSE result.
The narrative needs to be in paragraph format.

|    | Model                        |        R² |     MSE |
|---:|:-----------------------------|----------:|--------:|
|  0 | Linear Regression            | 0.207141  | 1.66216 |
|  1 | Random Forest Regression     | 0.193802  | 1.69012 |
|  2 | Gradient Boosting Regression | 0.0933274 | 1.90076 |
|  3 | Theil-Sen Regressor          | 0.109104  | 1.86768 |
|  4 | Bagging:Linear Regression    | 0.20956   | 1.65709 |
|  5 | Voting                       | 0.175924  | 1.7276  |



### Feature and permutation importance lac leman 2020-01-01 2021-05-31



__Model feature importance__

Feature importance is a technique used in machine learning to identify and quantify the significance of different input variables (features) in predicting the target variable. In models like decision trees, random forests, and gradient boosting machines, feature importance is often calculated by measuring how much the model's accuracy or error changes when a particular feature is included versus when it is excluded. 
The following table details the model feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Coefficient |
|---:|:----------------|--------------:|
|  5 | forest          |     1.04094   |
|  0 | buildings       |     0.744069  |
|  1 | public-services |     0.420408  |
|  3 | undefined       |     0.246276  |
|  2 | streets         |    -0.0189524 |
|  4 | recreation      |    -0.131914  |



__Permutation feature importance__

Permutation importance is a model-agnostic method for assessing the importance of individual features in a predictive model. It is particularly useful because it can be applied to any type of model, whether it's a linear model, a decision tree, or a complex ensemble model. This method involves randomly shuffling the values of a feature in the dataset and observing the impact on the model's performance. A significant drop in performance indicates that the feature is important.
The following table details the permutation feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  5 | forest          |   0.933158   |
|  0 | buildings       |   0.495407   |
|  1 | public-services |   0.233848   |
|  3 | undefined       |   0.0122203  |
|  2 | streets         |  -0.00171265 |
|  4 | recreation      |  -0.0436041  |


## Inventory items lac leman 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |       pcs/m |   % of total |   sample_id |   fail rate | object                                                                                       |
|:-------|-----------:|------------:|-------------:|------------:|------------:|:---------------------------------------------------------------------------------------------|
| Gfrags |       4212 | 1.50582     |  0.153459    |          98 |   0.969388  | Fragmented plastics                                                                          |
| Gfoams |       3586 | 1.28816     |  0.130652    |          98 |   0.836735  | Expanded polystyrene                                                                         |
| G27    |       3116 | 0.810918    |  0.113528    |          98 |   0.94898   | Cigarette filters                                                                            |
| G30    |       1679 | 0.50551     |  0.0611724   |          98 |   0.959184  | Food wrappers; candy, snacks                                                                 |
| G112   |       1387 | 0.403367    |  0.0505338   |          98 |   0.469388  | Industrial pellets (nurdles)                                                                 |
| Gcaps  |       1212 | 0.382959    |  0.0441578   |          98 |   0.887755  | plastic caps, lid rings: G21, G22, G23, G24                                                  |
| G95    |       1112 | 0.353673    |  0.0405144   |          98 |   0.816327  | Cotton bud/swab sticks                                                                       |
| G74    |       1097 | 0.169628    |  0.0399679   |          98 |   1.29592   | Foam packaging/insulation/polyurethane                                                       |
| G67    |       1058 | 0.367653    |  0.038547    |          98 |   0.77551   | Industrial sheeting                                                                          |
| G117   |        689 | 0.227347    |  0.0251029   |          98 |   0.295918  | Styrofoam < 5mm                                                                              |
| G89    |        584 | 0.174388    |  0.0212774   |          98 |   0.663265  | Plastic construction waste                                                                   |
| G200   |        510 | 0.148878    |  0.0185813   |          98 |   0.581633  | Glass drink bottles, pieces                                                                  |
| G106   |        427 | 0.109082    |  0.0155573   |          98 |   0.244898  | Plastic fragments angular <5mm                                                               |
| G70    |        345 | 0.105714    |  0.0125697   |          98 |   0.520408  | Shotgun cartridges                                                                           |
| G178   |        308 | 0.0663265   |  0.0112216   |          98 |   0.714286  | Metal bottle caps, lids & pull tabs from cans                                                |
| G25    |        295 | 0.0988776   |  0.010748    |          98 |   0.55102   | Tobacco; plastic packaging, containers                                                       |
| G10    |        288 | 0.0917347   |  0.010493    |          98 |   0.510204  | Food containers single use foamed or plastic                                                 |
| G35    |        278 | 0.0843878   |  0.0101286   |          98 |   0.734694  | Straws and stirrers                                                                          |
| G31    |        237 | 0.0766327   |  0.00863482  |          98 |   0.663265  | Lollypop sticks                                                                              |
| G103   |        229 | 0.062551    |  0.00834335  |          98 |   0.0612245 | Plastic fragments rounded <5mm                                                               |
| G33    |        196 | 0.0580612   |  0.00714104  |          98 |   0.571429  | Cups, lids, single use foamed and hard plastic                                               |
| G32    |        192 | 0.062449    |  0.0069953   |          98 |   0.632653  | Toys and party favors                                                                        |
| G177   |        177 | 0.0462245   |  0.00644879  |          98 |   0.561224  | Foil wrappers, aluminum foil                                                                 |
| G100   |        176 | 0.0687755   |  0.00641236  |          98 |   0.612245  | Medical; containers/tubes/ packaging                                                         |
| G921   |        175 | 0.0466327   |  0.00637592  |          98 |   0.244898  | Ceramic tile and pieces                                                                      |
| G73    |        162 | 0.0539796   |  0.00590228  |          98 |   0.397959  | Foamed items & pieces (non packaging/insulation) foamed sponge material                      |
| G3     |        156 | 0.049898    |  0.00568368  |          98 |   0.22449   | Bags; plastic shopping/carrier/grocery and pieces                                            |
| G38    |        151 | 0.0441837   |  0.00550151  |          98 |   0.112245  | Coverings; plastic packaging, sheeting for protecting large cargo items                      |
| G66    |        130 | 0.0481633   |  0.0047364   |          98 |   0.418367  | Straps/bands;  hard, plastic package fastener                                                |
| G98    |        113 | 0.0344898   |  0.00411703  |          98 |   0.336735  | Diapers - wipes                                                                              |
| G211   |        102 | 0.0222449   |  0.00371625  |          98 |   0.438776  | Other medical (swabs, bandaging, adhesive plaster)                                           |
| G156   |        101 | 0.0221429   |  0.00367982  |          98 |   0.27551   | Paper fragments                                                                              |
| G922   |         95 | 0.0314286   |  0.00346122  |          98 |   0.326531  | Labels, bar codes                                                                            |
| G91    |         95 | 0.0287755   |  0.00346122  |          98 |   0.367347  | Biomass holder                                                                               |
| G159   |         90 | 0.0247959   |  0.00327905  |          98 |   0.418367  | Corks                                                                                        |
| G208   |         87 | 0.0166327   |  0.00316975  |          98 |   0.153061  | Glass or ceramic fragments > 2.5 cm                                                          |
| G904   |         85 | 0.0230612   |  0.00309688  |          98 |   0.255102  | Fireworks; rocket caps, exploded parts & packaging                                           |
| G941   |         85 | 0.0196939   |  0.00309688  |          98 |   0.163265  | Packaging films nonfood or unknown                                                           |
| G90    |         79 | 0.0257143   |  0.00287827  |          98 |   0.265306  | Plastic flower pots                                                                          |
| G125   |         78 | 0.027449    |  0.00284184  |          98 |   0.27551   | Balloons and balloon sticks                                                                  |
| G124   |         68 | 0.0178571   |  0.0024775   |          98 |   0.173469  | Other plastic or foam products                                                               |
| G165   |         68 | 0.0162245   |  0.0024775   |          98 |   0.244898  | Ice cream sticks, toothpicks, chopsticks                                                     |
| G96    |         67 | 0.0211224   |  0.00244107  |          98 |   0.306122  | Sanitary pads /panty liners/tampons and applicators                                          |
| G914   |         64 | 0.0210204   |  0.00233177  |          98 |   0.255102  | Paperclips, clothespins, plastic utility items                                               |
| G153   |         62 | 0.0168367   |  0.0022589   |          98 |   0.193878  | Cups, food containers, wrappers (paper)                                                      |
| G50    |         61 | 0.0133673   |  0.00222247  |          98 |   0.306122  | String < 1cm                                                                                 |
| G105   |         59 | 0.0368367   |  0.0021496   |          98 |   0.0816327 | Plastic fragments subangular <5mm                                                            |
| G34    |         58 | 0.0152041   |  0.00211316  |          98 |   0.265306  | Cutlery, plates and trays                                                                    |
| G908   |         58 | 0.0155102   |  0.00211316  |          98 |   0.214286  | Tape; electrical, insulating                                                                 |
| G28    |         55 | 0.0167347   |  0.00200386  |          98 |   0.295918  | Pens, lids, mechanical pencils etc.                                                          |
| G923   |         51 | 0.0235714   |  0.00185813  |          98 |   0.204082  | Tissue, toilet paper, napkins, paper towels                                                  |
| G93    |         47 | 0.0119388   |  0.00171239  |          98 |   0.255102  | Cable ties; steggel, zip, zap straps                                                         |
| G26    |         45 | 0.0144898   |  0.00163952  |          98 |   0.244898  | Cigarette lighters                                                                           |
| G905   |         45 | 0.00989796  |  0.00163952  |          98 |   0.306122  | Hair clip,  hair ties, personal accessories plastic                                          |
| G155   |         44 | 0.00540816  |  0.00160309  |          98 |   0.0306122 | Fireworks paper tubes and fragments                                                          |
| G115   |         43 | 0.0113265   |  0.00156666  |          98 |   0.0408163 | Foamed  plastic <5mm                                                                         |
| G131   |         43 | 0.0126531   |  0.00156666  |          98 |   0.285714  | Rubber bands                                                                                 |
| G198   |         43 | 0.010102    |  0.00156666  |          98 |   0.244898  | Other metal pieces < 50cm                                                                    |
| G146   |         40 | 0.0130612   |  0.00145735  |          98 |   0.102041  | Paper, cardboard                                                                             |
| G152   |         39 | 0.0120408   |  0.00142092  |          98 |   0.142857  | Cigarette boxes, tobacco related paper/cardboard                                             |
| G149   |         39 | 0.0106122   |  0.00142092  |          98 |   0.122449  | Paper packaging                                                                              |
| G937   |         38 | 0.0120408   |  0.00138449  |          98 |   0.183673  | Pheromone baits for vineyards                                                                |
| G157   |         35 | 0.0108163   |  0.00127518  |          98 |   0.112245  | Paper                                                                                        |
| G939   |         33 | 0.00693878  |  0.00120232  |          98 |   0.142857  | Flowers, plants plastic                                                                      |
| G7     |         32 | 0.0110204   |  0.00116588  |          98 |   0.132653  | Drink bottles < = 0.5L                                                                       |
| G204   |         32 | 0.00959184  |  0.00116588  |          98 |   0.153061  | Construction material; bricks, pipes, cement                                                 |
| G4     |         32 | 0.0128571   |  0.00116588  |          98 |   0.132653  | Small plastic bags; freezer, zip-lock etc.                                                   |
| G20    |         31 | 0.00795918  |  0.00112945  |          98 |   0.132653  | Caps and lids                                                                                |
| G207   |         30 | 0.0109184   |  0.00109302  |          98 |   0.0102041 | Octopus pots                                                                                 |
| G137   |         28 | 0.00857143  |  0.00102015  |          98 |   0.163265  | Clothing, towels & rags                                                                      |
| G213   |         28 | 0.010102    |  0.00102015  |          98 |   0.193878  | Paraffin wax                                                                                 |
| G142   |         27 | 0.00663265  |  0.000983714 |          98 |   0.142857  | Rope , string or nets                                                                        |
| G65    |         26 | 0.0094898   |  0.00094728  |          98 |   0.132653  | Buckets                                                                                      |
| G12    |         25 | 0.00693878  |  0.000910846 |          98 |   0.142857  | Cosmetics, non-beach use personal care containers                                            |
| G148   |         23 | 0.00346939  |  0.000837979 |          98 |   0.0714286 | Cardboard (boxes and fragments)                                                              |
| G191   |         23 | 0.00612245  |  0.000837979 |          98 |   0.132653  | Wire and mesh                                                                                |
| G99    |         21 | 0.00785714  |  0.000765111 |          98 |   0.173469  | Syringes - needles                                                                           |
| G135   |         20 | 0.00459184  |  0.000728677 |          98 |   0.132653  | Clothes, footware, headware, gloves                                                          |
| G48    |         18 | 0.00602041  |  0.000655809 |          98 |   0.122449  | Rope, synthetic                                                                              |
| G943   |         18 | 0.00479592  |  0.000655809 |          98 |   0.0816327 | Fencing agriculture, plastic                                                                 |
| G114   |         18 | 0.00183673  |  0.000655809 |          98 |   0.0204082 | Films  <5mm                                                                                  |
| G6     |         18 | 0.00489796  |  0.000655809 |          98 |   0.0612245 | Bottles and containers, plastic non food/drink                                               |
| G134   |         17 | 0.00367347  |  0.000619376 |          98 |   0.132653  | Other rubber                                                                                 |
| G126   |         17 | 0.00571429  |  0.000619376 |          98 |   0.112245  | Balls                                                                                        |
| G123   |         17 | 0.00173469  |  0.000619376 |          98 |   0.0102041 | Polyurethane granules < 5mm                                                                  |
| G2     |         16 | 0.0044898   |  0.000582942 |          98 |   0.0816327 | Bags                                                                                         |
| G87    |         16 | 0.0022449   |  0.000582942 |          98 |   0.0816327 | Tape, masking/duct/packing                                                                   |
| G936   |         16 | 0.00479592  |  0.000582942 |          98 |   0.102041  | Sheeting ag. greenhouse film                                                                 |
| G194   |         16 | 0.00397959  |  0.000582942 |          98 |   0.153061  | Cables, metal wire(s) often inside rubber or plastic tubes                                   |
| G918   |         15 | 0.00744898  |  0.000546508 |          98 |   0.0816327 | Safety pins, paper clips, small metal utility items                                          |
| G43    |         15 | 0.00255102  |  0.000546508 |          98 |   0.0612245 | Tags fishing or industry (security tags, seals)                                              |
| G927   |         14 | 0.00428571  |  0.000510074 |          98 |   0.0816327 | String trimmer line, used to cut grass, weeds, and shrubbery                                 |
| G175   |         14 | 0.00377551  |  0.000510074 |          98 |   0.102041  | Cans, beverage                                                                               |
| G113   |         14 | 0.00142857  |  0.000510074 |          98 |   0.0408163 | Filaments  <5mm                                                                              |
| G182   |         14 | 0.00479592  |  0.000510074 |          98 |   0.0714286 | Fishing; hooks, weights, lures, sinkers etc.                                                 |
| G144   |         13 | 0.00826531  |  0.00047364  |          98 |   0.0816327 | Tampons                                                                                      |
| G145   |         13 | 0.00306122  |  0.00047364  |          98 |   0.0918367 | Other textiles                                                                               |
| G201   |         13 | 0.00397959  |  0.00047364  |          98 |   0.0612245 | Jars, includes pieces                                                                        |
| G203   |         13 | 0.00377551  |  0.00047364  |          98 |   0.0510204 | Tableware ceramic or glass, cups, plates, pieces                                             |
| G186   |         12 | 0.00377551  |  0.000437206 |          98 |   0.0408163 | Industrial scrap                                                                             |
| G930   |         12 | 0.00306122  |  0.000437206 |          98 |   0.102041  | Foam earplugs                                                                                |
| G59    |         11 | 0.00367347  |  0.000400772 |          98 |   0.0714286 | Fishing line monofilament (angling)                                                          |
| G928   |         11 | 0.00306122  |  0.000400772 |          98 |   0.0510204 | Ribbons and bows                                                                             |
| G170   |         11 | 0.00285714  |  0.000400772 |          98 |   0.0714286 | Wood (processed)                                                                             |
| G940   |         10 | 0.00326531  |  0.000364339 |          98 |   0.0408163 | Foamed EVA (flexible plastic) for crafts & watersports                                       |
| G942   |         10 | 0.00612245  |  0.000364339 |          98 |   0.0816327 | Plastic shavings from lathes, CNC machining                                                  |
| G901   |         10 | 0.00295918  |  0.000364339 |          98 |   0.0816327 | Mask medical, synthetic                                                                      |
| G210   |         10 | 0.00204082  |  0.000364339 |          98 |   0.0408163 | Other glass/ceramic                                                                          |
| G11    |         10 | 0.00367347  |  0.000364339 |          98 |   0.0816327 | Cosmetics for the beach, e.g. sunblock                                                       |
| G158   |         10 | 0.00306122  |  0.000364339 |          98 |   0.0306122 | Other paper items                                                                            |
| G938   |          9 | 0.00234694  |  0.000327905 |          98 |   0.0816327 | Toothpicks, dental floss plastic                                                             |
| G8     |          9 | 0.00316327  |  0.000327905 |          98 |   0.0714286 | Drink bottles  > 0.5L                                                                        |
| G128   |          8 | 0.00193878  |  0.000291471 |          98 |   0.0612245 | Tires and belts                                                                              |
| G926   |          8 | 0.00234694  |  0.000291471 |          98 |   0.0612245 | Chewing gum, often contains plastics                                                         |
| G133   |          8 | 0.0027551   |  0.000291471 |          98 |   0.0714286 | Condoms incl. packaging                                                                      |
| G119   |          8 | 0.00214286  |  0.000291471 |          98 |   0.0102041 | Sheetlike user plastic (>1mm)                                                                |
| G118   |          8 | 0.00183673  |  0.000291471 |          98 |   0.0408163 | Small industrial spheres <5mm                                                                |
| G68    |          7 | 0.00132653  |  0.000255037 |          98 |   0.0612245 | Fiberglass fragments                                                                         |
| G916   |          7 | 0.00102041  |  0.000255037 |          98 |   0.0612245 | Pencils and pieces                                                                           |
| G900   |          7 | 0.0022449   |  0.000255037 |          98 |   0.0612245 | Gloves latex  personal protective equipment                                                  |
| G929   |          7 | 0.00112245  |  0.000255037 |          98 |   0.0612245 | Electronics and pieces; sensors, headsets etc.                                               |
| G61    |          7 | 0.00377551  |  0.000255037 |          98 |   0.0612245 | Other fishing related                                                                        |
| G176   |          6 | 0.00183673  |  0.000218603 |          98 |   0.0306122 | Cans, food                                                                                   |
| G933   |          6 | 0.00244898  |  0.000218603 |          98 |   0.0204082 | Bags, cases for accessories; glasses, electronics, incl. straps, pieces, plstc. nylon etc.   |
| G101   |          5 | 0.00142857  |  0.000182169 |          98 |   0.0510204 | Dog feces bag                                                                                |
| G167   |          5 | 0.00122449  |  0.000182169 |          98 |   0.0306122 | Matches or fireworks                                                                         |
| G17    |          5 | 0.00183673  |  0.000182169 |          98 |   0.0204082 | Injection gun cartridge                                                                      |
| G195   |          5 | 0.00142857  |  0.000182169 |          98 |   0.0510204 | Batteries - household                                                                        |
| G147   |          5 | 0.00102041  |  0.000182169 |          98 |   0.0510204 | Paper bags                                                                                   |
| G97    |          5 | 0.00163265  |  0.000182169 |          98 |   0.0510204 | Toilet fresheners                                                                            |
| G919   |          5 | 0.00397959  |  0.000182169 |          98 |   0.0408163 | Nails, screws, bolts etc.                                                                    |
| G917   |          5 | 0.00183673  |  0.000182169 |          98 |   0.0306122 | Terracotta balls                                                                             |
| G136   |          4 | 0.00132653  |  0.000145735 |          98 |   0.0306122 | Shoes                                                                                        |
| G931   |          4 | 0.00153061  |  0.000145735 |          98 |   0.0204082 | Tape-caution for barrier, police, construction etc.                                          |
| G181   |          4 | 0.00122449  |  0.000145735 |          98 |   0.0408163 | Tableware metal;  cups, cutlery etc.                                                         |
| G29    |          4 | 0.00132653  |  0.000145735 |          98 |   0.0408163 | Combs, brushes and sunglasses                                                                |
| G915   |          3 | 0.00204082  |  0.000109302 |          98 |   0.0306122 | Reflectors, plastic mobility items                                                           |
| G906   |          3 | 0.000816327 |  0.000109302 |          98 |   0.0306122 | coffee capsules aluminum                                                                     |
| G913   |          3 | 0.000816327 |  0.000109302 |          98 |   0.0306122 | Pacifier                                                                                     |
| G92    |          3 | 0.000612245 |  0.000109302 |          98 |   0.0306122 | Bait containers                                                                              |
| G116   |          3 | 0.00173469  |  0.000109302 |          98 |   0.0102041 | Granules <5mm                                                                                |
| G19    |          3 | 0.000816327 |  0.000109302 |          98 |   0.0204082 | Car parts                                                                                    |
| G108   |          3 | 0.000918367 |  0.000109302 |          98 |   0.0204082 | disk pellets  <5mm                                                                           |
| G63    |          3 | 0.000816327 |  0.000109302 |          98 |   0.0204082 | Buoys                                                                                        |
| G62    |          3 | 0.00112245  |  0.000109302 |          98 |   0.0204082 | Floats for nets                                                                              |
| G161   |          3 | 0.000612245 |  0.000109302 |          98 |   0.0204082 | Processed timber                                                                             |
| G104   |          3 | 0.000306122 |  0.000109302 |          98 |   0.0204082 | Plastic fragments subrounded <5mm                                                            |
| G37    |          3 | 0.00102041  |  0.000109302 |          98 |   0.0204082 | Mesh bags                                                                                    |
| G197   |          3 | 0.000918367 |  0.000109302 |          98 |   0.0306122 | Other metal                                                                                  |
| G199   |          2 | 0.000510204 |  7.28677e-05 |          98 |   0.0204082 | Other metal pieces > 50cm                                                                    |
| G13    |          2 | 0.000408163 |  7.28677e-05 |          98 |   0.0102041 | Bottles, containers, drums to transport, store material                                      |
| G139   |          2 | 0.000510204 |  7.28677e-05 |          98 |   0.0102041 | Backpacks                                                                                    |
| G140   |          2 | 0.000204082 |  7.28677e-05 |          98 |   0.0102041 | Bags, burlap, hessian, jute or hemp                                                          |
| G150   |          2 | 0.000306122 |  7.28677e-05 |          98 |   0.0204082 | Milk cartons, tetrapack                                                                      |
| G151   |          2 | 0.000612245 |  7.28677e-05 |          98 |   0.0204082 | Cartons, Tetrapacks                                                                          |
| G932   |          2 | 0.000714286 |  7.28677e-05 |          98 |   0.0102041 | Bio-beads, micro plastic for wastewater treatment, irregular shape, ridged sides < 5mm       |
| G907   |          2 | 0.000408163 |  7.28677e-05 |          98 |   0.0204082 | coffee capsules plastic                                                                      |
| G109   |          2 | 0.000204082 |  7.28677e-05 |          98 |   0.0102041 | Flat pellets  <5mm                                                                           |
| G925   |          2 | 0.000816327 |  7.28677e-05 |          98 |   0.0204082 | Packets: desiccant/ moisture absorbers, plastic case filled with silica                      |
| G107   |          2 | 0.000306122 |  7.28677e-05 |          98 |   0.0102041 | Cylindrical pellets < 5mm                                                                    |
| G55    |          2 | 0.000408163 |  7.28677e-05 |          98 |   0.0204082 | Fishing line (entangled)                                                                     |
| G5     |          2 | 0.000408163 |  7.28677e-05 |          98 |   0.0204082 | Generic plastic bags                                                                         |
| G36    |          2 | 0.000306122 |  7.28677e-05 |          98 |   0.0102041 | Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc. |
| G49    |          2 | 0.000510204 |  7.28677e-05 |          98 |   0.0204082 | Rope > 1cm                                                                                   |
| G154   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Newspapers or magazines                                                                      |
| G129   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Inner tubes and rubber sheets                                                                |
| G102   |          1 | 0.000306122 |  3.64339e-05 |          98 |   0.0102041 | Flip-flops                                                                                   |
| G138   |          1 | 0.000408163 |  3.64339e-05 |          98 |   0.0102041 | Shoes and sandals                                                                            |
| G64    |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Fenders                                                                                      |
| G14    |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Engine oil bottles                                                                           |
| G51    |          1 | 0.000102041 |  3.64339e-05 |          98 |   0.0102041 | Fishing net                                                                                  |
| G202   |          1 | 0.000408163 |  3.64339e-05 |          98 |   0.0102041 | Light bulbs                                                                                  |
| G171   |          1 | 0.000102041 |  3.64339e-05 |          98 |   0.0102041 | Other wood < 50cm                                                                            |
| G172   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Other wood > 50cm                                                                            |
| G173   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Other                                                                                        |
| G935   |          1 | 0.000408163 |  3.64339e-05 |          98 |   0.0102041 | Walking stick pads and pieces, often elastomeric material                                    |
| G179   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Disposable BBQs                                                                              |
| G40    |          1 | 0.000510204 |  3.64339e-05 |          98 |   0.0102041 | Gloves household/gardening                                                                   |
| G183   |          1 | 0.00122449  |  3.64339e-05 |          98 |   0.0102041 | Fish hook remains                                                                            |
| G39    |          1 | 0.000102041 |  3.64339e-05 |          98 |   0.0102041 | Gloves                                                                                       |
| G193   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | car parts and batteries                                                                      |
| G166   |          1 | 0.000204082 |  3.64339e-05 |          98 |   0.0102041 | Paint brushes                                                                                |
