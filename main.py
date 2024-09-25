import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from shapely.geometry import Point
from shapely.geometry import box
import matplotlib.colors as mcolors
import seaborn as sns

import matplotlib.patches as mpatches
import session_config
from session_config import  collect_survey_data, feature_variables, agg_groups, feature_variables
from session_config import lat_lon, beaches, model_rough_draft, model_corrections, feature_type_labels
from session_config import tobo_snacks, report_meta_data, report_args, highlight_max, table_css_styles
from reports import make_report_objects
from reports import histograms_standard
from reports import ecdf_plots_standard, scatter_plot_standard
import gridforecast as gfcast
from linearmethods import LinearMethods
from roughdraft import ReportTexts, messages_for_chat_completion, use_chat_completion, construct_report_title_and_subtitle
from reportprompts import report_system_prompt, split_text_on_phrase, report_summary_prompt, report_stratification_prompt, executive_corrections_prompt
from reportprompts import grid_approximation_prompt, report_regression_prompt, final_draft_prompt, corrections_prompt, executive_summary_prompt
from IPython.display import Markdown
from geospatial import map_markers, make_map_caption, layer_selection_criteria


# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
import matplotlib.cm as cm
from session_config import canton_layer, municipal_layer, rivers_layer, lakes_layer
# import matplotlib.colormaps as mpl_color_caps
from matplotlib import colormaps as mpl_color_maps
# from reportlab.platypus import Paragraph, ListFlowable, ListItem
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import matplotlib.dates as mdates
# import seaborn as sns
import re

from reportlab.platypus import TableStyle, Spacer, KeepTogether
from reportlab.platypus import SimpleDocTemplate, Paragraph, ListFlowable, ListItem, Table, TableStyle, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import re
from bs4 import BeautifulSoup

from reportlab.platypus import Image, Table

from dotenv import load_dotenv
import os
from myst_nb import glue

from langchain_openai import ChatOpenAI
import openai

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

datax = collect_survey_data()

#%%
rcodes = session_config.code_definitions_map.index

cantons = ['Bern', 'Genève', 'Vaud', 'Neuchâtel', 'Valais']
datax = datax[datax.canton.isin(cantons)]
def get_user_input(data):
    # Define allowed choices
    allowed_boundaries = ['canton', 'city', 'survey_area']
    allowed_feature_types = ['l', 'r', 'p']  # Replace with actual feature types

    # Default values
    default_start = "2020-01-01"
    default_end = "2021-12-31"
    default_name = "Bern"
    default_boundary = "canton"
    default_boundary_name = "Bern"

    while True:
        # Collect user input with defaults
        start = input(f"Enter start date (YYYY-MM-DD) [{default_start}]: ") or default_start
        end = input(f"Enter end date (YYYY-MM-DD) [{default_end}]: ") or default_end
        name = input(f"Enter name [{default_name}]: ") or default_name

        # Validate boundary input
        while True:
            boundary = input(f"Enter boundary ({', '.join(allowed_boundaries)}) [{default_boundary}]: ") or default_boundary
            if boundary in allowed_boundaries:
                break
            print(f"Invalid boundary. Choose from {', '.join(allowed_boundaries)}.")

        # Collect possible boundary names based on selected boundary
        if boundary == 'canton':
            boundary_names = data['canton'].unique()
        elif boundary == 'city':
            boundary_names = data['city'].unique()
        elif boundary == 'survey_area':
            boundary_names = data['parent_boundary'].unique()

        # Validate boundary_name input
        while True:
            boundary_name = input(f"Enter boundary name ({', '.join(boundary_names)}) [{default_boundary_name}]: ") or default_boundary_name
            if boundary_name in boundary_names:
                break
            print(f"Invalid boundary name. Choose from {', '.join(boundary_names)}.")

        # Validate feature_type input
        while True:
            feature_type = input(f"Enter feature type ({', '.join(allowed_feature_types)}, or None for all types): ").strip().lower()
            if feature_type in allowed_feature_types or feature_type == 'none':
                feature_type = None if feature_type == 'none' else feature_type
                break
            print(f"Invalid feature type. Choose from {', '.join(allowed_feature_types)}, or enter None for all types.")

        # Collect possible feature names based on selected feature type
        if feature_type:
            feature_names = data[data.feature_type == feature_type].feature_name.unique()
        else:
            feature_names = data.feature_name.unique()

        # Validate feature_name input
        while True:
            feature_name = input(f"Enter feature name ({', '.join(feature_names)}, or None): ")
            if feature_name in feature_names or feature_name.lower() == 'none':
                feature_name = None if feature_name.lower() == 'none' else feature_name
                break
            print(f"Invalid feature name. Choose from {', '.join(feature_names)}, or enter None.")

        # Print collected inputs
        print("\nCollected Inputs:")
        print(f"Start Date: {start}")
        print(f"End Date: {end}")
        print(f"Name: {name}")
        print(f"Boundary: {boundary}")
        print(f"Boundary Name: {boundary_name}")
        print(f"Feature Type: {feature_type}")
        print(f"Feature Name: {feature_name}")

        # Ask if inputs are okay
        confirm = input("Are these inputs okay? (yes/y to confirm, no to change): ").strip().lower()
        if confirm in ['yes', 'y']:
            break

    # Collect report codes
    report_codes = session_config.code_definitions_map.index

    # Create the r_args dictionary
    r_args = {
        'data': data,
        'start': start,
        'end': end,
        'name': name,
        'boundary': boundary,
        'boundary_name': boundary_name,
        'feature_type': feature_type,
        'feature_name': feature_name,
        'report_codes': report_codes,
        'columns_of_interest': session_config.feature_variables
    }

    return r_args


def get_local_directory():
    while True:
        local_directory = input("Enter local directory name (alphanumeric, no spaces): ").strip()
        if re.match("^[a-zA-Z0-9]+$", local_directory):
            local_directory += '/'
            if not os.path.exists(local_directory):
                os.makedirs(local_directory)
            return local_directory
        else:
            print("Invalid input. Please enter an alphanumeric string with no spaces.")
# r_args = get_user_input(datax)
# local_directory =get_local_directory()

# r_args = {
#     'data': datax,
#     'start': '2020-01-01',
#     'end':'2021-05-31',
#     'name':'Biel',
#     'boundary': 'city',
#     'boundary_name': 'Biel/Bienne',
#     'feature_type': None,
#     'feature_name': None,
#     'report_codes': rcodes,
#     'columns_of_interest': feature_variables
# }



# this_report = report_args(**r_args)
# report_data, report_meta = report_meta_data(**this_report)
# all_report, all_land_use = make_report_objects(report_data, info_columns = ['canton', 'city', 'feature_name'])
#
# report_meta['resources'] = local_directory
#
# client = ChatOpenAI(model=model_rough_draft)
# args = {
#     'report_meta': report_meta,
#     'survey_report': all_report,
#     'landuse_report': all_land_use
# }

# firstdraft = ReportTexts(**args)
#
# asum, sampstrat, grid_f, lin_f, inv_f, data  = firstdraft.string_rep(f'{report_meta["resources"]}roughdraft.md', datax)
# title = construct_report_title_and_subtitle(report_meta)


import os
import webbrowser
import subprocess
import markdown
import tempfile

def main():
    reports = []

    while True:
        r_args = get_user_input(datax)
        local_directory = get_local_directory()

        this_report = report_args(**r_args)
        report_data, report_meta = report_meta_data(**this_report)
        all_report, all_land_use = make_report_objects(report_data, info_columns=['canton', 'city', 'feature_name'])

        report_meta['resources'] = local_directory

        client = ChatOpenAI(model=model_rough_draft)
        args = {
            'report_meta': report_meta,
            'survey_report': all_report,
            'landuse_report': all_land_use
        }

        firstdraft = ReportTexts(**args)
        asum, sampstrat, grid_f, lin_f, inv_f, data = firstdraft.string_rep(f'{report_meta["resources"]}roughdraft.md', datax)
        title = construct_report_title_and_subtitle(report_meta)

        report = {
            'name': report_meta['name'],
            'asum': asum,
            'sampstrat': sampstrat,
            'grid_f': grid_f,
            'lin_f': lin_f,
            'inv_f': inv_f,
            'data': data,
            'firstdraft': firstdraft,
            'title': title,
            'report_meta': report_meta,
            'all_report': all_report,
            'all_land_use': all_land_use
        }

        reports.append(report)

        while True:
            command = input("Enter a command (type 'help' for options, 'new' for new report, 'q' to quit): ").strip().lower()
            if command == 'q':
                return
            elif command == 'new':
                break
            elif command == 'help':
                print("Available commands:")
                print("  list - List available reports")
                print("  view <report_name> - View details of a report")
                print("  compare - Compare reports")
                print("  q - Quit the program")
            elif command == 'list':
                print("Available reports:")
                for report in reports:
                    print(f"  {report['name']}")
            elif command.startswith('view '):
                report_name = command.split(' ', 1)[1].strip().lower()
                selected_report = next((report for report in reports if report['name'].strip().lower() == report_name), None)
                if selected_report:
                    print(f"Details of report {report_name}:")
                    while True:
                        element = input("Enter the element to view (e.g., 'asum', 'grid_f', 'data', 'documents', 'q' to quit): ").strip().lower()
                        if element == 'q':
                            break
                        elif element == 'documents':
                            view_documents(selected_report['report_meta']['resources'])
                        elif element in selected_report:
                            print(f"{element}: {selected_report[element]}")
                        else:
                            print(f"Element '{element}' not found in report {report_name}.")
                else:
                    print(f"No report found with name {report_name}.")
            elif command == 'compare':
                compare_reports(reports)
            else:
                print("Unknown command. Type 'help' for a list of available commands.")

def view_documents(directory):
    files = [f for f in os.listdir(directory) if f.endswith(('.md', '.html', '.jpg', '.jpeg'))]
    if not files:
        print("No documents found in the directory.")
        return

    print("Available documents:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")

    while True:
        choice = input("Enter the number of the document to view, or 'q' to quit: ").strip().lower()
        if choice == 'q':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            file_path = os.path.join(directory, files[int(choice) - 1])
            open_document(file_path)
        else:
            print("Invalid choice. Please enter a valid number or 'q' to quit.")

def open_document(file_path):
    try:
        if file_path.endswith('.md'):
            # Convert Markdown to HTML
            with open(file_path, 'r') as md_file:
                md_content = md_file.read()
            html_content = markdown.markdown(md_content)

            # Save HTML to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_html:
                temp_html.write(html_content.encode('utf-8'))
                temp_html_path = temp_html.name

            # Open the HTML file in the default web browser
            webbrowser.open(f'file://{os.path.abspath(temp_html_path)}')
        elif file_path.endswith('.html'):
            webbrowser.open(f'file://{os.path.abspath(file_path)}')
        elif file_path.endswith(('.jpg', '.jpeg')):
            subprocess.run(['xdg-open', file_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to open {file_path}. Please ensure you have a viewer installed for this file type.")

def compare_reports(reports):
    while True:
        print("Available reports:")
        for report in reports:
            print(f"  {report['name']}")

        report_names = input("Enter the report names to compare (comma-separated), or 'q' to quit: ").strip().lower()
        if report_names == 'q':
            break

        names = [name.strip().lower() for name in report_names.split(',')]
        selected_reports = [report for report in reports if report['name'].strip().lower() in names]
        if len(selected_reports) < 2:
            print("Please enter at least two valid report names.")
            continue

        attribute = input("Enter the attribute to compare (e.g., 'grid_f'): ").strip()
        if not all(attribute in report for report in selected_reports):
            print(f"Attribute '{attribute}' not found in all selected reports.")
            continue

        for report in selected_reports:
            print(f"Report {report['name']} {attribute}: {report[attribute]}")

if __name__ == "__main__":
    main()