# +
import numpy as np 
import pandas as pd
import random

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

from scipy import stats
from scipy.stats import chi2_contingency, norm 
import researchpy as rp

from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.proportion import proportion_confint
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import optuna

import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

# -

def plot_bars(data,y,y_label,title):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=data.index, y=y,
            data=data, 
            errorbar="sd", color = sns.color_palette()[1]).set(title=title)
    plt.xticks(rotation=90)
    ax.bar_label(ax.containers[0])
    ax.set_ylabel(y_label)
    ax.set_xlabel("")
    plt.show()


def check_missing_values(file):
    check = numpy.where(file.isnull())
    check = pd.DataFrame(check)
    for i in range(len(check.iloc[0,:])):
        print(f'missing value in the row {check.iloc[0,i]} of the column {check.iloc[1,i]}.')
    print(f'The total number of missing values is: {len(check.axes[1])}')

def find_outliers(dataframe,x,coef):
    '''
    The function to find outliers in numerical variables on the basis of IQR rule
    '''
    count_lower = []    
    count_upper = []
    Q1 = dataframe.iloc[:,x].quantile(0.25)
    Q3 = dataframe.iloc[:,x].quantile(0.75)
    IQR = Q3 - Q1
    lower_lim = Q1 - coef*IQR
    upper_lim = Q3 + coef*IQR
    for data in range(len(dataframe.iloc[:,0])):
        if dataframe.iloc[data,x] < lower_lim:
            count_lower.append(data)
        elif dataframe.iloc[data,x] > upper_lim:
            count_upper.append(data)
    print(f'The number of lower outliers is:{len(count_lower)},\
    The number of upper outliers is :{len(count_upper)}')

def stacked_bars(file, title_label, title):
    ax = file.plot(kind="barh", stacked=True, rot=0)
    ax.legend(title=title_label, bbox_to_anchor=(1, 1.02),
             loc='upper left')
    plt.xlabel("")
    plt.xticks(rotation = "vertical")
    plt.xlabel("%")
    for c in ax.containers:
        ax.bar_label(c, label_type='center')
    plt.title(title)
    plt.show()

def chi_square_test(data, confidence, variable):
    stat, p, dof, expected = stats.chi2_contingency(data)
    alpha = 1 - confidence
    print('')
    print(f'Pearson chi square test:{stat.round(3)}')
    print('')
    print(f'P_value: {p.round(3)}')
    return p
