
import csv
from mrt_graph import Graph

def load_graph_from_csv():
    graph = Graph()
    with open("processed_stations.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            from_code = row['from_code']
            from_name = row['from_name']
            to_code = row['to_code']
            to_name = row['to_name']
            time = int(row['adjusted_time'])
            graph.add_station(from_code, from_name)
            graph.add_station(to_code, to_name)
            graph.connect(from_code, to_code, time)
    return graph
