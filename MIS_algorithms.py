import networkx as nx
import random as rand
import matplotlib.pyplot as plt

def lubys_MIS(G):
    G_ = nx.Graph(G) # Create copy of graph that can be manipulated
    empty_graph = False
    I = []
    rounds = 1
    while not empty_graph:
        X = []
        for v in G_.nodes():
            d = G_.degree(v)
            if d == 0:
                X.append(v)
            elif rand.uniform(0,1) <= 1 / (2*d):
                X.append(v)

        I_prime = X[:] # Independent set equals copy of X
        for v in range(len(X)):
            for w in range(v,len(X)):
                v_node = X[v]
                w_node = X[w]
                if G_.has_edge(v_node,w_node) or G_.has_edge(w_node, v_node):
                    if G_.degree(v_node) <= G_.degree(w_node):
                        if v_node in I_prime: I_prime.remove(v_node)
                    else:
                        if w_node in I_prime: I_prime.remove(w_node)
        I += I_prime

        Y = I_prime[:]
        for i in I_prime:
            for n in G_.neighbors(i):
                if n not in Y: Y.append(n)

        for y in Y:
            G_.remove_node(y)
     
        if G_.number_of_nodes() == 0:
            # print("Total Rounds:", rounds)
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
                    # print(neighbor)
                    if G_.degree(neighbor) == 1: # A pair of one degree nodes
                        pair = (n,neighbor)
                        if pair not in pairs: # Don't add redundant pairs
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

        # Once no degree one nodes are present utilize node labels and perform a single random parallel MIS round
        I = []
        nodes_to_remove = []
        total_MIS_rounds += 1
        for n in G_.nodes():
            highest_rank = True
            n_rank = node_ranks[n]
            potential_neighbors_to_remove = []
            for neigh in G_.neighbors(n): # Check if n is highest ranked node in set of neighbors. (Higher rank = Greater integer)
                if node_ranks[neigh] > n_rank:
                    highest_rank = False
                    break
                else:
                    potential_neighbors_to_remove.append(neigh)

            if highest_rank:
                I.append(n)
                nodes_to_remove += potential_neighbors_to_remove
        
        for i in I:
            G_.remove_node(i)
        for n in nodes_to_remove:
            try: # Will potentially try to remove the same neighbors
                G_.remove_node(n)
            except nx.NetworkXError:
                pass 
        MIS += I

        if G_.number_of_nodes() == 0:
            empty_graph = True        
            
    # print(total_one_degree_rounds, "one degree rounds")
    # print("Number of nodes in G:", G_.number_of_nodes())
    # print("MIS Size:", len(MIS))
    return MIS, total_MIS_rounds


def valid_MIS(MIS, G):
    '''Does not check for maximality, just checks that no adjacency violations are present'''
    for i in MIS:
        for neigh in G.neighbors(i):
            if neigh in MIS:
                return False
    return True