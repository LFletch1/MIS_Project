import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def graphs_comparison():
    bar_width = 0.20
    fig = plt.subplots(figsize = (12,8))
    graph_df = pd.read_csv("data\\MIS_data.csv")
    Algs_avg_MIS = {}
    for alg in graph_df["Algorithm"].unique():
        Algs_avg_MIS[alg] = list(graph_df[graph_df["Algorithm"] == alg]["Avg_MIS"])

    number_of_graphs = len(graph_df["Graph"].unique())
    first_bar = np.arange(number_of_graphs)
    bar_positions = []
    for x in range(number_of_graphs):
        bar_pos = []
        for pos in first_bar:
            bar_pos.append(pos + x * bar_width)
        bar_positions.append(bar_pos)

    keys = list(Algs_avg_MIS.keys())
    # print(keys)
    for i in range(len(keys)):
        plt.bar(bar_positions[i], Algs_avg_MIS[keys[i]], width = bar_width,
                 label = keys[i], edgecolor="black")
    
    plt.xlabel("Graph", fontweight="bold", fontsize=15)
    plt.ylabel("Average MIS Size", fontweight="bold", fontsize=15)
    plt.xticks([w + (1.5 * bar_width) for w in range(number_of_graphs)], graph_df["Graph"].unique())

    plt.legend()
    plt.savefig("graph_compare_bar_plot.png")



def main():
    graphs_comparison()

if __name__ == "__main__":
    main()