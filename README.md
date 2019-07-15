
#### About

This is part of my team's submission for the two-day d-fine hackathon which took place in autumn 2018. In our project we had traffic and air pollution data from the city of Frankfurt, Germany.

#### Goal

Our goal was to find and predict roads that, if blocked locally, would significantly reduce air pollution (as mandated by [law](https://www.reuters.com/article/us-volkswagen-emissions-frankfurt/german-court-says-frankfurt-must-ban-older-diesel-cars-idUSKCN1LL2GC)). The other members of my team analyzed the data and trained a regression model, while I focused on data processing and visualization.

#### Data

The animated map below shows our data over the course of a single day. I used [folium](https://github.com/python-visualization/folium) and added a custom legend and a plot overlay, generated in matplotlib. The <span style="color:blue">blue nodes</span> are measurements of traffic, their size reflecting registered cars per time unit (30min). The  <span style="color:orange">orange node</span> is the air pollution measurement station, the plot in the bottom left shows the time course of the measurements. The animation below loops over the duration of one day (current time indicated by the arrow in the left-corner plot).

![animated map](https://raw.githubusercontent.com/felix11h/dfine-hackathon-18/master/pub/original_data_animated.gif)


Folium is able to generate local html files, which provide an interactive map. An example of one of our generated maps is [here](https://felix11h.github.io/dfine-hackathon-18/maps/original_data/180704_07.html). Node values can be seen by clicking on the nodes.

#### Trained model

We used a regression model to try to predict which roadblocks would be effective in reducing the air pollution measured. In animation below, the grey curve shows the predicted pollution measurements when the roads with red nodes are blocked. 

![animated blocked roads map](https://raw.githubusercontent.com/felix11h/dfine-hackathon-18/master/pub/roadblocks_animated.gif)
