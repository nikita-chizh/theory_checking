import pandas as pd
import numpy as np
from pylab import rcParams
import os
import matplotlib.pyplot as plt
import seaborn as sns

cwd = os.getcwd()
plots_fir = cwd + "/plots/"
df = pd.read_csv(cwd + "/filtered.csv", index_col=0)
rcParams['figure.figsize'] = 7, 10
df.info()
def trivial_sum_plot(df, colname_x, colname_y, fname, mean):
    max_rubric = df[colname_x].max()
    avg_time_for_vis = pd.concat([df[[colname_x]], df[[colname_y]]], axis=1)
    if mean:
        avg_time_for_vis = avg_time_for_vis.groupby('rubric_id').mean()
    else:
        avg_time_for_vis = avg_time_for_vis.groupby('rubric_id').sum()
    avg_time_for_vis.plot(style=".", xticks=[x for x in range(1, max_rubric) if x % 3 == 0], grid=True)
    plt.savefig(plots_fir + "/" + fname)

trivial_sum_plot(df,"rubric_id","Avg. Time on Page", "time_rid_mean.png", mean=True)
trivial_sum_plot(df,"rubric_id","Pageviews", "views_rid_mean.png", mean=True)
trivial_sum_plot(df,"rubric_id","Percent Scrolls", "scrolls_rid_mean.png", mean=True)
#
trivial_sum_plot(df,"rubric_id","Avg. Time on Page", "time_rid.png", mean=False)
trivial_sum_plot(df,"rubric_id","Pageviews", "views_rid.png", mean=False)
trivial_sum_plot(df,"rubric_id","Percent Scrolls", "scrolls_rid.png", mean=False)
