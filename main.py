
from mrt_graph import Graph
import csv

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

def run_passenger_menu(graph):
    print()
    start_code = input("Enter current station code (e.g., TE20): ").strip().upper()
    end_code = input("Enter destination station code (e.g., NS24): ").strip().upper()

    if start_code not in graph.vertices or end_code not in graph.vertices:
        print("Error: Invalid station code. Please try again.")
        return

    if start_code == end_code:
        print("You're already at your destination.")
        return

    print("\nHow would you like to travel?")
    print("1: Fastest route (based on travel time)")
    print("2: Route with fewest stops")
    choice = input("Enter 1 or 2: ").strip()

    print()
    if choice == "1":
        print("Fastest route:")
        graph.dijkstra(start_code)
        graph.print_path(graph.vertices[end_code])
        print(f"\nTotal time: {graph.vertices[end_code].distance} minutes")
    elif choice == "2":
        print("Least stops route:")
        graph.bfs(start_code)
        graph.print_path(graph.vertices[end_code])
        print(f"\nTotal stops: {graph.vertices[end_code].distance}")
    else:
        print("Error: Invalid choice.")

def main():
    print("Singapore Metro Navigator")
    print("Loading MRT map from 'processed_stations.csv'...")
    graph = load_graph_from_csv()
    print("MRT map loaded successfully.")
    run_passenger_menu(graph)

if __name__ == "__main__":
    main()
