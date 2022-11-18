import networkx as nx
import random as rand
import matplotlib.pyplot as plt

def lubys_MIS(G):
    G_ = nx.Graph(G)
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
            print("Total Rounds:", rounds)
            empty_graph = True
        else:
            rounds += 1

    return I, rounds

# def verify_mis():