from graphviz import Digraph
import networkx as nx

graph = Digraph(filename='graph_with_cycles')

with open('assets/nodes.txt') as f:
    for line in f:
        line = line.strip()
        line_list = line.split('\t')
        graph.node(name=line_list[0], label=line_list[1])

with open('assets/edges.txt') as f:
    for line in f:
        line = line.strip()
        line_list = line.split('\t')
        if len(line_list) > 1:
            neighbors = line_list[1].split(',')
            for node in neighbors:
                graph.edge(line_list[0], node)

edges = []
cycles = []

# Parse edge data so it can be passed to nx.simple_cycles() as a graph
for element in graph.body:
    if '->' in element:
        element = element[1::]
        element = element.split()
        new_edge = (int(element[0]), int(element[2]))
        edges.append(new_edge)

new_graph = nx.DiGraph(edges)
# Calculate the initial cycles
cycles = list(nx.simple_cycles(new_graph))

"""
Writes the cycles to a text file. Creates a huge file and is unnecessary for the Aufgabe, so I have commented it out.
"""
# with open('assets/cycles.txt', 'w') as file:
#    for cycle in cycles:
#        file.write(str(cycle))

"""
Writes a file of the original graph with cycles and displays it onscreen. Only needed for Aufgabe 1.
"""
# graph.render('output/graph_with_cycles.gv', view=True)