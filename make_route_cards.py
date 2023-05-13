"""Script to make the route cards."""

from ttrdc_functions import *

# get stations and routes
stations = read_stations_csv('stations.csv')
routes = read_routes_csv('routes.csv')

# define network graph
G = define_network_graph(stations, routes)

# calculate 100 unique routes for the new route list
route_list = calculate_route_list(G, stations, 100)

# write out new routes to a CSV
export_routes_to_csv(route_list, 'routes_new.csv')