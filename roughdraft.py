# import openai
# from dotenv import load_dotenv
# import os
import pandas as pd
from session_config import code_definitions_map as codes
from gridforecast import GridForecast
from linearmethods import LinearMethods
from reports import construct_report_label

def append_to_markdown(filename, content):
    with open(filename, 'a') as f:
        f.write(content)

def use_chat_completion(client, model: str = 'gpt-3.5-turbo-0125', messages: [{}] = None):
    completed_chat = client.chat.completions.create(model=model, messages=messages)
    return completed_chat

def messages_for_chat_completion(system_prompt: str = None, user_prompt: str = None):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}]

    return messages

def create_system_prompt(prompt, context="") -> str:
    return f"{prompt}{context}"

def a_forecast_prompt(table):
    forecast_prompt = f"""
    <!--- INSTRUCTION_START\n\n
The following contains the expected distribution of survey results.

The table has the following format:

1. average: the expected average sample total
2. hdi min: the minimum of the 90% Highest Density Interval
3. hdi max: the maximum of the 90% of the Highest Density Interval
4. 5th, 25th, 50th, 75th, 95th : the percentile rankings based on the expected distribution
5. max predicted: the maximum value predicted by the model

Generate a narrative summary based on the following table. Include all values. Reply in paragraph format, do not comment do not embelish. Use the following style guide:
\n\n INSTRUCTION_END --->
{table}


"""
    return forecast_prompt


def admin_prompt(table, place_names):
    prompt = (
        "The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis.\n\n"
        "Please provide a concise narrative of the contents of the following table. In your narrative be sure to include the list of cities,\n"
        "and the names of the canton and survey areas.\n\n"
        "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table.\n\nINSTRUCTION_END ---> \n\n"
        " {table}\n\n"
        "The following is the names of the cities, cantons, and survey areas.\n\n"
        "{place_names}\n"
    ).format(table=table, place_names=place_names)
    return prompt


def feature_count_prompt(table, place_names):
    prompt = (
        "The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. "
        "Please provide a concise narrative of the contents of the following table. In your narrative be sure to the name "
        "of each park, lake or river"
        "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table.\n\n\n\n INSTRUCTION_END ---> \n\n"
        f"{table}\n\n"
        f"The following is the names of the lakes, rivers and parks included in the data.\n\n"
        f"{place_names}\n"
    )

    return prompt


def survey_result_summary_prompt(table):
    combined_summary_prompt = (
        "\n\n"
        "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table.\n\n\n\n INSTRUCTION_END ---> \n\n"
        f"{table}\n"
    )
    return combined_summary_prompt


def inventory_prompt(table):
    inventory_prompt = (

        "\n\n"
        "This is the list of all objects found at the beach."
        "Generate a narrative summary based on the following table. You need to mention all the objects that have a rate >= 0.5. Include "
        "% of total for each of the objects that have a rate >= 0.5, label these objects fail rate.\n\n"
        "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table.\n\n\n\n INSTRUCTION_END ---> \n\n"
        f"{table}\n"
    )
    

    return inventory_prompt

sampling_stratification_example = """
<!--- INSTRUCTION_START\n\n

The sampling stratification quantifies what proportion of the samples were conducted according to the proportion of the buffer zone that is dedicated to a particular land use feature.
Each survey location is surrounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. 
What changes is how the land use features are distributed within the buffer zone, That is we can group locations by the similarity of the measured topographical features present in the buffer zone. 

__Example of how to interpret sampling-stratification table:__\n\n


__Sample table:__\n\n

|   Proportion of buffer zone |   ('Proportion of samples collected', 'buildings') |   ('Proportion of samples collected', 'wetlands') |   ('Proportion of samples collected', 'forest') |   ('Proportion of samples collected', 'public-services') |   ('Proportion of samples collected', 'recreation') |   ('Proportion of samples collected', 'undefined') |   ('Proportion of samples collected', 'streets') |   ('Proportion of samples collected', 'vineyards') |   ('Proportion of samples collected', 'orchards') |
|----------------------------:|---------------------------------------------------:|--------------------------------------------------:|------------------------------------------------:|---------------------------------------------------------:|----------------------------------------------------:|---------------------------------------------------:|-------------------------------------------------:|---------------------------------------------------:|--------------------------------------------------:|
|                           1 |                                          0.0588235 |                                                 1 |                                       0.976471  |                                                0.776471  |                                                   1 |                                          0.870588  |                                                0 |                                          0.976471  |                                                 1 |
|                           2 |                                          0.0588235 |                                                 0 |                                       0.0235294 |                                                0.2       |                                                   0 |                                          0.0470588 |                                                0 |                                          0         |                                                 0 |
|                           3 |                                          0.0117647 |                                                 0 |                                       0         |                                                0.0235294 |                                                   0 |                                          0.0823529 |                                                0 |                                          0.0235294 |                                                 0 |
|                           4 |                                          0.376471  |                                                 0 |                                       0         |                                                0         |                                                   0 |                                          0         |                                                0 |                                          0         |                                                 0 |
|                           5 |                                          0.494118  |                                                 0 |                                       0         |                                                0         |                                                   0 |                                          0         |                                                0 |                                          0         |                                                 0 |


__exmple paragraph__

The sampling-stratification of the surveys was as follows: 49% of the surveys were taken at locations where 80-100% of the buffer was dedicated to buidlings. 37% of the surveys were taken at locations 
where 60 -80% of the buffer was dedicated to buidlings. 1% of the surveys were taken at locations where 40-60% of the buffer was dedicated to buidlings. 6% of the samples were taken at locations where 20 - 40% 
of the buffer was dedicated to buidlings. 6% of samples was taken at locations where 0-20% of the buffer was dedicated to buidlings. All of the samples were taken at locations where 0-20% of the buffer was 
dedicated to wetlands. 98% of the samples were taken at locations where 0-20% of the buffer was dedicated to forest. 2% of surveys were taken at locations where 20-40% of the buffer was dedicated to forest. 
77% of the samples were taken at locations where 0-20% of the buffer was dedicated to public-services. 20% of the surveys were taken at locations where 20-40% of the buffer was dedicated to public services. 
2% of surveys were taken at locations where 20-40% of the buffer was dedicated to public services.

\n\nINSTRUCTION_END -->
"""

def sampling_stratification_prompt(table):
    profile_prompt = (
        "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table. Consider the example above\n\n INSTRUCTION_END ---> \n\n"
        f"{table}\n"
    )

    return profile_prompt

land_use_rates_example = """
<!--- INSTRUCTION_START\n\n

The sampling stratification quantifies what proportion of the samples were conducted according to the proportion of the buffer zone that is dedicated to a particular land use feature.
Each survey location is surrounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. 
What changes is how the land use features are distributed within the buffer zone and the average objects found per meter found. 

__Example of how to interpret sampling-stratification-rates table:__\n\n


__Sample table:__\n\n

|   Proportion of buffer zone |   buildings |  wetlands |   forest  |   public-services|   
|----------------------------:|------------:|----------:|----------:|-----------------:|
|                     0 - 20% |   0.0588235 |       .09 | 0.976471  |  0.776471  |   
|                    20 - 40% |   0.0588235 |         0 | 0.0235294 |  0.2       |
|                    40 - 60% |   0.0117647 |         0 | 0         |  0.0235294 |
|                    60 - 80% |   0.376471  |         0 | 0         |  0         |
|                    80 - 100%|   0.494118  |         0 | 0         |   0         | 


__exmple paragraph__

The average objects per meter based on the sampling-stratification was as follows: where buildings occupied 2 - 20% of the buffer the average objects per meter was 0.05,
where buildings occupied 20 - 40% of the buffer the average objects per meter was 0.03, where buildings occupied 40 - 60% of the buffer the average objects per meter was 0.01,
where buildings occupied 60 - 80% of the buffer the average objects per meter was 0.37, where buildings occupied 80 - 100% of the buffer the average objects per meter was 0.49.
where wetlands occupied 0 - 20% of the buffer the average objects per meter was .09. where forest occupied 0-20% of the buffer the average objects per meter was 0.98.
Where forest occupied 20 - 40% of the buffer the average objects per meter was 0.02. where public-services occupied 0 - 20% of the buffer the average objects per meter was 0.78.

\n\nINSTRUCTION_END -->
"""


def landuse_rates_prompt(table):
    rates_prompt = (
        "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table. Consider the example above\n\n INSTRUCTION_END ---> \n\n"
        f"{table}\n"
    )
    return rates_prompt

def material_results_prompt(table):
    prompt = ("\n\n"
              "The following table details the proportion that each material type represents to the total. \n"
              "Generate a narrative summary based on the following table. You need to include all the material types and their float values.\n"
              "If their is more than one material entry in the table.\n\n"
              "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table. Consider the example above\n\n INSTRUCTION_END ---> \n\n"
              f"{table}\n"
             )
    return prompt


def municipal_results_prompt(table):
    prompt = (
        "\n\n"
        "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table. You need to include all "
        "the cities and their results\n\nINSTRUCTION_END -->\n\n"
        f"{table}\n"
    )

    return prompt


system_prompt = (
    "Transcribe the values from tables and put them in paragraph form."
    "Being carefull that each value in the table is accounted for in the"
    "paragraph. You are to do this in a narrative form. Answers must be concise."
    "\n\n"
    "{context}"
)

land_use_description = [
    "\n\n"
    "Each survey location is surounded by a buffer zone of radius = 1 500 meters. ",
    "The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). ",
    "The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. ",
    "Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, ",
    "Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. ",
    "The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken"
    "according to the different conditions.\n\n"


]
ldu = "".join(land_use_description)
land_use_litter_density = [
    "\n\n"
    "The land use profile allows us to group locations according to the topography. ",
    "Here we consdider how the observed litter density changes based on the land use "
    "feature and the proportion of the buffer-zone that the feature occupies\n\n"
]

ldud = "".join(land_use_litter_density)





grid_approximation_def = [
    "\n\nGrid approximation of the posterior is a technique used in Bayesian inference to estimate the posterior distribution ",
    "of parameters by discretizing the parameter space and evaluating the posterior probability at each point on a grid. ",
    "This method is especially useful when the posterior distribution does not have a closed-form solution and when the ",
    "parameter space is of low dimensionality, allowing for a feasible grid search. We use two priors, one is a weigheted ",
    "combination of survey results from locations similar to the likelihood. The other prior uses the samples taken from the ",
    "same location, but prior to the specified date range\n\n"
]
grd = "".join(grid_approximation_def)
model = 'gpt-4o-mini'
from session_config import agg_groups


report_instructions = """\n
<!-- INSTRUCTION_START\n\n
1. Analysis of Sampling Stratification and Sampling stratification and trash density tables
   * Objective: Ensure conclusions about the presence or absence of objects are based on a combined interpretation of sampling stratification and litter density data.
   * Data Validation: Confirm that any conclusions about trash density and land use are supported by the presence of samples in the sampling stratification table"
   * Interpretation Guidelines: Analyze how the distribution of land-use features influences the observed trash density. 
   * Draw conclusions only when both stratification and density data are aligned.
   * A zero in the trash density table indicates that no objects were found for that land-use feature and proportion of buffer zone.

2. Reporting Geographic Information

   * Always provide the names of all the cities, cantons, and survey areas included in the report.
   * Always provide the names of all the lakes, rivers, and parks included in the report.

3. Definitions of Urban, Rural Areas, fail-rate

   * Urban Areas: Defined as areas where 60-100% of the buffer zone is dedicated to buildings, and forest occupies 0-20% of the buffer zone. 
   * Rural Areas: Defined as areas where 60-100% of the buffer zone is dedicated to forest, and buildings occupy 0-20% of the buffer zone.
   * Fail Rate: The proportion of samples where at least one of the object categories was found.

INSTRUCTION_END -->
"""



class ReportTexts:
    def __init__(self, name: str, start: str, end: str, survey_report: pd.DataFrame,  landuse_report: pd.DataFrame,
                 prior_report: pd.DataFrame = None, client: callable = None,  region_type: str = None, report_meta: {} = None,
                 columns_of_interest: [] = None):
        self.name = name
        self.start = start
        self.end = end
        self.region = region_type
        self.report_meta = report_meta
        self.report_label = construct_report_label(self.report_meta)
        self.survey_report = survey_report
        self.landuse_report = landuse_report
        self.prior_report = prior_report
        self.client = client
        self.chat = False
        self.objects = None
        self.columns_of_interest = columns_of_interest
        self.info_cols = ['city', 'canton', 'parent_boundary']


    def the_admin_boundaries(self):
        d = self.survey_report.administrative_boundaries()[0]
        d.loc['survey areas', 'count'] = d.loc['parent_boundary', 'count']
        d.drop('parent_boundary', inplace=True)

        d_names = self.survey_report.administrative_boundaries()[1]
        d_names['survey_area'] = d_names['parent_boundary']
        d_names.pop('parent_boundary')
        report_label = f"\n## Administrative boundaries {self.report_label} : Cities, cantons, survey areas\n\n"
        section_description = "The number and and names of the cities, cantons and survey areas included in this report\n\n"
        section_label = report_label + section_description

        place_names = ""
        for a_label, a_list in d_names.items():
            if a_label != 'location':
                if len(a_list) > 0:
                    a_list = ', '.join([x.capitalize() for x in a_list])
                    place_names += f"__{a_label.capitalize()}:__ {a_list}\n\n"
        user_prompt = admin_prompt(d.to_markdown(), place_names)
        if self.chat is True:
            system_prompt = (
                "You are a helpful assistant charged with transcribing the values from data analysis"
                "You have been given a table that details the number of survey locations, cities, cantons and survey areas. "
                "You have also been given the names of the cities, cantons and survey areas."
                "Transcribe the values from table and put them in paragraph form, include the names of all cities, cantons and survey areas."
                "Avoid characterizing the data or making any comments. You are to do this in a narrative form. Answers must be concise."
                "\n\n"

            )


            messages = messages_for_chat_completion(system_prompt=system_prompt, user_prompt=user_prompt)

            completed_chat = use_chat_completion(self.client, model=model, messages=messages)
            return d, completed_chat, section_label
        else:

            return f'{section_label}\n\n{user_prompt}'

    def the_named_features(self):
        d = self.survey_report.feature_inventory()[0]
        d_names = self.survey_report.feature_inventory()[1]
        report_label = f"\n## Named features {self.report_label} : The lakes, rivers and parks\n\n"
        section_description = "The number and names of the lakes, rivers or parks included in this report\n\n"
        section_label = report_label + section_description

        place_names = ""
        for a_label, a_list in d_names.items():
            if len(a_list) > 0:
                a_list = ', '.join([x.capitalize() for x in a_list])
                place_names += f"__{a_label.capitalize()}:__ {a_list}\n\n"
        user_prompt = feature_count_prompt(d.to_markdown(), place_names)

        if self.chat is True:
            system_prompt = (
                "You are a helpful assistant charged with transcribing the values from data analysis"
                "You have been given a table that details the number of parks, lakes and rivers in the analysis. "
                "You have also been given the names of the parks, lakes and rivers."
                "Transcribe the values from table and put them in paragraph form, include the names of all parks, lakes and rivers."
                "Avoid characterizing the data or making any comments. You are to do this in a narrative form. Answers must be concise."
                "\n\n"

            )

            messages = messages_for_chat_completion(system_prompt=system_prompt, user_prompt=user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return d, completed_chat, section_label

        else:

            return f'{report_label}\n\n{user_prompt}'

    def summary_statistics(self):
        d = self.survey_report.sampling_results_summary.T
        report_label = f"\n## Summary statistics {self.report_label}: The descriptive statistics of the survey results\n\n"
        section_description = f"{self.name}: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.\n\n"
        section_label = report_label + section_description
        user_prompt = survey_result_summary_prompt(d.to_markdown())

        if self.chat is True:
            system_prompt = (
                "You are a helpful assistant charged with transcribing the values from data analysis"
                "You have been given a table that summarizes the number of objects found per meter of shoreline as well as the "
                "start and end date and the total number of objects found. The table has the following format"
                "1. total (quantity) = the total number of objects identified, 2. nsamples = the numner of samples collected"
                "3. average = average objects per meter, 4. 5th, 25th, 50th, 75th, 95th = the objects per meter percentile ranking"
                "5. std = standard deviation in objects per meter, 6. max = the maximum recorded objects per meter"
                "7. start = the date of the first sample, 8. end = the date of the last sample"
                "Transcribe the values from table and put them in paragraph form."
                "Avoid characterizing the data or making any comments. You are to do this in a narrative form. Answers must be concise."
                "\n\n"

            )

            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return d, completed_chat, section_label
        else:

            return f'{report_label}\n\n{user_prompt}'

    def material_composition(self):
        d = self.survey_report.material_report
        report_label = f"\n## Material composition of objects {self.report_label}: estimated material composition\n\n"
        section_description = f"{self.name}: The proportion of each material type according to material category\n\n"
        section_label = report_label + section_description
        user_prompt = material_results_prompt(d.to_markdown())
        if self.chat is True:
            system_prompt = (
                "You are a helpful assistant charged with transcribing the values from data analysis "
                "You have been given a table that summarizes the material classification of the objects found. "
                "The following table details the proportion that each material type represents to the total number of objects found. "
                "Transcribe the values from table and put them in paragraph form. "
                "Avoid characterizing the data or making any comments. You are to do this in a narrative form. Answers must be concise. "
                "\n\n"

            )

            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return d, completed_chat, section_label
        else:
            return f'{section_label}\n\n{user_prompt}'

    def inventory(self):
        d = self.survey_report.object_summary()
        d['object'] = d.index.map(lambda x: codes.loc[x, 'en'])
        self.objects = d[d.quantity > 0]['object'].values
        report_label = f"\n## Inventory items {self.report_label} : The complete list of the objects found and indentified included in this report.\n\n"
        section_description = "The quantity, average density, % of total and fail rate per object category\n\n"
        section_label = report_label + section_description
        user_prompt = inventory_prompt(d.to_markdown())

        if self.chat is True:
            system_prompt = (
            "You are a helpful assistant charged with transcribing the values from data analysis "
            "You have been given a table that summarizes the occurence of specific objects on the beach. "
            "The table has the following format: 1. code: object identifier, 2. quantity: the total number found"
            "3. pcs/m = average objects per meter, 4. % of total = the proportion of the total for for this object"
            "5. sample_id = the number of samples, 6. fails = the number of times at least one of the object was found at a survey"
            "7. rate =  fails/the number of samples the number of times that at least one object was found, 8. object: the plain english name of the object type. "
            "Avoid characterizing the data or making any comments. You are to do this in a narrative form. Answers must be concise. "
            )

            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return d, completed_chat, section_label
        else:
            return f'{section_label}\n\n{user_prompt}'

    def landuse_profile(self):
        d = self.landuse_report.n_samples_per_feature() / self.survey_report.number_of_samples
        d.sort_index(inplace=True)
        new_columns = pd.MultiIndex.from_product([["Proportion of samples collected"], d.columns])
        d.columns = new_columns
        d['proportion of buffer'] = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
        d.set_index('proportion of buffer', inplace=True, drop=True)
        d.replace(0, 'no samples', inplace=True)
        d = d.map(lambda x: f"{x * 100:.2f}%" if isinstance(x, (int, float)) else x)
        report_label = f"\n## Sampling stratification {self.report_label}: The environmental features surrounding the survey location.\n\n"
        section_description = ldu + "\n\n"
        section_label = report_label + section_description
        user_prompt = sampling_stratification_prompt(d.to_markdown())

        if self.chat is True:
            system_prompt = (
                "You are a helpful assistant charged with transcribing the values from data analysis "
                f'{sampling_stratification_example}'
                "Avoid characterizing the data or making any comments. You are to do this in a narrative form. Answers must be concise. "
            )

            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return d, completed_chat, section_label
        else:
            return f'{section_label}\n\n{user_prompt}'

    def landuse_rates(self):
        d = self.landuse_report.rate_per_feature()
        d['proportion of buffer'] = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
        d.set_index('proportion of buffer', inplace=True, drop=True)
        d.replace(0, 'no samples', inplace=True)
        report_label = f"\n## Sampling stratification and trash density {self.report_label}: The changes in the observed litter density and the changes in land use\n\n"
        section_description = ldud + "\n\n"
        section_label = report_label + section_description
        user_prompt = landuse_rates_prompt(d.to_markdown())

        if self.chat is True:

            system_prompt = (
                "You are a helpful assistant charged with transcribing the values from data analysis "
                f'{land_use_rates_example}'
                "Transcribe the values from table and put them in paragraph form."
                "Avoid characterizing the data or making any comments. You are to do this in a narrative form. Answers must be concise. "
            )
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return d, completed_chat, section_label
        else:
            return f'{section_label}\n\n{user_prompt}'

    def survey_totals_boundary(self, info_columns: []):
        d = self.survey_report.sample_results(info_columns=info_columns)
        dt = d.groupby(info_columns).agg(agg_groups)
        # print(dt)
        report_label = f"\n## Municipal results {self.report_label} : The average pcs/m by municipality.\n\n"
        section_description = "The average sample total for each municipality in the report\n\n"
        section_label = report_label + section_description
        user_prompt = municipal_results_prompt(dt.to_markdown())

        if self.chat is True:
            system_prompt = (
                "You are a helpful assistant charged with transcribing the values from data analysis. "
                "You have been given a table that details the quantity (total number of objects) and the average objects "
                "per meter found for each of the selected regions. "
                "Transcribe the values from table and put them in paragraph form."
                "Avoid characterizing the data or making any comments. You are to do this in a narrative form. Answers must be concise. "
            )
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return dt, completed_chat, section_label
        else:
            return f'{section_label}\n\n{user_prompt}'

    def grid_approximation(self, data):
        the_forecast_object = GridForecast(self.landuse_report.df_cont, self.report_meta, data)

        return the_forecast_object.report_draft(data)
    def linear_methods(self):
        linear_method_args = {
            'name': self.report_meta['name'],
            'start': self.report_meta['start'],
            'end': self.report_meta['end'],
            'survey_report': self.survey_report,
            'landuse_report': self.landuse_report,
            'columns_of_interest': self.columns_of_interest,
            'report_meta': self.report_meta

        }

        the_regression_object = LinearMethods(**linear_method_args)
        return the_regression_object.string_rep()

    def chat_rep(self, file_name, info_columns: []):


        title = f"\n# Survey report {self.report_label}\n\n"
        d = self.survey_report.object_summary()
        d['object'] = d.index.map(lambda x: codes.loc[x, 'en'])


        append_to_markdown(file_name, title)

        a, b, c = self.the_admin_boundaries()
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.the_named_features()
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.summary_statistics()
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.material_composition()
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.landuse_profile()
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.landuse_rates()
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.survey_totals_boundary(info_columns=self.info_cols)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.inventory()
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')



        return print(f"file saved as {file_name}")

    def string_rep(self, data: pd.DataFrame = None):
        title = f"\n# Survey report {self.report_label}\n\n"

        admin_boundaries = self.the_admin_boundaries()
        feature_names = self.the_named_features()
        summary_statistics = self.summary_statistics()
        inventory = self.inventory()
        material_report = self.material_composition()
        municipal_reports = self.survey_totals_boundary(['city'])
        landuse_profile = self.landuse_profile()
        landuse_rates = self.landuse_rates()
        regression_and_cluster = self.linear_methods()
        grid_string = ""
        if data is not None:
           grid_string += self.grid_approximation(data)

        astring = f"""
        {report_instructions}
        {title}
        {admin_boundaries}
        {feature_names}
        {summary_statistics}
        {municipal_reports}
        {material_report}
        {landuse_profile}
        {landuse_rates}
        {grid_string}
        {regression_and_cluster}
        {inventory}     
        """
        return astring

    def __repr__(self):
        return self.string_rep()