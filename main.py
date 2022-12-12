from MIS_algorithms import *

def main():
    G = get_graph_from_file("data/facebook_small_clean.txt", ",")

    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())
    k = 100
    _, _, _ = get_k_MIS(G, lubys_MIS, "Luby's", k=k)
    _, _, _ = get_k_MIS(G, alon_MIS, "Alon's", k=k)
    _, _, _ = get_k_MIS(G, blelloch_MIS, "Blelloch's", k=k)
    _, _, _ = get_k_MIS(G, degree_1_MIS, "Degree One", k=k, r=0)


if __name__ == "__main__":
    main()