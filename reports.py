"""
reports.py
hammerdirt 2024
Author: Roger Erismann

NOTE: This module is a work in progress.

The SurveyReport class is a container for the data and methods that are used to generate a report from a survey data set.
The report is a summary of the data in the survey. The exact contents of the report should be defined by the stakeholders
charged with the responsibility of interpreting the data. This has not happened. Therefore, this report is the byproduct
of the calculations necessary to forecast values. The <userdisplay.py> module is how the report is displayed for evaluation
by stakeholders.

Combined with the LandUseReport class, it is possible to describe the sampling conditions of a survey in a quantitative
scale. Therefore, if the data in the report is a collection of like items, the report can be used to describe the
concentration of the items per meter given the environmental conditions of the survey.

The report contains the following information:
1. Administrative boundaries: the political boundaries of the data
2. Feature inventory: the use case of the survey location
3. Date range: the date range of the data
4. Inventory: quantity and % of total for each object code
5. Total quantity: the total quantity of the data
6. Number of samples: the number of unique samples in the data
7. Material report: the % of total for each material type
8. Fail rate: the rate of failure for each object code
9. Sample results: the sample totals for the date range of the data
10. Sampling results summary: the summary of the sample totals
11. Object summary: the quantity, fail rate and % of total for each object code
"""
import pandas as pd
import numpy as np

import session_config
from session_config import administrative, feature_types
from session_config import object_of_interest, palette, bin_labels, feature_variables
from session_config import index_label, location_label, Y, Q
from session_config import unit_agg, agg_groups
from session_config import report_quantiles


import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import seaborn as sns


import geospatial
from gridforecast import MulitnomialDirichlet, forecast_weighted_prior
from IPython.display import Markdown


def collect_sample_totals(df, sample_id: str = 'sample_id', labels: str = location_label,
                          info_columns: list = None, afunc: {} = unit_agg):
    # a sample total is the sum of all the codes with the same sample Id. The code column is identified
    # with the object_of_interest variable
    if not info_columns:
        return df.groupby([sample_id, labels, 'date'], as_index=False).agg(afunc)
    else:
        return df.groupby([sample_id, labels, 'date', *info_columns], as_index=False).agg(afunc)

def collect_the_most_common(df, a_fail_rate: float = 0.5, n_greatest: int = 10):
    a = df.sort_values('quantity', ascending=False).head(n_greatest).code.unique()

    b = df[df['rate'] >= a_fail_rate].code.unique()
    mc_codes = list({*a, *b})
    data = df[df.code.isin(mc_codes)]
    data = data.sort_values('quantity', ascending=False)
    mc_q = data.quantity.sum()
    pct_total = mc_q / df.quantity.sum()

    return data, mc_codes, pct_total

def make_report_objects(df):
    # make a survey report and a landuse report
    # from filtered data
    this_report = SurveyReport(dfc=df)

    # generate the parameters for the landuse report
    target_df = this_report.sample_results
    features = geospatial.collect_topo_data(locations=target_df.location.unique())

    # make a landuse report
    this_land_use = geospatial.LandUseReport(target_df, features)

    return this_report, this_land_use


def create_mask(data, query_params):
    # create a boolean mask for the data based on query parameters including date range.
    # initialize the mask to True for all rows
    mask = pd.Series([True] * len(data))

    for key, value in query_params.items():
        if key == 'date_range':
            start_date = pd.to_datetime(value['start'])
            end_date = pd.to_datetime(value['end'])
            mask &= (data['date'] >= start_date) & (data['date'] <= end_date)
        elif key in data.columns:
            mask &= (data[key] == value)
        else:
            raise KeyError(f"Key '{key}' not found in data columns")

    return mask

def filter_data(datai, query_params):
    # filter the data based on the query parameters including date range.

    if 'date' in datai.columns:
        datai['date'] = pd.to_datetime(datai['date'])
    else:
        raise KeyError("The dataframe does not contain a 'date' column ")

    # mask using the create_mask function
    mask = create_mask(datai, query_params)
    # Apply the mask to the dataframe
    filtered_data = datai[mask].copy()

    return filtered_data, filtered_data.location.unique()


def check_params(params, data):
    # check if the query parameters are valid and return the filtered data
    # and unique locations if the query is valid. Otherwise, return an error message.
    # and empty arrays.

    try:
        a, b = filter_data(data, query_params=params)
        if len(b) == 0:
            message = "No survey results found. "
            return [], [], message
        message = 'ok'
        return a, b, message

    except Exception as e:
        message = f"An error occurred: {str(e)}. Please check your query parameters and try again. "
        return [], [], message


def reports_and_forecast(likelihood_params: dict, prior_params: dict, ldata: pd.DataFrame):
    # utility function to make reports and forecasts. The function checks the likelihood and prior parameters
    # and returns the reports and forecasts if the parameters are valid. Otherwise, the function returns any available
    # reports and a boolean flag indicating that a forecast was not made.

    comments = ''
    make_forecast = True
    ldi, l_locations, c = check_params(likelihood_params, ldata.copy())
    comments += f' {c}'
    if c != 'ok':
        make_forecast = False
        this_report, this_land_use = 'No likelihood', 'No likelihood'
    else:
        this_report, this_land_use = make_report_objects(ldi)
    pdf, p_locations, c = check_params(prior_params, ldata.copy())
    comments += f' {c}'
    if c != 'ok':
        make_forecast = False
        prior_report, prior_land_use = 'No prior', 'No prior'
    else:
        prior_report, prior_land_use = make_report_objects(pdf)

    if make_forecast:
        prr = prior_report.sample_results.groupby('sample_id')['pcs/m'].sum()

        lkl = this_report.sample_results.groupby('sample_id')['pcs/m'].sum()
        max_range = np.quantile(lkl.values, .99)

        # consider all values
        i = MulitnomialDirichlet('max value', prr, lkl)

        # limit to the 99th percentile
        limited = lkl[lkl <= max_range]
        h  = MulitnomialDirichlet('99th percentile', limited, prr)
        comments += c
    else:
        i = 'no forecast'
        h = 'no forecast'
        comments += 'No forecast was made.'
    results = dict(
        this_report=this_report,
        this_land_use=this_land_use,
        prior_report=prior_report,
        prior_land_use=prior_land_use,
        posterior_no_limit=i,
        posterior_99=h,
        comments=comments
    )

    return results


def admin_report(data, admin_boundary):
    d = data.groupby(admin_boundary).agg({'pcs/m': 'mean', 'quantity': 'sum', 'sample_id': 'nunique'})
    return d


def features_present(data, a_feature_inventory):
    ftypes = a_feature_inventory.gt(0).apply(lambda x: x.index[x].tolist(), axis=1)

    ftypes = [x[0] for x in ftypes]

    summardata = data.groupby(['sample_id', 'feature_type', 'feature_name'], as_index=False).agg(
        {'pcs/m': 'sum', 'quantity': 'sum'})

    feature_individual_summary = summardata.groupby(['feature_type', 'feature_name'], as_index=False).agg(
        {'sample_id': 'nunique', 'pcs/m': 'mean', 'quantity': 'sum'})
    results = {}
    for features in ftypes:
        d = feature_individual_summary[feature_individual_summary.feature_type == features[0]].copy()
        results[features] = d[['feature_name', 'sample_id', 'pcs/m', 'quantity']]

    return results


def histograms_standard(data):
    fig, ax = plt.subplots()

    for some_data in data:
        sns.histplot(data=some_data[0], x='pcs/m', stat='probability', label=some_data[1], ax=ax, color=some_data[2])
    ax.legend()
    plt.tight_layout()

    plt.close()

    return fig


def ecdf_plots_standard(data):
    fig, ax = plt.subplots()
    an_x_limit = 0
    for some_data in data:

        this_max = np.quantile(some_data[0], .8)
        if this_max > an_x_limit:
            an_x_limit = this_max
        sns.ecdfplot(some_data[0], label=some_data[1], ls=some_data[2], ax=ax, c=some_data[3], zorder=1)

    ax.set_xlim(-.1, an_x_limit)
    ax.legend()
    plt.tight_layout()
    plt.close()
    return fig


# title = f'All samples {canton}: {prior_dates["start"]} - {o_dates["end"]}'
def scatter_plot_standard(data):
    fig, ax = plt.subplots()

    # locate the ticks
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%m"))

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("\n%Y"))

    for some_data in data:
        sns.scatterplot(data=some_data[0], x='date', y='pcs/m', marker='x', label=some_data[1], ax=ax,
                        color=some_data[2])

    ax.legend()
    ax.set_xlabel('')
    plt.tight_layout()
    plt.close()

    return fig


def labels_for_display(args):
    start = args['date_range']['start'][:4]
    end = args['date_range']['end'][:4]
    labels = f"{start} - {end}"
    return labels


def make_standard_report(results, args):
    # data for plots
    observedvals = []
    forecasts = []

    display_results = [
        'weighted-forecast',
        'observed-max-forecast',
        'observed-99-forecast',
        'proportion-most-common',
        'most-common-objects',
        'sampling-summary',
        'prior-sampling-summary',
        'observed-values',
        'forecasted-values',
        'likelihood-labels',
        'prior-labels']

    display_r = {x: 'No data' for x in display_results}

    # make the labels for display
    likelihood_labels = labels_for_display(args['likelihood'])
    prior_labels = labels_for_display(args['prior'])

    l_summary = results['this_report'].sampling_results_summary.copy()

    # most common objects the likelihood data
    object_inventory = results['this_report'].object_summary()
    object_inventory.reset_index(drop=False, inplace=True)
    most_common_objects, mc_codes, proportions = collect_the_most_common(object_inventory)
    # most_common_objects = most_common_objects.set_caption("")
    ratio_most_common = Markdown(f'__The most common objects account for {int(proportions * 100)}% of all objects__')

    observedvals.append((results['this_report'].sample_results[['pcs/m']], likelihood_labels, palette['likelihood']))
    weighted_args = [
        results['this_land_use'].n_samples_per_feature(),
        args['land-use-inventory'],
        bin_labels,
        feature_variables,
        results['this_report'].sample_results['pcs/m']
    ]
    weighted_forecast, weighted_posterior, weighted_summary, selectedr = forecast_weighted_prior(*weighted_args,
                                                                                                 ncols=1)

    forecasts.append((weighted_forecast, 'weighted prior', '-.', 'black'))
    forecasts.append((results['this_report'].sample_results[['pcs/m']], likelihood_labels, '-', palette['likelihood']))

    display_r.update({
        'proportion-most-common': ratio_most_common,
        'most-common-objects': most_common_objects,
        'sampling-summary': l_summary,
        'likelihood-labels': likelihood_labels,
        'weighted-forecast': weighted_summary,
        'observed-values': observedvals
    })
    if results['prior_report'] == 'No prior':
        # print('no prior')
        # print(observedvals)

        # make the display text
        header = f"<font color=#daa520>{prior_labels}</font>"
        info = '* No data for the period requested\n'
        sampling_summary = Markdown(f'{header}\n{info}')
        forecast_maxval = Markdown('__Given the observed max__\n* No prior data to consider see weighted prior\n')
        forecast_99 = Markdown('__Given the observed 99__\n* No prior data to consider see weighted prior\n')

        # update display object
        display_r.update({
            'prior-sampling-summary': sampling_summary,
            'prior-labels': prior_labels,
            'observed-max-forecast': forecast_maxval,
            'observed-99-forecast': forecast_99,
            'forecasted-values': forecasts
        })

    else:

        p_summary = results['prior_report'].sampling_results_summary

        observedvals.append((results['prior_report'].sample_results[['pcs/m']], prior_labels, palette['prior']))
        forecasts.append((results['prior_report'].sample_results[['pcs/m']], prior_labels, ':', palette['prior']))

        forecast_maxval = results['posterior_no_limit'].get_descriptive_statistics()
        forecast_99 = results['posterior_99'].get_descriptive_statistics()

        forecasts.append((results['posterior_99'].posterior_samples, 'expected 99th', '-', 'blue'))
        forecasts.append((results['posterior_no_limit'].posterior_samples, 'observed max', ':', 'red'))

        display_r.update({
            'prior-sampling-summary': p_summary,
            'prior-labels': prior_labels,
            'observed-max-forecast': forecast_maxval,
            'observed-99-forecast': forecast_99,
            'observed-values': observedvals,
            'forecasted-values': forecasts

        })

    return display_r


class SurveyReport:
    
    def __init__(self, dfc):
        self.df = dfc
        
    def administrative_boundaries(self):
        """Returns the name and number of unique Cantons and Cities in a report"""
        result = {}
        for boundary in administrative:
            names = self.df[boundary].unique()
            if names.size == 0:
                result[boundary] = {'count': 0}
            else:
                result[boundary] = {'count': len(names)}
        result = pd.DataFrame(result).T
        
        return result

    def feature_inventory(self):
        """Returns the name and number of geographic boundaries in a report. River bassin, lake park etc"""
        result = {}
        for feature_type in feature_types:
            unique_features = self.df[self.df['feature_type'] == feature_type]['feature_name'].unique()
            if unique_features.size > 0:
                result[feature_type] = {'count': len(unique_features)}
        result = pd.DataFrame(result)
        result.rename(columns={'l': 'lake', 'r': 'river', 'p': 'park'}, inplace=True)

        return result

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
        return self.df.sample_id.nunique()

    @property
    def material_report(self):
        inv = self.inventory()
        inv['material'] = inv.merge(session_config.code_material, right_index=True, left_index=True)['material']
        material_report = inv.groupby(['material']).quantity.sum()
        mr = material_report / sum(material_report)
        mr = (mr * 100).astype(int)
        mr = pd.DataFrame(mr[mr >= 1])
        mr['% of total'] = mr.quantity.apply(lambda x: f'{x}%')
        mr = mr[['% of total']]

        return mr

    def fail_rate(self, threshold: int = 1):
        rates = self.df.groupby([object_of_interest])[index_label].nunique().reset_index()
        for anobject in rates[object_of_interest].unique():
            nfails = sum((self.df[object_of_interest] == anobject) & (self.df[Q] >= threshold))
            n_anobject = rates.loc[rates[object_of_interest] == anobject, index_label].values[0]
            rates.loc[rates[object_of_interest] == anobject, ['fails', 'rate']] = [nfails, nfails/n_anobject]

        return rates.set_index('code', drop=True)

    @property
    def sample_results(self, df: pd.DataFrame = None, **kwargs):
        """The sample totals for the date range of the selected results"""

        if not df:
            return collect_sample_totals(self.df.copy(), **kwargs)
        else:
            return collect_sample_totals(df.copy(), **kwargs)

    @property
    def sampling_results_summary(self):
        """The summary of the sample totals"""

        data = self.sample_results[Y].values
        qtiles = np.quantile(data, report_quantiles)
        q_labels = {session_config.quantile_labels[i]: qtiles[i] for i in range(len(qtiles))}

        asummary = {
            'total':self.total_quantity,
            'nsamples': self.number_of_samples,
            'average': np.mean(data),
            **q_labels,
            'std': np.std(data),
            'max':self.sample_results[Y].max(),
            'start': self.date_range['start'],
            'end': self.date_range['end']
        }
        result = pd.DataFrame(asummary.values(), index=list(asummary.keys()), columns=['result'])

        return result

    def object_summary(self):
        qtys = self.inventory()
        return qtys.merge(self.fail_rate(), right_on=object_of_interest, left_on=object_of_interest)
    

