"""
reports.py
hammerdirt 2024
Author: Roger Erismann

The SurveyReport class is a container for the data and methods that are used to generate a report from a survey data set.
The report is a summary of the data in the survey. The exact contents of the report should be defined by the stakeholders
charged with the responsibility of interpreting the data. This has not happened. Therefore, this report is the byproduct
of the calculations necessary to forecast values.

Combined with the LandUseReport class, it is possible to describe the sampling conditions of a survey in a quantitative
scale. Therefore, if the data in the report is a collection of like items, the report can be used to describe the
concentration of the items per meter given the environmental conditions of the survey.

Dependencies
------------
- pandas
- numpy
- session_config
- matplotlib.pyplot
- matplotlib.dates
- seaborn
- geospatial

Functions
---------
- collect_sample_totals(df: pd.DataFrame, sample_id: str = index_label, labels: str = location_label, info_columns: list[str] = None, afunc: dict = unit_agg) -> pd.DataFrame
- make_report_objects(df: pd.DataFrame, info_columns: list[str] = None) -> tuple
- histograms_standard(data: list[tuple[pd.DataFrame, str, str]]) -> plt.Figure
- ecdf_plots_standard(data: list[tuple[pd.DataFrame, str, str, str]]) -> plt.Figure
- scatter_plot_standard(data: list[tuple[pd.DataFrame, str, str]]) -> plt.Figure

Classes
-------
- SurveyReport
    - __init__(self, dfc)
    - administrative_boundaries(self) -> tuple[pd.DataFrame, dict[str, np.ndarray]]
    - feature_inventory(self) -> tuple[pd.DataFrame, dict[str, np.ndarray]]
    - date_range(self) -> dict
    - inventory(self) -> pd.DataFrame
    - total_quantity(self) -> int
    - number_of_samples(self) -> int
    - number_of_locations(self) -> int
    - material_report(self) -> pd.DataFrame
    - fail_rate(self, threshold: int = 1) -> pd.DataFrame
    - sample_results(self, df: pd.DataFrame = None, sample_id: str = index_label, labels: str = location_label, info_columns: list[str] = None, afunc: dict = unit_agg) -> pd.DataFrame
    - sampling_results_summary(self) -> pd.DataFrame
    - object_summary(self) -> pd.DataFrame
"""
import pandas as pd
import numpy as np
import session_config
from session_config import administrative, feature_types
from session_config import object_of_interest, feature_type_labels
from session_config import index_label, location_label, Y, Q
from session_config import unit_agg, agg_groups
from session_config import report_quantiles
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import geospatial

def collect_sample_totals(df: pd.DataFrame, sample_id: str = index_label, labels: str = location_label,
                          info_columns: list[str] = None, afunc: dict = unit_agg) -> pd.DataFrame:
    """
    Calculate the sample totals by grouping the data based on sample ID, labels, and date.

    This function groups the data by sample ID, labels, and date, and applies the aggregation function to calculate
    the sample totals. If additional information columns are provided, they are included in the grouping.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the survey data.
    sample_id : str, optional
        The column name representing the sample ID. Default is `index_label`.
    labels : str, optional
        The column name representing the location labels. Default is `location_label`.
    info_columns : list[str], optional
        Additional columns to include in the grouping. Default is None.
    afunc : dict, optional
        The aggregation function to apply to the grouped data. Default is `unit_agg`.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the aggregated sample totals.

    Raises
    ------
    ValueError
        If the input DataFrame is empty.
    """
    if df.empty:
        raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

    if not info_columns:
        return df.groupby([sample_id, labels, 'date'], as_index=False).agg(afunc)
    else:
        return df.groupby([sample_id, labels, 'date', *info_columns], as_index=False).agg(afunc)

def make_report_objects(df: pd.DataFrame, info_columns: list[str] = None) -> tuple:
    """
    Create SurveyReport and LandUseReport objects from the given DataFrame.

    This function creates a SurveyReport object and a LandUseReport object from the provided DataFrame.
    It first generates the parameters for the LandUseReport and then creates the LandUseReport using
    the target DataFrame and features.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the survey data.
    info_columns : list[str], optional
        Additional columns to include in the sample results. Default is None.

    Returns
    -------
    tuple
        A tuple containing the SurveyReport and LandUseReport objects.

    Raises
    ------
    ValueError
        If the input DataFrame is empty.
    """
    if df.empty:
        raise ValueError("No data in the DataFrame. Please check the query parameters and try again.")

    this_report = SurveyReport(dfc=df)

    # Generate the parameters for the LandUseReport
    target_df = this_report.sample_results(info_columns=info_columns)
    features = pd.read_csv('data/in_process/new_lu.csv')

    # Create a LandUseReport
    this_land_use = geospatial.LandUseReport(target_df, features)

    return this_report, this_land_use

def histograms_standard(data: list[tuple[pd.DataFrame, str, str]]) -> plt.Figure:
    """
    Generate standard histograms for the given data.

    This function generates histograms for each dataset provided in the input list. Each dataset is a tuple containing
    a DataFrame, a label, and a color. The histograms are plotted on the same figure.

    Parameters
    ----------
    data : list of tuple
        A list of tuples, where each tuple contains a DataFrame, a label, and a color. The DataFrame should contain the
        data to be plotted, the label is used for the legend, and the color specifies the color of the histogram.

    Returns
    -------
    plt.Figure
        A Matplotlib Figure object containing the histograms.

    Raises
    ------
    ValueError
        If the input data list is empty.
    """
    if not data:
        raise ValueError("The input data list is empty. Please provide valid data.")

    fig, ax = plt.subplots()

    for some_data in data:
        sns.histplot(data=some_data[0], x=Y, stat='probability', label=some_data[1], ax=ax, color=some_data[2])
    ax.legend()
    plt.tight_layout()
    plt.close()

    return fig

def ecdf_plots_standard(data: list[tuple[pd.DataFrame, str, str, str]]) -> plt.Figure:
    """
    Generate standard ECDF plots for the given data.

    This function generates ECDF plots for each dataset provided in the input list. Each dataset is a tuple containing
    a DataFrame, a label, a linestyle, and a color. The ECDF plots are plotted on the same figure.

    Parameters
    ----------
    data : list of tuple
        A list of tuples, where each tuple contains a DataFrame, a label, a linestyle, and a color. The DataFrame should
        contain the data to be plotted, the label is used for the legend, the linestyle specifies the line style, and the
        color specifies the color of the ECDF plot.

    Returns
    -------
    plt.Figure
        A Matplotlib Figure object containing the ECDF plots.

    Raises
    ------
    ValueError
        If the input data list is empty.
    """
    if not data:
        raise ValueError("The input data list is empty. Please provide valid data.")

    fig, ax = plt.subplots()
    an_x_limit = 0

    for some_data in data:
        this_max = np.quantile(some_data[0], .95)
        if this_max > an_x_limit:
            an_x_limit = this_max
        sns.ecdfplot(some_data[0], label=some_data[1], ls=some_data[2], ax=ax, c=some_data[3])

    ax.set_xlim(-.001, an_x_limit)
    ax.legend()
    plt.tight_layout()
    plt.close()

    return fig, ax

def scatter_plot_standard(data: list[tuple[pd.DataFrame, str, str]], file_name: str = 'scatter_plot_likelihood.jpg', report_meta: {} = None, title: 'str' = 'Title', show: bool = True) -> plt.Figure:
    """
    Generate standard scatter plots for the given data.

    This function generates scatter plots for each dataset provided in the input list. Each dataset is a tuple containing
    a DataFrame, a label, and a color. The scatter plots are plotted on the same figure.

    Parameters
    ----------
    data : list of tuple
        A list of tuples, where each tuple contains a DataFrame, a label, and a color. The DataFrame should contain the
        data to be plotted, the label is used for the legend, and the color specifies the color of the scatter plot.

    Returns
    -------
    plt.Figure
        A Matplotlib Figure object containing the scatter plots.

    Raises
    ------
    ValueError
        If the input data list is empty.
    """
    if not data:
        raise ValueError("The input data list is empty. Please provide valid data.")

    fig, ax = plt.subplots()

    # locate the ticks
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%m"))

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("\n%Y"))

    for some_data in data:
        sns.scatterplot(data=some_data[0], x='date', y=Y, marker='x', label=some_data[1], ax=ax, color=some_data[2])

    ax.legend()
    ax.set_title(title, loc='left')
    ax.set_xlabel('')
    plt.tight_layout()
    save_to = report_meta['resources']  + file_name
    plt.savefig(save_to, dpi=300)

    if show:
        plt.show()
        print(f'file saved to: {save_to}')
    else:
        print(f'file saved to: {save_to}')
        plt.close()

def boxplots_prior_likelihood(likelihood, grid_priors, report_meta: {} = None,
                              file_name: str = 'boxplots_observed_expected.jpeg', show=False):
    ecdfs = []
    chart_title = {
        'combined': "Expected combined",
        'out_boundary': "Expected out boundary",
        'in_boundary': "Expected in boundary",
        'observed': f'Observed {report_meta["name"]}'
    }
    # likelihood = firstdraft.survey_report.sample_results()
    llhood = likelihood[['pcs/m']]
    ecdfs.append([llhood, 'observed'])
    for a_prior in grid_priors:
        some_data = pd.DataFrame(grid_priors[a_prior]['dataframe'][0])
        ecdfs.append([some_data, a_prior])

    fig, axs = plt.subplots(1, len(ecdfs), figsize=(8, 5), sharey=True)

    for i, s_data in enumerate(ecdfs):

        sns.boxplot(data=s_data[0], y='pcs/m', ax=axs[i])
        axs[i].set_title(chart_title[s_data[1]], loc='left', fontsize=10)

        if i == 0:
            axs[i].set_xlabel('likelihood')
        else:
            axs[i].set_xlabel(f'Prior: {s_data[1]}')

    # ax.legend()
    plt.tight_layout()
    plt.savefig(f'{report_meta["resources"]}{file_name}', dpi=300)
    print(f'file saved to: {report_meta["resources"]}{file_name}')
    if show:
        plt.show()
    else:
        plt.close()
class SurveyReport:
    """
    The SurveyReport class is a container for the data and methods that are used to generate a report from a survey data set.

    The report is a summary of the data in the survey. The exact contents of the report should be defined by the stakeholders
    charged with the responsibility of interpreting the data. This has not happened. Therefore, this report is the byproduct
    of the calculations necessary to forecast values.

    Combined with the LandUseReport class, it is possible to describe the sampling conditions of a survey in a quantitative
    scale. Therefore, if the data in the report is a collection of like items, the report can be used to describe the
    concentration of the items per meter given the environmental conditions of the survey.

    Attributes
    ----------
    df : pd.DataFrame
        The DataFrame containing the survey data.

    Methods
    -------
    administrative_boundaries() -> tuple[pd.DataFrame, dict[str, np.ndarray]]
        Returns the name and number of unique Cantons and Cities in a report.
    feature_inventory() -> tuple[pd.DataFrame, dict[str, np.ndarray]]
        Returns the name and number of geographic boundaries in a report.
    date_range() -> dict
        The date range of the selected results.
    inventory() -> pd.DataFrame
        Returns the total quantity, median pcs/m, % of total and fail rate for each object code in the report.
    total_quantity() -> int
        Returns the total quantity of the report.
    number_of_samples() -> int
        Returns the number of unique sample_ids in the report.
    number_of_locations() -> int
        Returns the number of unique locations in the report.
    material_report() -> pd.DataFrame
        Generate a report on the material composition of the samples.
    fail_rate(threshold: int = 1) -> pd.DataFrame
        Calculate the fail rate for each object of interest.
    sample_results(df: pd.DataFrame = None, sample_id: str = index_label, labels: str = location_label,
                   info_columns: list[str] = None, afunc: dict = unit_agg) -> pd.DataFrame
        Calculate the sample totals by grouping the data based on sample ID, labels, and date.
    sampling_results_summary() -> pd.DataFrame
        Generate a summary of the sample totals.
    object_summary() -> pd.DataFrame
        Generate a summary of the object quantities and fail rates.
    """
    
    def __init__(self, dfc):
        self.df = dfc
        
    def administrative_boundaries(self) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
        """
        Returns the name and number of unique Cantons and Cities in a report.

        This method calculates the number of unique Cantons and Cities in the survey data and returns a DataFrame
        with the counts and a dictionary with the names of the unique Cantons and Cities.

        Returns
        -------
        tuple
            A tuple containing:
            - A DataFrame with the count of unique Cantons and Cities.
            - A dictionary with the names of the unique Cantons and Cities.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        result = {}
        boundary_names = {}
        for boundary in administrative:
            names = self.df[boundary].unique()
            boundary_names[boundary] = names
            if names.size == 0:
                result[boundary] = {'count': 0}
            else:
                result[boundary] = {'count': len(names)}
        result = pd.DataFrame(result).T

        return result, boundary_names

    def feature_inventory(self) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
        """
        Returns the name and number of geographic boundaries in a report.

        This method calculates the number of unique geographic boundaries (e.g., river basins, lakes, parks) in the survey data
        and returns a DataFrame with the counts and a dictionary with the names of the unique features.

        Returns
        -------
        tuple
            A tuple containing:
            - A DataFrame with the count of unique geographic boundaries.
            - A dictionary with the names of the unique geographic boundaries.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        result = {}
        feature_names = {}
        for feature_type in feature_types:
            unique_features = self.df[self.df['feature_type'] == feature_type]['feature_name'].unique()
            ftype_label = feature_type_labels[feature_type]
            feature_names[ftype_label] = unique_features
            if unique_features.size > 0:
                result[feature_type] = {'count': len(unique_features)}
        result = pd.DataFrame(result)
        result.rename(columns={'l': 'lake', 'r': 'river', 'p': 'park'}, inplace=True)

        return result, feature_names

    @property
    def date_range(self):
        """The date range of the selected results"""
        start = self.df['date'].min()
        end = self.df['date'].max()
        return {'start': start, 'end': end}

    def inventory(self):
        """Returns the total quantity, median pcs/m, % of total and fail rate for each object code in the report"""
        tq = self.total_quantity
        object_totals = self.df.groupby(object_of_interest).agg(agg_groups)
        object_totals['% of total'] = object_totals[Q]/tq
        
        return object_totals

    @property
    def total_quantity(self):
        """Returns the total quantity of the report"""
        return self.df[Q].sum()

    @property
    def number_of_samples(self):
        """Returns the number of unique sample_ids in the report"""
        return self.df[index_label].nunique()

    @property
    def number_of_locations(self):
        """Returns the number of unique locations in the report"""
        return self.df.location.nunique()

    @property
    def material_report(self) -> pd.DataFrame:
        """
        Generate a report on the material composition of the samples.

        This method calculates the material composition of the samples in the survey data. It groups the data by material,
        calculates the total quantity for each material, and returns a DataFrame with the percentage of the total for each material.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the percentage of the total for each material.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        inv = self.inventory()
        inv['material'] = inv.merge(session_config.code_material, right_index=True, left_index=True)['material']
        material_report = inv.groupby(['material']).quantity.sum()
        mr = material_report / sum(material_report)
        mr = (mr * 100).astype(int)
        mr = pd.DataFrame(mr[mr >= 1])
        mr['% of total'] = mr.quantity.apply(lambda x: f'{x}%')
        mr = mr[['% of total']]

        return mr

    def fail_rate(self, threshold: int = 1) -> pd.DataFrame:
        """
        Calculate the fail rate for each object of interest.

        This method calculates the fail rate for each object of interest in the survey data. The fail rate is defined as the
        number of samples where the quantity of the object is greater than or equal to the threshold, divided by the total
        number of samples for that object.

        Parameters
        ----------
        threshold : int, optional
            The quantity threshold to consider a sample as a fail. Default is 1.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the fail rate for each object of interest.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        rates = self.df.groupby([object_of_interest])[index_label].nunique().reset_index()
        for anobject in rates[object_of_interest].unique():
            nfails = sum((self.df[object_of_interest] == anobject) & (self.df[Q] >= threshold))
            n_anobject = rates.loc[rates[object_of_interest] == anobject, index_label].values[0]
            rates.loc[rates[object_of_interest] == anobject, ['fails', 'rate']] = [nfails, nfails / n_anobject]

        return rates.set_index(object_of_interest, drop=True)

    def sample_results(self, df: pd.DataFrame = None, sample_id: str = index_label, labels: str = location_label,
                   info_columns: list[str] = None, afunc: dict = unit_agg) -> pd.DataFrame:
        """
        Calculate the sample totals by grouping the data based on sample ID, labels, and date.

        This function groups the data by sample ID, labels, and date, and applies the aggregation function to calculate
        the sample totals. If additional information columns are provided, they are included in the grouping.

        Parameters
        ----------
        df : pd.DataFrame, optional
            The DataFrame containing the survey data. If not provided, the method uses the instance's DataFrame. Default is None.
        sample_id : str, optional
            The column name representing the sample ID. Default is `index_label`.
        labels : str, optional
            The column name representing the location labels. Default is `location_label`.
        info_columns : list of str, optional
            Additional columns to include in the grouping. Default is None.
        afunc : dict, optional
            The aggregation function to apply to the grouped data. Default is `unit_agg`.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the aggregated sample totals.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if df is None:
            df = self.df

        if df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        if not info_columns:
            return df.groupby([sample_id, labels, 'date'], as_index=False).agg(afunc)
        else:
            return df.groupby([sample_id, labels, 'date', *info_columns], as_index=False).agg(afunc)

    @property
    def sampling_results_summary(self) -> pd.DataFrame:
        """
        Generate a summary of the sample totals.

        This property calculates the summary of the sample totals, including total quantity, number of samples, average,
        quantiles, standard deviation, maximum value, and date range.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the summary of the sample totals.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        data = self.sample_results()[Y].values
        qtiles = np.quantile(data, report_quantiles)
        q_labels = {session_config.quantile_labels[i]: qtiles[i] for i in range(len(qtiles))}

        asummary = {
            'total': self.total_quantity,
            'nsamples': self.number_of_samples,
            'average': np.mean(data),
            **q_labels,
            'std': np.std(data),
            'max': self.sample_results()[Y].max(),
            'start': self.date_range['start'],
            'end': self.date_range['end']
        }
        result = pd.DataFrame(asummary.values(), index=list(asummary.keys()), columns=['result'])

        return result

    def object_summary(self) -> pd.DataFrame:
        """
        Generate a summary of the object quantities and fail rates.

        This method calculates the total quantity and fail rate for each object of interest in the survey data. It filters
        out objects with zero quantity, sorts the objects by quantity in descending order, and merges the fail rate data.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the summary of object quantities and fail rates.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        qtys = self.inventory()
        qtys = qtys[qtys[Q] > 0]
        qtys = qtys.sort_values(Q, ascending=False)
        qtys.rename(columns={index_label: 'nsamples'}, inplace=True)
        df = qtys.merge(self.fail_rate(), right_on=object_of_interest, left_on=object_of_interest)
        df = df.rename(columns={'rate': 'fail rate'})
        df.drop(columns=['fails'], inplace=True)
        return df

    

