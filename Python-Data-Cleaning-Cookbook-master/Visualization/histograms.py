# import pandas, matplotlib, and statsmodels
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
landtemps = pd.read_pickle("data/landtemps2019avgs.pkl")
covidtotals = pd.read_pickle("data/covidtotals720.pkl")

# show some of the temperature rows 
landtemps[['station','country','latabs','elevation','avgtemp']].sample(20)

# generate some descriptive statistics on the temperatures data
landtemps.describe()
landtemps.avgtemp.skew()
landtemps.avgtemp.kurtosis()

# plot temperature averages
plt.hist(landtemps.avgtemp)
plt.axvline(landtemps.avgtemp.mean(), color='red', linestyle='dashed', linewidth=1)
plt.title("Histogram of Average Temperatures (Celsius)")
plt.xlabel("Average Temperature")
plt.ylabel("Frequency")
plt.show()

# run a qq-plot to examine where the distribution deviates from a normal distribution
sm.qqplot(landtemps[['avgtemp']].sort_values(['avgtemp']), line='s')
plt.title("QQ Plot of Average Temperatures")
plt.show()

# show skewness and kurtosis for total_cases_pm
covidtotals.total_cases_pm.skew()
covidtotals.total_cases_pm.kurtosis()

# do a stacked histogram
showregions = ['Oceania / Aus','East Asia','Africa (other)','Western Europe']
plt.hist([covidtotals.loc[covidtotals.region=='Oceania / Aus'].total_cases_pm,\
  covidtotals.loc[covidtotals.region=='East Asia'].total_cases_pm,\
  covidtotals.loc[covidtotals.region=='Africa (other)'].total_cases_pm,\
  covidtotals.loc[covidtotals.region=='Western Europe'].total_cases_pm],\
  color=['blue','mediumslateblue','plum','mediumvioletred'],\
  label=showregions,\
  stacked=True)
plt.title("Stacked Histogram of Cases Per Million for Selected Regions")
plt.xlabel("Cases Per Million")
plt.ylabel("Frequency")
plt.xticks(np.arange(0, 22500, step=2500))
plt.legend()
plt.show()

# show multiple histograms on one figure
fig, axes = plt.subplots(2, 2)
fig.suptitle("Histograms of Covid Cases Per Million by Selected Regions")
axes = axes.ravel()

for j, ax in enumerate(axes):
  ax.hist(covidtotals.loc[covidtotals.region==showregions[j]].\
    total_cases_pm, bins=5)
  ax.set_title(showregions[j], fontsize=10)
  for tick in ax.get_xticklabels():
    tick.set_rotation(45)

plt.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()

temp = covidtotals.loc[covidtotals.region.isin(showregions)]
temp.shape
temp[['location','total_cases_pm']].sort_values('total_cases_pm')

