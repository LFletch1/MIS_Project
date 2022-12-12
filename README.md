# MIS_Project
Maximal Independent Set Project

Final project for CSCE 689 - Advanced Graph Algorithms Course. Project is focused on maximal independent sets (MIS) which are defined as a maximal subset of nodes within a graph such that no nodes within the set are adjacent to each other. The project specifically focuses on comparing the average MIS size returned by various parallel algorithms. MISs can be used in a vareity of other graph problems such as vertex cover, graph coloring, maximal matching, and correlation clustering. Therefore an algorithm which produces, on average, the best (largest) MIS could be prefered by many algorithms. The four algorithms compared in this project are Luby's, Alon's, Blelloch's, and a new algorithm call Degree One.

To see an example of the comparison, run main.py. This will utilize each of the four algorithms to generate 100 MISs. Note: The python library networkx is required to run the example.