# TTRDC - Ticket To Ride: District of Columbia

Custom Ticket To Ride map for the District of Columbia.
This repository includes the `.png` file for this custom map, as well as some basic python functions and scripts to generate the routes and associated point values that you can use to make route cards.

<br>

## The Map

![TTRDC Map](ttrdc_map.png)

<br>

## Map Data

`stations.csv` is a CSV file that lists all of the stations present on the map.

`routes.csv` is a CSV file that lists all of the routes present on the map, as well as the distance (in number of trains) of each route.

`routes_new.csv` is a CSV file providing an example of 100 randomly generated unique routes with a starting city, ending city, and associated point value (based on the minimum distance between the two cities) on each row.

<br>

## The Python

The package requirements for the Python scripts and functions in this repository can be installed using `pip` with the following command:

```bash
pip install -r requirements.txt
```

The `ttrdc_functions.py` file contains functions for loading the station and route information that is depicted on the map, as well as functions to generate a network graph, and define unique routes from that graph.

`make_route_cards.py` is a Python script that can be run to generate a random set of 100 unique routes and associated point values that is written out to the file `routes_new.csv`.

`route_analysis.ipynb` is a Jupyter notebook that shows a bit of rudimentary analysis of the overall map network as a graph, which could be further expanded to offer insights about the most 'valuable' routes and locations on the board. It also includes some basic route generation and analysis of the generated routes (unique starting and ending cities, point values, etc.)

<br>

## Disclaimer

This is a fan-made project and is not affiliated with Days of Wonder or Ticket To Ride in any way.
It is my understanding that Days of Wonder does support and encourage fan-made maps and content, as long as it is not used for commercial purposes, see their page on [fan contributions](https://www.daysofwonder.com/tickettoride/en/fans/).