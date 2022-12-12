from MIS_algorithms import *

def main():
    graph_files = [("data\\Email-Enron-Clean.txt","Enron"),
                ("data\\US-Power-Grid.txt","Powergrid"),
                ("data\\Cit-HepPh-Clean.txt", "Citation"), 
                ("data\\facebook_small_clean.txt","Facebook1"),
                ("data\\facebook_large.txt","Facebook2")]

    r_values = [0,1,2,3,4,5,None]

    output_file = open("data\\degree_one_r_comparison", "w")
    output_file.write("Graph,r_value,Avg_MIS,Avg_Rounds,Largest_MIS\n")
    k = 100

    for graph_file in graph_files:
        G = get_graph_from_file(graph_file[0], ",")
        for r_value in r_values:
            avg_MIS, avg_rounds, largest_MIS = get_k_MIS(G, degree_1_MIS, "Degree One", k=k, r=r_value)
            output_file.write(graph_file[1] + "," + str(r_value) + "," + str(avg_MIS) + "," + str(avg_rounds) + "," + str(largest_MIS) + "\n")


if __name__ == "__main__":
    main()