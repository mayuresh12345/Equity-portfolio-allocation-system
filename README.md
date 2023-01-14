
# Equity portfolio allocation system 

**Contributors** <br />

Mayuresh Wagh - mwagh@buffalo.edu <br />
Manpreet Ajmani - majmani@buffalo.edu <br />
Prapti Miglani - praptimi@buffalo.edu <br />
Hemanth Gorla - hgorla@buffalo.edu <br />


**Objective** <br />

The project's goal is to suggest a mechanism for allocating stocks to portfolios. To do this, we first used the K-Means algorithm to group S&P 500 stocks into several sectors, and we used stock’s close price to feed the distance metric. Then, in order to forecast stock prices for four different rolling time frames, we trained three different regression-based algorithms: Linear Regression, Ridge Regression, and Random Forest. The following step entails determining the optimal regression algorithm for each window using the test data's Mean Squared Error before settling on the method that provides the highest support out of the four chosen rolling windows. The chosen regression model will then be used to choose the top 20% of stocks from each sector with the highest anticipated returns. The next step is to choose the top 20% of companies from a diversified population of stocks from various sectors in an equitable distribution using portfolio allocation algorithms like mean-variance and min-variance. The results of our back testing of the stocks chosen by our algorithm are compared to the S&P 500 outcomes as well as the portfolio value and Sharpe Ratio for each of the ways of portfolio allocation.

**Financial Indicators:**

● <ins>Volume Traded:</ins> - Volume of trade is the quantity of shares traded in total for the specified security during a trading day. Volume trade is measured on stocks, bonds, ETFs, options, etc.

● EPS: - The ratio of a company’s net profit to the number of outstanding shares is known as Earnings per share (EPS). The higher the EPS the more profitable a company is.

● P/E: - The ratio of a company’s share price to the earnings per share is known as price-to-earnings (P/E) ratio.

**Proposed methodology**

● Clustering stocks according to sectors using K-means

● Training three regression-based algorithms namely – Linear Regression, Ridge

Regression, Random Forest for predicting stock prices for different rolling windows

● Selecting best regression algorithm for that quarter using Mean Squared Error for

each rolling window

● Selecting best algorithm from the 4 selected rolling windows

● Picking top 20% stocks with maximum predicted returns from each sector using the

selected regression algorithm

● Recommending and comparing stocks for the next quarter from 11 sectors using

portfolio allocation strategies like min-variance and mean-variance

● Comparing, back testing and selecting allocation strategy based on overall portfolio

value and Sharpe Ratio





**Dataset**

Yahoo Finance

● Daily data over a five-year period starting from Jan 2016 to Dec 2020.

● Features considered for clustering algorithm – Closing price

● Features considered for regression algorithm – EPS, P/E and volume traded

**Algorithms Used for Proposed Methodology**

**K-Means Clustering:**

\1. The algorithm is centroid-based, and sample data points are assigned to the

clusters that are closest to the cluster centroid.

\2. Reducing the overall distance between each point and its matching cluster

centroid is the main objective of the K-Means method.

\3. Choosing k, or the number of clusters, is the first stage in the procedure. In

the project, we have chosen k to be 11, the number of various stock sectors.

\4. Next, the centroids of k randomly chosen data sample points are chosen, and

for each of the k centroids, a Euclidean distance is calculated. The point is

then assigned to the cluster to which the distance from the cluster centroid is

the smallest.

\5. Again now, we compute the new k centroids of the clustered data and repeat

step 4.

\6. Lastly, we can halt iterations when the centroid is not shifting or when the

cluster's points are remaining constant.

**K-Means on stock prices:**

● Used daily dataset from Jan 2016 – Dec 2018

● Utilized returns and volatility as features to cluster stocks into similar

segments

● Returns: Mean of percentage change of closing prices\*756 (trading days of 3

years)

● Volatility: Standard deviation of percentage change of closing prices





**Fig:** Comparison between the origin sector wise distribution and the K-Means result

**Fig:** Quarterly test windows and Mean Squared error for each algorithm for each quarter

**Fig:** Trade Window(2019-2020) and Predicted return for tech sector in the first quarter

**Backtesting:**

● Used to compare the performance of our portfolio with the standard S&P 500 as the

base metric.

● Two metrics were used, one is Min Variance and the other is Mean Variance

● Min variance is an investing approach that involves mixing stock holdings and

diversifying the stocks.

● Mean variance is the method of evaluating risk, expressed as variance, against

expected return

● Between Min and Mean Variance, Min variance is giving better results. It gives nearly

11% more returns compared to the standard S&P 500 whereas the Mean variance

gives around 10% more returns.

● So, Min variance is used for stock selection in our portfolio.


**Future Prospect:**

● Dynamic weight given to each indicator and addressing the market bias.

● Dynamic weight allocation to each stock

● Incorporate other financial assets like ETFs, Bonds, Options, Debentures

● Minimize the portfolio risk with the help of threshold and rebalance the portfolio if the

risk goes beyond threshold


**References:**

● The Journal of Finance and Data Science, Volume 8, November 2022,

Pages 35-54- Machine learning portfolio allocation by Michael Pinelisa

and David Ruppert

● International Journal of Financial Studies- Markowitz Mean-Variance

Portfolio Optimization with Predictive Stock Selection Using Machine

Learning by Apichat Chaweewanchon and Rujira Chaysiri

● [https://medium.com/@nusfintech.ml/ml-optimisation-for-portfolio-allocati](https://medium.com/@nusfintech.ml/ml-optimisation-for-portfolio-allocation-9da34e7fe6b1)

[on-9da34e7fe6b1](https://medium.com/@nusfintech.ml/ml-optimisation-for-portfolio-allocation-9da34e7fe6b1)





● [https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1435&con](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1435&context=jitim)

[text=jitim](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1435&context=jitim)

● <https://ieeexplore.ieee.org/abstract/document/8456121>

● [https://www.herbert.miami.edu/_assets/pdfs/faculty-research/business-c](https://www.herbert.miami.edu/_assets/pdfs/faculty-research/business-conferences/machine-learning/yang-bai.pdf)

[onferences/machine-learning/yang-bai.pdf](https://www.herbert.miami.edu/_assets/pdfs/faculty-research/business-conferences/machine-learning/yang-bai.pdf)

● https://scholarship.claremont.edu/cgi/viewcontent.cgi?article=3517&cont

ext=cmc\_theses

● https://www.hindawi.com/journals/cin/2022/7588303/

