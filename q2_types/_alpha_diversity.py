# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os.path

import pandas as pd
from qiime.plugin import SemanticType

from .plugin_setup import plugin


AlphaDiversity = SemanticType('AlphaDiversity')


def validator(data_dir):
    raise NotImplementedError()


def alpha_diversity_to_pandas_series(data_dir):
    with open(os.path.join(data_dir, 'alpha-diversity.tsv'), 'r') as fh:
        # Since we're wanting to round-trip with pd.Series.to_csv, the pandas
        # docs recommend using from_csv here (rather than the more commonly
        # used pd.read_csv).
        return pd.Series.from_csv(fh, sep='\t', header=0)


def pandas_series_to_alpha_diversity(view, data_dir):
    with open(os.path.join(data_dir, 'alpha-diversity.tsv'), 'w') as fh:
        view.to_csv(fh, sep='\t', header=True)


plugin.register_data_layout('alpha-diversity', 1, validator)

plugin.register_data_layout_reader('alpha-diversity', 1, pd.Series,
                                   alpha_diversity_to_pandas_series)

plugin.register_data_layout_writer('alpha-diversity', 1, pd.Series,
                                   pandas_series_to_alpha_diversity)

plugin.register_semantic_type(AlphaDiversity)

plugin.register_type_to_data_layout(AlphaDiversity, 'alpha-diversity', 1)