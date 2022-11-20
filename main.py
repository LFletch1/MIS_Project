import networkx as nx
from MIS_algorithms import lubys_MIS, degree_1_MIS, valid_MIS


def get_graph_from_file(filename, delim=","):
    G = nx.Graph()
    file = open(filename, "r")
    for line in file:
        edge = line.strip("\n").split(delim)
        G.add_edge(int(edge[0]), int(edge[1]))

    return G

def main():
    # G = get_graph_from_file("data\\Email-Enron-Clean.txt", ",")
    # G = get_graph_from_file("data\\clean-roadNet-TX.txt", ",")
    # G = get_graph_from_file("data\\Cit-HepPh-Clean.txt", ",")
    # G = get_graph_from_file("data\\facebook_combined.txt", " ")
    # G = get_graph_from_file("data\\facebook_large.txt", ",")
    G = get_graph_from_file("data\\US-Power-Grid.txt", ",")
    # G = nx.gnm_random_graph(5000, 120000)
    print(G.number_of_nodes())
    print(G.number_of_edges())

    # Degree One MIS
    total = 0
    total_rounds = 0
    total_MIS_sets = 100
    largest_MIS = 0
    print("Degree One MIS")
    for i in range(total_MIS_sets): 
        print(i)
        MIS, rounds = degree_1_MIS(G)
        # print(valid_MIS(MIS,G))
        if len(MIS) > largest_MIS:
            largest_MIS = len(MIS)
        total += len(MIS)
        total_rounds += rounds
    print("Average MIS Size:", total/total_MIS_sets)
    print("Average Rounds:", total_rounds/total_MIS_sets)
    print("Largest MIS:", largest_MIS)

    # Lubys MIS
    total = 0
    total_rounds = 0
    largest_MIS = 0
    print("Luby MIS")
    for i in range(total_MIS_sets): 
        print(i)
        MIS, rounds = lubys_MIS(G)
        # print(valid_MIS(MIS,G))
        if len(MIS) > largest_MIS:
            largest_MIS = len(MIS)
        total += len(MIS)
        total_rounds += rounds 
    print("Average MIS Size:", total/total_MIS_sets)
    print("Average Rounds:", total_rounds/total_MIS_sets)
    print("Largest MIS:", largest_MIS)


if __name__ == "__main__":
    main()