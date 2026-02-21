# prediction-market-analysis

### Methodology
This project analyses data collected from Kalshi.com (prediction market) to determine which events ans markets are most active, traded and volatile. All data was collected from the "Politics" series category for project simplicity. Using a custom python script, the data was sourced from the platform's publicly available API. 

**Sources:** Kalshi.com 

**Insights:**
Most popular event by total market volume is "Who will Trump nominate as Fed Chair?" with	179,548,009 volume.
Most popular market by market volume is "Will Trump next nominate Judy Shelton as Fed Chair?" with 86,352,472 volume.

Volatile markets is calculated using the "Last Price in Dollars" - "Previous Price in Dollars" = "Difference" and a reasonably high market volume. A particularly large "Difference" and high volume indicates opinion has changed significantly. For the event "Who will attend the State of the Union?" and subsequent market "Will Ilhan Omar attend the 2026 State of the Union Address?" shows a 0.30¢ difference between the last and previous prices.

**Notes:**
All data tagged as 'Awards' or 'Television' was excluded from this analysis, as the data was unrelated to the stated series_category "Politics". Additionally, "Entertainment" and a single entryin the "Social" event category was also excluded futher ensuring a consistent and accurate analysis. 
