#! /bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib import rc

print('---------------')
print('[ Example Data ]')

data = pd.read_csv('./data/netflix_titles.csv')

data = data.loc[data['release_year'].isin([*range(2017, 2020)]), ['type', 'release_year']].copy()
data.dropna(inplace=True)
data['release_year'] = data['release_year'].astype('int')

cross_tab_prop = pd.crosstab(index=data['release_year'],
                             columns=data['type'],
                             normalize='index')

cross_tab = pd.crosstab(index=data['release_year'],
                        columns=data['type'])

print('\n---------------')
print('data:\n')
print(data)
print('\n---------------')
print('cross_tab_prop:\n')
print(cross_tab_prop)
print('\n---------------')
print('cross_tab:')
print(cross_tab)


def create_plot(data):
    cross_tab_prop = pd.crosstab(index=data['release_year'],
                                 columns=data['type'],
                                 normalize='index')

    cross_tab_prop.index.name = None


    cross_tab = pd.crosstab(index=data['release_year'],
                            columns=data['type'])


    cross_tab_prop.plot(kind='bar',
                        stacked=True,
                        colormap='tab10',
                        figsize=(5, 5))

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center',
               ncol=2, borderaxespad=0, title = 'Cashflow Dashboard',
               title_fontsize = 'xx-large',
               frameon = False)

    # for n, x in enumerate([*cross_tab.index.values]):
    for n, x in enumerate([*cross_tab_prop.index.values]):
        print('n: {}'.format(n))
        print('x: {}'.format(x))
        for (proportion, y_loc) in zip(cross_tab_prop.loc[x],
                                       cross_tab_prop.loc[x].cumsum()):
            print('cross_tab_prop: {}'.format(cross_tab_prop))
            print('proportion: {}'.format(proportion))
            print('y_loc: {}'.format(y_loc))

            plt.text(x=n - 0.17,
                     y=(y_loc - proportion) + (proportion / 2 ), # Position of percentag
                     # y=(y_loc- proportion) + (proportion - 30 ),
                     # ax.bar_label(p, label_type='center'),
                     s=f'{np.round(proportion * 100, 1)}%',
                     color='yellow',
                     fontsize=9,
                     fontweight='bold')
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    # plt.set_title('Contour plot of Delaunay triangulation')
    # plt.title(label=None)
    # plt.title(label='Title')
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()

    return plt

plt = create_plot(data)
plt.show()
