from main import get_graph_from_file, get_k_MIS
from MIS_algorithms import *

def graph_compare():
    graph_files = [("data\\Email-Enron-Clean.txt","Enron"),
                ("data\\US-Power-Grid.txt","Powergrid"),
                ("data\\Cit-HepPh-Clean.txt", "Citation"), 
                ("data\\facebook_small_clean.txt","Facebook1"),
                ("data\\facebook_large.txt","Facebook2")]
    
    MLS_algorithms = [(lubys_MIS,"Luby"), (alon_MIS,"Alon"), (blelloch_MIS,"Blelloch"), (degree_1_MIS,"Degree One")]
    output_file = open("data\\MIS_data.csv","w")
    output_file.write("Graph,Algorithm,Avg_MIS,Avg_Rounds,Largest_MIS\n")
    k = 100
    for graph_file in graph_files:
        G = get_graph_from_file(graph_file[0], ",")
        for MIS_alg in MLS_algorithms:
            print(MIS_alg[1],graph_file[1],"...")
            avg_MIS, avg_rounds, largest_MIS = get_k_MIS(G, MIS_alg[0], MIS_alg[1], k=k)
            output_file.write(graph_file[1] + "," + MIS_alg[1] + "," + str(avg_MIS) + "," + str(avg_rounds) + "," + str(largest_MIS) + "\n")

def erdos_renyi_compare():
    # List of various n,m parameters to generate a variety of Erdos Renyi graphs
    graph_types = [(500,10000),(500,100000),(1000,5000),(1000,10000),(2500,250000)]
    
    MLS_algorithms = [(lubys_MIS,"Luby"), (alon_MIS,"Alon"), (blelloch_MIS,"Blelloch"), (degree_1_MIS,"Degree One")]
    output_file = open("data\\MIS_erdos_renyi_data.csv","w")
    output_file.write("Graph,Algorithm,Avg_MIS,Avg_Rounds,Largest_MIS\n")
    k = 100
    for graph_type in graph_types:
        G = nx.gnm_random_graph(graph_type[0], graph_type[1])
        for MIS_alg in MLS_algorithms:
            print(MIS_alg[1],graph_type[0],"-",graph_type[1],"...")
            avg_MIS, avg_rounds, largest_MIS = get_k_MIS(G, MIS_alg[0], MIS_alg[1], k=k)
            output_file.write(str(graph_type[0]) + "-" + str(graph_type[1]) + "," + MIS_alg[1] + "," + str(avg_MIS) + "," + \
                str(avg_rounds) + "," + str(largest_MIS) + "\n")



def main():
    # graph_compare()
    erdos_renyi_compare()


if __name__ == "__main__":
    main()