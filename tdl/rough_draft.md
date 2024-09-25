

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

# Bielersee lake 2020-01-01 2021-05-31
**Summary and analysis of observations of trash density**: objects related to recreation, personal items, unclassified, infrastructure, food and drink, packaging non food, plastic pieces, waste water, agriculture, tobaccoand micro plastics (< 5mm) found in lakes.


## Administrative boundaries Bielersee lake 2020-01-01 2021-05-31 : Cities, cantons, survey areas

The number and and names of the cities, cantons and survey areas included in this report



The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis.

Please provide a narrative of the contents of the following table. In your narrative be sure to include the list of cities and the names of the canton and survey areas.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

 |              |   count |
|:-------------|--------:|
| location     |      10 |
| city         |       8 |
| canton       |       2 |
| survey areas |       1 |

The following is the names of the cities, cantons, and survey areas.

city: Vinelz, Le Landeron, Erlach, Gals, Ligerz, Lüscherz, Biel/Bienne, Nidau
canton: Bern, Neuchâtel
survey_area: aare


## Named features Bielersee lake 2020-01-01 2021-05-31 : The lakes, rivers and parks

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
lake: bielersee
park: 


## Summary statistics Bielersee lake 2020-01-01 2021-05-31: The descriptive statistics of the survey results

Bielersee: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.





This table summarizes the sample total in pcs/m for each survey. Each survey is defined by a sample_id. A survey total is the sum of all rows that have the same sample_id.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

|        |   total |   nsamples |   average |   5th |   25th |   50th |   75th |   95th |     std |   max | start      | end        |
|:-------|--------:|-----------:|----------:|------:|-------:|-------:|-------:|-------:|--------:|------:|:-----------|:-----------|
| result |    4714 |         39 |   4.31872 | 0.619 |  1.435 |    3.4 |   6.17 |  9.759 | 3.26734 |  14.8 | 2020-01-26 | 2021-03-31 |

## Material composition of objects Bielersee lake 2020-01-01 2021-05-31: estimated material composition

Bielersee: The proportion of each material type according to material category





The following table details the proportion that each material type represents to the total. 
Generate a narrative summary based on the following table. You need to include all the material types and their float values.
If there is more than one material entry in the table.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. Consider the example above

 INSTRUCTION_END ---> 

| material   | % of total   |
|:-----------|:-------------|
| chemicals  | 1%           |
| glass      | 4%           |
| metal      | 3%           |
| paper      | 2%           |
| plastic    | 85%          |
| wood       | 1%           |
## Survey Totals for city


## Bielersee lake 2020-01-01 2021-05-31 city: The average pcs/m by city.

The average sample total for each city in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | city        |   quantity |   pcs/m |
|---:|:------------|-----------:|--------:|
|  0 | Biel/Bienne |       3209 | 5.61333 |
|  1 | Erlach      |        101 | 1.83    |
|  2 | Gals        |         48 | 1.28    |
|  3 | Le Landeron |         53 | 1.45    |
|  4 | Ligerz      |        143 | 9.1     |
|  5 | Lüscherz    |        202 | 0.746   |
|  6 | Nidau       |         63 | 2.52    |
|  7 | Vinelz      |        895 | 4.495   |


## Survey Totals for canton


## Bielersee lake 2020-01-01 2021-05-31 canton: The average pcs/m by canton.

The average sample total for each canton in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | canton    |   quantity |   pcs/m |
|---:|:----------|-----------:|--------:|
|  0 | Bern      |       4661 | 4.39421 |
|  1 | Neuchâtel |         53 | 1.45    |


## Survey Totals for parent_boundary


## Bielersee lake 2020-01-01 2021-05-31 survey area: The average pcs/m by survey area.

The average sample total for each survey area in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | parent_boundary   |   quantity |   pcs/m |
|---:|:------------------|-----------:|--------:|
|  0 | aare              |       4714 | 4.31872 |



## Inventory items Bielersee lake 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |       pcs/m |   % of total |   sample_id |   fail rate | object                                                                                       |
|:-------|-----------:|------------:|-------------:|------------:|------------:|:---------------------------------------------------------------------------------------------|
| G27    |        819 | 0.6         |  0.173738    |          39 |   0.794872  | Cigarette filters                                                                            |
| Gfrags |        776 | 0.795385    |  0.164616    |          39 |   0.974359  | Fragmented plastics                                                                          |
| G30    |        347 | 0.32359     |  0.0736105   |          39 |   0.871795  | Food wrappers; candy, snacks                                                                 |
| G67    |        316 | 0.382821    |  0.0670344   |          39 |   0.897436  | Industrial sheeting                                                                          |
| Gfoams |        185 | 0.151538    |  0.0392448   |          39 |   0.641026  | Expanded polystyrene                                                                         |
| G200   |        178 | 0.197436    |  0.0377599   |          39 |   0.692308  | Glass drink bottles, pieces                                                                  |
| G941   |        173 | 0.172308    |  0.0366992   |          39 |   0.615385  | Packaging films nonfood or unknown                                                           |
| Gcaps  |        113 | 0.0982051   |  0.0239711   |          39 |   0.717949  | plastic caps, lid rings: G21, G22, G23, G24                                                  |
| G89    |         95 | 0.104359    |  0.0201527   |          39 |   0.717949  | Plastic construction waste                                                                   |
| G25    |         94 | 0.0941026   |  0.0199406   |          39 |   0.74359   | Tobacco; plastic packaging, containers                                                       |
| G940   |         92 | 0.0633333   |  0.0195163   |          39 |   0.307692  | Foamed EVA (flexible plastic) for crafts & watersports                                       |
| G117   |         79 | 0.0553846   |  0.0167586   |          39 |   0.358974  | Styrofoam < 5mm                                                                              |
| G904   |         76 | 0.0761538   |  0.0161222   |          39 |   0.666667  | Fireworks; rocket caps, exploded parts & packaging                                           |
| G213   |         76 | 0.0535897   |  0.0161222   |          39 |   0.282051  | Paraffin wax                                                                                 |
| G95    |         72 | 0.0589744   |  0.0152737   |          39 |   0.512821  | Cotton bud/swab sticks                                                                       |
| G112   |         71 | 0.0684615   |  0.0150615   |          39 |   0.589744  | Industrial pellets (nurdles)                                                                 |
| G74    |         70 | 0.0350769   |  0.0148494   |          39 |   0.666667  | Foam packaging/insulation/polyurethane                                                       |
| G177   |         63 | 0.0528205   |  0.0133644   |          39 |   0.615385  | Foil wrappers, aluminum foil                                                                 |
| G156   |         49 | 0.0323077   |  0.0103946   |          39 |   0.307692  | Paper fragments                                                                              |
| G106   |         48 | 0.0374359   |  0.0101824   |          39 |   0.487179  | Plastic fragments angular <5mm                                                               |
| G73    |         40 | 0.0253846   |  0.00848536  |          39 |   0.307692  | Foamed items & pieces (non packaging/insulation) foamed sponge material                      |
| G31    |         38 | 0.0246154   |  0.00806109  |          39 |   0.410256  | Lollypop sticks                                                                              |
| G35    |         35 | 0.0310256   |  0.00742469  |          39 |   0.461538  | Straws and stirrers                                                                          |
| G33    |         32 | 0.0353846   |  0.00678829  |          39 |   0.410256  | Cups, lids, single use foamed and hard plastic                                               |
| G178   |         32 | 0.0261538   |  0.00678829  |          39 |   0.487179  | Metal bottle caps, lids & pull tabs from cans                                                |
| G211   |         29 | 0.0225641   |  0.00615189  |          39 |   0.487179  | Other medical (swabs, bandaging, adhesive plaster)                                           |
| G50    |         28 | 0.0276923   |  0.00593975  |          39 |   0.358974  | String < 1cm                                                                                 |
| G10    |         26 | 0.0261538   |  0.00551549  |          39 |   0.435897  | Food containers single use foamed or plastic                                                 |
| G922   |         24 | 0.0333333   |  0.00509122  |          39 |   0.307692  | Labels, bar codes                                                                            |
| G32    |         22 | 0.0212821   |  0.00466695  |          39 |   0.410256  | Toys and party favors                                                                        |
| G204   |         20 | 0.0161538   |  0.00424268  |          39 |   0.0512821 | Construction material; bricks, pipes, cement                                                 |
| G137   |         18 | 0.0202564   |  0.00381841  |          39 |   0.205128  | Clothing, towels & rags                                                                      |
| G908   |         17 | 0.0161538   |  0.00360628  |          39 |   0.333333  | Tape; electrical, insulating                                                                 |
| G125   |         16 | 0.0110256   |  0.00339415  |          39 |   0.230769  | Balloons and balloon sticks                                                                  |
| G87    |         16 | 0.014359    |  0.00339415  |          39 |   0.25641   | Tape, masking/duct/packing                                                                   |
| G152   |         16 | 0.0148718   |  0.00339415  |          39 |   0.128205  | Cigarette boxes, tobacco related paper/cardboard                                             |
| G66    |         15 | 0.0130769   |  0.00318201  |          39 |   0.25641   | Straps/bands;  hard, plastic package fastener                                                |
| G159   |         15 | 0.0102564   |  0.00318201  |          39 |   0.205128  | Corks                                                                                        |
| G93    |         15 | 0.0176923   |  0.00318201  |          39 |   0.25641   | Cable ties; steggel, zip, zap straps                                                         |
| G923   |         14 | 0.0110256   |  0.00296988  |          39 |   0.179487  | Tissue, toilet paper, napkins, paper towels                                                  |
| G191   |         14 | 0.014359    |  0.00296988  |          39 |   0.25641   | Wire and mesh                                                                                |
| G927   |         13 | 0.00820513  |  0.00275774  |          39 |   0.128205  | String trimmer line, used to cut grass, weeds, and shrubbery                                 |
| G98    |         13 | 0.0117949   |  0.00275774  |          39 |   0.230769  | Diapers - wipes                                                                              |
| G905   |         13 | 0.0074359   |  0.00275774  |          39 |   0.25641   | Hair clip,  hair ties, personal accessories plastic                                          |
| G91    |         11 | 0.0115385   |  0.00233347  |          39 |   0.230769  | Biomass holder                                                                               |
| G165   |         11 | 0.00615385  |  0.00233347  |          39 |   0.205128  | Ice cream sticks, toothpicks, chopsticks                                                     |
| G928   |         11 | 0.0176923   |  0.00233347  |          39 |   0.230769  | Ribbons and bows                                                                             |
| G100   |         11 | 0.0115385   |  0.00233347  |          39 |   0.25641   | Medical; containers/tubes/ packaging                                                         |
| G3     |         11 | 0.0074359   |  0.00233347  |          39 |   0.153846  | Bags; plastic shopping/carrier/grocery and pieces                                            |
| G153   |         11 | 0.00897436  |  0.00233347  |          39 |   0.179487  | Cups, food containers, wrappers (paper)                                                      |
| G198   |         11 | 0.0105128   |  0.00233347  |          39 |   0.230769  | Other metal pieces < 50cm                                                                    |
| G142   |         10 | 0.0107692   |  0.00212134  |          39 |   0.102564  | Rope , string or nets                                                                        |
| G914   |         10 | 0.00512821  |  0.00212134  |          39 |   0.102564  | Paperclips, clothespins, plastic utility items                                               |
| G161   |         10 | 0.00666667  |  0.00212134  |          39 |   0.102564  | Processed timber                                                                             |
| G70    |         10 | 0.00717949  |  0.00212134  |          39 |   0.205128  | Shotgun cartridges                                                                           |
| G4     |          9 | 0.00666667  |  0.00190921  |          39 |   0.128205  | Small plastic bags; freezer, zip-lock etc.                                                   |
| G34    |          9 | 0.00820513  |  0.00190921  |          39 |   0.179487  | Cutlery, plates and trays                                                                    |
| G148   |          9 | 0.00512821  |  0.00190921  |          39 |   0.102564  | Cardboard (boxes and fragments)                                                              |
| G936   |          9 | 0.00923077  |  0.00190921  |          39 |   0.179487  | Sheeting ag. greenhouse film                                                                 |
| G942   |          9 | 0.00692308  |  0.00190921  |          39 |   0.153846  | Plastic shavings from lathes, CNC machining                                                  |
| G96    |          9 | 0.0135897   |  0.00190921  |          39 |   0.179487  | Sanitary pads /panty liners/tampons and applicators                                          |
| G186   |          8 | 0.00615385  |  0.00169707  |          39 |   0.128205  | Industrial scrap                                                                             |
| G26    |          8 | 0.00769231  |  0.00169707  |          39 |   0.179487  | Cigarette lighters                                                                           |
| G115   |          8 | 0.00717949  |  0.00169707  |          39 |   0.153846  | Foamed  plastic <5mm                                                                         |
| G28    |          8 | 0.00846154  |  0.00169707  |          39 |   0.179487  | Pens, lids, mechanical pencils etc.                                                          |
| G122   |          7 | 0.0148718   |  0.00148494  |          39 |   0.025641  | Plastic fragments ( >1mm)                                                                    |
| G118   |          7 | 0.00538462  |  0.00148494  |          39 |   0.0769231 | Small industrial spheres <5mm                                                                |
| G175   |          7 | 0.00487179  |  0.00148494  |          39 |   0.102564  | Cans, beverage                                                                               |
| G101   |          7 | 0.00615385  |  0.00148494  |          39 |   0.102564  | Dog feces bag                                                                                |
| G7     |          6 | 0.00358974  |  0.0012728   |          39 |   0.102564  | Drink bottles < = 0.5L                                                                       |
| G939   |          6 | 0.00461538  |  0.0012728   |          39 |   0.102564  | Flowers, plants plastic                                                                      |
| G48    |          6 | 0.00769231  |  0.0012728   |          39 |   0.153846  | Rope, synthetic                                                                              |
| G170   |          6 | 0.00384615  |  0.0012728   |          39 |   0.0769231 | Wood (processed)                                                                             |
| G59    |          5 | 0.00538462  |  0.00106067  |          39 |   0.102564  | Fishing line monofilament (angling)                                                          |
| G134   |          5 | 0.00410256  |  0.00106067  |          39 |   0.0769231 | Other rubber                                                                                 |
| G901   |          5 | 0.00307692  |  0.00106067  |          39 |   0.102564  | Mask medical, synthetic                                                                      |
| G208   |          5 | 0.00589744  |  0.00106067  |          39 |   0.0769231 | Glass or ceramic fragments > 2.5 cm                                                          |
| G68    |          5 | 0.00487179  |  0.00106067  |          39 |   0.128205  | Fiberglass fragments                                                                         |
| G141   |          5 | 0.00615385  |  0.00106067  |          39 |   0.0769231 | Carpet                                                                                       |
| G131   |          4 | 0.00358974  |  0.000848536 |          39 |   0.0512821 | Rubber bands                                                                                 |
| G116   |          4 | 0.00410256  |  0.000848536 |          39 |   0.025641  | Granules <5mm                                                                                |
| G933   |          4 | 0.0025641   |  0.000848536 |          39 |   0.0769231 | Bags, cases for accessories; glasses, electronics, incl. straps, pieces, plstc. nylon etc.   |
| G2     |          4 | 0.00307692  |  0.000848536 |          39 |   0.0512821 | Bags                                                                                         |
| G143   |          4 | 0.00307692  |  0.000848536 |          39 |   0.102564  | Sails and canvas                                                                             |
| G203   |          4 | 0.0074359   |  0.000848536 |          39 |   0.0769231 | Tableware ceramic or glass, cups, plates, pieces                                             |
| G124   |          4 | 0.00846154  |  0.000848536 |          39 |   0.0512821 | Other plastic or foam products                                                               |
| G20    |          4 | 0.00333333  |  0.000848536 |          39 |   0.102564  | Caps and lids                                                                                |
| G49    |          4 | 0.00487179  |  0.000848536 |          39 |   0.0512821 | Rope > 1cm                                                                                   |
| G917   |          3 | 0.00179487  |  0.000636402 |          39 |   0.0512821 | Terracotta balls                                                                             |
| G133   |          3 | 0.00179487  |  0.000636402 |          39 |   0.0769231 | Condoms incl. packaging                                                                      |
| G155   |          3 | 0.00153846  |  0.000636402 |          39 |   0.0769231 | Fireworks paper tubes and fragments                                                          |
| G194   |          3 | 0.00512821  |  0.000636402 |          39 |   0.0769231 | Cables, metal wire(s) often inside rubber or plastic tubes                                   |
| G135   |          3 | 0.00307692  |  0.000636402 |          39 |   0.0769231 | Clothes, footware, headware, gloves                                                          |
| G176   |          3 | 0.00384615  |  0.000636402 |          39 |   0.0512821 | Cans, food                                                                                   |
| G158   |          3 | 0.00230769  |  0.000636402 |          39 |   0.0512821 | Other paper items                                                                            |
| G64    |          3 | 0.00230769  |  0.000636402 |          39 |   0.025641  | Fenders                                                                                      |
| G119   |          3 | 0.00641026  |  0.000636402 |          39 |   0.025641  | Sheetlike user plastic (>1mm)                                                                |
| G167   |          3 | 0.00179487  |  0.000636402 |          39 |   0.025641  | Matches or fireworks                                                                         |
| G931   |          3 | 0.00128205  |  0.000636402 |          39 |   0.025641  | Tape-caution for barrier, police, construction etc.                                          |
| G38    |          3 | 0.00358974  |  0.000636402 |          39 |   0.0769231 | Coverings; plastic packaging, sheeting for protecting large cargo items                      |
| G921   |          2 | 0.00102564  |  0.000424268 |          39 |   0.0512821 | Ceramic tile and pieces                                                                      |
| G188   |          2 | 0.00128205  |  0.000424268 |          39 |   0.025641  | Other cans < 4 L                                                                             |
| G182   |          2 | 0.00358974  |  0.000424268 |          39 |   0.025641  | Fishing; hooks, weights, lures, sinkers etc.                                                 |
| G929   |          2 | 0.00128205  |  0.000424268 |          39 |   0.0512821 | Electronics and pieces; sensors, headsets etc.                                               |
| G930   |          2 | 0.00102564  |  0.000424268 |          39 |   0.0512821 | Foam earplugs                                                                                |
| G12    |          2 | 0.00102564  |  0.000424268 |          39 |   0.0512821 | Cosmetics, non-beach use personal care containers                                            |
| G145   |          2 | 0.00179487  |  0.000424268 |          39 |   0.0512821 | Other textiles                                                                               |
| G149   |          2 | 0.00358974  |  0.000424268 |          39 |   0.0512821 | Paper packaging                                                                              |
| G103   |          2 | 0.00153846  |  0.000424268 |          39 |   0.0512821 | Plastic fragments rounded <5mm                                                               |
| G201   |          2 | 0.00358974  |  0.000424268 |          39 |   0.025641  | Jars, includes pieces                                                                        |
| G53    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Nets and pieces < 50cm                                                                       |
| G37    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Mesh bags                                                                                    |
| G171   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Other wood < 50cm                                                                            |
| G938   |          1 | 0.00102564  |  0.000212134 |          39 |   0.025641  | Toothpicks, dental floss plastic                                                             |
| G129   |          1 | 0.000769231 |  0.000212134 |          39 |   0.025641  | Inner tubes and rubber sheets                                                                |
| G104   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Plastic fragments subrounded <5mm                                                            |
| G157   |          1 | 0.00307692  |  0.000212134 |          39 |   0.025641  | Paper                                                                                        |
| G36    |          1 | 0.00230769  |  0.000212134 |          39 |   0.025641  | Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc. |
| G918   |          1 | 0.000769231 |  0.000212134 |          39 |   0.025641  | Safety pins, paper clips, small metal utility items                                          |
| G172   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Other wood > 50cm                                                                            |
| G926   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Chewing gum, often contains plastics                                                         |
| G916   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Pencils and pieces                                                                           |
| G913   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Pacifier                                                                                     |
| G197   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Other metal                                                                                  |
| G41    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Glove industrial/professional                                                                |
| G43    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Tags fishing or industry (security tags, seals)                                              |
| G90    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Plastic flower pots                                                                          |
| G8     |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Drink bottles  > 0.5L                                                                        |
| G202   |          1 | 0.00307692  |  0.000212134 |          39 |   0.025641  | Light bulbs                                                                                  |
| G71    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Shoes sandals                                                                                |
| G5     |          1 | 0.00230769  |  0.000212134 |          39 |   0.025641  | Generic plastic bags                                                                         |
| G52    |          1 | 0.00153846  |  0.000212134 |          39 |   0.025641  | Nets and pieces                                                                              |
| G210   |          1 | 0.000769231 |  0.000212134 |          39 |   0.025641  | Other glass/ceramic                                                                          |
| G150   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Milk cartons, tetrapack                                                                      |

## Sampling stratification Bielersee lake 2020-01-01 2021-05-31: The environmental features surrounding the survey location.

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
| 0-20%                  | 17.9%                                              | 100.0%                                            | 38.5%                                           | 100.0%                                                   | 100.0%                                              | 53.8%                                              | 20.5%                                            | 100.0%                                             | 100.0%                                            |
| 20-40%                 | 41.0%                                              | none                                              | 48.7%                                           | none                                                     | none                                                | 5.1%                                               | 5.1%                                             | none                                               | none                                              |
| 40-60%                 | 33.3%                                              | none                                              | 12.8%                                           | none                                                     | none                                                | 41.0%                                              | 30.8%                                            | none                                               | none                                              |
| 60-80%                 | 7.7%                                               | none                                              | none                                            | none                                                     | none                                                | none                                               | 35.9%                                            | none                                               | none                                              |
| 80-100%                | none                                               | none                                              | none                                            | none                                                     | none                                                | none                                               | 5.1%                                             | none                                               | none                                              |

## Sampling stratification and trash density Bielersee lake 2020-01-01 2021-05-31: The changes in the observed litter density and the changes in land use



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

| proportion of buffer   | ('Pieces of trash per meter', 'buildings')   | ('Pieces of trash per meter', 'wetlands')   | ('Pieces of trash per meter', 'forest')   | ('Pieces of trash per meter', 'public-services')   | ('Pieces of trash per meter', 'recreation')   | ('Pieces of trash per meter', 'undefined')   |   ('Pieces of trash per meter', 'streets') | ('Pieces of trash per meter', 'vineyards')   | ('Pieces of trash per meter', 'orchards')   |
|:-----------------------|:---------------------------------------------|:--------------------------------------------|:------------------------------------------|:---------------------------------------------------|:----------------------------------------------|:---------------------------------------------|-------------------------------------------:|:---------------------------------------------|:--------------------------------------------|
| 0-20%                  | 3.132857142857143                            | 4.318717948717949                           | 3.9826666666666672                        | 4.318717948717949                                  | 4.318717948717949                             | 4.307142857142857                            |                                    2.97    | 4.318717948717949                            | 4.318717948717949                           |
| 20-40%                 | 3.73625                                      | none                                        | 5.52421052631579                          | none                                               | none                                          | 9.100000000000001                            |                                    1.28    | none                                         | none                                        |
| 40-60%                 | 5.945384615384616                            | none                                        | 0.746                                     | none                                               | none                                          | 3.73625                                      |                                    4.495   | none                                         | none                                        |
| 60-80%                 | 3.143333333333333                            | none                                        | none                                      | none                                               | none                                          | none                                         |                                    5.62429 | none                                         | none                                        |
| 80-100%                | none                                         | none                                        | none                                      | none                                               | none                                          | none                                         |                                    3.455   | none                                         | none                                        |

## Grid forecast Bielersee lake 2020-01-01 2021-05-31


### Grid Approximation method:

Grid approximation is a numerical technique used in Bayesian inference to approximate the posterior distribution of a parameter. The method uses conditional probability to answer the question _What am I likely to observe given what was observed previously, under similar conditions ?_ The conditions are the land use features (reference sampling stratification table) and the proportion of the buffer zone dedicated to each land use feature. The data for the prior is randomly selected from the existing data with similar land use features, similarity is measured with cosine similarity or manhattan distance. The data for the prior does not include the data from the likelihood (ie the data defined by the report parameters).

In this report we identified three priors that represent different possible interpretation of the survey results.

 1. **In Boundary Prior**: The prior distribution is selected from random samples from within the requested administrative boundary (if a boundary was selected). This prior responds to the hypothesis that the quanity of trash on the beach is a local problem and trends or results from other areas are not relevant.
2. **Out Boundary Prior**: The prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected). This prior responds to the hypothesis that the quantity of trash on the beach is a regional problem and trends or results from other areas are relevant.
3. **Prior**: The prior distribution is selected from random samples from all of the data (in different of geographic boundary). This prior responds to the hypothesis that the amount trash on the beach is similar indifferent of geographic location.

 The grid approximation method is used to estimate the posterior distribution of the parameter of interest (e.g., the litter density) given the land use profile of the survey location. Therefore this method is an indicator of what the next survey will yield given the land use profile of the survey locations of interest. The steps of the grid approximation are the same for all three priors. The only difference is the data used for the prior (in-boundary, out-boundary, prior).

1. **Parameter Space Discretization**: Divide the continuous parameter space into a discrete grid of points. We use the 0 as the start of the grid and the 99th percentile of the observed values as the grid limit and we evaluate the function every 0.01.

2. **Evaluation of Function**: Evaluate the statistical function of interest (e.g., likelihood, posterior) at each grid point. This step gives a set of unnormalized values across the grid.

3. **Normalization**:
   - **Sum the Values**: Compute the sum of the evaluated function values over all grid points. This sum is used as the normalizing constant.
   - **Normalize**: Divide each evaluated function value by the normalizing constant to ensure that the sum (or integral, in the continuous case) over the grid points is 1. This is crucial when dealing with probability distributions, as it ensures the result is a valid probability distribution.

- **Probability Distributions**: In Bayesian inference, the posterior distribution needs to be properly normalized so that it integrates (or sums) to 1 over the parameter space.
- **Accuracy of Estimates**: Normalization ensures that derived quantities, like expectations or credible intervals, are accurate representations of the true statistical measures.

The normalization step is particularly crucial in Bayesian grid approximations because it transforms the unnormalized posterior into a proper probability distribution, enabling meaningful statistical inference.


### Prior grid approximation
These are random samples from all of the data (in different of geographic boundary) not including the likelihood and limited to the requested end date.  The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples This prior makes no difference between the locations inside or outside the boundary of interest. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations (indifferent of the geographic boundary) ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.6800000000000004
The expected posterior distribution is a grid approximation from 0 to 16.900000000000002 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   2.092   |
| std   |   2.04545 |
| min   |   0.01    |
| 25%   |   0.4675  |
| 50%   |   1.425   |
| 75%   |   3.075   |
| max   |   7.43    |

### Out boundary grid approximation
This prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations outside the geographic boundary ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.6800000000000004
The expected posterior distribution is a grid approximation from 0 to 13.67 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   1.6919  |
| std   |   1.72272 |
| min   |   0       |
| 25%   |   0.44    |
| 50%   |   1.255   |
| 75%   |   2.2575  |
| max   |  11.31    |




### Cluster analysis Bielersee lake 2020-01-01 2021-05-31


Bielersee: Cluster compositionThe survey locations were labeled according to the type and magnitude of land use in a 1 500 m buffer zone aroundaround each survey location. A cluster analysis was performed using K-Means clustering, the optimal amount of clusters was determined using the elbow method. Each cluster represents a group of locations that have similar land use profiles, that is the locations are surrounded by similar quantities of buildings or forest or undefined land use.We consider the cluster composition and the proportion of each cluster dedicated to a particular land use. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location whose buffer zone was 45% dedicated to forest. 

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
|         0 |       0.309 |      0.022 |    0.107 |             0.061 |        0.025 |       0.541 |  0.44332  |       0.02  |       0    |
|         1 |       0.167 |      0     |    0.559 |             0.038 |        0.002 |       0.133 |  0        |       0     |       0.14 |
|         2 |       0.32  |      0     |    0.106 |             0.127 |        0.022 |       0.481 |  0.710774 |       0.093 |       0    |





Bielersee: Average density per cluster
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
|         0 | 4.67903 |
|         1 | 0.746   |
|         2 | 6.55    |



### Summary of regression methods Bielersee lake 2020-01-01 2021-05-31: 

In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. The feature variables are the land-use features identified in the land-use profile. From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model with the highest r² is then used in the BaggingRegressor and the VotingRegressor.





The following table details the results from different regression analysis of our data.

The table has the following format:

1. Model: the type of regression model used
2. R²: The coefficient of determination
3. MSE: the mean squared error

Generate a narrative summary based on the following table. You need to include all the models and the R² and MSE result.
The narrative needs to be in paragraph format.

|    | Model                                |         R² |      MSE |
|---:|:-------------------------------------|-----------:|---------:|
|  0 | Linear Regression                    | -20.1741   | 7.79272  |
|  1 | Random Forest Regression             |  -0.187724 | 0.437119 |
|  2 | Gradient Boosting Regression         |   0.221795 | 0.286404 |
|  3 | Theil-Sen Regressor                  |  -1.62023  | 0.964327 |
|  4 | Bagging:Gradient Boosting Regression |  -0.155279 | 0.425179 |
|  5 | Voting                               |  -2.40909  | 1.25465  |



### Feature and permutation importance Bielersee lake 2020-01-01 2021-05-31



__Model feature importance__

Feature importance is a technique used in machine learning to identify and quantify the significance of different input variables (features) in predicting the target variable. In models like decision trees, random forests, and gradient boosting machines, feature importance is often calculated by measuring how much the model's accuracy or error changes when a particular feature is included versus when it is excluded. 
The following table details the model feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  2 | forest          |   0.592117   |
|  7 | vineyards       |   0.157895   |
|  3 | public-services |   0.134249   |
|  4 | recreation      |   0.0624718  |
|  6 | streets         |   0.047398   |
|  0 | buildings       |   0.00251824 |
|  1 | wetlands        |   0.00192249 |
|  5 | undefined       |   0.00142823 |



__Permutation feature importance__

Permutation importance is a model-agnostic method for assessing the importance of individual features in a predictive model. It is particularly useful because it can be applied to any type of model, whether it's a linear model, a decision tree, or a complex ensemble model. This method involves randomly shuffling the values of a feature in the dataset and observing the impact on the model's performance. A significant drop in performance indicates that the feature is important.
The following table details the permutation feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  2 | forest          |  0.528821    |
|  7 | vineyards       |  0.0930233   |
|  6 | streets         |  0.000128345 |
|  1 | wetlands        | -0.00305384  |
|  5 | undefined       | -0.00398496  |
|  3 | public-services | -0.00470558  |
|  0 | buildings       | -0.00591377  |
|  4 | recreation      | -0.00640211  |


## Inventory items Bielersee lake 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |       pcs/m |   % of total |   sample_id |   fail rate | object                                                                                       |
|:-------|-----------:|------------:|-------------:|------------:|------------:|:---------------------------------------------------------------------------------------------|
| G27    |        819 | 0.6         |  0.173738    |          39 |   0.794872  | Cigarette filters                                                                            |
| Gfrags |        776 | 0.795385    |  0.164616    |          39 |   0.974359  | Fragmented plastics                                                                          |
| G30    |        347 | 0.32359     |  0.0736105   |          39 |   0.871795  | Food wrappers; candy, snacks                                                                 |
| G67    |        316 | 0.382821    |  0.0670344   |          39 |   0.897436  | Industrial sheeting                                                                          |
| Gfoams |        185 | 0.151538    |  0.0392448   |          39 |   0.641026  | Expanded polystyrene                                                                         |
| G200   |        178 | 0.197436    |  0.0377599   |          39 |   0.692308  | Glass drink bottles, pieces                                                                  |
| G941   |        173 | 0.172308    |  0.0366992   |          39 |   0.615385  | Packaging films nonfood or unknown                                                           |
| Gcaps  |        113 | 0.0982051   |  0.0239711   |          39 |   0.717949  | plastic caps, lid rings: G21, G22, G23, G24                                                  |
| G89    |         95 | 0.104359    |  0.0201527   |          39 |   0.717949  | Plastic construction waste                                                                   |
| G25    |         94 | 0.0941026   |  0.0199406   |          39 |   0.74359   | Tobacco; plastic packaging, containers                                                       |
| G940   |         92 | 0.0633333   |  0.0195163   |          39 |   0.307692  | Foamed EVA (flexible plastic) for crafts & watersports                                       |
| G117   |         79 | 0.0553846   |  0.0167586   |          39 |   0.358974  | Styrofoam < 5mm                                                                              |
| G904   |         76 | 0.0761538   |  0.0161222   |          39 |   0.666667  | Fireworks; rocket caps, exploded parts & packaging                                           |
| G213   |         76 | 0.0535897   |  0.0161222   |          39 |   0.282051  | Paraffin wax                                                                                 |
| G95    |         72 | 0.0589744   |  0.0152737   |          39 |   0.512821  | Cotton bud/swab sticks                                                                       |
| G112   |         71 | 0.0684615   |  0.0150615   |          39 |   0.589744  | Industrial pellets (nurdles)                                                                 |
| G74    |         70 | 0.0350769   |  0.0148494   |          39 |   0.666667  | Foam packaging/insulation/polyurethane                                                       |
| G177   |         63 | 0.0528205   |  0.0133644   |          39 |   0.615385  | Foil wrappers, aluminum foil                                                                 |
| G156   |         49 | 0.0323077   |  0.0103946   |          39 |   0.307692  | Paper fragments                                                                              |
| G106   |         48 | 0.0374359   |  0.0101824   |          39 |   0.487179  | Plastic fragments angular <5mm                                                               |
| G73    |         40 | 0.0253846   |  0.00848536  |          39 |   0.307692  | Foamed items & pieces (non packaging/insulation) foamed sponge material                      |
| G31    |         38 | 0.0246154   |  0.00806109  |          39 |   0.410256  | Lollypop sticks                                                                              |
| G35    |         35 | 0.0310256   |  0.00742469  |          39 |   0.461538  | Straws and stirrers                                                                          |
| G33    |         32 | 0.0353846   |  0.00678829  |          39 |   0.410256  | Cups, lids, single use foamed and hard plastic                                               |
| G178   |         32 | 0.0261538   |  0.00678829  |          39 |   0.487179  | Metal bottle caps, lids & pull tabs from cans                                                |
| G211   |         29 | 0.0225641   |  0.00615189  |          39 |   0.487179  | Other medical (swabs, bandaging, adhesive plaster)                                           |
| G50    |         28 | 0.0276923   |  0.00593975  |          39 |   0.358974  | String < 1cm                                                                                 |
| G10    |         26 | 0.0261538   |  0.00551549  |          39 |   0.435897  | Food containers single use foamed or plastic                                                 |
| G922   |         24 | 0.0333333   |  0.00509122  |          39 |   0.307692  | Labels, bar codes                                                                            |
| G32    |         22 | 0.0212821   |  0.00466695  |          39 |   0.410256  | Toys and party favors                                                                        |
| G204   |         20 | 0.0161538   |  0.00424268  |          39 |   0.0512821 | Construction material; bricks, pipes, cement                                                 |
| G137   |         18 | 0.0202564   |  0.00381841  |          39 |   0.205128  | Clothing, towels & rags                                                                      |
| G908   |         17 | 0.0161538   |  0.00360628  |          39 |   0.333333  | Tape; electrical, insulating                                                                 |
| G125   |         16 | 0.0110256   |  0.00339415  |          39 |   0.230769  | Balloons and balloon sticks                                                                  |
| G87    |         16 | 0.014359    |  0.00339415  |          39 |   0.25641   | Tape, masking/duct/packing                                                                   |
| G152   |         16 | 0.0148718   |  0.00339415  |          39 |   0.128205  | Cigarette boxes, tobacco related paper/cardboard                                             |
| G66    |         15 | 0.0130769   |  0.00318201  |          39 |   0.25641   | Straps/bands;  hard, plastic package fastener                                                |
| G159   |         15 | 0.0102564   |  0.00318201  |          39 |   0.205128  | Corks                                                                                        |
| G93    |         15 | 0.0176923   |  0.00318201  |          39 |   0.25641   | Cable ties; steggel, zip, zap straps                                                         |
| G923   |         14 | 0.0110256   |  0.00296988  |          39 |   0.179487  | Tissue, toilet paper, napkins, paper towels                                                  |
| G191   |         14 | 0.014359    |  0.00296988  |          39 |   0.25641   | Wire and mesh                                                                                |
| G927   |         13 | 0.00820513  |  0.00275774  |          39 |   0.128205  | String trimmer line, used to cut grass, weeds, and shrubbery                                 |
| G98    |         13 | 0.0117949   |  0.00275774  |          39 |   0.230769  | Diapers - wipes                                                                              |
| G905   |         13 | 0.0074359   |  0.00275774  |          39 |   0.25641   | Hair clip,  hair ties, personal accessories plastic                                          |
| G91    |         11 | 0.0115385   |  0.00233347  |          39 |   0.230769  | Biomass holder                                                                               |
| G165   |         11 | 0.00615385  |  0.00233347  |          39 |   0.205128  | Ice cream sticks, toothpicks, chopsticks                                                     |
| G928   |         11 | 0.0176923   |  0.00233347  |          39 |   0.230769  | Ribbons and bows                                                                             |
| G100   |         11 | 0.0115385   |  0.00233347  |          39 |   0.25641   | Medical; containers/tubes/ packaging                                                         |
| G3     |         11 | 0.0074359   |  0.00233347  |          39 |   0.153846  | Bags; plastic shopping/carrier/grocery and pieces                                            |
| G153   |         11 | 0.00897436  |  0.00233347  |          39 |   0.179487  | Cups, food containers, wrappers (paper)                                                      |
| G198   |         11 | 0.0105128   |  0.00233347  |          39 |   0.230769  | Other metal pieces < 50cm                                                                    |
| G142   |         10 | 0.0107692   |  0.00212134  |          39 |   0.102564  | Rope , string or nets                                                                        |
| G914   |         10 | 0.00512821  |  0.00212134  |          39 |   0.102564  | Paperclips, clothespins, plastic utility items                                               |
| G161   |         10 | 0.00666667  |  0.00212134  |          39 |   0.102564  | Processed timber                                                                             |
| G70    |         10 | 0.00717949  |  0.00212134  |          39 |   0.205128  | Shotgun cartridges                                                                           |
| G4     |          9 | 0.00666667  |  0.00190921  |          39 |   0.128205  | Small plastic bags; freezer, zip-lock etc.                                                   |
| G34    |          9 | 0.00820513  |  0.00190921  |          39 |   0.179487  | Cutlery, plates and trays                                                                    |
| G148   |          9 | 0.00512821  |  0.00190921  |          39 |   0.102564  | Cardboard (boxes and fragments)                                                              |
| G936   |          9 | 0.00923077  |  0.00190921  |          39 |   0.179487  | Sheeting ag. greenhouse film                                                                 |
| G942   |          9 | 0.00692308  |  0.00190921  |          39 |   0.153846  | Plastic shavings from lathes, CNC machining                                                  |
| G96    |          9 | 0.0135897   |  0.00190921  |          39 |   0.179487  | Sanitary pads /panty liners/tampons and applicators                                          |
| G186   |          8 | 0.00615385  |  0.00169707  |          39 |   0.128205  | Industrial scrap                                                                             |
| G26    |          8 | 0.00769231  |  0.00169707  |          39 |   0.179487  | Cigarette lighters                                                                           |
| G115   |          8 | 0.00717949  |  0.00169707  |          39 |   0.153846  | Foamed  plastic <5mm                                                                         |
| G28    |          8 | 0.00846154  |  0.00169707  |          39 |   0.179487  | Pens, lids, mechanical pencils etc.                                                          |
| G122   |          7 | 0.0148718   |  0.00148494  |          39 |   0.025641  | Plastic fragments ( >1mm)                                                                    |
| G118   |          7 | 0.00538462  |  0.00148494  |          39 |   0.0769231 | Small industrial spheres <5mm                                                                |
| G175   |          7 | 0.00487179  |  0.00148494  |          39 |   0.102564  | Cans, beverage                                                                               |
| G101   |          7 | 0.00615385  |  0.00148494  |          39 |   0.102564  | Dog feces bag                                                                                |
| G7     |          6 | 0.00358974  |  0.0012728   |          39 |   0.102564  | Drink bottles < = 0.5L                                                                       |
| G939   |          6 | 0.00461538  |  0.0012728   |          39 |   0.102564  | Flowers, plants plastic                                                                      |
| G48    |          6 | 0.00769231  |  0.0012728   |          39 |   0.153846  | Rope, synthetic                                                                              |
| G170   |          6 | 0.00384615  |  0.0012728   |          39 |   0.0769231 | Wood (processed)                                                                             |
| G59    |          5 | 0.00538462  |  0.00106067  |          39 |   0.102564  | Fishing line monofilament (angling)                                                          |
| G134   |          5 | 0.00410256  |  0.00106067  |          39 |   0.0769231 | Other rubber                                                                                 |
| G901   |          5 | 0.00307692  |  0.00106067  |          39 |   0.102564  | Mask medical, synthetic                                                                      |
| G208   |          5 | 0.00589744  |  0.00106067  |          39 |   0.0769231 | Glass or ceramic fragments > 2.5 cm                                                          |
| G68    |          5 | 0.00487179  |  0.00106067  |          39 |   0.128205  | Fiberglass fragments                                                                         |
| G141   |          5 | 0.00615385  |  0.00106067  |          39 |   0.0769231 | Carpet                                                                                       |
| G131   |          4 | 0.00358974  |  0.000848536 |          39 |   0.0512821 | Rubber bands                                                                                 |
| G116   |          4 | 0.00410256  |  0.000848536 |          39 |   0.025641  | Granules <5mm                                                                                |
| G933   |          4 | 0.0025641   |  0.000848536 |          39 |   0.0769231 | Bags, cases for accessories; glasses, electronics, incl. straps, pieces, plstc. nylon etc.   |
| G2     |          4 | 0.00307692  |  0.000848536 |          39 |   0.0512821 | Bags                                                                                         |
| G143   |          4 | 0.00307692  |  0.000848536 |          39 |   0.102564  | Sails and canvas                                                                             |
| G203   |          4 | 0.0074359   |  0.000848536 |          39 |   0.0769231 | Tableware ceramic or glass, cups, plates, pieces                                             |
| G124   |          4 | 0.00846154  |  0.000848536 |          39 |   0.0512821 | Other plastic or foam products                                                               |
| G20    |          4 | 0.00333333  |  0.000848536 |          39 |   0.102564  | Caps and lids                                                                                |
| G49    |          4 | 0.00487179  |  0.000848536 |          39 |   0.0512821 | Rope > 1cm                                                                                   |
| G917   |          3 | 0.00179487  |  0.000636402 |          39 |   0.0512821 | Terracotta balls                                                                             |
| G133   |          3 | 0.00179487  |  0.000636402 |          39 |   0.0769231 | Condoms incl. packaging                                                                      |
| G155   |          3 | 0.00153846  |  0.000636402 |          39 |   0.0769231 | Fireworks paper tubes and fragments                                                          |
| G194   |          3 | 0.00512821  |  0.000636402 |          39 |   0.0769231 | Cables, metal wire(s) often inside rubber or plastic tubes                                   |
| G135   |          3 | 0.00307692  |  0.000636402 |          39 |   0.0769231 | Clothes, footware, headware, gloves                                                          |
| G176   |          3 | 0.00384615  |  0.000636402 |          39 |   0.0512821 | Cans, food                                                                                   |
| G158   |          3 | 0.00230769  |  0.000636402 |          39 |   0.0512821 | Other paper items                                                                            |
| G64    |          3 | 0.00230769  |  0.000636402 |          39 |   0.025641  | Fenders                                                                                      |
| G119   |          3 | 0.00641026  |  0.000636402 |          39 |   0.025641  | Sheetlike user plastic (>1mm)                                                                |
| G167   |          3 | 0.00179487  |  0.000636402 |          39 |   0.025641  | Matches or fireworks                                                                         |
| G931   |          3 | 0.00128205  |  0.000636402 |          39 |   0.025641  | Tape-caution for barrier, police, construction etc.                                          |
| G38    |          3 | 0.00358974  |  0.000636402 |          39 |   0.0769231 | Coverings; plastic packaging, sheeting for protecting large cargo items                      |
| G921   |          2 | 0.00102564  |  0.000424268 |          39 |   0.0512821 | Ceramic tile and pieces                                                                      |
| G188   |          2 | 0.00128205  |  0.000424268 |          39 |   0.025641  | Other cans < 4 L                                                                             |
| G182   |          2 | 0.00358974  |  0.000424268 |          39 |   0.025641  | Fishing; hooks, weights, lures, sinkers etc.                                                 |
| G929   |          2 | 0.00128205  |  0.000424268 |          39 |   0.0512821 | Electronics and pieces; sensors, headsets etc.                                               |
| G930   |          2 | 0.00102564  |  0.000424268 |          39 |   0.0512821 | Foam earplugs                                                                                |
| G12    |          2 | 0.00102564  |  0.000424268 |          39 |   0.0512821 | Cosmetics, non-beach use personal care containers                                            |
| G145   |          2 | 0.00179487  |  0.000424268 |          39 |   0.0512821 | Other textiles                                                                               |
| G149   |          2 | 0.00358974  |  0.000424268 |          39 |   0.0512821 | Paper packaging                                                                              |
| G103   |          2 | 0.00153846  |  0.000424268 |          39 |   0.0512821 | Plastic fragments rounded <5mm                                                               |
| G201   |          2 | 0.00358974  |  0.000424268 |          39 |   0.025641  | Jars, includes pieces                                                                        |
| G53    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Nets and pieces < 50cm                                                                       |
| G37    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Mesh bags                                                                                    |
| G171   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Other wood < 50cm                                                                            |
| G938   |          1 | 0.00102564  |  0.000212134 |          39 |   0.025641  | Toothpicks, dental floss plastic                                                             |
| G129   |          1 | 0.000769231 |  0.000212134 |          39 |   0.025641  | Inner tubes and rubber sheets                                                                |
| G104   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Plastic fragments subrounded <5mm                                                            |
| G157   |          1 | 0.00307692  |  0.000212134 |          39 |   0.025641  | Paper                                                                                        |
| G36    |          1 | 0.00230769  |  0.000212134 |          39 |   0.025641  | Bags/sacks heavy duty plastic for 25 Kg or more; animal feed, fertilizers, garden trash etc. |
| G918   |          1 | 0.000769231 |  0.000212134 |          39 |   0.025641  | Safety pins, paper clips, small metal utility items                                          |
| G172   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Other wood > 50cm                                                                            |
| G926   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Chewing gum, often contains plastics                                                         |
| G916   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Pencils and pieces                                                                           |
| G913   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Pacifier                                                                                     |
| G197   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Other metal                                                                                  |
| G41    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Glove industrial/professional                                                                |
| G43    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Tags fishing or industry (security tags, seals)                                              |
| G90    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Plastic flower pots                                                                          |
| G8     |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Drink bottles  > 0.5L                                                                        |
| G202   |          1 | 0.00307692  |  0.000212134 |          39 |   0.025641  | Light bulbs                                                                                  |
| G71    |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Shoes sandals                                                                                |
| G5     |          1 | 0.00230769  |  0.000212134 |          39 |   0.025641  | Generic plastic bags                                                                         |
| G52    |          1 | 0.00153846  |  0.000212134 |          39 |   0.025641  | Nets and pieces                                                                              |
| G210   |          1 | 0.000769231 |  0.000212134 |          39 |   0.025641  | Other glass/ceramic                                                                          |
| G150   |          1 | 0.000512821 |  0.000212134 |          39 |   0.025641  | Milk cartons, tetrapack                                                                      |
