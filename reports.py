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
            result.update({boundary: {'count': len(names), 'names': names}})
        
        return result

    def feature_inventory(self):
        """Returns the name and number of geographic boundaries in a report. River bassin, lake park etc"""
        result = {}
        for feature_type in feature_types:
            unique_features = self.df[self.df['feature_type'] == feature_type]['feature_name'].unique()
            if unique_features.size == 0:
                result[feature_type] = {
                    'count': 0,
                    'names': None
                }
            else:
                result[feature_type] = {
                    'count': len(unique_features),
                    'names': unique_features.tolist()
                }
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

    def material_report(self):
        inv = self.inventory()
        inv['material'] = inv.merge(session_config.code_material, right_index=True, left_index=True)['material']
        material_report = inv.groupby(['material']).quantity.sum()
        mr = material_report / sum(material_report)
        mr = (mr * 100).astype(int)
        mr = pd.DataFrame(mr[mr > 1])
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

        asummary = {
            'total':self.total_quantity,
            'nsamples': self.number_of_samples,
            'average': np.mean(data),
            'quantiles': qtiles,
            'std': np.std(data),
            'max':self.sample_results[Y].max(),
            'start': self.date_range['start'],
            'end': self.date_range['end']
        }

        return asummary

    def object_summary(self):
        qtys = self.inventory()
        return qtys.merge(self.fail_rate(), right_on=object_of_interest, left_on=object_of_interest)
    

