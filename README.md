# McNulty - Exploring Heart Health Data

![Heart Health](https://cloud.githubusercontent.com/assets/9892419/7461438/5cba9ca0-f278-11e4-9353-0939be04db27.jpg)

Third project within the Metis Bootcamp. Asked to choose between Heart Health, Advertising, and Financial data, I choose to work on the former. Within the last year, heart health became part of my personal family health history and I jumped at the opportunity to gleam some insights.

After initial exploration into the health dataset and into the significance (in terms of health) of certain markers/measurements in the dataset, I became dissatified because of a dearth of female patient data and very limited temporal information. I ventured into the web looking for alternate sources and found a sample of longitudial patient information from the [Framingham Heart Study](https://www.framinghamheartstudy.org/). I built a MySQL database on [DigitalOcean](https://www.digitalocean.com/ "Digital Ocean") cloud server to store the data.

![Framingham](https://cloud.githubusercontent.com/assets/9892419/7461542/0e2882cc-f279-11e4-9207-1e04fe765951.png)
![longitudinal study](https://cloud.githubusercontent.com/assets/9892419/7461435/5cb3913a-f278-11e4-91f0-68c6bd01d4f7.jpg)

To handle longitudinal data, I read [research papers](https://github.com/JessicaFreaner/McNulty/tree/master/research_papers "Link to Research Papers") on [Discrete Time Survival Analysis](http://www.ats.ucla.edu/stat/mplus/seminars/DiscreteTimeSurvival/ "Discrete Time Survival Analysis") by Willet / Singer (1993). Replicating the methodolgy, I ran discrete person-time logistic models to identify risk factors for heart health related life events and demonstrate how hazard effect size varies over time and by gender. There was a significant level of data cleaning / preprocessing for analysis. And I created an [interactive D3 tool](http://bl.ocks.org/jessicafreaner/8fb0ac6c12aa1dab5f70 "Dual Multi-Line Graph with Interactive Legend") to allow users to explore how effect size changes over time and varies by condition and gender. 

![D3 Interactive](https://cloud.githubusercontent.com/assets/9892419/7504830/34744526-f41b-11e4-9e38-bf8089859cd3.gif)

###Flask App for Angina: 
To visualize the effect of features, I also created a Flask App for Angina ( a Heart Health Related Life Event ). Can be adapted to other Life Events explored in D3.

![Flask App](https://cloud.githubusercontent.com/assets/9892419/7620640/595be9e2-f98f-11e4-8ce1-119a166f3861.gif)

![ThisIsMetis](https://cloud.githubusercontent.com/assets/9892419/7356548/e1a3b3ac-ecf6-11e4-8fb6-be39f563742e.jpg) 
##Other Metis Projects:

[Benson](http://jessicafreaner.github.io/Benson/ "Exploring MTA Data") - Exploring MTA Data

[Luther](http://jessicafreaner.github.io/Luther/ "Exploring Movie Data") - Exploring Movie Data

[Fletcher](http://jessicafreaner.github.io/Fletcher/ "Exploring Data with NLP") - Exploring Data with NLP

[Kojak](http://jessicafreaner.github.io/Kojak/ "Exploring NYC's Moving Populations") - Exploring NYC's Moving Populations
