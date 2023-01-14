import matplotlib.pyplot as plt
import cluster
import rolling_windows
from cluster import x
x = rolling_windows.getTimePeriod(['2019-03-31', '2019-06-30', '2019-09-30', '2019-12-31', '2020-03-31', '2020-06-30', '2020-09-30', '2020-12-31'])
y = cluster.kmeans.predict([x[0,0], x[1,0], x[2,0], x[3,0], x[4,0], x[5,0], x[7,0]])
plt.plot(x, y, label='min-variance')
plt.xticks([x[0,0], x[1,0], x[2,0], x[3,0], x[4,0], x[5,0], x[7,0]], ['2019-03-31', '2019-06-30', '2019-09-30', '2019-12-31', '2020-03-31', '2020-06-30', '2020-09-30', '2020-12-31'], rotation=90)

x = rolling_windows.getTimePeriod(['2019-03-31', '2019-06-30', '2019-09-30', '2019-12-31', '2020-03-31', '2020-06-30', '2020-09-30', '2020-12-31'])
y = cluster.kmeans.predict([x[0,0], x[1,0], x[2,0], x[3,0], x[4,0], x[5,0], x[7,0]])
plt.plot(x1, y1, label='mean-variance')
plt.xticks([1,2,3,4,5,6,7,8], ['2019-03-31', '2019-06-30', '2019-09-30', '2019-12-31', '2020-03-31', '2020-06-30', '2020-09-30', '2020-12-31'], rotation=90)

x = rolling_windows.getTimePeriod(['2019-03-31', '2019-06-30', '2019-09-30', '2019-12-31', '2020-03-31', '2020-06-30', '2020-09-30', '2020-12-31'])
y = cluster.kmeans.predict([x[0,0], x[1,0], x[2,0], x[3,0], x[4,0], x[5,0], x[7,0]])
plt.plot(x2, y2, label='S&P 500')
plt.xticks([1,2,3,4,5,6,7,8], ['2019-03-31', '2019-06-30', '2019-09-30', '2019-12-31', '2020-03-31', '2020-06-30', '2020-09-30', '2020-12-31'], rotation=90)
plt.legend()

plt.imsave('Figs//backtest.jpg')