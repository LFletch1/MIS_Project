from main import get_graph_from_file, get_k_MIS
from MIS_algorithms import *

def main():
    graph_files = [("data\\Email-Enron-Clean.txt","Enron"),
                ("data\\US-Power-Grid.txt","Power-Grid"),
                ("data\\Cit-HepPh-Clean.txt", "Citation"), 
                ("data\\facebook_small_clean.txt","Facebook1"),
                ("data\\facebook_large.txt","Facebook2")]
    
    MLS_algorithms = [(lubys_MIS,"Luby"), (alon_MIS,"Alon"), (blelloch_MIS,"Blelloch"), (degree_1_MIS,"Degree One")]
    output_file = open("data\\MIS_data.csv","w")
    output_file.write("Graph,Algorithm,Avg_MIS,Avg_Rounds,Largest_MIS\n")
    # G = nx.gnm_random_graph(5000, 120000)
    k = 100
    for graph_file in graph_files:
        G = get_graph_from_file(graph_file[0], ",")
        for MIS_alg in MLS_algorithms:
            print(MIS_alg[1],graph_file[1],"...")
            avg_MIS, avg_rounds, largest_MIS = get_k_MIS(G, MIS_alg[0], MIS_alg[1], k=k)
            output_file.write(graph_file[1] + "," + MIS_alg[1] + "," + str(avg_MIS) + "," + str(avg_rounds) + "," + str(largest_MIS) + "\n")
            # print(MLS_alg[1],avg_MIS)


if __name__ == "__main__":
    main()