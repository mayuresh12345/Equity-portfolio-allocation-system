import read_data
from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
import numpy as np
from scipy.cluster.vq import kmeans,vq
import pandas_datareader as dr
from math import sqrt
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

closing_prices = []
df = pd.DataFrame()
for i in range(len(read_data.tickers)):
    try:
        closing_prices = dr.DataReader(read_data.tickers[i],'yahoo','01/01/2016')['Close']
        prices = pd.DataFrame(closing_prices)
    except:
        pass
    df = pd.concat(closing_prices,axis=1)
df.sort_index(inplace=True)

#Calculating returns, volatilties
returns = pd.DataFrame(df.pct_change().mean() * 756)
df.columns = ['Returns']
df['Volatility'] = df.pct_change().std()
data = np.expand_dims([np.array(returns['Returns']),np.asarray(returns['Volatility'])]).T

for i in range(len(data['close'])):
    if data.iloc[i]['close'] == np.isnan():
        data = data.drop(data.iloc[i]['close'])

kms = []
for k in range(1, 12):
    km = KMeans(n_clusters=k)
    km.fit(k)
    kms.append(km.inertia_)
    
plt.plot(range(1, 12), kms)
plt.grid()

# Clusters for 11 sectors

centroids,_ = kmeans(km, 11)
new_data = vq(df, centroids)
plt.scatter(x[0,0],x[0,1],c='red',label='Communication Services')
plt.scatter(x[1,0],x[1,1],c='blue',label='Energy')
plt.scatter(x[2,0],x[2,1],c='green',label='Consumer Discretionary')
plt.scatter(x[3,0],x[3,1],c='cyan',label='Industrials')
plt.scatter(x[4,0],x[4,1],c='black',label='Utilities')
plt.scatter(x[5,0],x[5,1],c='olive',label='Information Technology')
plt.scatter(x[6,0],x[6,1],c='brown',label='Financials')
plt.scatter(x[7,0],x[7,1],c='pink',label='Consumer Staples')
plt.scatter(x[8,0],x[8,1],c='purple',label='Materials')
plt.scatter(x[9,0],x[9,1],c='white',label='Real Estate')
plt.scatter(x[10,0],x[10,1],c='gray',label='Health Care')
plt.title('Clustering according to sectors', fontsize=12, fontweight="bold")
plt.imsave('Figs//sectorwise_cluster.jpg')

# Save histograms

x = industry_list
y = [km.predict(x[0,0]).shape[0], km.predict(x[1,0]).shape[0], km.predict(x[2,0]).shape[0], km.predict(x[3,0]).shape[0], km.predict(x[4,0]).shape[0], km.predict(x[5,0]).shape[0]],
km.predict(x[6,0]).shape[0], km.predict(x[7,0]).shape[0], km.predict(x[8,0]).shape[0], km.predict(x[9,0]).shape[0], km.predict(x[10,0]).shape[0]
plt.bar(x, y)
plt.xticks(rotation=90)
plt.title('K-Means clustering histogram', fontsize=12, fontweight="bold")
plt.xlabel('Sectors')
plt.ylabel('No of stocks')
plt.imsave('Figs//distribution.jpg')