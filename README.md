
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

● <ins>EPS:</ins> - The ratio of a company’s net profit to the number of outstanding shares is known as Earnings per share (EPS). The higher the EPS the more profitable a company is.

● <ins>P/E:</ins> - The ratio of a company’s share price to the earnings per share is known as price-to-earnings (P/E) ratio.

**Dataset**

Yahoo Finance

● Daily data over a five-year period starting from Jan 2016 to Dec 2020.

● Features considered for clustering algorithm – Closing price

● Features considered for regression algorithm – EPS, P/E and volume traded


**Proposed methodology**

1. Clustering stocks according to sectors using K-means

2. Training three regression-based algorithms namely – Linear Regression, Ridge Regression, Random Forest for predicting stock prices for different rolling windows

3. Selecting best regression algorithm for that quarter using Mean Squared Error for each rolling window

4. Selecting best algorithm from the 4 selected rolling windows

5. Picking top 20% stocks with maximum predicted returns from each sector using the selected regression algorithm

6. Recommending and comparing stocks for the next quarter from 11 sectors using portfolio allocation strategies like min-variance and mean-variance

7. Comparing, back testing and selecting allocation strategy based on overall portfolio value and Sharpe Ratio



**Comparison between the origin sector wise distribution and the K-Means result**

<img src="https://github.com/mayuresh12345/Equity-portfolio-allocation-system/blob/main/Figs/distribution.jpg" width="300"/> &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;<img src="https://github.com/mayuresh12345/Equity-portfolio-allocation-system/blob/main/Figs/sectorwise_clustering.jpg" width="300"/> 

**Quarterly test windows and Mean Squared error for each algorithm for each quarter**

<img src="https://github.com/mayuresh12345/Equity-portfolio-allocation-system/blob/main/Figs/rolling.jpg" width="450"/>

**Trade Window(2019-2020) and Predicted return for tech sector in the first quarter**

<img src="https://github.com/mayuresh12345/Equity-portfolio-allocation-system/blob/main/Figs/TechSectorPredReturns.jpg" width="450"/>

**Backtesting:**

● Used to compare the performance of our portfolio with the standard S&P 500 as the base metric.

● Min Variance and Mean Variance were used as metrics

● Min variance gives better results. Nearly 11% more returns compared to the standard S&P 500

<img src="https://github.com/mayuresh12345/Equity-portfolio-allocation-system/blob/main/Figs/backtest.jpg" width="450"/>


**Future Prospect:**

● Dynamic weight given to each indicator and addressing the market bias.

● Dynamic weight allocation to each stock

● Incorporate other financial assets like ETFs, Bonds, Options, Debentures

● Minimize the portfolio risk with the help of threshold and rebalance the portfolio if the

risk goes beyond threshold


**References:**

1. The Journal of Finance and Data Science, Volume 8, November 2022, Pages 35-54- Machine learning portfolio allocation by Michael Pinelisa and David Ruppert

2. International Journal of Financial Studies- Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning by Apichat Chaweewanchon and Rujira Chaysiri

3. [https://medium.com/@nusfintech.ml/ml-optimisation-for-portfolio-allocati](https://medium.com/@nusfintech.ml/ml-optimisation-for-portfolio-allocation-9da34e7fe6b1)


4. <https://ieeexplore.ieee.org/abstract/document/8456121>

5. [https://www.herbert.miami.edu/_assets/pdfs/faculty-research/business-c](https://www.herbert.miami.edu/_assets/pdfs/faculty-research/business-conferences/machine-learning/yang-bai.pdf)

[onferences/machine-learning/yang-bai.pdf](https://www.herbert.miami.edu/_assets/pdfs/faculty-research/business-conferences/machine-learning/yang-bai.pdf)

6. https://scholarship.claremont.edu/cgi/viewcontent.cgi?article=3517&cont

ext=cmc\_theses

7. https://www.hindawi.com/journals/cin/2022/7588303/

