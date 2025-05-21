from load_data import load_graph_from_csv

def run_20_tests_shortest():
    graph = load_graph_from_csv()
    print('Running 20 MRT Navigator Test Cases (Fewest Stops)\n')
    print("Test: NS2 -> EW9 [Fewest Stops]")
    if "NS2" not in graph.vertices or "EW9" not in graph.vertices:
        print(" One or both stations not found: NS2, EW9\n"); return
    if "NS2" == "EW9": print(" Already at destination.\n"); return
    graph.bfs("NS2")
    end = graph.vertices["EW9"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: TE4 -> EW22 [Fewest Stops]")
    if "TE4" not in graph.vertices or "EW22" not in graph.vertices:
        print(" One or both stations not found: TE4, EW22\n"); return
    if "TE4" == "EW22": print(" Already at destination.\n"); return
    graph.bfs("TE4")
    end = graph.vertices["EW22"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: DT29 -> DT1 [Fewest Stops]")
    if "DT29" not in graph.vertices or "DT1" not in graph.vertices:
        print(" One or both stations not found: DT29, DT1\n"); return
    if "DT29" == "DT1": print(" Already at destination.\n"); return
    graph.bfs("DT29")
    end = graph.vertices["DT1"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: NE12 -> EW14 [Fewest Stops]")
    if "NE12" not in graph.vertices or "EW14" not in graph.vertices:
        print(" One or both stations not found: NE12, EW14\n"); return
    if "NE12" == "EW14": print(" Already at destination.\n"); return
    graph.bfs("NE12")
    end = graph.vertices["EW14"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: EW15 -> TE5 [Fewest Stops]")
    if "EW15" not in graph.vertices or "TE5" not in graph.vertices:
        print(" One or both stations not found: EW15, TE5\n"); return
    if "EW15" == "TE5": print(" Already at destination.\n"); return
    graph.bfs("EW15")
    end = graph.vertices["TE5"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: NE9 -> CC5 [Fewest Stops]")
    if "NE9" not in graph.vertices or "CC5" not in graph.vertices:
        print(" One or both stations not found: NE9, CC5\n"); return
    if "NE9" == "CC5": print(" Already at destination.\n"); return
    graph.bfs("NE9")
    end = graph.vertices["CC5"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: CC7 -> EW25 [Fewest Stops]")
    if "CC7" not in graph.vertices or "EW25" not in graph.vertices:
        print(" One or both stations not found: CC7, EW25\n"); return
    if "CC7" == "EW25": print(" Already at destination.\n"); return
    graph.bfs("CC7")
    end = graph.vertices["EW25"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f"Total stops: {end.distance}\n")
    print("Test: CG2 -> NS24 [Fewest Stops]")
    if "CG2" not in graph.vertices or "NS24" not in graph.vertices:
        print(" One or both stations not found: CG2, NS24\n"); return
    if "CG2" == "NS24": print(" Already at destination.\n"); return
    graph.bfs("CG2")
    end = graph.vertices["NS24"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: CC17 -> NS23 [Fewest Stops]")
    if "CC17" not in graph.vertices or "NS23" not in graph.vertices:
        print(" One or both stations not found: CC17, NS23\n"); return
    if "CC17" == "NS23": print(" Already at destination.\n"); return
    graph.bfs("CC17")
    end = graph.vertices["NS23"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: NS19 -> EW12 [Fewest Stops]")
    if "NS19" not in graph.vertices or "EW12" not in graph.vertices:
        print(" One or both stations not found: NS19, EW12\n"); return
    if "NS19" == "EW12": print(" Already at destination.\n"); return
    graph.bfs("NS19")
    end = graph.vertices["EW12"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: EW3 -> TE4 [Fewest Stops]")
    if "EW3" not in graph.vertices or "TE4" not in graph.vertices:
        print(" One or both stations not found: EW3, TE4\n"); return
    if "EW3" == "TE4": print(" Already at destination.\n"); return
    graph.bfs("EW3")
    end = graph.vertices["TE4"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: NS15 -> NS14 [Fewest Stops]")
    if "NS15" not in graph.vertices or "NS14" not in graph.vertices:
        print(" One or both stations not found: NS15, NS14\n"); return
    if "NS15" == "NS14": print(" Already at destination.\n"); return
    graph.bfs("NS15")
    end = graph.vertices["NS14"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total stops: {end.distance}\n")
    print("Test: EW2 -> NE15 [Fewest Stops]")
    if "EW2" not in graph.vertices or "NE15" not in graph.vertices:
        print(" One or both stations not found: EW2, NE15\n"); return
if __name__ == "__main__":
    run_20_tests_shortest()