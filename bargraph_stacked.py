#! /bin/python


# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# import mpld3

import matplotlib.ticker as mtick
from matplotlib import rc



def create_plot(data_percentage, data_quantities):
    fig2, ax2 = plt.subplots()
    # cross_tab_prop = pd.crosstab(index=data['release_year'],
    # cross_tab_prop = pd.crosstab(index=data['Budget'],
    #                              columns=data[['Income', 'Reserve']],
    #                              normalize='index')
    cross_tab_prop = data_percentage
    cross_tab_prop.index.name = None
    cross_tab_prop.plot(
        kind='bar',
        stacked=True,
        colormap='tab10',
        figsize=(5, 5))
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center',
        ncol=2, borderaxespad=0, title = 'Cashflow Dashboard',
        title_fontsize = 'xx-large',
        frameon = False)
    for n, x in enumerate([*cross_tab_prop.index.values]):
        for (proportion, y_loc) in zip(
                cross_tab_prop.loc[x],
                cross_tab_prop.loc[x].cumsum()):
            # plt.text(x=n - 0.17,
            plt.text(x=n - 0.20,
                # y=(y_loc - proportion) + (proportion / 2 ), # Position of percentag
                # y=(proportion), # Position of percentag
                y = y_loc - 150,
                # s='${:,.2f}'.format(np.round(proportion, 12)),
                s='${:,.2f}'.format(proportion),
                color='yellow',
                fontsize=9,
                fontweight='bold')
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()
    return plt

graph_income_expense = create_plot(data_sandbox_proportions, data_sandbox_quantities)
data_sandbox_budget.rename('Budget', inplace=True)
plt = create_plot(data_sandbox_budget)
plt.show()
