# Small script that will make node labels start from 0 and continue on 1, 2, .... n.
# This is to allow the rank array size to be set based on the number of nodes without
# causing an index error. Additionally get rid of any repeat edges to remove any
# redundant work for the MIS algorithms. Also remove self edges.

file = open("data\\facebook_combined.txt", "r")
write_file = open("data\\facebook_small_clean.txt", "w")

# 1921660
edge_dict = {}
nodes_dict = {}
current_node = 0
for line in file:
    edge_nodes = line.strip().split(" ")

    if not (edge_nodes[0] in nodes_dict):
        nodes_dict[edge_nodes[0]] = current_node
        current_node += 1
    if not (edge_nodes[1] in nodes_dict):
        nodes_dict[edge_nodes[1]] = current_node
        current_node += 1    

    edge = (int(nodes_dict[edge_nodes[1]]),int(nodes_dict[edge_nodes[0]]))
    if edge[0] == edge[1]:
        continue
    if not (edge in edge_dict):
        edge_dict[(edge[1],edge[0])] = 1
        write_file.write(str(edge[1]) + "," + str(edge[0]) + "\n")



    