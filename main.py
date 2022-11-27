import time
import networkx as nx
from MIS_algorithms import *


def get_k_MIS(graph, MIS_func, name, k, v=True):
    '''Get k amount of MISs and be returned the Avg. MIS Size, Avg. Parallel Rounds, and Largest MIS'''
    if v:
        print("Generting Maximal Independent Sets using " + name)
    total = 0
    total_rounds = 0
    largest_MIS = 0
    loader_length = 50
    div = k // loader_length
    for i in range(1, k+1):
        if v:
            if i % div == 0:
                percent_done = i // div
                print("\r", end="")
                print("[" + "#" * (i // div) + " " * (loader_length - percent_done) + "]", end="")
                time.sleep(0.5)
        MIS, rounds = MIS_func(graph)
        size = len(MIS)
        if size > largest_MIS:
            largest_MIS = size 
        total += size
        total_rounds += rounds 
    print()
    
    avg_MIS = total / k
    avg_rounds = total_rounds / k
    if v:
        print("Average MIS Size:", total / k)
        print("Average Rounds:", total_rounds / k)
        print("Largest MIS:", largest_MIS)

    return avg_MIS, avg_rounds, largest_MIS


def get_graph_from_file(filename, delim=","):
    G = nx.Graph()
    file = open(filename, "r")
    for line in file:
        edge = line.strip("\n").split(delim)
        G.add_edge(int(edge[0]), int(edge[1]))

    return G


def main():
    G = get_graph_from_file("data\\facebook_combined.txt", " ")

    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())
    k = 100
    _, _, _ = get_k_MIS(G, lubys_MIS, "Luby's", k=k)
    _, _, _ = get_k_MIS(G, alon_MIS, "Alon's", k=k)
    _, _, _ = get_k_MIS(G, blelloch_MIS, "Blelloch's", k=k)
    _, _, _ = get_k_MIS(G, degree_1_MIS, "Degree One", k=k)


if __name__ == "__main__":
    main()