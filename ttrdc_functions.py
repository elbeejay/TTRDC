"""Functions for the TTRDC project."""
import csv
import numpy as np
import networkx as nx
from tqdm import tqdm


def read_stations_csv(path):
    """Read stations csv."""
    stations = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # remove leading spaces then append
            row = [x.strip() for x in row]
            stations.append(row)
    return stations


def read_routes_csv(path):
    """Read routes csv."""
    routes = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # remove leading spaces then append
            row = [x.strip() for x in row]
            routes.append(row)
    return routes


def define_network_graph(stations, routes):
    """Define network graph."""
    G = nx.Graph()
    # assign stations as nodes of the graph
    for station in stations[0]:
        G.add_node(station)
    # assign routes as edges of the graph
    for route in routes:
        G.add_edge(route[0], route[1], weight=int(route[2]))
    return G


def calculate_route_list(G, stations, n_routes):
    """Determine route list.

    Define a list of n_routes that have unique start and end stations.
    """
    i = 0  # counter
    ghost_i = 0  # counter to check for infinite loop
    route_list = []
    with tqdm(total=n_routes) as pbar:
        while i < n_routes:
            # randomly select two stations
            start = np.random.choice(stations[0])
            end = np.random.choice(stations[0])
            # check that the two stations are not the same and are not neighbors
            while (start == end) or (end in G.neighbors(start)):
                end = np.random.choice(stations[0])
            # determine the shortest route between the two stations
            pts = nx.shortest_path_length(G, start, end, weight='weight')
            # set the route
            route = (start, end, pts)
            route_inv = (end, start, pts)
            # check that the route is not already in the list
            if (route not in route_list) and (route_inv not in route_list):
                route_list.append(route)
                i += 1
                ghost_i = 0
                pbar.update(1)
            else:
                ghost_i += 1
                if ghost_i > 1000:
                    print('Infinite loop detected. Exiting.')
                    break
    return route_list


def export_routes_to_csv(route_list, path):
    """Export routes to csv."""
    with open(path, 'w') as f:
        writer = csv.writer(f)
        for route in route_list:
            writer.writerow(route)
