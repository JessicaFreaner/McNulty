# McNulty - Exploring Heart Health Data

Third project within the Metis Bootcamp. Asked to choose between Heart Health, Advertising, and Financial data, I choose to work on the former. Within the last year, heart health became part of my personal family health history and I jumped at the opportunity to gleam some insights.

After initial exploration into the health dataset and into the significance (in terms of health) of certain markers/measurements in the dataset, I became dissatified because of a dearth of female patient data and very limited temporal information. I ventured into the web looking for alternate sources and found a sample of longitudial patient information from the [Framingham Heart Study](https://www.framinghamheartstudy.org/).

To handle longitudinal data, I read research papers on Discrete Time Survival Analysis by Willet / Singer (1993). Replicating the methodolgy, I ran discrete person-time logistic models to identify risk factors for heart health related life events and demonstrate how hazard effect size varies over time and by gender. There was a significant level of data cleaning / preprocessing for analysis. And I created an interactive D3 tool to allow users to explore how effect size changes over time and varies by condition and gender.
