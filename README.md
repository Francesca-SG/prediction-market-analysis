# prediction-market-analysis

### Methodology
This project analyses data collected from Kalshi.com (prediction market) to determine which events ans markets are most active, traded and volatile. All data was collected from the "Politics" series category for project simplicity. Using a custom python script, the data was sourced from the platform's publicly available API. 

**Sources:** Kalshi.com 

**Insights:**
Most popular event by total market volume is "Who will Trump nominate as Fed Chair?" with	179,548,009 volume.
Most popular market by market volume is "Will Trump next nominate Judy Shelton as Fed Chair?" with 86,352,472 volume.

Volatility is measured by the change in price between the previous and last recored values. A market is considered volatile when the price is large and the maket has traded abouve a reasonable threshhold, showing that many traders are involded in the value shift. A particularly large "Difference" and high volume indicates opinion has changed significantly. The market "Will Ilhan Omar attend the 2026 State of the Union Address?" shows a 30 cent increase between the previous and last recorded prices, and as it has traded over $33,000 dollars, the price jump reflects a meaing shift in trader expectations.

The event "Which party will win the U.S. House of Representatives?" has over $5 million in total market volume and more then $3 million in open interest, making this a highly active event across the dataset. The average Yes and No bids sit at exactly 50 cents, reflecting deep engaging but real uncertainty amongst traders.

**Notes:**
All data tagged as 'Awards' or 'Television' was excluded from this analysis, as the data was unrelated to the stated series_category "Politics". Additionally, "Entertainment" and a single entryin the "Social" event category was also excluded futher ensuring a consistent and accurate analysis. 
