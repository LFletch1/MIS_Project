import networkx as nx
import random as rand
import matplotlib.pyplot as plt

def lubys_MIS(G):
    G_ = nx.Graph(G) # Create copy of graph that can be manipulated
    empty_graph = False
    I = []
    rounds = 1
    while not empty_graph:
        X = {}

        # print("Part 1")
        for v in G_.nodes():
            d = G_.degree(v)
            if d == 0:
                X[v] = 1
            elif rand.uniform(0,1) <= 1 / (2*d):
                X[v] = 1

        # print("Part 2")
        I_prime = list(X.keys()) # Independent set equals copy of X
        for edge in G_.edges():
            if X.get(edge[0]) != None and X.get(edge[1]) != None:
                try:
                    if G_.degree(edge[0]) <= G_.degree(edge[1]):
                        I_prime.remove(edge[0])
                    else:
                        I_prime.remove(edge[1])
                except ValueError:
                    continue

        # print("Part 3")
        I += I_prime
        Y = I_prime[:]
        for i in I_prime:
            for n in G_.neighbors(i):
                Y.append(n)

        # print("Part 4")
        for y in Y:
            try:
                G_.remove_node(y) 
            except nx.NetworkXError:
                pass
        # print(G_.number_of_nodes())
        if G_.number_of_nodes() == 0:
            empty_graph = True
        else:
            rounds += 1

    return I, rounds


def degree_1_MIS(G):
    G_ = nx.Graph(G) # Create copy of graph that can be manipulated
    node_ranks =  rand.sample(range(0, G_.number_of_nodes()+1), G_.number_of_nodes())
    empty_graph = False
    MIS = []
    total_one_degree_rounds = 0
    total_MIS_rounds = 0
    while not empty_graph:
        # Add all degree one vertices to the MIS. Then remove all of these nodes and their neighbors from the graph.
        # Continue doing this until no degree node one vertices remain. Note: Non-one degree nodes can become degree one
        # during this process. Similar to k-core.
        
        one_degree_nodes_exist = True
        k = 0
        while one_degree_nodes_exist: # Could potentially set this to a limit of k iterations
            neighbors_to_remove = []
            I = []
            pairs = []
            for n in G_.nodes():
                n_degree = G_.degree(n)
                if n_degree == 0:
                    I.append(n)
                elif n_degree == 1:
                    neighbor = [neigh for neigh in G_.neighbors(n)][0]
                    if G_.degree(neighbor) == 1: # A pair of one degree nodes
                        other_pair = (neighbor,n)
                        if other_pair not in pairs: # Don't add redundant pairs
                            pairs.append((n, neighbor)) 
                    else: 
                        neighbors_to_remove.append(neighbor)
                        I.append(n)
            for pair in pairs:
                I.append(pair[0])
                neighbors_to_remove.append(pair[1])

            MIS += I

            for i in I:
                G_.remove_node(i)
            for n in neighbors_to_remove:
                try: # Will potentially try to remove the same neighbors
                    G_.remove_node(n)
                except nx.NetworkXError:
                    pass

            k += 1

            if len(I) == 0:
                one_degree_nodes_exist = False
        
        total_one_degree_rounds += k

        # Once no degree one nodes are present apply a slightly modified version of Libby's Algorithm
        X = {}
        # print("Part 1")
        for v in G_.nodes():
            d = G_.degree(v)
            if d == 0:
                X[v] = 1
            elif rand.uniform(0,1) <= 1 / (2*d):
                X[v] = 1

        # print("Part 2")
        I_prime = list(X.keys()) # Independent set equals copy of X
        for edge in G_.edges():
            if X.get(edge[0]) != None and X.get(edge[1]) != None:
                try:
                    if G_.degree(edge[0]) >= G_.degree(edge[1]):
                        I_prime.remove(edge[0])
                    else:
                        I_prime.remove(edge[1])
                except ValueError:
                    continue

        # print("Part 3")
        MIS += I_prime
        Y = I_prime[:]
        for i in I_prime:
            for n in G_.neighbors(i):
                Y.append(n)

        # print("Part 4")
        for y in Y:
            try:
                G_.remove_node(y) 
            except nx.NetworkXError:
                pass

        # print(G_.number_of_edges())
        if G_.number_of_nodes() == 0:
            empty_graph = True        
            
    # print(total_one_degree_rounds, "one degree rounds")
    # print("Number of nodes in G:", G_.number_of_nodes())
    # print("MIS Size:", len(MIS))
    return MIS, total_MIS_rounds


def valid_MIS(MIS, G):
    '''Checks for maximality and checks that no adjacency violations are present (independent set)'''
    # Independent Set Check
    for i in MIS:
        for neigh in G.neighbors(i):
            if neigh in MIS:
                return False
    # Maximality Check
    for n in G.nodes():
        if n in MIS:
            continue
        neighbor_in_mis = False
        for neigh in G.neighbors(n):
            if neigh in MIS:
                neighbor_in_mis = True
                break
        if not neighbor_in_mis:
            return False
    return True


        # I = []
        # nodes_to_remove = []
        # total_MIS_rounds += 1
        # for n in G_.nodes():
        #     highest_rank = True
        #     n_rank = node_ranks[n]
        #     potential_neighbors_to_remove = []
        #     for neigh in G_.neighbors(n): # Check if n is highest ranked node in set of neighbors. (Higher rank = Greater integer)
        #         if node_ranks[neigh] > n_rank:
        #             highest_rank = False
        #             break
        #         else:
        #             potential_neighbors_to_remove.append(neigh)

        #     if highest_rank:
        #         I.append(n)
        #         nodes_to_remove += potential_neighbors_to_remove
        
        # for i in I:
        #     G_.remove_node(i)
        # for n in nodes_to_remove:
        #     try: # Will potentially try to remove the same neighbors
        #         G_.remove_node(n)
        #     except nx.NetworkXError:
        #         pass 
        # MIS += I