from load_data import load_graph_from_csv

def run_20_tests():
    graph = load_graph_from_csv()
    print('Running 20 MRT Navigator Test Cases\n')
    print("Test: NS2 -> EW9 [Fastest]")
    if "NS2" not in graph.vertices or "EW9" not in graph.vertices:
        print(" One or both stations not found: NS2, EW9\n"); return
    if "NS2" == "EW9": print(" Already at destination.\n"); return
    graph.dijkstra("NS2")
    end = graph.vertices["EW9"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total time: {end.distance} minutes\n")
    print("Test: TE4 -> EW22 [Fastest]")
    if "TE4" not in graph.vertices or "EW22" not in graph.vertices:
        print(" One or both stations not found: TE4, EW22\n"); return
    if "TE4" == "EW22": print(" Already at destination.\n"); return
    graph.dijkstra("TE4")
    end = graph.vertices["EW22"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total time: {end.distance} minutes\n")
    print("Test: DT29 -> DT1 [Fastest]")
    if "DT29" not in graph.vertices or "DT1" not in graph.vertices:
        print(" One or both stations not found: DT29, DT1\n"); return
    if "DT29" == "DT1": print("Already at destination.\n"); return
    graph.dijkstra("DT29")
    end = graph.vertices["DT1"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f"Total time: {end.distance} minutes\n")
    print("Test: NE12 -> EW14 [Fastest]")
    if "NE12" not in graph.vertices or "EW14" not in graph.vertices:
        print(" One or both stations not found: NE12, EW14\n"); return
    if "NE12" == "EW14": print(" Already at destination.\n"); return
    graph.dijkstra("NE12")
    end = graph.vertices["EW14"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total time: {end.distance} minutes\n")
    print("Test: EW15 -> TE5 [Fastest]")
    if "EW15" not in graph.vertices or "TE5" not in graph.vertices:
        print(" One or both stations not found: EW15, TE5\n"); return
    if "EW15" == "TE5": print(" Already at destination.\n"); return
    graph.dijkstra("EW15")
    end = graph.vertices["TE5"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total time: {end.distance} minutes\n")
    print("Test: NE9 -> CC5 [Fastest]")
    if "NE9" not in graph.vertices or "CC5" not in graph.vertices:
        print(" One or both stations not found: NE9, CC5\n"); return
    if "NE9" == "CC5": print(" Already at destination.\n"); return
    graph.dijkstra("NE9")
    end = graph.vertices["CC5"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total time: {end.distance} minutes\n")
    print("Test: CC7 -> EW25 [Fastest]")
    if "CC7" not in graph.vertices or "EW25" not in graph.vertices:
        print(" One or both stations not found: CC7, EW25\n"); return
    if "CC7" == "EW25": print(" Already at destination.\n"); return
    graph.dijkstra("CC7")
    end = graph.vertices["EW25"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total time: {end.distance} minutes\n")
    print("Test: CG2 -> NS24 [Fastest]")
    if "CG2" not in graph.vertices or "NS24" not in graph.vertices:
        print(" One or both stations not found: CG2, NS24\n"); return
    if "CG2" == "NS24": print(" Already at destination.\n"); return
    graph.dijkstra("CG2")
    end = graph.vertices["NS24"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total time: {end.distance} minutes\n")
    print("Test: CC17 -> NS23 [Fastest]")
    if "CC17" not in graph.vertices or "NS23" not in graph.vertices:
        print(" One or both stations not found: CC17, NS23\n"); return
    if "CC17" == "NS23": print(" Already at destination.\n"); return
    graph.dijkstra("CC17")
    end = graph.vertices["NS23"]
    if end.distance == float("inf"): print(" No path found.\n"); return
    print(f" Total time: {end.distance} minutes\n")
    print("Test: NS19 -> EW12 [Fastest]")
    if "NS19" not in graph.vertices or "EW12" not in graph.vertices:
        print(" One or both stations not found: NS19, EW12\n"); return
    if "NS19" == "EW12": print(" Already at destination.\n"); return
    graph.dijkstra("NS19")
    end = graph.vertices["EW12"]
if __name__ == "__main__":
    run_20_tests()