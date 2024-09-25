

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

# Vaud canton

**Summary and analysis of observations of trash density**: objects related to recreation, personal items, unclassified, infrastructure, food and drink, packaging non food, plastic pieces, waste water, agriculture, tobacco and micro plastics (< 5mm) found in lakes and rivers. <i>Report number: Vaud canton 2020-01-01 2021-05-31</i>



## Administrative boundaries Vaud canton 2020-01-01 2021-05-31 : Cities, cantons, survey areas

The number and and names of the cities, cantons and survey areas included in this report



The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis.

Please provide a narrative of the contents of the following table. In your narrative be sure to include the list of cities and the names of the canton and survey areas.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

 |              |   count |
|:-------------|--------:|
| location     |      26 |
| city         |      14 |
| canton       |       1 |
| survey areas |       2 |

The following is the names of the cities, cantons, and survey areas.

city: La Tour-de-Peilz, Montreux, Tolochenaz, Bourg-en-Lavaux, Cudrefin, Allaman, Yverdon-les-Bains, Gland, Lavey-Morcles, Saint-Sulpice (VD), Grandson, Préverenges, Vevey, Lausanne
canton: Vaud
survey_area: rhone, aare


## Named features Vaud canton 2020-01-01 2021-05-31 : The lakes, rivers and parks

The number and names of the lakes, rivers or parks included in this report



The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. Please provide a concise narrative of the contents of the following table. In your narrative be sure to the name of each park, lake or river

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
 INSTRUCTION_END ---> 

|       |   river |   lake |
|:------|--------:|-------:|
| count |       2 |      2 |

The following is the names of the lakes, rivers and parks included in the data.

river: la-thiele, rhone
lake: lac-leman, neuenburgersee
park: 


## Summary statistics Vaud canton 2020-01-01 2021-05-31: The descriptive statistics of the survey results

Vaud: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.





This table summarizes the sample total in pcs/m for each survey. Each survey is defined by a sample_id. A survey total is the sum of all rows that have the same sample_id.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

|        |   total |   nsamples |   average |   5th |   25th |   50th |   75th |   95th |     std |   max | start      | end        |
|:-------|--------:|-----------:|----------:|------:|-------:|-------:|-------:|-------:|--------:|------:|:-----------|:-----------|
| result |   17414 |         87 |   6.42149 | 0.463 |   2.07 |   3.62 |  6.915 | 18.276 | 9.30723 | 66.17 | 2020-04-28 | 2021-05-12 |

## Material composition of objects Vaud canton 2020-01-01 2021-05-31: estimated material composition

Vaud: The proportion of each material type according to material category





The following table details the proportion that each material type represents to the total. 
Generate a narrative summary based on the following table. You need to include all the material types and their float values.
If there is more than one material entry in the table.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. Consider the example above

 INSTRUCTION_END ---> 

| material   | % of total   |
|:-----------|:-------------|
| glass      | 4%           |
| metal      | 2%           |
| paper      | 1%           |
| plastic    | 89%          |
## Survey Totals for city


## Vaud canton 2020-01-01 2021-05-31 city: The average pcs/m by city.

The average sample total for each city in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | city               |   quantity |    pcs/m |
|---:|:-------------------|-----------:|---------:|
|  0 | Allaman            |        631 |  7.22667 |
|  1 | Bourg-en-Lavaux    |        121 |  5.015   |
|  2 | Cudrefin           |         27 |  2.23    |
|  3 | Gland              |        134 |  1.43    |
|  4 | Grandson           |        104 |  1.41    |
|  5 | La Tour-de-Peilz   |       2936 |  4.326   |
|  6 | Lausanne           |        997 | 19.4114  |
|  7 | Lavey-Morcles      |        594 |  3.29333 |
|  8 | Montreux           |        738 |  4.21    |
|  9 | Préverenges        |       3744 |  6.61615 |
| 10 | Saint-Sulpice (VD) |       2507 | 18.426   |
| 11 | Tolochenaz         |        274 |  3.555   |
| 12 | Vevey              |       3163 |  6.38917 |
| 13 | Yverdon-les-Bains  |       1444 |  1.31571 |


## Survey Totals for parent_boundary


## Vaud canton 2020-01-01 2021-05-31 survey area: The average pcs/m by survey area.

The average sample total for each survey area in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | parent_boundary   |   quantity |   pcs/m |
|---:|:------------------|-----------:|--------:|
|  0 | aare              |       1575 | 1.37875 |
|  1 | rhone             |      15839 | 7.55789 |



## Inventory items Vaud canton 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |       pcs/m |   % of total |   sample_id |   fail rate | object                                                                                       |
|:-------|-----------:|------------:|-------------:|------------:|------------:|:---------------------------------------------------------------------------------------------|
| Gfrags |       2544 | 1.16966     |  0.146089    |          87 |   0.954023  | Fragmented plastics                                                                          |
| G27    |       2366 | 0.805172    |  0.135868    |          87 |   0.91954   | Cigarette filters                                                                            |
| Gfoams |       2100 | 0.897471    |  0.120593    |          87 |   0.827586  | Expanded polystyrene                                                                         |
| G30    |       1050 | 0.32069     |  0.0602963   |          87 |   0.954023  | Food wrappers; candy, snacks                                                                 |
| G112   |        907 | 0.384483    |  0.0520845   |          87 |   0.436782  | Industrial pellets (nurdles)                                                                 |
| G67    |        639 | 0.190345    |  0.0366946   |          87 |   0.827586  | Industrial sheeting                                                                          |
| G95    |        623 | 0.217701    |  0.0357758   |          87 |   0.793103  | Cotton bud/swab sticks                                                                       |
| G74    |        603 | 0.12        |  0.0346273   |          87 |   1.12644   | Foam packaging/insulation/polyurethane                                                       |
| G117   |        547 | 0.198736    |  0.0314115   |          87 |   0.298851  | Styrofoam < 5mm                                                                              |
| Gcaps  |        543 | 0.172644    |  0.0311818   |          87 |   0.83908   | plastic caps, lid rings: G21, G22, G23, G24                                                  |
| G200   |        429 | 0.149885    |  0.0246354   |          87 |   0.597701  | Glass drink bottles, pieces                                                                  |
| G89    |        279 | 0.0805747   |  0.0160216   |          87 |   0.655172  | Plastic construction waste                                                                   |
| G98    |        271 | 0.0625287   |  0.0155622   |          87 |   0.390805  | Diapers - wipes                                                                              |
| G103   |        204 | 0.0675862   |  0.0117147   |          87 |   0.0574713 | Plastic fragments rounded <5mm                                                               |
| G35    |        178 | 0.0593103   |  0.0102217   |          87 |   0.666667  | Straws and stirrers                                                                          |
| G921   |        173 | 0.0514943   |  0.00993454  |          87 |   0.275862  | Ceramic tile and pieces                                                                      |
| G106   |        173 | 0.0781609   |  0.00993454  |          87 |   0.252874  | Plastic fragments angular <5mm                                                               |
| G3     |        169 | 0.0582759   |  0.00970484  |          87 |   0.252874  | Bags; plastic shopping/carrier/grocery and pieces                                            |
| G177   |        161 | 0.0516092   |  0.00924543  |          87 |   0.586207  | Foil wrappers, aluminum foil                                                                 |
| G25    |        154 | 0.0471264   |  0.00884346  |          87 |   0.528736  | Tobacco; plastic packaging, containers                                                       |
| G31    |        136 | 0.0516092   |  0.00780981  |          87 |   0.62069   | Lollypop sticks                                                                              |
| G178   |        134 | 0.0478161   |  0.00769496  |          87 |   0.609195  | Metal bottle caps, lids & pull tabs from cans                                                |
| G73    |        123 | 0.0471264   |  0.00706328  |          87 |   0.390805  | Foamed items & pieces (non packaging/insulation) foamed sponge material                      |
| G100   |        122 | 0.0597701   |  0.00700586  |          87 |   0.563218  | Medical; containers/tubes/ packaging                                                         |
| G38    |        114 | 0.0267816   |  0.00654646  |          87 |   0.091954  | Coverings; plastic packaging, sheeting for protecting large cargo items                      |
| G10    |        111 | 0.0318391   |  0.00637418  |          87 |   0.448276  | Food containers single use foamed or plastic                                                 |
| G70    |        110 | 0.0333333   |  0.00631676  |          87 |   0.425287  | Shotgun cartridges                                                                           |
| G941   |        107 | 0.0250575   |  0.00614448  |          87 |   0.229885  | Packaging films nonfood or unknown                                                           |
| G32    |        104 | 0.0371264   |  0.00597221  |          87 |   0.574713  | Toys and party favors                                                                        |
| G66    |         98 | 0.0398851   |  0.00562766  |          87 |   0.390805  | Straps/bands;  hard, plastic package fastener                                                |
| G33    |         85 | 0.023908    |  0.00488113  |          87 |   0.54023   | Cups, lids, single use foamed and hard plastic                                               |
| G922   |         71 | 0.0198851   |  0.00407718  |          87 |   0.321839  | Labels, bar codes                                                                            |
| G156   |         70 | 0.0198851   |  0.00401975  |          87 |   0.264368  | Paper fragments                                                                              |
| G165   |         62 | 0.0167816   |  0.00356035  |          87 |   0.229885  | Ice cream sticks, toothpicks, chopsticks                                                     |
| G159   |         54 | 0.018046    |  0.00310095  |          87 |   0.344828  | Corks                                                                                        |
| G204   |         53 | 0.0104598   |  0.00304353  |          87 |   0.126437  | Construction material; bricks, pipes, cement                                                 |
| G153   |         51 | 0.0156322   |  0.00292868  |          87 |   0.16092   | Cups, food containers, wrappers (paper)                                                      |
| G125   |         50 | 0.0222989   |  0.00287125  |          87 |   0.229885  | Balloons and balloon sticks                                                                  |
| G137   |         50 | 0.0118391   |  0.00287125  |          87 |   0.172414  | Clothing, towels & rags                                                                      |
| G91    |         48 | 0.0137931   |  0.0027564   |          87 |   0.287356  | Biomass holder                                                                               |
| G211   |         47 | 0.0163218   |  0.00269898  |          87 |   0.333333  | Other medical (swabs, bandaging, adhesive plaster)                                           |
| G96    |         47 | 0.0135632   |  0.00269898  |          87 |   0.275862  | Sanitary pads /panty liners/tampons and applicators                                          |
| G904   |         46 | 0.0118391   |  0.00264155  |          87 |   0.195402  | Fireworks; rocket caps, exploded parts & packaging                                           |
| G146   |         43 | 0.0150575   |  0.00246928  |          87 |   0.126437  | Paper, cardboard                                                                             |
| G50    |         42 | 0.011954    |  0.00241185  |          87 |   0.252874  | String < 1cm                                                                                 |
| G923   |         40 | 0.0251724   |  0.002297    |          87 |   0.206897  | Tissue, toilet paper, napkins, paper towels                                                  |
| G152   |         38 | 0.0126437   |  0.00218215  |          87 |   0.149425  | Cigarette boxes, tobacco related paper/cardboard                                             |
| G105   |         38 | 0.0390805   |  0.00218215  |          87 |   0.0574713 | Plastic fragments subangular <5mm                                                            |
| G914   |         37 | 0.0148276   |  0.00212473  |          87 |   0.218391  | Paperclips, clothespins, plastic utility items                                               |
| G198   |         37 | 0.00850575  |  0.00212473  |          87 |   0.241379  | Other metal pieces < 50cm                                                                    |
| G93    |         33 | 0.0105747   |  0.00189503  |          87 |   0.218391  | Cable ties; steggel, zip, zap straps                                                         |
| G90    |         33 | 0.0101149   |  0.00189503  |          87 |   0.195402  | Plastic flower pots                                                                          |
| G131   |         32 | 0.01        |  0.0018376   |          87 |   0.229885  | Rubber bands                                                                                 |
| G905   |         30 | 0.00862069  |  0.00172275  |          87 |   0.252874  | Hair clip,  hair ties, personal accessories plastic                                          |
| G937   |         30 | 0.0106897   |  0.00172275  |          87 |   0.126437  | Pheromone baits for vineyards                                                                |
| G207   |         30 | 0.0122989   |  0.00172275  |          87 |   0.0114943 | Octopus pots                                                                                 |
| G908   |         27 | 0.00747126  |  0.00155048  |          87 |   0.103448  | Tape; electrical, insulating                                                                 |
| G124   |         27 | 0.00655172  |  0.00155048  |          87 |   0.114943  | Other plastic or foam products                                                               |
| G26    |         27 | 0.00827586  |  0.00155048  |          87 |   0.229885  | Cigarette lighters                                                                           |
| G939   |         27 | 0.00609195  |  0.00155048  |          87 |   0.103448  | Flowers, plants plastic                                                                      |
| G28    |         26 | 0.00804598  |  0.00149305  |          87 |   0.195402  | Pens, lids, mechanical pencils etc.                                                          |
| G144   |         26 | 0.0122989   |  0.00149305  |          87 |   0.114943  | Tampons                                                                                      |
| G208   |         25 | 0.012069    |  0.00143563  |          87 |   0.103448  | Glass or ceramic fragments > 2.5 cm                                                          |
| G34    |         25 | 0.00793103  |  0.00143563  |          87 |   0.16092   | Cutlery, plates and trays                                                                    |
| G157   |         24 | 0.0109195   |  0.0013782   |          87 |   0.103448  | Paper                                                                                        |
| G115   |         24 | 0.00689655  |  0.0013782   |          87 |   0.0229885 | Foamed  plastic <5mm                                                                         |
| G191   |         22 | 0.00666667  |  0.00126335  |          87 |   0.137931  | Wire and mesh                                                                                |
| G175   |         22 | 0.00413793  |  0.00126335  |          87 |   0.091954  | Cans, beverage                                                                               |
| G142   |         19 | 0.00655172  |  0.00109108  |          87 |   0.172414  | Rope , string or nets                                                                        |
| G135   |         19 | 0.00678161  |  0.00109108  |          87 |   0.103448  | Clothes, footware, headware, gloves                                                          |
| G20    |         18 | 0.00689655  |  0.00103365  |          87 |   0.103448  | Caps and lids                                                                                |
| G2     |         17 | 0.00494253  |  0.000976226 |          87 |   0.103448  | Bags                                                                                         |
| G149   |         17 | 0.00781609  |  0.000976226 |          87 |   0.126437  | Paper packaging                                                                              |
| G4     |         16 | 0.0045977   |  0.000918801 |          87 |   0.103448  | Small plastic bags; freezer, zip-lock etc.                                                   |
| G213   |         16 | 0.00712644  |  0.000918801 |          87 |   0.126437  | Paraffin wax                                                                                 |
| G87    |         15 | 0.00229885  |  0.000861376 |          87 |   0.103448  | Tape, masking/duct/packing                                                                   |
| G126   |         15 | 0.0054023   |  0.000861376 |          87 |   0.103448  | Balls                                                                                        |
| G6     |         14 | 0.00390805  |  0.000803951 |          87 |   0.045977  | Bottles and containers, plastic non food/drink                                               |
| G186   |         14 | 0.00448276  |  0.000803951 |          87 |   0.0689655 | Industrial scrap                                                                             |
| G65    |         14 | 0.00505747  |  0.000803951 |          87 |   0.103448  | Buckets                                                                                      |
| G134   |         13 | 0.00298851  |  0.000746526 |          87 |   0.091954  | Other rubber                                                                                 |
| G194   |         13 | 0.00436782  |  0.000746526 |          87 |   0.137931  | Cables, metal wire(s) often inside rubber or plastic tubes                                   |
| G48    |         12 | 0.00517241  |  0.000689101 |          87 |   0.114943  | Rope, synthetic                                                                              |
| G182   |         12 | 0.00436782  |  0.000689101 |          87 |   0.0689655 | Fishing; hooks, weights, lures, sinkers etc.                                                 |
| G64    |         12 | 0.00149425  |  0.000689101 |          87 |   0.0344828 | Fenders                                                                                      |
| G928   |         11 | 0.00344828  |  0.000631676 |          87 |   0.0574713 | Ribbons and bows                                                                             |
| G927   |         11 | 0.00321839  |  0.000631676 |          87 |   0.0689655 | String trimmer line, used to cut grass, weeds, and shrubbery                                 |
| G99    |         11 | 0.00505747  |  0.000631676 |          87 |   0.114943  | Syringes - needles                                                                           |
| G199   |         11 | 0.00137931  |  0.000631676 |          87 |   0.0229885 | Other metal pieces > 50cm                                                                    |
| G943   |         11 | 0.00252874  |  0.000631676 |          87 |   0.0574713 | Fencing agriculture, plastic                                                                 |
| G158   |         10 | 0.00344828  |  0.000574251 |          87 |   0.0344828 | Other paper items                                                                            |
| G201   |         10 | 0.00344828  |  0.000574251 |          87 |   0.045977  | Jars, includes pieces                                                                        |
| G59    |         10 | 0.00390805  |  0.000574251 |          87 |   0.0689655 | Fishing line monofilament (angling)                                                          |
| G8     |         10 | 0.00137931  |  0.000574251 |          87 |   0.045977  | Drink bottles  > 0.5L                                                                        |
| G145   |          9 | 0.00287356  |  0.000516826 |          87 |   0.0804598 | Other textiles                                                                               |
| G148   |          9 | 0.00229885  |  0.000516826 |          87 |   0.0689655 | Cardboard (boxes and fragments)                                                              |
| G940   |          9 | 0.00183908  |  0.000516826 |          87 |   0.0574713 | Foamed EVA (flexible plastic) for crafts & watersports                                       |
| G210   |          9 | 0.00528736  |  0.000516826 |          87 |   0.045977  | Other glass/ceramic                                                                          |
| G203   |          9 | 0.00333333  |  0.000516826 |          87 |   0.045977  | Tableware ceramic or glass, cups, plates, pieces                                             |
| G11    |          8 | 0.00310345  |  0.0004594   |          87 |   0.0804598 | Cosmetics for the beach, e.g. sunblock                                                       |
| G938   |          8 | 0.00264368  |  0.0004594   |          87 |   0.0804598 | Toothpicks, dental floss plastic                                                             |
| G930   |          8 | 0.00206897  |  0.0004594   |          87 |   0.0804598 | Foam earplugs                                                                                |
| G7     |          8 | 0.00390805  |  0.0004594   |          87 |   0.0689655 | Drink bottles < = 0.5L                                                                       |
| G128   |          8 | 0.00218391  |  0.0004594   |          87 |   0.0689655 | Tires and belts                                                                              |
| G119   |          8 | 0.00241379  |  0.0004594   |          87 |   0.0114943 | Sheetlike user plastic (>1mm)                                                                |
| G101   |          8 | 0.00195402  |  0.0004594   |          87 |   0.0804598 | Dog feces bag                                                                                |
| G936   |          8 | 0.00183908  |  0.0004594   |          87 |   0.0574713 | Sheeting ag. greenhouse film                                                                 |
| G942   |          8 | 0.00551724  |  0.0004594   |          87 |   0.0804598 | Plastic shavings from lathes, CNC machining                                                  |
| G919   |          7 | 0.00482759  |  0.000401975 |          87 |   0.045977  | Nails, screws, bolts etc.                                                                    |
| G933   |          7 | 0.00287356  |  0.000401975 |          87 |   0.0344828 | Bags, cases for accessories; glasses, electronics, incl. straps, pieces, plstc. nylon etc.   |
| G12    |          7 | 0.00172414  |  0.000401975 |          87 |   0.0804598 | Cosmetics, non-beach use personal care containers                                            |
| G926   |          6 | 0.00218391  |  0.00034455  |          87 |   0.045977  | Chewing gum, often contains plastics                                                         |
| G918   |          6 | 0.00321839  |  0.00034455  |          87 |   0.0689655 | Safety pins, paper clips, small metal utility items                                          |
| G118   |          6 | 0.00183908  |  0.00034455  |          87 |   0.0344828 | Small industrial spheres <5mm                                                                |
| G43    |          6 | 0.00103448  |  0.00034455  |          87 |   0.0229885 | Tags fishing or industry (security tags, seals)                                              |
| G901   |          6 | 0.00137931  |  0.00034455  |          87 |   0.0689655 | Mask medical, synthetic                                                                      |
| G61    |          5 | 0.00344828  |  0.000287125 |          87 |   0.0574713 | Other fishing related                                                                        |
| G36    |          5 | 0.00287356  |  0.000287125 |          87 |   0.0114943 | Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc. |
| G170   |          5 | 0.00195402  |  0.000287125 |          87 |   0.0344828 | Wood (processed)                                                                             |
| G195   |          5 | 0.0016092   |  0.000287125 |          87 |   0.0574713 | Batteries - household                                                                        |
| G917   |          5 | 0.00206897  |  0.000287125 |          87 |   0.0344828 | Terracotta balls                                                                             |
| G136   |          5 | 0.00091954  |  0.000287125 |          87 |   0.0344828 | Shoes                                                                                        |
| G37    |          5 | 0.00114943  |  0.000287125 |          87 |   0.0229885 | Mesh bags                                                                                    |
| G68    |          5 | 0.00126437  |  0.000287125 |          87 |   0.045977  | Fiberglass fragments                                                                         |
| G915   |          4 | 0.00264368  |  0.0002297   |          87 |   0.0344828 | Reflectors, plastic mobility items                                                           |
| G176   |          4 | 0.00114943  |  0.0002297   |          87 |   0.0344828 | Cans, food                                                                                   |
| G931   |          4 | 0.000804598 |  0.0002297   |          87 |   0.0344828 | Tape-caution for barrier, police, construction etc.                                          |
| G107   |          3 | 0.00045977  |  0.000172275 |          87 |   0.0229885 | Cylindrical pellets < 5mm                                                                    |
| G161   |          3 | 0.000689655 |  0.000172275 |          87 |   0.0229885 | Processed timber                                                                             |
| G17    |          3 | 0.000804598 |  0.000172275 |          87 |   0.0114943 | Injection gun cartridge                                                                      |
| G929   |          3 | 0.000804598 |  0.000172275 |          87 |   0.0344828 | Electronics and pieces; sensors, headsets etc.                                               |
| G900   |          3 | 0.000689655 |  0.000172275 |          87 |   0.0344828 | Gloves latex  personal protective equipment                                                  |
| G197   |          3 | 0.00103448  |  0.000172275 |          87 |   0.0344828 | Other metal                                                                                  |
| G40    |          3 | 0.00091954  |  0.000172275 |          87 |   0.0229885 | Gloves household/gardening                                                                   |
| G108   |          3 | 0.00103448  |  0.000172275 |          87 |   0.0229885 | disk pellets  <5mm                                                                           |
| G129   |          3 | 0.00045977  |  0.000172275 |          87 |   0.0229885 | Inner tubes and rubber sheets                                                                |
| G133   |          3 | 0.00114943  |  0.000172275 |          87 |   0.0344828 | Condoms incl. packaging                                                                      |
| G13    |          3 | 0.000574713 |  0.000172275 |          87 |   0.0229885 | Bottles, containers, drums to transport, store material                                      |
| G104   |          2 | 0.000229885 |  0.00011485  |          87 |   0.0114943 | Plastic fragments subrounded <5mm                                                            |
| G147   |          2 | 0.00045977  |  0.00011485  |          87 |   0.0229885 | Paper bags                                                                                   |
| G97    |          2 | 0.000574713 |  0.00011485  |          87 |   0.0229885 | Toilet fresheners                                                                            |
| G155   |          2 | 0.000574713 |  0.00011485  |          87 |   0.0229885 | Fireworks paper tubes and fragments                                                          |
| G19    |          2 | 0.000229885 |  0.00011485  |          87 |   0.0114943 | Car parts                                                                                    |
| G39    |          2 | 0.000344828 |  0.00011485  |          87 |   0.0114943 | Gloves                                                                                       |
| G181   |          2 | 0.000689655 |  0.00011485  |          87 |   0.0229885 | Tableware metal;  cups, cutlery etc.                                                         |
| G932   |          2 | 0.000804598 |  0.00011485  |          87 |   0.0114943 | Bio-beads, micro plastic for wastewater treatment, irregular shape, ridged sides < 5mm       |
| G29    |          2 | 0.000804598 |  0.00011485  |          87 |   0.0229885 | Combs, brushes and sunglasses                                                                |
| G139   |          2 | 0.000574713 |  0.00011485  |          87 |   0.0114943 | Backpacks                                                                                    |
| G14    |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Engine oil bottles                                                                           |
| G172   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Other wood > 50cm                                                                            |
| G902   |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Mask medical, cloth                                                                          |
| G167   |          1 | 0.00091954  |  5.74251e-05 |          87 |   0.0114943 | Matches or fireworks                                                                         |
| G51    |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Fishing net                                                                                  |
| G916   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Pencils and pieces                                                                           |
| G173   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Other                                                                                        |
| G174   |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Aerosol spray cans                                                                           |
| G179   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Disposable BBQs                                                                              |
| G906   |          1 | 0.000344828 |  5.74251e-05 |          87 |   0.0114943 | coffee capsules aluminum                                                                     |
| G183   |          1 | 0.00137931  |  5.74251e-05 |          87 |   0.0114943 | Fish hook remains                                                                            |
| G907   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | coffee capsules plastic                                                                      |
| G202   |          1 | 0.00045977  |  5.74251e-05 |          87 |   0.0114943 | Light bulbs                                                                                  |
| G193   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | car parts and batteries                                                                      |
| G5     |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Generic plastic bags                                                                         |
| G55    |          1 | 0.000344828 |  5.74251e-05 |          87 |   0.0114943 | Fishing line (entangled)                                                                     |
| G913   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Pacifier                                                                                     |
| G49    |          1 | 0.000344828 |  5.74251e-05 |          87 |   0.0114943 | Rope > 1cm                                                                                   |
| G185   |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Middle size containers                                                                       |

## Sampling stratification Vaud canton 2020-01-01 2021-05-31: The environmental features surrounding the survey location.

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
| 0-20%                  | 6.9%                                               | 100.0%                                            | 94.3%                                           | 80.5%                                                    | 100.0%                                              | 82.8%                                              | 8.0%                                             | 97.7%                                              | 100.0%                                            |
| 20-40%                 | 8.0%                                               | none                                              | 4.6%                                            | 17.2%                                                    | none                                                | 8.0%                                               | 19.5%                                            | none                                               | none                                              |
| 40-60%                 | 2.3%                                               | none                                              | 1.1%                                            | 2.3%                                                     | none                                                | 9.2%                                               | 56.3%                                            | 2.3%                                               | none                                              |
| 60-80%                 | 36.8%                                              | none                                              | none                                            | none                                                     | none                                                | none                                               | 3.4%                                             | none                                               | none                                              |
| 80-100%                | 46.0%                                              | none                                              | none                                            | none                                                     | none                                                | none                                               | 12.6%                                            | none                                               | none                                              |

## Sampling stratification and trash density Vaud canton 2020-01-01 2021-05-31: The changes in the observed litter density and the changes in land use



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
| 0-20%                  |                                      4.84833 | 6.421494252873564                           | 6.657682926829269                         | 4.270714285714286                                  | 6.421494252873564                             | 6.98625                                      |                                    5.72857 | 6.454588235294119                            | 6.421494252873564                           |
| 20-40%                 |                                      2.96571 | none                                        | 2.0475000000000003                        | 16.646                                             | none                                          | 3.8600000000000003                           |                                    3.30647 | none                                         | none                                        |
| 40-60%                 |                                      2.905   | none                                        | 4.55                                      | 5.015                                              | none                                          | 3.5799999999999996                           |                                    4.93755 | 5.015                                        | none                                        |
| 60-80%                 |                                      4.08625 | none                                        | none                                      | none                                               | none                                          | none                                         |                                   24.7333  | none                                         | none                                        |
| 80-100%                |                                      9.30625 | none                                        | none                                      | none                                               | none                                          | none                                         |                                   13.2927  | none                                         | none                                        |

## Grid forecast Vaud canton 2020-01-01 2021-05-31


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
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7600000000000005
The expected posterior distribution is a grid approximation from 0 to 51.050000000000004 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   2.3045  |
| std   |   3.00639 |
| min   |   0       |
| 25%   |   0.645   |
| 50%   |   1.5     |
| 75%   |   2.4225  |
| max   |  16.96    |

### In boundary grid approximation
This prior distribution is selected from random samples from within the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood feature variables  and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations in the geographic boundary ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.4300000000000001
The expected posterior distribution is a grid approximation from 0 to 51.050000000000004 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   3.3227  |
| std   |   5.15642 |
| min   |   0.05    |
| 25%   |   0.755   |
| 50%   |   1.87    |
| 75%   |   3.735   |
| max   |  42.06    |

### Out boundary grid approximation
This prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations outside the geographic boundary ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7600000000000005
The expected posterior distribution is a grid approximation from 0 to 51.050000000000004 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   2.2066  |
| std   |   2.65252 |
| min   |   0       |
| 25%   |   0.4975  |
| 50%   |   1.24    |
| 75%   |   2.905   |
| max   |  13.4     |




### Cluster analysis Vaud canton 2020-01-01 2021-05-31


Vaud: Cluster compositionThe survey locations were labeled according to the type and magnitude of land use in a 1 500 m buffer zone aroundaround each survey location. A cluster analysis was performed using K-Means clustering, the optimal amount of clusters was determined using the elbow method. Each cluster represents a group of locations that have similar land use profiles, that is the locations are surrounded by similar quantities of buildings or forest or undefined land use.We consider the cluster composition and the proportion of each cluster dedicated to a particular land use. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location whose buffer zone was 45% dedicated to forest. 

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
|         0 |       0.055 |      0     |    0.357 |             0.011 |        0.125 |       0.588 |  0.139474 | 6.93889e-18 |       0    |
|         1 |       1     |      0     |    0     |             0.079 |        0.02  |       0     |  0        | 6.93889e-18 |       0    |
|         2 |       0.203 |      0     |    0.07  |             0.467 |        0.003 |       0.236 |  0.533138 | 0.481       |       0.01 |
|         3 |       0.182 |      0     |    0.492 |             0.142 |        0.006 |       0.222 |  1        | 6.93889e-18 |       0    |
|         4 |       0.945 |      0     |    0.041 |             0.38  |        0.044 |       0.014 |  0.571441 | 6.93889e-18 |       0    |
|         5 |       0.245 |      0.089 |    0.118 |             0.007 |        0.027 |       0.548 |  0.227685 | 6.93889e-18 |       0    |





Vaud: Average density per cluster
The following are the observed sample average per cluster. The units is objects per meter of beach. The columns are the use case of the objects: personal or professional. The index is
the cluster number.

Table has the following format:

1. the columns are the object use case
2. the index is the cluster number
3. the value is the objects found per meter of beach

Convert the following table into a paragraph, reporting the values for each column along with their respective cluster values without any comments or analysis:
The narrative needs to be in paragraph format.

|   cluster |    pcs/m |
|----------:|---------:|
|         0 |  1.43    |
|         1 |  4.60985 |
|         2 |  5.015   |
|         3 |  3.29333 |
|         4 | 19.0008  |
|         5 |  1.82    |



### Summary of regression methods Vaud canton 2020-01-01 2021-05-31: 

In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. The feature variables are the land-use features identified in the land-use profile. From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model with the highest r² is then used in the BaggingRegressor and the VotingRegressor.





The following table details the results from different regression analysis of our data.

The table has the following format:

1. Model: the type of regression model used
2. R²: The coefficient of determination
3. MSE: the mean squared error

Generate a narrative summary based on the following table. You need to include all the models and the R² and MSE result.
The narrative needs to be in paragraph format.

|    | Model                        |        R² |      MSE |
|---:|:-----------------------------|----------:|---------:|
|  0 | Linear Regression            | -1.05037  | 0.421186 |
|  1 | Random Forest Regression     | -2.69357  | 0.758732 |
|  2 | Gradient Boosting Regression |  0.40006  | 0.12324  |
|  3 | Theil-Sen Regressor          |  0.500618 | 0.102583 |
|  4 | Bagging:Theil-Sen Regressor  |  0.472829 | 0.108291 |
|  5 | Voting                       | -0.43219  | 0.2942   |



### Feature and permutation importance Vaud canton 2020-01-01 2021-05-31



__Model feature importance__

Feature importance is a technique used in machine learning to identify and quantify the significance of different input variables (features) in predicting the target variable. In models like decision trees, random forests, and gradient boosting machines, feature importance is often calculated by measuring how much the model's accuracy or error changes when a particular feature is included versus when it is excluded. 
The following table details the model feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Coefficient |
|---:|:----------------|--------------:|
|  2 | public-services |     0.219878  |
|  5 | streets         |     0.158653  |
|  0 | buildings       |     0.145168  |
|  4 | undefined       |     0.082159  |
|  7 | orchards        |     0.015747  |
|  3 | recreation      |    -0.0416925 |
|  6 | vineyards       |    -0.0639743 |
|  1 | forest          |    -0.0785087 |



__Permutation feature importance__

Permutation importance is a model-agnostic method for assessing the importance of individual features in a predictive model. It is particularly useful because it can be applied to any type of model, whether it's a linear model, a decision tree, or a complex ensemble model. This method involves randomly shuffling the values of a feature in the dataset and observing the impact on the model's performance. A significant drop in performance indicates that the feature is important.
The following table details the permutation feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  2 | public-services |   0.601358   |
|  0 | buildings       |   0.252019   |
|  5 | streets         |   0.219584   |
|  6 | vineyards       |   0.0669095  |
|  1 | forest          |   0.0441402  |
|  3 | recreation      |   0.0417567  |
|  4 | undefined       |   0.0397685  |
|  7 | orchards        |   0.00520042 |


## Inventory items Vaud canton 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |       pcs/m |   % of total |   sample_id |   fail rate | object                                                                                       |
|:-------|-----------:|------------:|-------------:|------------:|------------:|:---------------------------------------------------------------------------------------------|
| Gfrags |       2544 | 1.16966     |  0.146089    |          87 |   0.954023  | Fragmented plastics                                                                          |
| G27    |       2366 | 0.805172    |  0.135868    |          87 |   0.91954   | Cigarette filters                                                                            |
| Gfoams |       2100 | 0.897471    |  0.120593    |          87 |   0.827586  | Expanded polystyrene                                                                         |
| G30    |       1050 | 0.32069     |  0.0602963   |          87 |   0.954023  | Food wrappers; candy, snacks                                                                 |
| G112   |        907 | 0.384483    |  0.0520845   |          87 |   0.436782  | Industrial pellets (nurdles)                                                                 |
| G67    |        639 | 0.190345    |  0.0366946   |          87 |   0.827586  | Industrial sheeting                                                                          |
| G95    |        623 | 0.217701    |  0.0357758   |          87 |   0.793103  | Cotton bud/swab sticks                                                                       |
| G74    |        603 | 0.12        |  0.0346273   |          87 |   1.12644   | Foam packaging/insulation/polyurethane                                                       |
| G117   |        547 | 0.198736    |  0.0314115   |          87 |   0.298851  | Styrofoam < 5mm                                                                              |
| Gcaps  |        543 | 0.172644    |  0.0311818   |          87 |   0.83908   | plastic caps, lid rings: G21, G22, G23, G24                                                  |
| G200   |        429 | 0.149885    |  0.0246354   |          87 |   0.597701  | Glass drink bottles, pieces                                                                  |
| G89    |        279 | 0.0805747   |  0.0160216   |          87 |   0.655172  | Plastic construction waste                                                                   |
| G98    |        271 | 0.0625287   |  0.0155622   |          87 |   0.390805  | Diapers - wipes                                                                              |
| G103   |        204 | 0.0675862   |  0.0117147   |          87 |   0.0574713 | Plastic fragments rounded <5mm                                                               |
| G35    |        178 | 0.0593103   |  0.0102217   |          87 |   0.666667  | Straws and stirrers                                                                          |
| G921   |        173 | 0.0514943   |  0.00993454  |          87 |   0.275862  | Ceramic tile and pieces                                                                      |
| G106   |        173 | 0.0781609   |  0.00993454  |          87 |   0.252874  | Plastic fragments angular <5mm                                                               |
| G3     |        169 | 0.0582759   |  0.00970484  |          87 |   0.252874  | Bags; plastic shopping/carrier/grocery and pieces                                            |
| G177   |        161 | 0.0516092   |  0.00924543  |          87 |   0.586207  | Foil wrappers, aluminum foil                                                                 |
| G25    |        154 | 0.0471264   |  0.00884346  |          87 |   0.528736  | Tobacco; plastic packaging, containers                                                       |
| G31    |        136 | 0.0516092   |  0.00780981  |          87 |   0.62069   | Lollypop sticks                                                                              |
| G178   |        134 | 0.0478161   |  0.00769496  |          87 |   0.609195  | Metal bottle caps, lids & pull tabs from cans                                                |
| G73    |        123 | 0.0471264   |  0.00706328  |          87 |   0.390805  | Foamed items & pieces (non packaging/insulation) foamed sponge material                      |
| G100   |        122 | 0.0597701   |  0.00700586  |          87 |   0.563218  | Medical; containers/tubes/ packaging                                                         |
| G38    |        114 | 0.0267816   |  0.00654646  |          87 |   0.091954  | Coverings; plastic packaging, sheeting for protecting large cargo items                      |
| G10    |        111 | 0.0318391   |  0.00637418  |          87 |   0.448276  | Food containers single use foamed or plastic                                                 |
| G70    |        110 | 0.0333333   |  0.00631676  |          87 |   0.425287  | Shotgun cartridges                                                                           |
| G941   |        107 | 0.0250575   |  0.00614448  |          87 |   0.229885  | Packaging films nonfood or unknown                                                           |
| G32    |        104 | 0.0371264   |  0.00597221  |          87 |   0.574713  | Toys and party favors                                                                        |
| G66    |         98 | 0.0398851   |  0.00562766  |          87 |   0.390805  | Straps/bands;  hard, plastic package fastener                                                |
| G33    |         85 | 0.023908    |  0.00488113  |          87 |   0.54023   | Cups, lids, single use foamed and hard plastic                                               |
| G922   |         71 | 0.0198851   |  0.00407718  |          87 |   0.321839  | Labels, bar codes                                                                            |
| G156   |         70 | 0.0198851   |  0.00401975  |          87 |   0.264368  | Paper fragments                                                                              |
| G165   |         62 | 0.0167816   |  0.00356035  |          87 |   0.229885  | Ice cream sticks, toothpicks, chopsticks                                                     |
| G159   |         54 | 0.018046    |  0.00310095  |          87 |   0.344828  | Corks                                                                                        |
| G204   |         53 | 0.0104598   |  0.00304353  |          87 |   0.126437  | Construction material; bricks, pipes, cement                                                 |
| G153   |         51 | 0.0156322   |  0.00292868  |          87 |   0.16092   | Cups, food containers, wrappers (paper)                                                      |
| G125   |         50 | 0.0222989   |  0.00287125  |          87 |   0.229885  | Balloons and balloon sticks                                                                  |
| G137   |         50 | 0.0118391   |  0.00287125  |          87 |   0.172414  | Clothing, towels & rags                                                                      |
| G91    |         48 | 0.0137931   |  0.0027564   |          87 |   0.287356  | Biomass holder                                                                               |
| G211   |         47 | 0.0163218   |  0.00269898  |          87 |   0.333333  | Other medical (swabs, bandaging, adhesive plaster)                                           |
| G96    |         47 | 0.0135632   |  0.00269898  |          87 |   0.275862  | Sanitary pads /panty liners/tampons and applicators                                          |
| G904   |         46 | 0.0118391   |  0.00264155  |          87 |   0.195402  | Fireworks; rocket caps, exploded parts & packaging                                           |
| G146   |         43 | 0.0150575   |  0.00246928  |          87 |   0.126437  | Paper, cardboard                                                                             |
| G50    |         42 | 0.011954    |  0.00241185  |          87 |   0.252874  | String < 1cm                                                                                 |
| G923   |         40 | 0.0251724   |  0.002297    |          87 |   0.206897  | Tissue, toilet paper, napkins, paper towels                                                  |
| G152   |         38 | 0.0126437   |  0.00218215  |          87 |   0.149425  | Cigarette boxes, tobacco related paper/cardboard                                             |
| G105   |         38 | 0.0390805   |  0.00218215  |          87 |   0.0574713 | Plastic fragments subangular <5mm                                                            |
| G914   |         37 | 0.0148276   |  0.00212473  |          87 |   0.218391  | Paperclips, clothespins, plastic utility items                                               |
| G198   |         37 | 0.00850575  |  0.00212473  |          87 |   0.241379  | Other metal pieces < 50cm                                                                    |
| G93    |         33 | 0.0105747   |  0.00189503  |          87 |   0.218391  | Cable ties; steggel, zip, zap straps                                                         |
| G90    |         33 | 0.0101149   |  0.00189503  |          87 |   0.195402  | Plastic flower pots                                                                          |
| G131   |         32 | 0.01        |  0.0018376   |          87 |   0.229885  | Rubber bands                                                                                 |
| G905   |         30 | 0.00862069  |  0.00172275  |          87 |   0.252874  | Hair clip,  hair ties, personal accessories plastic                                          |
| G937   |         30 | 0.0106897   |  0.00172275  |          87 |   0.126437  | Pheromone baits for vineyards                                                                |
| G207   |         30 | 0.0122989   |  0.00172275  |          87 |   0.0114943 | Octopus pots                                                                                 |
| G908   |         27 | 0.00747126  |  0.00155048  |          87 |   0.103448  | Tape; electrical, insulating                                                                 |
| G124   |         27 | 0.00655172  |  0.00155048  |          87 |   0.114943  | Other plastic or foam products                                                               |
| G26    |         27 | 0.00827586  |  0.00155048  |          87 |   0.229885  | Cigarette lighters                                                                           |
| G939   |         27 | 0.00609195  |  0.00155048  |          87 |   0.103448  | Flowers, plants plastic                                                                      |
| G28    |         26 | 0.00804598  |  0.00149305  |          87 |   0.195402  | Pens, lids, mechanical pencils etc.                                                          |
| G144   |         26 | 0.0122989   |  0.00149305  |          87 |   0.114943  | Tampons                                                                                      |
| G208   |         25 | 0.012069    |  0.00143563  |          87 |   0.103448  | Glass or ceramic fragments > 2.5 cm                                                          |
| G34    |         25 | 0.00793103  |  0.00143563  |          87 |   0.16092   | Cutlery, plates and trays                                                                    |
| G157   |         24 | 0.0109195   |  0.0013782   |          87 |   0.103448  | Paper                                                                                        |
| G115   |         24 | 0.00689655  |  0.0013782   |          87 |   0.0229885 | Foamed  plastic <5mm                                                                         |
| G191   |         22 | 0.00666667  |  0.00126335  |          87 |   0.137931  | Wire and mesh                                                                                |
| G175   |         22 | 0.00413793  |  0.00126335  |          87 |   0.091954  | Cans, beverage                                                                               |
| G142   |         19 | 0.00655172  |  0.00109108  |          87 |   0.172414  | Rope , string or nets                                                                        |
| G135   |         19 | 0.00678161  |  0.00109108  |          87 |   0.103448  | Clothes, footware, headware, gloves                                                          |
| G20    |         18 | 0.00689655  |  0.00103365  |          87 |   0.103448  | Caps and lids                                                                                |
| G2     |         17 | 0.00494253  |  0.000976226 |          87 |   0.103448  | Bags                                                                                         |
| G149   |         17 | 0.00781609  |  0.000976226 |          87 |   0.126437  | Paper packaging                                                                              |
| G4     |         16 | 0.0045977   |  0.000918801 |          87 |   0.103448  | Small plastic bags; freezer, zip-lock etc.                                                   |
| G213   |         16 | 0.00712644  |  0.000918801 |          87 |   0.126437  | Paraffin wax                                                                                 |
| G87    |         15 | 0.00229885  |  0.000861376 |          87 |   0.103448  | Tape, masking/duct/packing                                                                   |
| G126   |         15 | 0.0054023   |  0.000861376 |          87 |   0.103448  | Balls                                                                                        |
| G6     |         14 | 0.00390805  |  0.000803951 |          87 |   0.045977  | Bottles and containers, plastic non food/drink                                               |
| G186   |         14 | 0.00448276  |  0.000803951 |          87 |   0.0689655 | Industrial scrap                                                                             |
| G65    |         14 | 0.00505747  |  0.000803951 |          87 |   0.103448  | Buckets                                                                                      |
| G134   |         13 | 0.00298851  |  0.000746526 |          87 |   0.091954  | Other rubber                                                                                 |
| G194   |         13 | 0.00436782  |  0.000746526 |          87 |   0.137931  | Cables, metal wire(s) often inside rubber or plastic tubes                                   |
| G48    |         12 | 0.00517241  |  0.000689101 |          87 |   0.114943  | Rope, synthetic                                                                              |
| G182   |         12 | 0.00436782  |  0.000689101 |          87 |   0.0689655 | Fishing; hooks, weights, lures, sinkers etc.                                                 |
| G64    |         12 | 0.00149425  |  0.000689101 |          87 |   0.0344828 | Fenders                                                                                      |
| G928   |         11 | 0.00344828  |  0.000631676 |          87 |   0.0574713 | Ribbons and bows                                                                             |
| G927   |         11 | 0.00321839  |  0.000631676 |          87 |   0.0689655 | String trimmer line, used to cut grass, weeds, and shrubbery                                 |
| G99    |         11 | 0.00505747  |  0.000631676 |          87 |   0.114943  | Syringes - needles                                                                           |
| G199   |         11 | 0.00137931  |  0.000631676 |          87 |   0.0229885 | Other metal pieces > 50cm                                                                    |
| G943   |         11 | 0.00252874  |  0.000631676 |          87 |   0.0574713 | Fencing agriculture, plastic                                                                 |
| G158   |         10 | 0.00344828  |  0.000574251 |          87 |   0.0344828 | Other paper items                                                                            |
| G201   |         10 | 0.00344828  |  0.000574251 |          87 |   0.045977  | Jars, includes pieces                                                                        |
| G59    |         10 | 0.00390805  |  0.000574251 |          87 |   0.0689655 | Fishing line monofilament (angling)                                                          |
| G8     |         10 | 0.00137931  |  0.000574251 |          87 |   0.045977  | Drink bottles  > 0.5L                                                                        |
| G145   |          9 | 0.00287356  |  0.000516826 |          87 |   0.0804598 | Other textiles                                                                               |
| G148   |          9 | 0.00229885  |  0.000516826 |          87 |   0.0689655 | Cardboard (boxes and fragments)                                                              |
| G940   |          9 | 0.00183908  |  0.000516826 |          87 |   0.0574713 | Foamed EVA (flexible plastic) for crafts & watersports                                       |
| G210   |          9 | 0.00528736  |  0.000516826 |          87 |   0.045977  | Other glass/ceramic                                                                          |
| G203   |          9 | 0.00333333  |  0.000516826 |          87 |   0.045977  | Tableware ceramic or glass, cups, plates, pieces                                             |
| G11    |          8 | 0.00310345  |  0.0004594   |          87 |   0.0804598 | Cosmetics for the beach, e.g. sunblock                                                       |
| G938   |          8 | 0.00264368  |  0.0004594   |          87 |   0.0804598 | Toothpicks, dental floss plastic                                                             |
| G930   |          8 | 0.00206897  |  0.0004594   |          87 |   0.0804598 | Foam earplugs                                                                                |
| G7     |          8 | 0.00390805  |  0.0004594   |          87 |   0.0689655 | Drink bottles < = 0.5L                                                                       |
| G128   |          8 | 0.00218391  |  0.0004594   |          87 |   0.0689655 | Tires and belts                                                                              |
| G119   |          8 | 0.00241379  |  0.0004594   |          87 |   0.0114943 | Sheetlike user plastic (>1mm)                                                                |
| G101   |          8 | 0.00195402  |  0.0004594   |          87 |   0.0804598 | Dog feces bag                                                                                |
| G936   |          8 | 0.00183908  |  0.0004594   |          87 |   0.0574713 | Sheeting ag. greenhouse film                                                                 |
| G942   |          8 | 0.00551724  |  0.0004594   |          87 |   0.0804598 | Plastic shavings from lathes, CNC machining                                                  |
| G919   |          7 | 0.00482759  |  0.000401975 |          87 |   0.045977  | Nails, screws, bolts etc.                                                                    |
| G933   |          7 | 0.00287356  |  0.000401975 |          87 |   0.0344828 | Bags, cases for accessories; glasses, electronics, incl. straps, pieces, plstc. nylon etc.   |
| G12    |          7 | 0.00172414  |  0.000401975 |          87 |   0.0804598 | Cosmetics, non-beach use personal care containers                                            |
| G926   |          6 | 0.00218391  |  0.00034455  |          87 |   0.045977  | Chewing gum, often contains plastics                                                         |
| G918   |          6 | 0.00321839  |  0.00034455  |          87 |   0.0689655 | Safety pins, paper clips, small metal utility items                                          |
| G118   |          6 | 0.00183908  |  0.00034455  |          87 |   0.0344828 | Small industrial spheres <5mm                                                                |
| G43    |          6 | 0.00103448  |  0.00034455  |          87 |   0.0229885 | Tags fishing or industry (security tags, seals)                                              |
| G901   |          6 | 0.00137931  |  0.00034455  |          87 |   0.0689655 | Mask medical, synthetic                                                                      |
| G61    |          5 | 0.00344828  |  0.000287125 |          87 |   0.0574713 | Other fishing related                                                                        |
| G36    |          5 | 0.00287356  |  0.000287125 |          87 |   0.0114943 | Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc. |
| G170   |          5 | 0.00195402  |  0.000287125 |          87 |   0.0344828 | Wood (processed)                                                                             |
| G195   |          5 | 0.0016092   |  0.000287125 |          87 |   0.0574713 | Batteries - household                                                                        |
| G917   |          5 | 0.00206897  |  0.000287125 |          87 |   0.0344828 | Terracotta balls                                                                             |
| G136   |          5 | 0.00091954  |  0.000287125 |          87 |   0.0344828 | Shoes                                                                                        |
| G37    |          5 | 0.00114943  |  0.000287125 |          87 |   0.0229885 | Mesh bags                                                                                    |
| G68    |          5 | 0.00126437  |  0.000287125 |          87 |   0.045977  | Fiberglass fragments                                                                         |
| G915   |          4 | 0.00264368  |  0.0002297   |          87 |   0.0344828 | Reflectors, plastic mobility items                                                           |
| G176   |          4 | 0.00114943  |  0.0002297   |          87 |   0.0344828 | Cans, food                                                                                   |
| G931   |          4 | 0.000804598 |  0.0002297   |          87 |   0.0344828 | Tape-caution for barrier, police, construction etc.                                          |
| G107   |          3 | 0.00045977  |  0.000172275 |          87 |   0.0229885 | Cylindrical pellets < 5mm                                                                    |
| G161   |          3 | 0.000689655 |  0.000172275 |          87 |   0.0229885 | Processed timber                                                                             |
| G17    |          3 | 0.000804598 |  0.000172275 |          87 |   0.0114943 | Injection gun cartridge                                                                      |
| G929   |          3 | 0.000804598 |  0.000172275 |          87 |   0.0344828 | Electronics and pieces; sensors, headsets etc.                                               |
| G900   |          3 | 0.000689655 |  0.000172275 |          87 |   0.0344828 | Gloves latex  personal protective equipment                                                  |
| G197   |          3 | 0.00103448  |  0.000172275 |          87 |   0.0344828 | Other metal                                                                                  |
| G40    |          3 | 0.00091954  |  0.000172275 |          87 |   0.0229885 | Gloves household/gardening                                                                   |
| G108   |          3 | 0.00103448  |  0.000172275 |          87 |   0.0229885 | disk pellets  <5mm                                                                           |
| G129   |          3 | 0.00045977  |  0.000172275 |          87 |   0.0229885 | Inner tubes and rubber sheets                                                                |
| G133   |          3 | 0.00114943  |  0.000172275 |          87 |   0.0344828 | Condoms incl. packaging                                                                      |
| G13    |          3 | 0.000574713 |  0.000172275 |          87 |   0.0229885 | Bottles, containers, drums to transport, store material                                      |
| G104   |          2 | 0.000229885 |  0.00011485  |          87 |   0.0114943 | Plastic fragments subrounded <5mm                                                            |
| G147   |          2 | 0.00045977  |  0.00011485  |          87 |   0.0229885 | Paper bags                                                                                   |
| G97    |          2 | 0.000574713 |  0.00011485  |          87 |   0.0229885 | Toilet fresheners                                                                            |
| G155   |          2 | 0.000574713 |  0.00011485  |          87 |   0.0229885 | Fireworks paper tubes and fragments                                                          |
| G19    |          2 | 0.000229885 |  0.00011485  |          87 |   0.0114943 | Car parts                                                                                    |
| G39    |          2 | 0.000344828 |  0.00011485  |          87 |   0.0114943 | Gloves                                                                                       |
| G181   |          2 | 0.000689655 |  0.00011485  |          87 |   0.0229885 | Tableware metal;  cups, cutlery etc.                                                         |
| G932   |          2 | 0.000804598 |  0.00011485  |          87 |   0.0114943 | Bio-beads, micro plastic for wastewater treatment, irregular shape, ridged sides < 5mm       |
| G29    |          2 | 0.000804598 |  0.00011485  |          87 |   0.0229885 | Combs, brushes and sunglasses                                                                |
| G139   |          2 | 0.000574713 |  0.00011485  |          87 |   0.0114943 | Backpacks                                                                                    |
| G14    |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Engine oil bottles                                                                           |
| G172   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Other wood > 50cm                                                                            |
| G902   |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Mask medical, cloth                                                                          |
| G167   |          1 | 0.00091954  |  5.74251e-05 |          87 |   0.0114943 | Matches or fireworks                                                                         |
| G51    |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Fishing net                                                                                  |
| G916   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Pencils and pieces                                                                           |
| G173   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Other                                                                                        |
| G174   |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Aerosol spray cans                                                                           |
| G179   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Disposable BBQs                                                                              |
| G906   |          1 | 0.000344828 |  5.74251e-05 |          87 |   0.0114943 | coffee capsules aluminum                                                                     |
| G183   |          1 | 0.00137931  |  5.74251e-05 |          87 |   0.0114943 | Fish hook remains                                                                            |
| G907   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | coffee capsules plastic                                                                      |
| G202   |          1 | 0.00045977  |  5.74251e-05 |          87 |   0.0114943 | Light bulbs                                                                                  |
| G193   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | car parts and batteries                                                                      |
| G5     |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Generic plastic bags                                                                         |
| G55    |          1 | 0.000344828 |  5.74251e-05 |          87 |   0.0114943 | Fishing line (entangled)                                                                     |
| G913   |          1 | 0.000229885 |  5.74251e-05 |          87 |   0.0114943 | Pacifier                                                                                     |
| G49    |          1 | 0.000344828 |  5.74251e-05 |          87 |   0.0114943 | Rope > 1cm                                                                                   |
| G185   |          1 | 0.000114943 |  5.74251e-05 |          87 |   0.0114943 | Middle size containers                                                                       |
