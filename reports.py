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
from session_config import object_of_interest
from session_config import index_label, location_label, Y, Q
from session_config import unit_agg, agg_groups
from session_config import report_quantiles


def collect_sample_totals(df, sample_id: str = 'sample_id', location_label: str = location_label,
                          info_columns: list = None, afunc: {} = unit_agg):
    # a sample total is the sum of all the codes with the same sample Id. The code column is identified
    # with the object_of_interest variable
    if not info_columns:
        return df.groupby([sample_id, location_label, 'date'], as_index=False).agg(afunc)
    else:
        return df.groupby([sample_id, location_label, 'date', *info_columns], as_index=False).agg(afunc)


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
        result = pd.DataFrame(result)
        
        return result

    def feature_inventory(self):
        """Returns the name and number of geographic boundaries in a report. River bassin, lake park etc"""
        result = {}
        for feature_type in feature_types:
            unique_features = self.df[self.df['feature_type'] == feature_type]['feature_name'].unique()
            if unique_features.size == 0:
                result[feature_type] = {'count': 0}
            else:
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
        mr = mr[['% of total']].T

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
        result = pd.DataFrame([asummary])

        return result

    def object_summary(self):
        qtys = self.inventory()
        return qtys.merge(self.fail_rate(), right_on=object_of_interest, left_on=object_of_interest)
    

