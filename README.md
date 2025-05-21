# Singapore MRT Route Finder

## Overview
This project implements a graph-based route finder for Singapore's MRT system. It supports:

- Finding the **fastest route** (based on total travel time, including line-change penalties).
- Finding the **shortest route** (based on fewest stops).

The MRT system is represented as a weighted graph, where stations are nodes and travel times are edge weights.

## Features
- Reads MRT data from a CSV file.
- Implements Dijkstra's algorithm for the fastest route.
- Implements BFS for the fewest stops.
- Includes a 5-minute penalty when switching lines.
- Includes a test suite (`test_mrt_routes.py`) for validating routes.
- Includes a test suite (`test_mrt_20_shortest.py`) for validating routes.
## Files
- `main.py`: Main user interface.
- `load_data.py`: Loads graph from CSV.
- `mrt_graph.py`: Custom Graph, Vertex, Edge classes.
- `processed_stations_with_penalty.csv`: Data source with line-change penalties.
- `test_mrt_routes.py`: Automated test script.
- `README.md`: This file.
- `requirements.txt`: Dependencies list.

## How to Run
```bash
python main.py
```

Follow the prompts to enter:
- Start station code (e.g. `NS1`)
- End station code (e.g. `NS24`)
- Route type (1 = fastest, 2 = fewest stops)

## How to Test
```bash
python test_mrt_routes.py
python test_mrt_20_shortest.py

```

This runs automated test cases and prints results to console.

## Example Stations
- `NS1`: Jurong East
- `NS24`: Dhoby Ghaut
- `CG2`: Changi Airport
- `TE1`: Woodlands North
