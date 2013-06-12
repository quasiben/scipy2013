import matplotlib.pyplot as plt
import pandas as pd

#read in pandas file pd.read_csv() and handle missing values. 
#use additional options parse_dates=[1] and index_col=1 (this appropriately loads
# dates as DateTime objects)
df = pd.read_csv('../data/CGM_DATA/CGM.csv',sep=',',parse_dates=[1],index_col=1,na_values='nil')
df = df.apply(pd.Series.interpolate)


#boolean selection of glucose lower than 180 and/& greater than 80
df['inrange'] = (df['glucose'] < 180) & (df['glucose'] > 80)

#rolling_sum
window = 30.5*288
inrange = pd.rolling_sum(df.inrange,window)
inrange = inrange.dropna()
inrange = inrange/float(window)

#plot
inrange.plot()
plt.show()

