"""
roughdraft.py
hammerdirt 2024
Author: Roger Erismann

This module provides functions and classes to generate various textual reports based on survey and land use data.
It includes methods for creating narrative summaries, generating prompts for chat-based completions, and appending content to markdown files.

Functions
---------
use_chat_completion(client: ChatOpenAI, model: str = 'gpt-3.5-turbo-0125', messages: list[dict] = None) -> dict
    Generate a chat completion using the specified model and messages.

messages_for_chat_completion(system_prompt: str = None, user_prompt: str = None) -> list[dict]
    Create a list of messages for chat completion.

admin_prompt(table: str, place_names: str) -> str
    Generate a summary of administrative data that enumerates the different expected aggregates based on usage.

feature_count_prompt(table: str, place_names: str) -> str
    Generate a prompt to summarize the count of features in the survey data.

survey_result_summary_prompt(table: str) -> str
    Generate a prompt to summarize the survey results.

inventory_prompt(table: str) -> str
    Generate a prompt to summarize the inventory of objects found at the beach.

sampling_stratification_prompt(table: str) -> str
    Generate a prompt to summarize the sampling stratification.

landuse_rates_prompt(table: str) -> str
    Generate a prompt to summarize the land use rates.

material_results_prompt(table: str) -> str
    Generate a prompt to summarize the material results.

municipal_results_prompt(table: str) -> str
    Generate a prompt to summarize the municipal results.

Classes
-------
ReportTexts
    A class to generate various textual reports based on survey and land use data.
"""

import pandas as pd
from session_config import code_definitions_map, construct_report_label, feature_type_labels
from gridforecast import GridForecast
from linearmethods import LinearMethods

from session_config import land_use_description, sampling_stratification_example, land_use_rates_example
from session_config import grid_approximation_def, report_instructions #, landuse_litter_density
from session_config import agg_groups, append_to_markdown
from langchain_openai import ChatOpenAI


def construct_sub_title(report_meta):
    prefix = '**Summary and analysis of observations of trash density**: objects related to '
    if len(report_meta['code_types']) > 2:
        o_types = ', '.join(report_meta['code_types'][:-1])
        o_types += f" and {report_meta['code_types'][-1]}"
    elif len(report_meta['code_types']) == 2:
        o_types = f"{report_meta['code_types'][0]} and {report_meta['code_types'][1]}"
    else:
        o_types = report_meta['code_types'][0]

    if report_meta['feature_type'] is not None:
        feature_types = f" found in {feature_type_labels[report_meta['feature_type']]}s."
        subtitle = prefix + o_types + feature_types
    else:
        feature_types = f" found in lakes and rivers."
        subtitle = prefix + o_types + feature_types

    report_number = construct_report_label(report_meta)
    subtitle = f"{subtitle} <i>Report number: {report_number}</i>\n"
    return subtitle

def construct_report_title_and_subtitle(report_meta, notes: str = None):
    if report_meta['boundary'] is not None:
        print('boundary is not none')
        suffix = report_meta['boundary']
        title = f"# {report_meta['name']} {suffix}\n"
    else:
        title = f"\n# {report_meta['name']}\n"


    sub_title = construct_sub_title(report_meta)
    if notes is not None:
        sub_title += f"\n\n{notes}"
    return f'{title}\n{sub_title}'

# ldu: This variable is a string that concatenates the elements of the list `land_use_description`.
# The list `land_use_description` is defined in `session_config.py` and contains a detailed description
# of the land use profile and buffer zone characteristics for survey locations.
ldu = "".join(land_use_description)
# ldud: This variable is a string that concatenates the elements of the list `landuse_litter_density`.
# The list `landuse_litter_density` is defined in `session_config.py` and provides an explanation
# of how observed litter density changes based on land use features and their proportions in the buffer zone.
# ldud = "".join(landuse_litter_density)
# grd: This variable is a string that concatenates the elements of the list `grid_approximation_def`.
# The list `grid_approximation_def` is defined in `session_config.py` and describes the technique of grid approximation
# used in Bayesian inference to estimate posterior distributions of parameters.
grd = "".join(grid_approximation_def)

def use_chat_completion(client: ChatOpenAI, model: str = 'gpt-3.5-turbo-0125', messages: list[dict] = None) -> dict:
    """
    Generate a chat completion using the specified model and messages.

    This function interacts with the chat completion API of the client to generate a response based on the provided
    model and messages.

    Parameters
    ----------
    client : ChatOpenAI
        The client object used to interact with the chat completion API.
    model : str, optional
        The model to use for generating the chat completion. Default is 'gpt-3.5-turbo-0125'.
    messages : list of dict, optional
        A list of message dictionaries to be used as input for the chat completion. Each dictionary should have a 'role'
         and 'content' key.

    Returns
    -------
    dict
        The completed chat response generated by the model.

    Raises
    ------
    ValueError
        If the client is None.
    """
    if client is None:
        raise ValueError("Client cannot be None")

    completed_chat = client.chat.completions.create(model=model, messages=messages)
    return completed_chat

def messages_for_chat_completion(system_prompt: str = None, user_prompt: str = None) -> list[dict]:
    """
    Create a list of messages for chat completion.

    This function generates a list of message dictionaries to be used as input for the chat completion API.
    Each dictionary contains a role and content.

    Parameters
    ----------
    system_prompt : str, optional
        The system prompt to be included in the messages. Default is None.
    user_prompt : str, optional
        The user prompt to be included in the messages. Default is None.

    Returns
    -------
    list of dict
        A list of message dictionaries, each containing a 'role' and 'content' key.

    Raises
    ------
    ValueError
        If either system_prompt or user_prompt is None.
    """
    if system_prompt is None or user_prompt is None:
        raise ValueError("Both system_prompt and user_prompt cannot be None")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    return messages

def admin_prompt(table: str, place_names: str) -> str:
    """
    Generate a summary of administrative data that enumerates the different expected aggregates based on usage.

    This function creates a prompt to generate a narrative summary of the provided table and place names, detailing the
     number of survey locations, cities, cantons, and survey areas.

    Parameters
    ----------
    table : str
        The table containing the administrative data in markdown format.
    place_names : str
        The names of the places to be included in the prompt.

    Returns
    -------
    str
        The formatted prompt for generating a summary of administrative data.

    Raises
    ------
    ValueError
        If either table or place_names is None.
    """
    if table is None or place_names is None:
        raise ValueError("Both table and place_names cannot be None")

    prompt = (
        "The following table details the number of survey locations, cities, cantons and survey areas present in the "
        "data under analysis.\n\n"
        "{table}\n\n"
        "The following is the names of the cities, cantons, and survey areas.\n\n"
        "{place_names}\n"
    ).format(table=table, place_names=place_names)
    return prompt

def feature_count_prompt(table: str, place_names: str) -> str:
    """
    Generate a prompt to summarize the count of features in the survey data.

    This function creates a prompt to generate a narrative summary of the provided table and place names, detailing
    the number and names of lakes, rivers, and parks in the survey data.

    Parameters
    ----------
    table : str
        The table containing the feature count data in markdown format.
    place_names : str
        The names of the lakes, rivers, and parks to be included in the prompt.

    Returns
    -------
    str
        The formatted prompt for generating a summary of feature counts.

    Raises
    ------
    ValueError
        If either table or place_names is None.
    """
    if table is None or place_names is None:
        raise ValueError("Both table and place_names cannot be None")

    prompt = (
        "The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. "
       "\n\n"
       f"{table}\n\n"
       "The following is the names of the lakes, rivers and parks included in the data.\n\n"
       f"{place_names}\n"
    )

    return prompt

def survey_result_summary_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the survey results.

    This function creates a prompt to generate a narrative summary of the provided table, detailing the sample total
    in pcs/m for each survey.

    Parameters
    ----------
    table : str
        The table containing the survey results data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of survey results.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    combined_summary_prompt = (
        "\n\n"
        "This table summarizes the sample total in pcs/m for each survey. Each survey is defined by a sample_id. A "
        "survey total is the sum of all rows that have the same sample_id.\n\n"
        f"{table}\n"
    )
    return combined_summary_prompt

def inventory_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the inventory of objects found at the beach.

    This function creates a prompt to generate a narrative summary of the provided table, mentioning all objects with a rate >= 0.5 and their percentage of the total.

    Parameters
    ----------
    table : str
        The table containing the inventory data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the inventory.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    inv_prompt = (
        "\n"
        "This is the list of all objects found at the beach. Generate a narrative summary based on the following table."
        "You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects "
        "that have a rate >= 0.5, label these objects fail rate.\n\n"
        "<!--- INSTRUCTION_START\n\nGenerate a narrative summary based on the following table. "
        "The Fail Rate is The proportion of samples where at least one of the objects were found."
        "\n\nINSTRUCTION_END ---> \n"
        f"{table}\n"
    )
    return inv_prompt

def sampling_stratification_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the sampling stratification.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the proportion of samples collected according to the proportion of the buffer zone
    dedicated to each land use feature.

    Parameters
    ----------
    table : str
        The table containing the sampling stratification data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the sampling stratification.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    profile_prompt = (
        f"{sampling_stratification_example}"
        f"{table}\n"
    )

    return profile_prompt

def landuse_rates_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the land use rates.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the average objects per meter based on the proportion of the buffer zone
    dedicated to each land use feature.

    Parameters
    ----------
    table : str
        The table containing the land use rates data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the land use rates.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    rates_prompt = (
        f"{land_use_rates_example}\n\n"
        f"{table}\n"
    )
    return rates_prompt

def material_results_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the material results.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the proportion that each material type represents to the total.

    Parameters
    ----------
    table : str
        The table containing the material results data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the material results.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    prompt = (
        "\n\n"
        "The following table details the proportion that each material type represents to the total. \n\n"       
        f"{table}\n"
    )
    return prompt

def municipal_results_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the municipal results.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the average pcs/m by municipality.

    Parameters
    ----------
    table : str
        The table containing the municipal results data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the municipal results.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    prompt = (
        "\n\n"
        "The following table details the results of the survey for each unique occurrence of the selected variable. \n\n"
        f"{table}\n"
    )

    return prompt



class ReportTexts:
    """
    A class to generate various textual reports based on survey and land use data.

    This class provides methods to generate summaries and detailed reports on survey results, land use profiles,
    material composition, and other related data. It supports generating these reports in both narrative and tabular
    forms, with optional integration for chat-based completion.

    Attributes
    ----------
    survey_report : pd.DataFrame
        DataFrame containing the survey report data.
    landuse_report : pd.DataFrame
        DataFrame containing the land use report data.
    prior_report : pd.DataFrame, optional
        DataFrame containing prior report data, if available.
    report_meta : dict
        Metadata for the report, including name, start date, and end date.
    info_cols : list
        List of information columns to be included in the report.
    name : str
        Name of the report.
    start : str
        Start date of the report.
    end : str
        End date of the report.
    report_label : str
        Label for the report.
    objects : list
        List of objects found in the survey.

    Methods
    -------
    the_admin_boundaries() -> dict
        Generate a summary of administrative boundaries.
    the_named_features() -> dict
        Generate a summary of named features.
    summary_statistics() -> dict
        Generate summary statistics of the survey results.
    material_composition() -> dict
        Generate a summary of the material composition of objects found.
    inventory() -> dict
        Generate an inventory of objects found at the beach.
    landuse_profile() ->dict
        Generate a summary of the land use profile around the survey location.
    landuse_rates() -> str
        Generate a summary of land use rates around the survey location.
    survey_totals_boundary(info_columns: list) -> str
        Generate a summary of survey totals by boundary.
    survey_totals_for_all_info_cols() -> str
        Generate a summary of survey totals by boundary for each column in info_cols.
    grid_approximation(data: pd.DataFrame) -> str
        Generate a grid approximation report.
    linear_methods() -> str
        Generate a cluster and regression report.
    string_rep(file_name: str, data: pd.DataFrame) -> tuple
        Generate a chat-based report and save it to a markdown file.
    """

    def __init__(self, report_meta: dict, survey_report: pd.DataFrame, landuse_report: pd.DataFrame,
                 prior_report: pd.DataFrame = None, info_cols: list = None):
        self.name = report_meta['name']
        self.start = report_meta['start']
        self.end = report_meta['end']
        self.report_meta = report_meta
        self.report_label = construct_report_label(self.report_meta)
        self.survey_report = survey_report
        self.landuse_report = landuse_report
        self.prior_report = prior_report
        self.objects = None
        self.columns_of_interest = report_meta['columns_of_interest']
        self.info_cols = [x for x in ['city', 'canton', 'parent_boundary'] if info_cols is None or x in info_cols]

    def the_admin_boundaries(self) -> dict:
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
                place_names += f"{a_label}: {', '.join(a_list)}\n"
        user_prompt = admin_prompt(d.to_markdown(), place_names)

        return {'dataframe': d , 'prompt': f'{section_label}\n\n{user_prompt}'}

    def the_named_features(self) -> dict:
        d = self.survey_report.feature_inventory()[0]
        d_names = self.survey_report.feature_inventory()[1]
        report_label = f"\n## Named features {self.report_label} : The lakes, rivers and parks\n\n"
        section_description = "The number and names of the lakes, rivers or parks included in this report\n\n"
        section_label = report_label + section_description

        place_names = ""
        for a_label, a_list in d_names.items():
            if a_label != 'location':
                place_names += f"{a_label}: {', '.join(a_list)}\n"
        user_prompt = feature_count_prompt(d.to_markdown(), place_names)
        return {'dataframe': d, 'prompt': f'{section_label}\n\n{user_prompt}'}

    def summary_statistics(self) -> dict:
        d = self.survey_report.sampling_results_summary.T
        report_label = f"\n## Summary statistics {self.report_label}: The descriptive statistics of the survey results\n\n"
        section_description = f"{self.name}: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.\n\n"
        section_label = report_label + section_description
        user_prompt = survey_result_summary_prompt(d.to_markdown())

        return {'dataframe': d, 'prompt': f'{section_label}\n\n{user_prompt}'}

    def material_composition(self) -> dict:
        d = self.survey_report.material_report
        report_label = f"\n## Material composition of objects {self.report_label}: estimated material composition\n\n"
        section_description = f"{self.name}: The proportion of each material type according to material category\n\n"
        section_label = report_label + section_description
        user_prompt = material_results_prompt(d.to_markdown())
        return {'dataframe': d, 'prompt': f'{section_label}\n\n{user_prompt}'}

    def inventory(self) -> dict:
        d = self.survey_report.object_summary()
        d['object'] = d.index.map(lambda x: code_definitions_map.loc[x, 'en'])
        self.objects = d[d.quantity > 0]['object'].values
        report_label = f"\n## Inventory items {self.report_label} : The complete list of the objects found and identified included in this report.\n\n"
        section_description = "The quantity, average density, % of total and fail rate per object category\n\n"
        section_label = report_label + section_description
        user_prompt = inventory_prompt(d.to_markdown())

        return {'dataframe': d, 'prompt': f'{section_label}\n\n{user_prompt}'}

    def landuse_profile(self) -> dict:
        d = self.landuse_report.n_samples_per_feature() / self.survey_report.number_of_samples
        d.sort_index(inplace=True)
        new_columns = pd.MultiIndex.from_product([["Proportion of samples collected"], d.columns])
        d.columns = new_columns
        d['proportion of buffer'] = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
        d.set_index('proportion of buffer', inplace=True, drop=True)
        d.replace(0, 'none', inplace=True)
        d = d.map(lambda x: f"{x * 100:.1f}%" if isinstance(x, (int, float)) else x)
        report_label = f"\n## Sampling stratification {self.report_label}: The environmental features surrounding the survey location.\n"
        # section_description = ldu"
        section_label = report_label + ldu
        user_prompt = sampling_stratification_prompt(d.to_markdown())

        return {'dataframe': d, 'prompt': f'{section_label}\n{user_prompt}'}

    def landuse_rates(self) -> dict:
        d = self.landuse_report.rate_per_feature()
        # d = d.round(2)
        new_columns = pd.MultiIndex.from_product([["Pieces of trash per meter"], d.columns])
        d.columns = new_columns
        d['proportion of buffer'] = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
        d.set_index('proportion of buffer', inplace=True, drop=True)
        # d = d.round(2)
        d.replace(0, 'none', inplace=True)
        report_label = f"\n## Sampling stratification and trash density {self.report_label}: The changes in the observed litter density and the changes in land use\n"
        # section_description = ldud
        section_label = report_label
        user_prompt = landuse_rates_prompt(d.to_markdown())

        return {'dataframe': d, 'prompt': f'{section_label}\n{user_prompt}'}

    def survey_totals_boundary(self, info_columns: list) -> dict:
        d = self.survey_report.sample_results(info_columns=info_columns)
        dt = d.groupby(info_columns, as_index=False).agg(agg_groups)
        the_theme = info_columns[0]
        if the_theme == 'parent_boundary':
            the_theme = 'survey area'
        report_label = f"\n## {self.report_label} {the_theme}: The average pcs/m by {the_theme}.\n\n"
        section_description = f"The average sample total for each {the_theme} in the report\n\n"
        section_label = report_label + section_description
        user_prompt = municipal_results_prompt(dt.to_markdown())

        return {'dataframe': dt, 'prompt': f'{section_label}\n\n{user_prompt}'}

    def survey_totals_for_all_info_cols(self) -> dict:
        results = []
        data_frames = []
        if 'boundary' in self.report_meta:
            these_cols = [x for x in self.info_cols if x != self.report_meta['boundary']]
        else:
            these_cols = self.info_cols
        for col in these_cols:
            result = self.survey_totals_boundary([col])
            result_str = f"## Survey Totals for {col}\n\n{result['prompt']}\n\n"
            results.append(result_str)
            data_frames.append(result['dataframe'])

        return {'dataframe': data_frames, 'prompt': ''.join(results)}

    def grid_approximation(self, data: pd.DataFrame) -> dict:
        the_forecast_object = GridForecast(self.landuse_report.df_cont, self.report_meta, data)
        report = the_forecast_object.report_draft()
        return report

    def linear_methods(self) -> dict:
        methods = LinearMethods(
            self.report_meta,
            survey_report=self.survey_report,
            landuse_report=self.landuse_report
        )

        cluster_analysis_result = methods.cluster_analysis(self.columns_of_interest)
        regression_result = methods.linear_and_ensemble_regression()
        feature_importance_result = methods.feature_importance()

        report = (
            "\n\n"
            f"{cluster_analysis_result['prompt']}\n\n"
            f"{regression_result['prompt']}\n\n"
            f"{feature_importance_result['prompt']}\n"
        )
        d = {
            'cluster_analysis': cluster_analysis_result['dataframe'],
            'regression': regression_result['dataframe'],
            'feature_importance': feature_importance_result['dataframe']
        }
        return {'dataframe': d, 'prompt': report}

    def string_rep(self, file_name: str, data: pd.DataFrame) -> tuple:
        title =construct_report_title_and_subtitle(self.report_meta) + '\n\n'
        d = self.survey_report.object_summary()
        d['object'] = d.index.map(lambda x: code_definitions_map.loc[x, 'en'])

        with open(file_name, 'w') as f:
            f.write(report_instructions)

        append_to_markdown(file_name, title)

        entry = ''
        print('processing admin boundaries')
        data_frames= {}
        a = self.the_admin_boundaries()
        entry += a['prompt']
        data_frames['the_admin_boundaries'] = a['dataframe']

        a = self.the_named_features()
        print('processing named features')
        entry += a['prompt']
        data_frames['the_named_feature'] = a['dataframe']

        a = self.summary_statistics()
        print('processing summary statistics')
        entry += a['prompt']
        data_frames['summary_statistics'] = a['dataframe']

        a = self.material_composition()
        print('processing material composition')
        entry += a['prompt']
        data_frames['material_composition'] = a['dataframe']

        a = self.survey_totals_for_all_info_cols()
        print('processing survey totals for all info cols')
        entry += a['prompt']
        data_frames['survey_totals_for_all_info_cols'] = a['dataframe']

        b = self.inventory()
        print('processing inventory')
        entry += b['prompt']
        data_frames['inventory'] = b['dataframe']

        admin_summary = title + entry

        append_to_markdown(file_name, entry)

        entry = ''

        a = self.landuse_profile()
        print('processing landuse profile')
        entry += a['prompt']
        data_frames['landuse_profile'] = a['dataframe']

        a = self.landuse_rates()
        print('processing landuse rates')

        entry += a['prompt']
        data_frames['landuse_rates'] = a['dataframe']

        sampling_strat = title + entry
        append_to_markdown(file_name, entry)

        entry = ''
        print('processing grid approximation')
        a = self.grid_approximation(data)

        entry += a['prompt']
        data_frames['grid_approximation'] = a['dataframe']
        grid_f = title + entry
        append_to_markdown(file_name, entry)

        entry = ''
        print('processing linear methods')
        a = self.linear_methods()
        entry += a['prompt']
        data_frames['linear_methods'] = a['dataframe']

        lin_f = title + entry
        append_to_markdown(file_name, entry)

        entry = ''
        entry += b['prompt']
        inventory_f = title + entry
        append_to_markdown(file_name, entry)

        return admin_summary, sampling_strat, grid_f, lin_f, inventory_f, data_frames

    def __repr__(self) -> str:
        return str(self.report_meta)