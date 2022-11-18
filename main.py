import networkx as nx
from MIS_algorithms import lubys_MIS


def get_graph_from_file(filename, delim=","):
    G = nx.Graph()
    file = open(filename, "r")
    for line in file:
        edge = line.strip("\n").split(delim)
        G.add_edge(int(edge[0]), int(edge[1]))

    return G

def main():
    G = get_graph_from_file("data\\facebook_combined.txt", " ")
    total = 0
    total_rounds = 0
    total_MIS_sets = 100
    for i in range(total_MIS_sets): 
        mis, rounds = lubys_MIS(G)
        total += len(mis)
        total_rounds += rounds

    
    print("Average MIS Size:", total/total_MIS_sets)
    print("Average Rounds:", total_rounds/total_MIS_sets)


if __name__ == "__main__":
    main()