from IPython.display import Markdown
from session_config import bin_labels, feature_variables, palette
from gridforecast import forecast_weighted_prior
from reports import collect_the_most_common

import numpy as np


import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import seaborn as sns




def admin_report(data, admin_boundary):
    d = data.groupby(admin_boundary).agg({'pcs/m':'mean', 'quantity':'sum', 'sample_id':'nunique'})
    return d

def features_present(data, a_feature_inventory):
    feature_types = a_feature_inventory.gt(0).apply(lambda x: x.index[x].tolist(), axis=1)
    
    feature_types = [x[0] for x in feature_types]

    summardata = data.groupby(['sample_id', 'feature_type','feature_name'], as_index=False).agg({'pcs/m':'sum', 'quantity':'sum'})
    
    feature_individual_summary = summardata.groupby(['feature_type','feature_name'], as_index=False).agg({'sample_id':'nunique', 'pcs/m':'mean', 'quantity':'sum'})
    results = {}
    for features in feature_types:
        
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
        
        this_max = np.quantile(some_data[0], .99)
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
        sns.scatterplot(data=some_data[0], x='date', y='pcs/m', marker='x', label=some_data[1], ax=ax, color=some_data[2])
    
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
    ratio_most_common = Markdown(f'__The most common objects account for {int(proportions*100)}% of all objects__')

    observedvals.append((results['this_report'].sample_results[['pcs/m']], likelihood_labels, palette['likelihood']))
    weighted_args = [
        results['this_land_use'].n_samples_per_feature(), 
        args['land-use-inventory'],
        bin_labels,
        feature_variables,
        results['this_report'].sample_results['pcs/m']
    ]
    weighted_forecast, weighted_posterior, weighted_summary, selectedr = forecast_weighted_prior(*weighted_args, ncols=1)
    
    forecasts.append((weighted_forecast, 'weighted prior', '-.', 'black'))
    forecasts.append((results['this_report'].sample_results[['pcs/m']], likelihood_labels, '-',palette['likelihood']))
    
    display_r.update({
        'proportion-most-common' : ratio_most_common,
        'most-common-objects' : most_common_objects,
        'sampling-summary' : l_summary,
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
        forecast_maxval =  Markdown('__Given the observed max__\n* No prior data to consider see weighted prior\n')
        forecast_99 = Markdown('__Given the observed 99__\n* No prior data to consider see weighted prior\n')
        
                
        # update display object
        display_r.update({
            'prior-sampling-summary' : sampling_summary,
            'prior-labels': prior_labels,
            'observed-max-forecast': forecast_maxval,
            'observed-99-forecast' : forecast_99,
            'forecasted-values': forecasts
        })

    else:
        
        p_summary = results['prior_report'].sampling_results_summary
        
        
        observedvals.append((results['prior_report'].sample_results[['pcs/m']], prior_labels, palette['prior']))
        forecasts.append((results['prior_report'].sample_results[['pcs/m']], prior_labels, ':',palette['prior']))
        
        forecast_maxval = results['posterior_no_limit'].get_descriptive_statistics()        
        forecast_99 = results['posterior_99'].get_descriptive_statistics()
        
        forecasts.append((results['posterior_99'].posterior_samples, 'expected 99th', '-', 'blue'))
        forecasts.append((results['posterior_no_limit'].posterior_samples, 'observed max', ':', 'red'))
        
        display_r.update({
            'prior-sampling-summary' : p_summary,
            'prior-labels': prior_labels,
            'observed-max-forecast': forecast_maxval,
            'observed-99-forecast' : forecast_99,
            'observed-values': observedvals,
            'forecasted-values': forecasts
            
        })

    return display_r
    

