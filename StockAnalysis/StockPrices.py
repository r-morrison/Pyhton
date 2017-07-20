# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:09:51 2017

@author: rorym
"""

from pandas_datareader import data
import pandas as pd
import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style
    
style.use('ggplot')

# Define date range
start_date = start=datetime.datetime(2010,1,1)
end_date = end=datetime.date.today()

# Load data from google
stock_data = data.DataReader('AMZN', 'google', start_date, end_date)

# Data to plot
close_price = stock_data['Close']    
moving_average = close_price.rolling(window=100).mean()

# Create charts
mpl.rc('figure', figsize = (8,7))

close_price.plot(label = 'Apple')
moving_average.plot(label = 'Moving Average')
plt.legend()

# Correlations between tech companies
stock_data_corrs = data.DataReader(['AAPL','MSFT', 'GOOGL', 'AMZN'], 'google', start_date, end_date)['Close']

# Percentage change matrix
pcc_comp = stock_data_corrs.pct_change()

# Percentage change correlation
pcc_corr = pcc_comp.corr()

# Scatter plot - Microsoft vs Apple
plt.scatter(stock_data_corrs.AAPL, stock_data_corrs.MSFT)
plt.xlabel('Apple')
plt.ylabel('Microsoft')

# KDE Scatter plot
pd.scatter_matrix(pcc_comp, diagonal = 'kde', figsize = (10,10))

# Heatmap scatter plot
plt.imshow(pcc_corr, cmap = 'hot', interpolation = 'none')
plt.colorbar()
plt.xticks(range(len(pcc_corr)), pcc_corr.columns)
plt.yticks(range(len(pcc_corr)), pcc_corr.columns)